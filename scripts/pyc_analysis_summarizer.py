#!/usr/bin/env python3
"""
PYC Analysis Summarizer - Extracts key information from decompiled PYC files
"""

import os
import json
import re
import argparse
from pathlib import Path

def extract_strings_from_disassembly(output_dir):
    """Extract potentially interesting strings from disassembly files"""
    print("Extracting strings from disassembly files...")
    
    disassembly_dir = os.path.join(output_dir, 'disassembly')
    if not os.path.exists(disassembly_dir):
        print("Disassembly directory not found")
        return {}
        
    strings_by_file = {}
    
    # Regular expression for finding strings in disassembly
    string_pattern = r'LOAD_CONST.*\'([^\']{5,})\''
    
    # For each disassembly file
    for file_path in Path(disassembly_dir).glob('**/*.dis'):
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                
            # Extract strings
            strings = re.findall(string_pattern, content)
            
            # Filter out common Python strings and keep only interesting ones
            interesting_strings = []
            for s in strings:
                # Skip if it looks like a Python internal string
                if (s.startswith('__') and s.endswith('__')) or \
                   s in ('True', 'False', 'None', 'self'):
                    continue
                    
                # Skip if it's just whitespace or very common
                if s.isspace() or s in ('\n', '\t', ' ', ',', '.'):
                    continue
                    
                # Skip if it's a common Python method name
                if s in ('append', 'extend', 'insert', 'remove', 'pop', 'clear', 
                         'index', 'count', 'sort', 'reverse', 'copy'):
                    continue
                    
                interesting_strings.append(s)
                
            # Remove duplicates
            interesting_strings = list(set(interesting_strings))
            
            # Store if we found anything interesting
            if interesting_strings:
                file_name = os.path.basename(file_path)
                strings_by_file[file_name] = interesting_strings
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            
    return strings_by_file

def extract_function_patterns(output_dir):
    """Extract key functions and their patterns from the function details"""
    print("Extracting function patterns...")
    
    functions_file = os.path.join(output_dir, 'function_details', 'all_functions.json')
    if not os.path.exists(functions_file):
        print("Functions file not found")
        return {}
        
    with open(functions_file, 'r') as f:
        all_functions = json.load(f)
        
    # Categories of functions to look for
    categories = {
        'file_operations': ['open', 'read', 'write', 'close', 'chmod', 'chown', 'remove', 'rename', 'mkdir', 'rmdir'],
        'system_operations': ['system', 'popen', 'spawn', 'execv', 'subprocess', 'Popen', 'call', 'check_output'],
        'network_operations': ['socket', 'connect', 'bind', 'listen', 'accept', 'send', 'recv', 'urlopen', 'Request'],
        'gui_operations': ['Tk', 'Frame', 'Label', 'Button', 'Entry', 'Canvas', 'Listbox', 'Menu', 'Scrollbar'],
        'crypto_operations': ['encrypt', 'decrypt', 'hash', 'md5', 'sha1', 'sha256', 'cipher', 'sign', 'verify'],
        'data_processing': ['json', 'parse', 'dump', 'load', 'loads', 'dumps', 'marshal', 'pickle', 'unpickle']
    }
    
    results = {category: {} for category in categories}
    
    for module, functions in all_functions.items():
        for func in functions:
            func_name = func['name']
            func_args = func.get('args', '')
            
            # Check which category this function might belong to
            for category, keywords in categories.items():
                for keyword in keywords:
                    if keyword.lower() in func_name.lower():
                        if module not in results[category]:
                            results[category][module] = []
                        results[category][module].append({
                            'name': func_name,
                            'args': func_args
                        })
                        break
    
    return results

def extract_import_patterns(output_dir):
    """Extract key imports and categorize them"""
    print("Extracting import patterns...")
    
    imports_file = os.path.join(output_dir, 'imports', 'all_imports.json')
    if not os.path.exists(imports_file):
        print("Imports file not found")
        return {}
        
    with open(imports_file, 'r') as f:
        all_imports = json.load(f)
        
    # Categories of imports to look for
    categories = {
        'gui': ['tkinter', 'tk', 'ttk', 'wx', 'PyQt', 'PySide', 'kivy'],
        'network': ['socket', 'http', 'urllib', 'requests', 'ftplib', 'asyncio'],
        'system': ['os', 'sys', 'subprocess', 'platform', 'shutil', 'stat'],
        'data': ['json', 'pickle', 'marshal', 'yaml', 'xml', 'csv'],
        'crypto': ['hashlib', 'hmac', 'ssl', 'cryptography', 'Crypto'],
        'compression': ['gzip', 'zipfile', 'tarfile', 'bz2', 'lzma'],
        'misc': ['time', 'datetime', 'calendar', 'logging', 'argparse', 'random']
    }
    
    results = {category: {} for category in categories}
    
    for module, imports in all_imports.items():
        for imp in imports:
            # For each import statement, check which category it belongs to
            for category, keywords in categories.items():
                for keyword in keywords:
                    if keyword.lower() in imp.lower():
                        if module not in results[category]:
                            results[category][module] = []
                        results[category][module].append(imp)
                        break
    
    return results

def extract_class_hierarchy(output_dir):
    """Extract class hierarchy and relationships"""
    print("Extracting class hierarchy...")
    
    classes_file = os.path.join(output_dir, 'class_details', 'all_classes.json')
    if not os.path.exists(classes_file):
        print("Classes file not found")
        return {}
        
    with open(classes_file, 'r') as f:
        all_classes = json.load(f)
        
    # Build inheritance hierarchy
    class_hierarchy = {}
    for module, classes in all_classes.items():
        for cls in classes:
            class_name = cls['name']
            parents = cls.get('parents', '')
            
            if parents:
                # Add to hierarchy
                parent_classes = [p.strip() for p in parents.split(',')]
                if class_name not in class_hierarchy:
                    class_hierarchy[class_name] = {
                        'module': module,
                        'parents': parent_classes,
                        'methods': [m['name'] for m in cls.get('methods', [])]
                    }
            else:
                # Base class
                if class_name not in class_hierarchy:
                    class_hierarchy[class_name] = {
                        'module': module,
                        'parents': [],
                        'methods': [m['name'] for m in cls.get('methods', [])]
                    }
    
    return class_hierarchy

def analyze_application_structure(output_dir):
    """Analyze the overall application structure"""
    print("Analyzing application structure...")
    
    # Extract core modules
    core_modules = []
    
    # Check module structure
    structure_file = os.path.join(output_dir, 'module_structure.md')
    if os.path.exists(structure_file):
        with open(structure_file, 'r') as f:
            content = f.read()
            
        # Find potentially important modules
        important_patterns = ['install', 'main', 'app', 'core', 'ui', 'config', 'util']
        for line in content.split('\n'):
            for pattern in important_patterns:
                if pattern in line.lower() and '.pyc' in line:
                    module_name = line.strip().split('.pyc')[0].strip('- ')
                    if module_name not in core_modules:
                        core_modules.append(module_name)
    
    return {
        'core_modules': core_modules
    }

def generate_findings_report(output_dir, results):
    """Generate a report of key findings"""
    print("Generating findings report...")
    
    report_file = os.path.join(output_dir, 'key_findings.md')
    
    with open(report_file, 'w') as f:
        f.write("# Key Findings from PYC Analysis\n\n")
        
        # Application structure
        f.write("## Core Application Modules\n\n")
        for module in results['app_structure']['core_modules']:
            f.write(f"- `{module}`\n")
        f.write("\n")
        
        # Class hierarchy
        f.write("## Key Classes\n\n")
        important_classes = {}
        for class_name, info in results['class_hierarchy'].items():
            # Filter to the most important classes
            if (class_name.startswith('_') and not class_name.startswith('__')) or \
               class_name in ('object', 'type', 'Exception', 'dict', 'list'):
                continue
                
            module = info['module']
            if module not in important_classes:
                important_classes[module] = []
            important_classes[module].append({
                'name': class_name,
                'parents': info['parents'],
                'methods': info['methods']
            })
        
        for module, classes in important_classes.items():
            if not classes:
                continue
            f.write(f"### Module: {module}\n\n")
            for cls in classes:
                parents = f" ({', '.join(cls['parents'])})" if cls['parents'] else ""
                f.write(f"- `{cls['name']}{parents}`\n")
                methods = cls['methods']
                if methods and len(methods) <= 10:  # Only show methods if there aren't too many
                    f.write("  - Methods: " + ", ".join([f"`{m}`" for m in methods]) + "\n")
                elif methods:
                    f.write(f"  - {len(methods)} methods\n")
            f.write("\n")
        
        # Function patterns
        f.write("## Notable Function Patterns\n\n")
        for category, modules in results['function_patterns'].items():
            if not any(modules.values()):
                continue
            f.write(f"### {category.replace('_', ' ').title()}\n\n")
            for module, functions in modules.items():
                if not functions:
                    continue
                f.write(f"- **{module}**: " + ", ".join([f"`{func['name']}`" for func in functions]) + "\n")
            f.write("\n")
        
        # Import patterns
        f.write("## Import Dependencies\n\n")
        for category, modules in results['import_patterns'].items():
            if not any(modules.values()):
                continue
            f.write(f"### {category.title()} Libraries\n\n")
            for module, imports in modules.items():
                if not imports:
                    continue
                f.write(f"- **{module}**: " + ", ".join([f"`{imp.split()[-1]}`" for imp in imports]) + "\n")
            f.write("\n")
        
        # Interesting strings
        f.write("## Interesting Strings\n\n")
        for file, strings in results['strings'].items():
            # Only show if there are at least a few interesting strings
            if len(strings) < 3:
                continue
            f.write(f"### {file}\n\n")
            for string in strings[:20]:  # Limit to first 20 strings
                if len(string) > 100:
                    string = string[:100] + "..."
                f.write(f"- `{string}`\n")
            if len(strings) > 20:
                f.write(f"- Plus {len(strings) - 20} more strings...\n")
            f.write("\n")
    
    print(f"Findings report saved to {report_file}")

def main():
    parser = argparse.ArgumentParser(description='Summarize PYC analysis results')
    parser.add_argument('output_dir', help='Directory containing analysis results')
    args = parser.parse_args()
    
    if not os.path.exists(args.output_dir):
        print(f"Error: Output directory '{args.output_dir}' does not exist.")
        return 1
    
    # Extract key information
    strings = extract_strings_from_disassembly(args.output_dir)
    function_patterns = extract_function_patterns(args.output_dir)
    import_patterns = extract_import_patterns(args.output_dir)
    class_hierarchy = extract_class_hierarchy(args.output_dir)
    app_structure = analyze_application_structure(args.output_dir)
    
    # Compile results
    results = {
        'strings': strings,
        'function_patterns': function_patterns,
        'import_patterns': import_patterns,
        'class_hierarchy': class_hierarchy,
        'app_structure': app_structure
    }
    
    # Generate report
    generate_findings_report(args.output_dir, results)
    
    return 0

if __name__ == '__main__':
    main()
