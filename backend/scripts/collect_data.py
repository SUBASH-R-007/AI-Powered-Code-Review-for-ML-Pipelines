import git
import os
import ast
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def collect_code_data(output_path: str):
    repos = [
        "https://github.com/scikit-learn/scikit-learn",
        "https://github.com/pytorch/examples"
    ]
    
    data = []
    temp_dir = Path("temp_repos")
    temp_dir.mkdir(exist_ok=True)
    
    for repo_url in repos:
        repo_name = repo_url.split("/")[-1]
        repo_path = temp_dir / repo_name
        
        try:
            # Clone repository
            git.Repo.clone_from(repo_url, repo_path)
            
            # Walk through repository
            for root, _, files in os.walk(repo_path):
                for file in files:
                    if file.endswith(".py"):
                        file_path = Path(root) / file
                        try:
                            with open(file_path, "r", encoding="utf-8") as f:
                                code = f.read()
                                # Try parsing to ensure valid Python
                                ast.parse(code)
                                data.append({
                                    "file": str(file_path),
                                    "code": code
                                })
                        except (SyntaxError, UnicodeDecodeError) as e:
                            logger.warning(f"Skipping {file_path}: {str(e)}")
                            
        except Exception as e:
            logger.error(f"Failed to process repo {repo_url}: {str(e)}")
    
    # Save collected data
    output_file = Path(output_path) / "code_data.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f)
    
    # Clean up
    # import shutil
    # shutil.rmtree(temp_dir)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    collect_code_data("./data")
