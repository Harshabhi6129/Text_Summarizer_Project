import os
from box.exceptions import BoxValueError
import yaml
from TextSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads YAML file and returns contents."""
    
    # Convert relative path to absolute path
    absolute_path = os.path.abspath(path_to_yaml)
    print(f"🔍 Trying to open YAML file at: {absolute_path}")

    try:
        with open(absolute_path, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            print("✅ YAML file loaded successfully!")
            return ConfigBox(content)
    except FileNotFoundError:
        print(f"❌ Error: File not found at {absolute_path}")
        raise


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

    