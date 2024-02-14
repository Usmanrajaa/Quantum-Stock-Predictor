import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "Quantum-genreative-adversial-network-for stock price prediction"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"data/{project_name}/DS_Store",
    f"data/{project_name}/daily_adjusted_FB.csv",
    f"data/{project_name}/daily_adjusted_MSFT.csv",
    f"data/{project_name}/parserData.py",
    f"utils/{project_name}/__pycache__/__init__.cpython-36.pyc",
    f"utils/{project_name}/__pycache__/parser.cpython-36.pyc",
    f"utils/{project_name}/__init__.py",
    f"models/{project_name}/__pychache__",
    f"models/{project_name}/__pychache__/__init__.py",
    f"models/{project_name}/__pychache__/costs.txt",
    f"models/{project_name}/__pychache__/parser.py",
    f"models/{project_name}/__pychache__/qubits5.py",
    f"models/{project_name}/__pychache__/stats.pkl",
    f"models/{project_name}/__pychache__/stats45.pkl",
    f"models/{project_name}/__pychache__/stats49.pkl",
    f"models/{project_name}/__pychache__/text.py",
    f"models/{project_name}/__pychache__/train.py",
    f"models/{project_name}/__pychache__/utils.py",
    "DS_Store",
    "costs.txt",
    "research/trials.ipynb",

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")