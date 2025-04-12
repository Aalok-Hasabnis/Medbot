import os
from pathlib import Path
import logging

# Set up logging configuration
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

# List of files to create
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trails.ipynb"  # Fixed missing comma
]

# Create directories for each file in the list if they don't exist
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # If there is a directory path, create it
    if filedir != "":
        try:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Created directory: {filedir}")
        except Exception as e:
            logging.error(f"Error creating directory {filedir}: {e}")
    
    # If the file doesn't exist, you could optionally create an empty file
    if not filepath.exists():
        try:
            with open(filepath, 'w') as f:
                # Optionally add a comment or default content to the file
                f.write(f"# Created {filename}\n")
            logging.info(f"Created file: {filepath}")
        except Exception as e:
            logging.error(f"Error creating file {filepath}: {e}")
    else:
        logging.info(f"File {filepath} already exists.")
