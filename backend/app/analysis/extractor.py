import ast
from .rules import check_data_leakage, check_inefficient_iteration, check_hardcoded_paths, \
    check_missing_docstrings, check_reproducibility
import logging

logger = logging.getLogger(__name__)

def analyze_code(code: str) -> list:
    """Analyze code using all registered rules."""
    issues = []
    try:
        tree = ast.parse(code)
        
        # Apply all rules
        rules = [
            check_data_leakage,
            check_inefficient_iteration,
            check_hardcoded_paths,
            check_missing_docstrings,
            check_reproducibility
        ]
        
        for rule in rules:
            try:
                result = rule(tree)
                if result:
                    issues.append(result)
            except Exception as e:
                logger.warning(f"Rule {rule.__name__} failed: {str(e)}")
                
        return issues
    except SyntaxError as e:
        logger.error(f"Syntax error in code: {str(e)}")
        return [{
            "issue_type": "SyntaxError",
            "message": f"Invalid Python syntax: {str(e)}",
            "line_number": getattr(e, 'lineno', None)
        }]
    except Exception as e:
        logger.error(f"Error analyzing code: {str(e)}")
        return [{
            "issue_type": "AnalysisError",
            "message": f"Error analyzing code: {str(e)}"
        }]