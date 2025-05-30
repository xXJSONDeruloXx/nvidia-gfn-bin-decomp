# NVIDIA GeForce NOW Installer Decompilation Analysis

## Project Overview

This repository contains the analysis results from decompiling the NVIDIA GeForce NOW Linux installer (`GeForceNOWSetup.bin`). The primary goal is to understand the installer's internals and potentially modify it to work on a broader range of Linux distributions beyond just Steam Deck.

## Background

NVIDIA's GeForce NOW is a cloud gaming service that allows users to stream and play games from NVIDIA's servers. While NVIDIA has officially released a Linux installer, it appears to be primarily designed for SteamOS/Steam Deck with limited support for other Linux distributions.

## Repository Contents

- **Decompiled Python Code**: Python bytecode extracted and decompiled from the installer
- **Analysis Documents**:
  - `application_summary.md`: Overview of the application's structure and functionality
  - `technical_analysis.md`: Detailed technical breakdown of the installer
  - `key_findings.md`: Important discoveries from the decompilation
  - `module_structure.md`: Structure of the Python modules within the installer
  - `summary_report.md`: Comprehensive report of all findings
  - `classes_by_module.md`: Documentation of classes in each module
  - `functions_by_module.md`: Documentation of functions in each module
  - `import_dependencies.md`: Analysis of import dependencies between modules

## Key Findings

### System Requirements

The installer enforces the following requirements:

- **Disk Space**: Minimum 2GB of free space in the user's home directory
- **Operating System**: 
  - Focused on SteamOS with version checking (requires 3.6.19+)
  - References to flatpak suggest it's the primary installation method
- **Dependencies**:
  - Flatpak package manager
  - Various Flatpak runtimes including `org.freedesktop.Platform`
  - Steam client (for Steam integration features)

### Installation Process

The installer:
1. Checks system compatibility (OS, disk space)
2. Verifies dependencies (especially Flatpak)
3. Downloads and installs the GeForce NOW Flatpak package
4. Integrates with the desktop environment
5. Optionally adds itself to Steam for easier launching

### Steam Deck Specific Features

- Special handling for SteamOS version verification
- Custom controller configurations for Steam Deck
- Integration with the Steam library

## Modification Goals

The primary modifications needed to make the installer work on more Linux distributions include:

1. Bypassing or modifying the OS verification checks
2. Adjusting dependency checks for different package managers
3. Creating alternative installation paths for non-Flatpak environments
4. Generalizing the desktop integration for different Linux desktop environments

## Files of Interest

- `install_pycdc.py`: Main installer logic with system checks
- `install_ui.py`: UI implementation for the installer
- `platform_*.py`: Platform detection and compatibility logic

## Contributing

If you're interested in contributing to this project:

1. Examine the decompiled code and analysis documents
2. Focus on the OS detection and verification routines
3. Propose modifications that would allow installation on other Linux distributions
4. Test modifications on various Linux environments

## Disclaimer

This project is for educational and research purposes only. The goal is to improve Linux compatibility for GeForce NOW, not to circumvent any licensing or terms of service. All modifications should be used at your own risk.

## Decompilation Methodology

### Tools Used

The decompilation process utilized multiple Python bytecode decompilers to maximize the chances of successful code recovery:

1. **uncompyle6**: A Python bytecode decompiler supporting Python 2.7 to 3.8
2. **decompyle3**: Fork of uncompyle6 with improved Python 3.7+ support
3. **pycdc**: C++ based Python bytecode disassembler and decompiler
4. **pycdas**: Companion disassembler for pycdc, providing low-level bytecode analysis

### Extraction Process

1. The GeForce NOW installer (`GeForceNOWSetup.bin`) was identified as a PyInstaller-based executable
2. The executable was unpacked to extract the embedded Python bytecode files (`.pyc` files)
3. Multiple decompilation tools were applied to each bytecode file
4. Results were compared to identify the most complete and accurate decompiled source

### Scripts

The `scripts/` directory contains the following utilities:

- **pyc_decompiler.py**: Applies multiple decompilation tools to extracted `.pyc` files
- **pyc_analyzer.py**: Analyzes decompiled code to extract key information
- **pyc_analysis_summarizer.py**: Generates summary reports from analysis results
- **pyc_comprehensive_analyzer.py**: Combines analysis results into comprehensive reports

## Decompilation Results

### Successful Decompilation

We were able to successfully recover:

- The main system check routines that verify OS compatibility
- Disk space verification functions (requires 2GB minimum)
- UI implementation and localization mechanisms
- The overall installation flow and process
- Steam integration logic, particularly for Steam Deck

### Challenges and Limitations

The decompilation process encountered several challenges:

- Some functions were only partially recovered, with missing or corrupted code
- The complete implementation of `is_unsupported_os()` could not be fully decompiled
- Some Python bytecode versions were incompatible with available decompilers
- Control flow in complex functions was sometimes incorrectly reconstructed
- String constants were recovered, but their context wasn't always clear

Despite these challenges, we were able to extract enough information to understand the installer's system requirements, compatibility checks, and installation process.

## License

This analysis and documentation are provided for educational purposes. The original NVIDIA GeForce NOW software is proprietary and belongs to NVIDIA Corporation.
