import os
from pathlib import Path

# ROOT_DIR_cwd = Path(__file__).cwd().parent
ROOT_DIR = Path(__file__).resolve().parent.parent
STATIC_FILES_DIR = os.path.join(ROOT_DIR, 'static_files')
STATIC_URL = '/static/'