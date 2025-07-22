import ast

def check_data_leakage(tree: ast.AST) -> dict | None:
    """Check for data leakage by detecting transformer fit before train_test_split."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == 'fit' and isinstance(node.func.value, ast.Name):
                transformer_names = ['StandardScaler', 'MinMaxScaler']
                if node.func.value.id in transformer_names:
                    # Check if train_test_split appears after
                    for sibling in ast.walk(tree):
                        if isinstance(sibling, ast.Call) and isinstance(sibling.func, ast.Name):
                            if sibling.func.id == 'train_test_split':
                                return {
                                    "issue_type": "DataLeakage",
                                    "message": f"Potential data leakage: {node.func.value.id}.fit() called before train_test_split",
                                    "line_number": node.lineno
                                }
    return None

def check_inefficient_iteration(tree: ast.AST) -> dict | None:
    """Check for inefficient pandas iterrows usage."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == 'iterrows':
                return {
                    "issue_type": "InefficientIteration",
                    "message": "Use of pandas.iterrows() detected. Consider vectorized operations or itertuples()",
                    "line_number": node.lineno
                }
    return None

# def check_hardcoded_paths(tree: ast.AST) -> dict | None:
#     """Check for hardcoded file paths."""
#     for node in ast.walk(tree):
#         if isinstance(node, ast.Str):
#             if node.s.startswith(('/', 'C:\\')):
#                 return {
#                     "issue_type": "HardcodedPath",
#                     "message": f"Hardcoded path detected: {node.s}",
#                     "line_number": node.lineno
#                 }
#     return None
def check_hardcoded_paths(tree: ast.AST) -> dict | None:
    """Check for hardcoded file paths."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if node.value.startswith(('/', 'C:\\')):
                return {
                    "issue_type": "HardcodedPath",
                    "message": f"Hardcoded path detected: {node.value}",
                    "line_number": node.lineno
                }
    return None

def check_missing_docstrings(tree: ast.AST) -> dict | None:
    """Check for missing docstrings in functions and classes."""
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if not ast.get_docstring(node):
                return {
                    "issue_type": "MissingDocstring",
                    "message": f"Missing docstring for {node.name}",
                    "line_number": node.lineno
                }
    return None
import logging
import ast

logger = logging.getLogger(__name__)

def check_reproducibility(tree: ast.AST) -> dict | None:
    """Check for missing random seed settings."""
    seed_functions = ['random.seed', 'np.random.seed', 'torch.manual_seed']
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            try:
                if isinstance(node.func, ast.Attribute):
                    func_value_id = getattr(node.func.value, 'id', None)
                    if func_value_id and f"{func_value_id}.{node.func.attr}" in seed_functions:
                        return None
                elif isinstance(node.func, ast.Name):
                    func_id = getattr(node.func, 'id', None)
                    if func_id and func_id in seed_functions:
                        return None
            except AttributeError:
                logger.warning(f"Rule check_reproducibility failed: {type(node).__name__} object has no attribute 'id'")
                continue
    return {
        "issue_type": "Reproducibility",
        "message": "No random seed set for reproducibility",
        "line_number": 1
    }