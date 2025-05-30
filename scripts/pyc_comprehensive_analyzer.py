#!/usr/bin/env python3
"""
PYC Comprehensive Analyzer - Coordinates multiple decompilation tools
This script utilizes existing scripts to extract as much information as possible from .pyc files
"""

import os
import sys
import subprocess
import argparse
import json
import time
from pathlib import Path
import shutil

def check_requirements():
    """Check if required tools are installed"""
    tools = {
        'uncompyle6': False,
        'decompyle3': False,
        'pycdc': False,
        'pycdas': False,
        'python-magic': False,
    }
    
    print("Checking for required tools...")
    
    # Check command line tools
    for tool in ['uncompyle6', 'decompyle3', 'pycdc', 'pycdas']:
        try:
            subprocess.run(['which', tool], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
            tools[tool] = True
            print(f"✅ {tool} found")
        except:
            print(f"❌ {tool} not found")
    
    # Check Python packages
    try:
        import magic
        tools['python-magic'] = True
        print("✅ python-magic found")
    except ImportError:
        print("❌ python-magic not found")
    
    return tools

def install_missing_requirements(tools):
    """Attempt to install missing tools"""
    if not all(tools.values()):
        print("\nSome required tools are missing. Attempting to install...")
        
        if not tools['python-magic']:
            print("Installing python-magic...")
            subprocess.run(['pip3', 'install', 'python-magic'], check=False)
        
        if not tools['uncompyle6']:
            print("Installing uncompyle6...")
            subprocess.run(['pip3', 'install', 'uncompyle6'], check=False)
        
        if not tools['decompyle3']:
            print("Installing decompyle3...")
            subprocess.run(['pip3', 'install', 'decompyle3'], check=False)
        
        # pycdc and pycdas need to be installed from source if not available
        if not tools['pycdc'] or not tools['pycdas']:
            print("pycdc/pycdas require manual installation. See: https://github.com/zrax/pycdc")
            
        # Recheck after installation
        return check_requirements()
    
    return tools

def create_output_dir(output_dir):
    """Create and prepare output directory structure"""
    print(f"Creating output directory: {output_dir}")
    
    # Create main output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Create subdirectories for different analysis types
    subdirs = [
        'decompiled_code',  # For decompiled Python code
        'disassembly',      # For bytecode disassembly
        'ast_analysis',     # For abstract syntax tree analysis
        'imports',          # For extracted import statements
        'function_details', # For extracted function details
        'class_details',    # For extracted class details
        'constants',        # For extracted constants
        'combined_results'  # For unified analysis results
    ]
    
    for subdir in subdirs:
        os.makedirs(os.path.join(output_dir, subdir), exist_ok=True)
    
    return output_dir

def run_existing_scripts(input_dir, output_dir):
    """Run existing pyc analysis scripts"""
    print("\nRunning existing pyc analysis scripts...")
    
    # Run pyc_analyzer.py
    print("Running pyc_analyzer.py...")
    try:
        subprocess.run(
            [sys.executable, '/Users/kurt/Desktop/pyc_analyzer.py', input_dir, '-o', 
             os.path.join(output_dir, 'analyzer_results')],
            check=True
        )
        print("✅ pyc_analyzer.py completed successfully")
    except subprocess.CalledProcessError:
        print("⚠️ pyc_analyzer.py encountered errors")
    
    # Run pyc_decompiler.py
    print("Running pyc_decompiler.py...")
    try:
        subprocess.run(
            [sys.executable, '/Users/kurt/Desktop/pyc_decompiler.py', input_dir, '-o', 
             os.path.join(output_dir, 'decompiler_results')],
            check=True
        )
        print("✅ pyc_decompiler.py completed successfully")
    except subprocess.CalledProcessError:
        print("⚠️ pyc_decompiler.py encountered errors")

def run_direct_decompilation(input_dir, output_dir, tools):
    """Run direct decompilation on all .pyc files"""
    print("\nRunning direct decompilation of .pyc files...")
    
    # Get all .pyc files
    pyc_files = list(Path(input_dir).glob('**/*.pyc'))
    print(f"Found {len(pyc_files)} .pyc files")
    
    # Prepare output directories
    decompiled_dir = os.path.join(output_dir, 'decompiled_code')
    disassembly_dir = os.path.join(output_dir, 'disassembly')
    
    # Process each file
    for i, pyc_file in enumerate(pyc_files):
        rel_path = os.path.relpath(pyc_file, input_dir)
        base_name = os.path.splitext(os.path.basename(pyc_file))[0]
        module_path = os.path.dirname(rel_path)
        
        print(f"Processing ({i+1}/{len(pyc_files)}): {rel_path}")
        
        # Create output subdirectories to maintain structure
        decompiled_module_dir = os.path.join(decompiled_dir, module_path)
        disassembly_module_dir = os.path.join(disassembly_dir, module_path)
        os.makedirs(decompiled_module_dir, exist_ok=True)
        os.makedirs(disassembly_module_dir, exist_ok=True)
        
        # Run uncompyle6 if available
        if tools['uncompyle6']:
            out_file = os.path.join(decompiled_module_dir, f"{base_name}_uncompyle6.py")
            try:
                subprocess.run(
                    ['uncompyle6', '-o', out_file, str(pyc_file)],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=30
                )
            except:
                pass
        
        # Run decompyle3 if available
        if tools['decompyle3']:
            out_file = os.path.join(decompiled_module_dir, f"{base_name}_decompyle3.py")
            try:
                subprocess.run(
                    ['decompyle3', '-o', out_file, str(pyc_file)],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=30
                )
            except:
                pass
        
        # Run pycdc if available
        if tools['pycdc']:
            out_file = os.path.join(decompiled_module_dir, f"{base_name}_pycdc.py")
            try:
                with open(out_file, 'w') as f:
                    subprocess.run(
                        ['pycdc', str(pyc_file)],
                        stdout=f,
                        stderr=subprocess.PIPE,
                        timeout=30
                    )
            except:
                pass
        
        # Run pycdas if available
        if tools['pycdas']:
            out_file = os.path.join(disassembly_module_dir, f"{base_name}_pycdas.dis")
            try:
                with open(out_file, 'w') as f:
                    subprocess.run(
                        ['pycdas', str(pyc_file)],
                        stdout=f,
                        stderr=subprocess.PIPE,
                        timeout=30
                    )
            except:
                pass

def extract_best_decompilation(output_dir):
    """Extract and consolidate the best decompilation results"""
    print("\nExtracting and consolidating best decompilation results...")
    
    decompiled_dir = os.path.join(output_dir, 'decompiled_code')
    combined_dir = os.path.join(output_dir, 'combined_results')
    
    # Walk through all decompiled files
    for root, _, files in os.walk(decompiled_dir):
        py_files = [f for f in files if f.endswith('.py')]
        
        if not py_files:
            continue
        
        # Group files by base name
        grouped_files = {}
        for file in py_files:
            # Extract base name without the tool suffix
            base_name = file.split('_')[0]
            if base_name not in grouped_files:
                grouped_files[base_name] = []
            grouped_files[base_name].append(os.path.join(root, file))
        
        # Process each group
        for base_name, file_paths in grouped_files.items():
            # Determine the best decompilation
            best_file = select_best_decompilation(file_paths)
            
            if best_file:
                # Create destination directory structure
                rel_path = os.path.relpath(os.path.dirname(best_file), decompiled_dir)
                dest_dir = os.path.join(combined_dir, rel_path)
                os.makedirs(dest_dir, exist_ok=True)
                
                # Copy to combined results
                dest_file = os.path.join(dest_dir, f"{base_name}.py")
                shutil.copy2(best_file, dest_file)

def select_best_decompilation(file_paths):
    """Select the best decompilation from multiple outputs based on heuristics"""
    if not file_paths:
        return None
    
    # Check file sizes and content
    valid_files = []
    for path in file_paths:
        try:
            size = os.path.getsize(path)
            if size > 0:
                with open(path, 'r') as f:
                    content = f.read()
                    
                # Skip files with error messages or minimal content
                if ('Error' not in content and 
                    'Traceback' not in content and 
                    len(content.strip().split('\n')) > 3):
                    valid_files.append((path, size, content))
        except:
            continue
    
    if not valid_files:
        return None
    
    # Prioritize by tool (based on empirical success rates)
    for path, _, _ in valid_files:
        if '_uncompyle6.py' in path:
            return path
    
    for path, _, _ in valid_files:
        if '_decompyle3.py' in path:
            return path
    
    for path, _, _ in valid_files:
        if '_pycdc.py' in path:
            return path
    
    # If no preferred tool, take the file with the most content
    return max(valid_files, key=lambda x: x[1])[0]

def analyze_module_structure(input_dir, output_dir):
    """Analyze the module structure and generate a report"""
    print("\nAnalyzing module structure...")
    
    pyc_files = list(Path(input_dir).glob('**/*.pyc'))
    
    # Create a module structure representation
    module_structure = {}
    
    for pyc_file in pyc_files:
        rel_path = os.path.relpath(pyc_file, input_dir)
        path_parts = os.path.normpath(rel_path).split(os.sep)
        
        current = module_structure
        # Build nested dictionary representation of module structure
        for i, part in enumerate(path_parts):
            if i == len(path_parts) - 1:
                # Last part is the file name
                name = os.path.splitext(part)[0]
                current[name] = str(pyc_file)
            else:
                if part not in current:
                    current[part] = {}
                current = current[part]
    
    # Save module structure to JSON
    structure_file = os.path.join(output_dir, 'module_structure.json')
    with open(structure_file, 'w') as f:
        json.dump(module_structure, f, indent=2)
    
    # Generate module structure report
    report_file = os.path.join(output_dir, 'module_structure.md')
    with open(report_file, 'w') as f:
        f.write("# Python Module Structure\n\n")
        write_module_structure(f, module_structure)
    
    print(f"Module structure saved to {structure_file}")
    print(f"Module structure report saved to {report_file}")

def write_module_structure(file, structure, level=0):
    """Write module structure to markdown file"""
    for name, value in sorted(structure.items()):
        indent = "  " * level
        if isinstance(value, dict):
            file.write(f"{indent}- **{name}/** (package)\n")
            write_module_structure(file, value, level + 1)
        else:
            file.write(f"{indent}- {name}.pyc (module)\n")

def extract_imports_and_functions(output_dir):
    """Extract import statements and function definitions from decompiled code"""
    print("\nExtracting imports and functions from decompiled code...")
    
    combined_dir = os.path.join(output_dir, 'combined_results')
    decompiled_dir = os.path.join(output_dir, 'decompiled_code')
    imports_dir = os.path.join(output_dir, 'imports')
    functions_dir = os.path.join(output_dir, 'function_details')
    
    # Find all .py files in combined results and decompiled_code directories
    combined_files = list(Path(combined_dir).glob('**/*.py')) if os.path.exists(combined_dir) else []
    decompiled_files = list(Path(decompiled_dir).glob('**/*.py')) if os.path.exists(decompiled_dir) else []
    
    # Use combined files first, then add any decompiled files that don't exist in combined
    combined_basenames = {os.path.splitext(os.path.basename(p))[0].split('_')[0] for p in combined_files}
    extra_decompiled = [p for p in decompiled_files 
                        if os.path.splitext(os.path.basename(p))[0].split('_')[0] not in combined_basenames]
    
    py_files = combined_files + extra_decompiled
    print(f"Processing {len(py_files)} Python files for imports and functions")
    
    all_imports = {}
    all_functions = {}
    all_classes = {}
    
    import re
    
    for py_file in py_files:
        filename = os.path.basename(py_file)
        module_parts = filename.split('_')
        # Get base module name without the decompiler suffix
        if len(module_parts) > 1 and module_parts[-1] in ['uncompyle6.py', 'decompyle3.py', 'pycdc.py']:
            module_name = '_'.join(module_parts[:-1])
        else:
            module_name = os.path.splitext(filename)[0]
        
        try:
            with open(py_file, 'r') as f:
                content = f.read()
            
            # Extract imports using regex
            import_statements = []
            import_regex = r'^(?:from\s+[\w.]+\s+import\s+[\w,\s*]+|import\s+[\w,\s.]+)(?:\s+as\s+[\w,\s]+)?'
            for line in content.split('\n'):
                line = line.strip()
                if re.match(import_regex, line):
                    import_statements.append(line)
            
            all_imports[module_name] = import_statements
            
            # Extract function definitions using regex
            function_defs = []
            function_regex = r'(?:^|\n)\s*def\s+([^\s(]+)\s*\(([^)]*)\)\s*:'
            for match in re.finditer(function_regex, content, re.MULTILINE):
                function_name = match.group(1)
                args = match.group(2)
                # Get the full function definition by finding the indented block
                start_pos = match.start()
                end_line_pos = content.find('\n', match.end())
                
                # Try to get the docstring if present
                docstring = ""
                if end_line_pos > 0:
                    next_lines = content[end_line_pos:end_line_pos+200]  # Look at next ~200 chars
                    docstring_match = re.search(r'^\s+"""(.+?)"""', next_lines, re.DOTALL | re.MULTILINE)
                    if docstring_match:
                        docstring = docstring_match.group(1).strip()
                
                function_defs.append({
                    'name': function_name,
                    'args': args,
                    'signature': f"def {function_name}({args}):",
                    'docstring': docstring
                })
            
            all_functions[module_name] = function_defs
            
            # Extract class definitions
            class_defs = []
            class_regex = r'(?:^|\n)\s*class\s+([^\s(:]+)(?:\(([^)]*)\))?\s*:'
            for match in re.finditer(class_regex, content, re.MULTILINE):
                class_name = match.group(1)
                class_parents = match.group(2) if match.group(2) else ""
                
                # Find methods in this class
                class_start = match.end()
                # Try to find the end of the class by indentation level
                next_line_start = content.find('\n', class_start) + 1
                if next_line_start > 0:
                    # Get the indentation of the first line in the class
                    class_indent_match = re.search(r'^(\s+)', content[next_line_start:next_line_start+50], re.MULTILINE)
                    if class_indent_match:
                        class_indent = class_indent_match.group(1)
                        
                        # Methods will have one more level of indentation
                        methods = []
                        method_regex = fr'{class_indent}    def\s+([^\s(]+)\s*\(([^)]*)\)\s*:'
                        for method_match in re.finditer(method_regex, content[next_line_start:], re.MULTILINE):
                            method_name = method_match.group(1)
                            method_args = method_match.group(2)
                            methods.append({
                                'name': method_name,
                                'args': method_args
                            })
                        
                        class_defs.append({
                            'name': class_name,
                            'parents': class_parents,
                            'methods': methods
                        })
            
            all_classes[module_name] = class_defs
            
        except Exception as e:
            print(f"Error processing {py_file}: {e}")
    
    # Save imports to JSON
    imports_file = os.path.join(imports_dir, 'all_imports.json')
    with open(imports_file, 'w') as f:
        json.dump(all_imports, f, indent=2)
    
    # Save functions to JSON
    functions_file = os.path.join(functions_dir, 'all_functions.json')
    with open(functions_file, 'w') as f:
        json.dump(all_functions, f, indent=2)
    
    # Save classes to JSON
    classes_dir = os.path.join(output_dir, 'class_details')
    os.makedirs(classes_dir, exist_ok=True)
    classes_file = os.path.join(classes_dir, 'all_classes.json')
    with open(classes_file, 'w') as f:
        json.dump(all_classes, f, indent=2)
    
    # Generate import dependencies report
    deps_file = os.path.join(imports_dir, 'import_dependencies.md')
    with open(deps_file, 'w') as f:
        f.write("# Module Import Dependencies\n\n")
        for module, imports in sorted(all_imports.items()):
            if imports:
                f.write(f"## {module}\n\n")
                for imp in imports:
                    f.write(f"- `{imp}`\n")
                f.write("\n")
    
    # Generate functions report
    func_file = os.path.join(functions_dir, 'functions_by_module.md')
    with open(func_file, 'w') as f:
        f.write("# Functions by Module\n\n")
        for module, functions in sorted(all_functions.items()):
            if functions:
                f.write(f"## {module}\n\n")
                for func in functions:
                    f.write(f"- `{func['name']}({func['args']})`\n")
                    if func.get('docstring'):
                        f.write(f"  - Docstring: {func['docstring']}\n")
                f.write("\n")
    
    # Generate classes report
    class_file = os.path.join(classes_dir, 'classes_by_module.md')
    with open(class_file, 'w') as f:
        f.write("# Classes by Module\n\n")
        for module, classes in sorted(all_classes.items()):
            if classes:
                f.write(f"## {module}\n\n")
                for cls in classes:
                    parents = f" ({cls['parents']})" if cls['parents'] else ""
                    f.write(f"- `{cls['name']}{parents}`\n")
                    if cls.get('methods'):
                        f.write("  - Methods:\n")
                        for method in cls['methods']:
                            f.write(f"    - `{method['name']}({method['args']})`\n")
                f.write("\n")
    
    print(f"Imports saved to {imports_file}")
    print(f"Functions saved to {functions_file}")
    print(f"Classes saved to {classes_file}")

def generate_summary_report(output_dir, tools):
    """Generate a summary report of all analysis"""
    print("\nGenerating summary report...")
    
    report_file = os.path.join(output_dir, 'summary_report.md')
    
    with open(report_file, 'w') as f:
        f.write("# PYC Files Analysis Summary\n\n")
        
        # Tools information
        f.write("## Tools Used\n\n")
        for tool, available in tools.items():
            status = "✅ Available" if available else "❌ Not available"
            f.write(f"- **{tool}**: {status}\n")
        
        f.write("\n## Analysis Results\n\n")
        
        # Count files processed
        pyc_count = len(list(Path(output_dir).glob('decompiled_code/**/*.py')))
        f.write(f"- Total PYC files processed: {pyc_count}\n")
        
        # Count successful decompilations
        combined_count = len(list(Path(output_dir).glob('combined_results/**/*.py')))
        f.write(f"- Successfully decompiled files: {combined_count}\n")
        
        # Check imports
        imports_file = os.path.join(output_dir, 'imports', 'all_imports.json')
        if os.path.exists(imports_file):
            with open(imports_file, 'r') as imports_f:
                imports_data = json.load(imports_f)
                total_imports = sum(len(imports) for imports in imports_data.values())
                f.write(f"- Total import statements extracted: {total_imports}\n")
        
        # Check functions
        functions_file = os.path.join(output_dir, 'function_details', 'all_functions.json')
        if os.path.exists(functions_file):
            with open(functions_file, 'r') as funcs_f:
                funcs_data = json.load(funcs_f)
                total_funcs = sum(len(funcs) for funcs in funcs_data.values())
                f.write(f"- Total functions extracted: {total_funcs}\n")
        
        f.write("\n## Reports Available\n\n")
        f.write("- [Module Structure](module_structure.md)\n")
        f.write("- [Import Dependencies](imports/import_dependencies.md)\n")
        f.write("- [Functions by Module](function_details/functions_by_module.md)\n")
        f.write("- [Classes by Module](class_details/classes_by_module.md)\n")
        
        # Check for class details
        classes_file = os.path.join(output_dir, 'class_details', 'all_classes.json')
        if os.path.exists(classes_file):
            with open(classes_file, 'r') as classes_f:
                classes_data = json.load(classes_f)
                total_classes = sum(len(classes) for classes in classes_data.values())
                f.write(f"- Total classes extracted: {total_classes}\n")
                
                # Count methods
                total_methods = 0
                for module_classes in classes_data.values():
                    for cls in module_classes:
                        total_methods += len(cls.get('methods', []))
                f.write(f"- Total class methods extracted: {total_methods}\n")
        
        if os.path.exists(os.path.join(output_dir, 'analyzer_results')):
            f.write("- [PYC Analyzer Results](analyzer_results/)\n")
        
        if os.path.exists(os.path.join(output_dir, 'decompiler_results')):
            f.write("- [PYC Decompiler Results](decompiler_results/)\n")
    
    print(f"Summary report saved to {report_file}")

def main():
    parser = argparse.ArgumentParser(description='Comprehensive Python Bytecode Analyzer')
    parser.add_argument('input_dir', help='Directory containing .pyc files')
    parser.add_argument('-o', '--output-dir', default='pyc_comprehensive_analysis',
                        help='Output directory for analysis results')
    parser.add_argument('--skip-scripts', action='store_true',
                        help='Skip running existing scripts')
    args = parser.parse_args()
    
    print("=== PYC Comprehensive Analyzer ===")
    
    start_time = time.time()
    
    # Check input directory
    if not os.path.exists(args.input_dir):
        print(f"Error: Input directory '{args.input_dir}' does not exist.")
        return 1
    
    # Check and install requirements
    tools = check_requirements()
    tools = install_missing_requirements(tools)
    
    # Create output directory
    output_dir = create_output_dir(args.output_dir)
    
    # Run existing scripts if not skipped
    if not args.skip_scripts:
        run_existing_scripts(args.input_dir, output_dir)
    
    # Run direct decompilation
    run_direct_decompilation(args.input_dir, output_dir, tools)
    
    # Extract best decompilation results
    extract_best_decompilation(output_dir)
    
    # Analyze module structure
    analyze_module_structure(args.input_dir, output_dir)
    
    # Extract imports and functions
    extract_imports_and_functions(output_dir)
    
    # Generate summary report
    generate_summary_report(output_dir, tools)
    
    elapsed_time = time.time() - start_time
    print(f"\nAnalysis completed in {elapsed_time:.2f} seconds.")
    print(f"Results saved to: {os.path.abspath(output_dir)}")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
