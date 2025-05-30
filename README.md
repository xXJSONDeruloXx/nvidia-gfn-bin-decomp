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

## License

This analysis and documentation are provided for educational purposes. The original NVIDIA GeForce NOW software is proprietary and belongs to NVIDIA Corporation.
