#!/usr/bin/env python3

import os
import sys
import subprocess
import argparse
import shutil
import concurrent.futures
from pathlib import Path

def run_command(cmd, timeout=30):
    """Run a command with timeout and return its output."""
    try:
        result = subprocess.run(
            cmd, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True, 
            timeout=timeout
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired:
        return "", f"Command timed out after {timeout} seconds", 1
    except Exception as e:
        return "", f"Error running command: {e}", 1

def find_pyc_files(input_dir):
    """Find all .pyc files in the input directory."""
    pyc_files = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".pyc"):
                pyc_files.append(os.path.join(root, file))
    return pyc_files

def decompile_with_uncompyle6(pyc_file, output_dir):
    """Decompile using uncompyle6."""
    rel_path = os.path.relpath(pyc_file, start=args.input_dir)
    output_subdir = os.path.join(output_dir, "uncompyle6", os.path.dirname(rel_path))
    os.makedirs(output_subdir, exist_ok=True)
    
    output_file = os.path.join(output_subdir, os.path.basename(pyc_file).replace(".pyc", ".py"))
    
    cmd = ["python3", "-m", "uncompyle6", "-o", output_file, pyc_file]
    stdout, stderr, returncode = run_command(cmd)
    
    if returncode != 0:
        with open(output_file, 'w') as f:
            f.write(f"# Failed to decompile with uncompyle6\n# Error: {stderr}")
        return False
    return True

def decompile_with_decompyle3(pyc_file, output_dir):
    """Decompile using decompyle3."""
    rel_path = os.path.relpath(pyc_file, start=args.input_dir)
    output_subdir = os.path.join(output_dir, "decompyle3", os.path.dirname(rel_path))
    os.makedirs(output_subdir, exist_ok=True)
    
    output_file = os.path.join(output_subdir, os.path.basename(pyc_file).replace(".pyc", ".py"))
    
    cmd = ["python3", "-m", "decompyle3", "-o", output_file, pyc_file]
    stdout, stderr, returncode = run_command(cmd)
    
    if returncode != 0:
        with open(output_file, 'w') as f:
            f.write(f"# Failed to decompile with decompyle3\n# Error: {stderr}")
        return False
    return True

def decompile_with_pycdc(pyc_file, output_dir):
    """Decompile using pycdc."""
    rel_path = os.path.relpath(pyc_file, start=args.input_dir)
    output_subdir = os.path.join(output_dir, "pycdc", os.path.dirname(rel_path))
    os.makedirs(output_subdir, exist_ok=True)
    
    output_file = os.path.join(output_subdir, os.path.basename(pyc_file).replace(".pyc", ".py"))
    
    cmd = ["pycdc", pyc_file]
    stdout, stderr, returncode = run_command(cmd)
    
    with open(output_file, 'w') as f:
        if returncode != 0:
            f.write(f"# Failed to decompile with pycdc\n# Error: {stderr}")
            return False
        else:
            f.write(stdout)
    return True

def disassemble_with_pycdas(pyc_file, output_dir):
    """Disassemble using pycdas."""
    rel_path = os.path.relpath(pyc_file, start=args.input_dir)
    output_subdir = os.path.join(output_dir, "pycdas", os.path.dirname(rel_path))
    os.makedirs(output_subdir, exist_ok=True)
    
    output_file = os.path.join(output_subdir, os.path.basename(pyc_file).replace(".pyc", ".txt"))
    
    cmd = ["pycdas", pyc_file]
    stdout, stderr, returncode = run_command(cmd)
    
    with open(output_file, 'w') as f:
        if returncode != 0:
            f.write(f"# Failed to disassemble with pycdas\n# Error: {stderr}")
            return False
        else:
            f.write(stdout)
    return True

def process_pyc_file(pyc_file, output_dir):
    """Process a single .pyc file with all available tools."""
    print(f"Processing: {pyc_file}")
    
    try:
        # Try each decompiler
        uncompyle6_result = decompile_with_uncompyle6(pyc_file, output_dir)
        decompyle3_result = decompile_with_decompyle3(pyc_file, output_dir)
        pycdc_result = decompile_with_pycdc(pyc_file, output_dir)
        pycdas_result = disassemble_with_pycdas(pyc_file, output_dir)
        
        print(f"Completed: {pyc_file}")
        print(f"  uncompyle6: {'Success' if uncompyle6_result else 'Failed'}")
        print(f"  decompyle3: {'Success' if decompyle3_result else 'Failed'}")
        print(f"  pycdc: {'Success' if pycdc_result else 'Failed'}")
        print(f"  pycdas: {'Success' if pycdas_result else 'Failed'}")
        print()
        
        return {
            "file": pyc_file,
            "uncompyle6": uncompyle6_result,
            "decompyle3": decompyle3_result,
            "pycdc": pycdc_result,
            "pycdas": pycdas_result
        }
    except Exception as e:
        print(f"Error processing {pyc_file}: {e}")
        return None

def create_summary_html(output_dir, results):
    """Create an HTML summary of the decompilation results."""
    summary_file = os.path.join(output_dir, "summary.html")
    
    with open(summary_file, 'w') as f:
        f.write("""
<!DOCTYPE html>
<html>
<head>
    <title>PYC Decompilation Results</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1, h2 { color: #333; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        .success { color: green; }
        .failure { color: red; }
        .tool-section { margin-top: 30px; }
    </style>
</head>
<body>
    <h1>PYC Decompilation Results</h1>
    
    <h2>Summary</h2>
    <table>
        <tr>
            <th>Total Files</th>
            <td>""" + str(len(results)) + """</td>
        </tr>
        <tr>
            <th>Uncompyle6 Success</th>
            <td>""" + str(sum(1 for r in results if r and r["uncompyle6"])) + "/" + str(len(results)) + """</td>
        </tr>
        <tr>
            <th>Decompyle3 Success</th>
            <td>""" + str(sum(1 for r in results if r and r["decompyle3"])) + "/" + str(len(results)) + """</td>
        </tr>
        <tr>
            <th>Pycdc Success</th>
            <td>""" + str(sum(1 for r in results if r and r["pycdc"])) + "/" + str(len(results)) + """</td>
        </tr>
        <tr>
            <th>Pycdas Success</th>
            <td>""" + str(sum(1 for r in results if r and r["pycdas"])) + "/" + str(len(results)) + """</td>
        </tr>
    </table>
    
    <h2>Tool Directories</h2>
    <ul>
        <li><a href="uncompyle6/">Uncompyle6 Results</a></li>
        <li><a href="decompyle3/">Decompyle3 Results</a></li>
        <li><a href="pycdc/">Pycdc Results</a></li>
        <li><a href="pycdas/">Pycdas Results</a></li>
    </ul>
    
    <h2>File Details</h2>
    <table>
        <tr>
            <th>File</th>
            <th>Uncompyle6</th>
            <th>Decompyle3</th>
            <th>Pycdc</th>
            <th>Pycdas</th>
        </tr>
""")
        
        for result in results:
            if result:
                rel_path = os.path.relpath(result["file"], start=args.input_dir)
                base_name = os.path.basename(rel_path).replace(".pyc", ".py")
                dir_name = os.path.dirname(rel_path)
                
                uncompyle6_link = f"uncompyle6/{dir_name}/{base_name}" if result["uncompyle6"] else "#"
                decompyle3_link = f"decompyle3/{dir_name}/{base_name}" if result["decompyle3"] else "#"
                pycdc_link = f"pycdc/{dir_name}/{base_name}" if result["pycdc"] else "#"
                pycdas_link = f"pycdas/{dir_name}/{base_name.replace('.py', '.txt')}" if result["pycdas"] else "#"
                
                f.write(f"""
        <tr>
            <td>{rel_path}</td>
            <td>{"<a href='" + uncompyle6_link + "'>Success</a>" if result["uncompyle6"] else "<span class='failure'>Failed</span>"}</td>
            <td>{"<a href='" + decompyle3_link + "'>Success</a>" if result["decompyle3"] else "<span class='failure'>Failed</span>"}</td>
            <td>{"<a href='" + pycdc_link + "'>Success</a>" if result["pycdc"] else "<span class='failure'>Failed</span>"}</td>
            <td>{"<a href='" + pycdas_link + "'>Success</a>" if result["pycdas"] else "<span class='failure'>Failed</span>"}</td>
        </tr>""")
        
        f.write("""
    </table>
</body>
</html>""")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decompile .pyc files using multiple tools")
    parser.add_argument("input_dir", help="Directory containing .pyc files")
    parser.add_argument("--output-dir", help="Output directory for results", default="pyc_decompilation_results")
    parser.add_argument("--max-workers", type=int, help="Maximum number of parallel workers", default=4)
    
    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Find all .pyc files
    pyc_files = find_pyc_files(args.input_dir)
    print(f"Found {len(pyc_files)} .pyc files to process")
    
    # Process each file
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        future_to_file = {executor.submit(process_pyc_file, file, args.output_dir): file for file in pyc_files}
        
        for future in concurrent.futures.as_completed(future_to_file):
            file = future_to_file[future]
            try:
                result = future.result()
                if result:
                    results.append(result)
            except Exception as e:
                print(f"Error processing {file}: {e}")
    
    # Create summary HTML
    create_summary_html(args.output_dir, results)
    
    print(f"\nProcessing complete! Results are in: {os.path.abspath(args.output_dir)}")
    print(f"Open {os.path.join(os.path.abspath(args.output_dir), 'summary.html')} to view the results")
