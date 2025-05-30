#!/usr/bin/env python3

import os
import sys
import subprocess
import tempfile
import shutil
import concurrent.futures
import re
import argparse
import time
from pathlib import Path

def create_output_dir(base_dir, name):
    """Create an output directory for storing results."""
    output_dir = os.path.join(base_dir, name)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def get_python_version_from_pyc(pyc_file):
    """Try to determine the Python version from the .pyc file magic number."""
    try:
        with open(pyc_file, 'rb') as f:
            magic = f.read(4)
            
        # Magic number mappings
        magic_numbers = {
            b'\x03\xf3\r\n': '2.7',
            b'\x33\r\r\n': '3.0',
            b'B\r\r\n': '3.1',
            b'A\r\r\n': '3.2',
            b'E\r\r\n': '3.3',
            b'I\r\r\n': '3.4',
            b'N\r\r\n': '3.5',
            b'M\r\r\n': '3.5+',
            b'S\r\r\n': '3.6',
            b'T\r\r\n': '3.6+',
            b'X\r\r\n': '3.7',
            b'Y\r\r\n': '3.7+',
            b'\\\r\r\n': '3.8',
            b']\r\r\n': '3.8+',
            b'a\r\r\n': '3.9',
            b'b\r\r\n': '3.9+',
            b'e\r\r\n': '3.10',
            b'f\r\r\n': '3.10+',
            b'j\r\r\n': '3.11',
            b'k\r\r\n': '3.11+',
            b'n\r\r\n': '3.12',
            b'o\r\r\n': '3.12+',
        }
        
        if magic in magic_numbers:
            return magic_numbers[magic]
        return "Unknown"
    except Exception as e:
        return f"Error determining version: {e}"

def get_file_info(pyc_file):
    """Get basic info about the .pyc file."""
    file_size = os.path.getsize(pyc_file)
    mod_time = time.ctime(os.path.getmtime(pyc_file))
    py_version = get_python_version_from_pyc(pyc_file)
    
    return {
        "path": pyc_file,
        "size": file_size,
        "modified": mod_time,
        "python_version": py_version
    }

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

def decompile_with_uncompyle6(pyc_file, output_dir):
    """Decompile using uncompyle6."""
    output_file = os.path.join(output_dir, os.path.basename(pyc_file).replace(".pyc", "_uncompyle6.py"))
    
    cmd = ["python3", "-m", "uncompyle6", "-o", output_file, pyc_file]
    stdout, stderr, returncode = run_command(cmd)
    
    if returncode != 0:
        with open(output_file, 'w') as f:
            f.write(f"# Failed to decompile with uncompyle6\n# Error: {stderr}")
        return False
    return True

def decompile_with_decompyle3(pyc_file, output_dir):
    """Decompile using decompyle3."""
    output_file = os.path.join(output_dir, os.path.basename(pyc_file).replace(".pyc", "_decompyle3.py"))
    
    cmd = ["python3", "-m", "decompyle3", "-o", output_file, pyc_file]
    stdout, stderr, returncode = run_command(cmd)
    
    if returncode != 0:
        with open(output_file, 'w') as f:
            f.write(f"# Failed to decompile with decompyle3\n# Error: {stderr}")
        return False
    return True

def decompile_with_pycdc(pyc_file, output_dir):
    """Decompile using pycdc."""
    output_file = os.path.join(output_dir, os.path.basename(pyc_file).replace(".pyc", "_pycdc.py"))
    
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
    output_file = os.path.join(output_dir, os.path.basename(pyc_file).replace(".pyc", "_pycdas.txt"))
    
    cmd = ["pycdas", pyc_file]
    stdout, stderr, returncode = run_command(cmd)
    
    with open(output_file, 'w') as f:
        if returncode != 0:
            f.write(f"# Failed to disassemble with pycdas\n# Error: {stderr}")
            return False
        else:
            f.write(stdout)
    return True

def disassemble_with_dis(pyc_file, output_dir):
    """Disassemble using Python's dis module."""
    output_file = os.path.join(output_dir, os.path.basename(pyc_file).replace(".pyc", "_dis.txt"))
    
    # Create a temporary script to disassemble the .pyc file
    temp_script = tempfile.NamedTemporaryFile(delete=False, suffix='.py')
    try:
        with open(temp_script.name, 'w') as f:
            f.write(f"""
import dis
import marshal
import sys
import types

def disassemble_pyc(filename):
    with open(filename, 'rb') as f:
        # Skip the magic number and timestamp/size
        f.seek(16)  # This should work for most Python 3.x versions
        try:
            code = marshal.load(f)
            dis.dis(code)
        except Exception as e:
            print(f"Error disassembling: {{e}}")

if __name__ == "__main__":
    disassemble_pyc("{pyc_file}")
""")
        
        cmd = ["python3", temp_script.name]
        stdout, stderr, returncode = run_command(cmd)
        
        with open(output_file, 'w') as f:
            if returncode != 0:
                f.write(f"# Failed to disassemble with dis\n# Error: {stderr}")
                return False
            else:
                f.write(stdout)
        return True
    finally:
        os.unlink(temp_script.name)

def extract_metadata(pyc_file, output_dir):
    """Extract metadata from the .pyc file."""
    output_file = os.path.join(output_dir, os.path.basename(pyc_file).replace(".pyc", "_metadata.txt"))
    
    # Create a temporary script to extract metadata
    temp_script = tempfile.NamedTemporaryFile(delete=False, suffix='.py')
    try:
        with open(temp_script.name, 'w') as f:
            f.write(f"""
import marshal
import sys
import types
import time
import struct

def extract_pyc_metadata(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        
    if len(data) < 16:
        print("File too small to be a valid .pyc file")
        return
    
    magic = data[:4]
    print(f"Magic number: {magic.hex()}")
    
    # Handle different .pyc formats across Python versions
    if len(data) >= 12:
        try:
            timestamp = struct.unpack('<I', data[4:8])[0]
            print(f"Timestamp: {timestamp} ({time.ctime(timestamp)})")
        except:
            print("Failed to extract timestamp")
    
    if len(data) >= 16:
        try:
            size = struct.unpack('<I', data[8:12])[0]
            print(f"Source size: {size} bytes")
        except:
            print("Failed to extract source size")
            
    # Try to extract code object
    try:
        with open(filename, 'rb') as f:
            f.seek(16)  # Skip header
            code = marshal.load(f)
            if isinstance(code, types.CodeType):
                print("\\nCode Object Information:")
                print(f"Filename: {code.co_filename}")
                print(f"Name: {code.co_name}")
                print(f"Argument count: {code.co_argcount}")
                print(f"Positional-only arguments: {code.co_posonlyargcount if hasattr(code, 'co_posonlyargcount') else 'N/A'}")
                print(f"Keyword-only arguments: {code.co_kwonlyargcount if hasattr(code, 'co_kwonlyargcount') else 'N/A'}")
                print(f"Number of locals: {code.co_nlocals}")
                print(f"Stack size: {code.co_stacksize}")
                print(f"Flags: {code.co_flags} ({bin(code.co_flags)})")
                
                # Extract constants
                print("\\nConstants:")
                for i, const in enumerate(code.co_consts):
                    if isinstance(const, types.CodeType):
                        print(f"  {i}: <code object {const.co_name}>")
                    else:
                        print(f"  {i}: {repr(const)}")
                
                # Extract names
                print("\\nNames:")
                for i, name in enumerate(code.co_names):
                    print(f"  {i}: {name}")
                
                # Extract variable names
                print("\\nVariable names:")
                for i, var in enumerate(code.co_varnames):
                    print(f"  {i}: {var}")
    except Exception as e:
        print(f"Error extracting code object: {e}")

if __name__ == "__main__":
    extract_pyc_metadata("{pyc_file}")
""")
        
        cmd = ["python3", temp_script.name]
        stdout, stderr, returncode = run_command(cmd)
        
        with open(output_file, 'w') as f:
            if returncode != 0:
                f.write(f"# Failed to extract metadata\n# Error: {stderr}")
                return False
            else:
                f.write(stdout)
        return True
    finally:
        os.unlink(temp_script.name)

def process_pyc_file(pyc_file, output_base_dir, input_dir):
    """Process a single .pyc file with all available tools."""
    print(f"Processing: {pyc_file}")
    
    # Create output directory structure
    rel_path = os.path.relpath(pyc_file, start=input_dir)
    file_output_dir = os.path.join(output_base_dir, os.path.dirname(rel_path))
    os.makedirs(file_output_dir, exist_ok=True)
    
    # Get file info
    file_info = get_file_info(pyc_file)
    
    # Create an info file
    info_file = os.path.join(file_output_dir, os.path.basename(pyc_file).replace(".pyc", "_info.txt"))
    with open(info_file, 'w') as f:
        f.write(f"File: {pyc_file}\n")
        f.write(f"Size: {file_info['size']} bytes\n")
        f.write(f"Modified: {file_info['modified']}\n")
        f.write(f"Python Version: {file_info['python_version']}\n")
    
    # Run each decompiler
    results = {
        "uncompyle6": decompile_with_uncompyle6(pyc_file, file_output_dir),
        "decompyle3": decompile_with_decompyle3(pyc_file, file_output_dir),
        "pycdc": decompile_with_pycdc(pyc_file, file_output_dir),
        "pycdas": disassemble_with_pycdas(pyc_file, file_output_dir),
        "dis": disassemble_with_dis(pyc_file, file_output_dir),
        "metadata": extract_metadata(pyc_file, file_output_dir)
    }
    
    # Create a summary report
    summary_file = os.path.join(file_output_dir, os.path.basename(pyc_file).replace(".pyc", "_summary.txt"))
    with open(summary_file, 'w') as f:
        f.write(f"Summary for {pyc_file}\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Python Version: {file_info['python_version']}\n\n")
        f.write("Decompiler Results:\n")
        f.write(f"  uncompyle6: {'Success' if results['uncompyle6'] else 'Failed'}\n")
        f.write(f"  decompyle3: {'Success' if results['decompyle3'] else 'Failed'}\n")
        f.write(f"  pycdc: {'Success' if results['pycdc'] else 'Failed'}\n\n")
        f.write("Disassembly Results:\n")
        f.write(f"  pycdas: {'Success' if results['pycdas'] else 'Failed'}\n")
        f.write(f"  dis: {'Success' if results['dis'] else 'Failed'}\n\n")
        f.write(f"Metadata Extraction: {'Success' if results['metadata'] else 'Failed'}\n")
    
    return results

def find_pyc_files(input_dir):
    """Find all .pyc files in the input directory."""
    pyc_files = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".pyc"):
                pyc_files.append(os.path.join(root, file))
    return pyc_files

def generate_final_report(output_dir, results):
    """Generate a final report summarizing all processed files."""
    report_file = os.path.join(output_dir, "final_report.txt")
    
    with open(report_file, 'w') as f:
        f.write("PYC Decompilation Report\n")
        f.write("=" * 50 + "\n\n")
        
        f.write(f"Total files processed: {len(results)}\n\n")
        
        success_count = {
            "uncompyle6": sum(1 for r in results if r["uncompyle6"]),
            "decompyle3": sum(1 for r in results if r["decompyle3"]),
            "pycdc": sum(1 for r in results if r["pycdc"]),
            "pycdas": sum(1 for r in results if r["pycdas"]),
            "dis": sum(1 for r in results if r["dis"]),
            "metadata": sum(1 for r in results if r["metadata"])
        }
        
        f.write("Success Rates:\n")
        for tool, count in success_count.items():
            percentage = (count / len(results)) * 100 if results else 0
            f.write(f"  {tool}: {count}/{len(results)} ({percentage:.2f}%)\n")
        
        f.write("\nDecompilation worked best with:\n")
        best_tool = max(success_count.items(), key=lambda x: x[1])
        f.write(f"  {best_tool[0]}: {best_tool[1]}/{len(results)} files\n")

def create_index_html(output_dir, pyc_files, input_dir):
    """Create an HTML index file for easier navigation."""
    index_file = os.path.join(output_dir, "index.html")
    
    with open(index_file, 'w') as f:
        f.write("""
<!DOCTYPE html>
<html>
<head>
    <title>PYC Decompilation Results</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        .success { color: green; }
        .failure { color: red; }
    </style>
</head>
<body>
    <h1>PYC Decompilation Results</h1>
    <p>Generated on: """ + time.ctime() + """</p>
    <table>
        <tr>
            <th>File</th>
            <th>Python Version</th>
            <th>Summary</th>
            <th>Decompiled Source</th>
            <th>Disassembly</th>
            <th>Metadata</th>
        </tr>
""")
        
        for pyc_file in pyc_files:
            rel_path = os.path.relpath(pyc_file, start=input_dir)
            file_basename = os.path.basename(pyc_file).replace(".pyc", "")
            file_dir = os.path.dirname(rel_path)
            
            # Paths to various output files
            summary_path = os.path.join(file_dir, file_basename + "_summary.txt")
            uncompyle6_path = os.path.join(file_dir, file_basename + "_uncompyle6.py")
            decompyle3_path = os.path.join(file_dir, file_basename + "_decompyle3.py")
            pycdc_path = os.path.join(file_dir, file_basename + "_pycdc.py")
            pycdas_path = os.path.join(file_dir, file_basename + "_pycdas.txt")
            dis_path = os.path.join(file_dir, file_basename + "_dis.txt")
            metadata_path = os.path.join(file_dir, file_basename + "_metadata.txt")
            
            # Get Python version
            file_info = get_file_info(pyc_file)
            py_version = file_info["python_version"]
            
            f.write(f"""
        <tr>
            <td>{rel_path}</td>
            <td>{py_version}</td>
            <td><a href="{summary_path}">Summary</a></td>
            <td>
                <a href="{uncompyle6_path}">uncompyle6</a> | 
                <a href="{decompyle3_path}">decompyle3</a> | 
                <a href="{pycdc_path}">pycdc</a>
            </td>
            <td>
                <a href="{pycdas_path}">pycdas</a> | 
                <a href="{dis_path}">dis</a>
            </td>
            <td><a href="{metadata_path}">Metadata</a></td>
        </tr>""")
        
        f.write("""
    </table>
    <hr>
    <p><a href="final_report.txt">View Final Report</a></p>
</body>
</html>
""")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze and decompile .pyc files")
    parser.add_argument("input_dir", help="Directory containing .pyc files")
    parser.add_argument("--output-dir", help="Output directory for results", default="pyc_analysis_output")
    parser.add_argument("--max-workers", type=int, help="Maximum number of parallel workers", default=4)
    
    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Find all .pyc files
    pyc_files = find_pyc_files(args.input_dir)
    print(f"Found {len(pyc_files)} .pyc files to process")
    
    # Process each file
    all_results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        future_to_file = {executor.submit(process_pyc_file, file, args.output_dir, args.input_dir): file for file in pyc_files}
        
        for future in concurrent.futures.as_completed(future_to_file):
            file = future_to_file[future]
            try:
                result = future.result()
                all_results.append(result)
                print(f"Completed processing: {file}")
            except Exception as e:
                print(f"Error processing {file}: {e}")
    
    # Generate final report
    generate_final_report(args.output_dir, all_results)
    
    # Create HTML index
    create_index_html(args.output_dir, pyc_files, args.input_dir)
    
    print(f"\nProcessing complete! Results are in: {os.path.abspath(args.output_dir)}")
    print(f"Open {os.path.join(os.path.abspath(args.output_dir), 'index.html')} to view the results")
