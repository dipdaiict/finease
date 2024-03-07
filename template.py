# This is Base Skeleton Structure for Creating Project Structure Related Files

# Package for Interacting with Operating System
import os

# Package handle file paths in a platform (OS) -independent manner
from pathlib import Path

# Package for Log The Important Events
import logging

while True:
    project_name = input(
        "Enter the Project Name: "
    )  # Asking project Name While You do Not Give any name
    if project_name != "":
        break


# Log file Configuration:
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s",
    filename=f"{project_name}_project.log",  # Specify the filename for the log file
)

# format print the message like: [2024-03-01 15:30:45: INFO]: This is an informational message.

logging.info(f"Creating Project by Name: {project_name}")

# List of files Required for Project Structure:
list_of_files = [
    f"src/{project_name}/__init__.py",  # Package init file: To Consider all .py files as Pkg
    # Add Any other Files to Project Structure.....
]

# Code of Creating Files related to Projects:
for filepath in list_of_files:
    filepath = Path(filepath)  # To Handle Path based on Operating System
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        # Creating Empty Directory
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Creating Empty File
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")
