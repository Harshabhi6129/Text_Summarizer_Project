from pathlib import Path
import os

# Convert relative path to absolute path
CONFIG_FILE_PATH = Path(os.getcwd()) / "config/config.yaml"
PARAMS_FILE_PATH = Path(os.getcwd()) / "params.yaml"

print(f"✅ Config file path resolved to: {CONFIG_FILE_PATH}")
