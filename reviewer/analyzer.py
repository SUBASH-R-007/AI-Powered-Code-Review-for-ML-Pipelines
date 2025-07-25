# reviewer/analyzer.py

import ast
import re
from .rules import get_comprehensive_rules

class MLCodeReviewer:
    """
    Analyzes Python ML code based on a set of predefined rules.
    """

    def __init__(self):
        """Initializes the reviewer by loading the analysis rules."""
        self.rules = get_comprehensive_rules()

    def analyze_code(self, code):
        """
        Performs a comprehensive analysis of the given code snippet.

        Args:
            code (str): The Python code to analyze.

        Returns:
            list: A list of dictionaries, where each represents a found issue.
        """
        issues = []
        lines = code.splitlines()

        # Generic pattern-based checks
        for category, details in self.rules.items():
            severity = details.get('severity', 'suggestion')
            for pattern, message in details.get('patterns', []):
                if re.search(pattern, code, re.IGNORECASE):
                    line_num = self._find_line_for_pattern(lines, pattern)
                    issues.append({
                        'line': line_num,
                        'issue': message,
                        'severity': severity,
                        'category': category
                    })

        # Specific, more complex checks
        issues.extend(self._detect_scaling_issues(code, lines))
        issues.extend(self._ast_analysis(code))

        return self._deduplicate_issues(issues)

    def _find_line_for_pattern(self, lines, pattern):
        """Finds the first line number matching a regex pattern."""
        for i, line in enumerate(lines, 1):
            if re.search(pattern, line, re.IGNORECASE):
                return i
        return 1 # Default to line 1 if not found in a specific line

    def _detect_scaling_issues(self, code, lines):
        """Detects missing feature scaling for scale-sensitive algorithms."""
        issues = []
        rule_info = self.rules['feature_scaling']
        scale_sensitive = rule_info['scale_sensitive_algorithms']
        scalers = rule_info['scalers']

        for algorithm, full_name in scale_sensitive.items():
            if re.search(r'\b' + algorithm + r'\b', code) and not any(scaler in code for scaler in scalers):
                line_num = self._find_line_for_pattern(lines, r'\b' + algorithm + r'\b')
                issues.append({
                    'line': line_num,
                    'issue': f'{full_name} is sensitive to feature scaling. Consider using a scaler.',
                    'severity': 'warning',
                    'category': 'scaling'
                })
        return issues

    def _ast_analysis(self, code):
        """Performs AST-based analysis to find syntax errors."""
        issues = []
        try:
            ast.parse(code)
        except SyntaxError as e:
            issues.append({
                'line': e.lineno or 1,
                'issue': f'Syntax error: {e.msg}',
                'severity': 'error',
                'category': 'syntax'
            })
        return issues

    def _deduplicate_issues(self, issues):
        """Removes duplicate issues."""
        seen = set()
        unique_issues = []
        for issue in issues:
            identifier = (issue['issue'], issue.get('line', 1))
            if identifier not in seen:
                seen.add(identifier)
                unique_issues.append(issue)
        return unique_issues

    def generate_review_report(self, code):
        """Generates a formatted string report from the list of found issues."""
        issues = self.analyze_code(code)
        if not issues:
            return "✅ **Excellent!** No issues detected."

        report_parts = []
        severities = ['critical', 'error', 'warning', 'suggestion', 'positive']
        grouped_issues = {sev: [] for sev in severities}
        for issue in issues:
            grouped_issues[issue['severity']].append(issue)

        # Define icons for report
        icons = {'critical': '🚨', 'error': '❌', 'warning': '⚠️', 'suggestion': '💡', 'positive': '✅'}
        headers = {
            'critical': 'CRITICAL ISSUES (Fix Immediately)',
            'error': 'SYNTAX ERRORS',
            'warning': 'WARNINGS',
            'suggestion': 'SUGGESTIONS FOR IMPROVEMENT',
            'positive': 'GOOD PRACTICES DETECTED'
        }

        for sev in severities:
            if grouped_issues[sev]:
                report_parts.append(f"**{icons[sev]} {headers[sev]}:**")
                for issue in grouped_issues[sev]:
                    line_info = f"Line {issue['line']}: " if 'line' in issue and sev not in ['warning', 'suggestion', 'positive'] else ""
                    report_parts.append(f"- {line_info}{issue['issue']}")
                report_parts.append("")

        return "\n".join(report_parts)

