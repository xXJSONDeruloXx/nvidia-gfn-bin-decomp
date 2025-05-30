# Source Generated with Decompyle++
# File: install.pyc (Python 3.10)

import os
import sys
import platform
import stat
import re
import shutil
import logging
import time
import subprocess
from install_ui import UI
import threading
import shutil
from translate import Translate
import fcntl
import vdf
ld_path = os.environ.get('LD_LIBRARY_PATH', '')
os.environ['LD_LIBRARY_PATH'] = f'''.:/usr/lib:/usr/lib/x86_64-linux-gnu:{ld_path}'''
VERSION = '1.0.0.6'
APP_NAME = 'NVIDIA GeForce NOW'
APP_NAME_TO_DISPLAY = 'GeForce NOW'
APP_ID = 'com.nvidia.geforcenow'
REQUIRED_DISK_SIZE = '2'
MSG_UNSUPPORTED_SYSTEM = 'Unsupported system!'
MSG_FLATPAK_NOT_FOUND = 'Flatpak not found!'
MSG_DISK_SIZE_LOW = f'''Disk size low. Minimum required is {REQUIRED_DISK_SIZE} GB'''
MSG_GENERIC_ERROR = f'''There was a problem setting up {APP_NAME} on your system.'''
MSG_UNINSTALL_CONFORMATION = f'''Do you really want to uninstall {APP_NAME} ?'''
MSG_UNINSTALL_COMPLETED = f'''{APP_NAME} has been successfully uninstalled.'''
MSG_UNINSTALL_FAILED = f'''There was a problem unstalling {APP_NAME} from your system.'''
MSG_STEAM_UNINSTALL_FAILED = 'Removal from Steam Library failed!'
MSG_STEAM_ADD_LIB_FAILED = 'Add to Steam Library failed!'
PREGRESS_TEXT_INSTALLING = 'Installing...'
PREGRESS_TEXT_UNINSTALLING = 'Uninstalling...'
PREGRESS_TEXT_DOWNLOADING = 'Downloading...'
PREGRESS_TEXT_ADD_TO_STEAM = 'Adding to Steam...'
PREGRESS_TEXT_REMOVE_FROM_STEAM = 'Removing from Steam...'
MSG_SETUP_COMPLETE_CONSOLE = f'''{APP_NAME} setup complete!'''
MSG_SETUP_START_CONSOLE = f'''Running {APP_NAME} Setup...'''
MSG_SETUP_RUNNING = 'An instance is already running. Exiting.'
LOG_FILE = 'GeForceNOWSetup.log'
LOCK_FILE = '/tmp/my_app.lock'
log_format = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
# WARNING: Decompyle incomplete
