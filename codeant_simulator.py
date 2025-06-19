#!/usr/bin/env python3
"""
CodeAnt AI Simulator Demo
This script simulates CodeAnt AI's code analysis capabilities
Run this during your pitch to show real-time code analysis
"""

import re
import ast
import time
import random
from typing import List, Dict, Any
from datetime import datetime

class CodeAntSimulator:
    def __init__(self):
        self.issues_found = []
        self.analysis_results = {}
        
    def analyze_code(self, code: str, filename: str = "demo.py") -> Dict[str, Any]:
        """
        Simulate CodeAnt AI's comprehensive code analysis
        """
        print(f"\n🚀 CodeAnt AI Analysis Started for {filename}")
        print("=" * 60)
        
        # Simulate analysis delay
        self._animate_analysis()
        
        # Reset results
        self.issues_found = []
        
        # Run different types of analysis
        self._security_analysis(code)
        self._quality_analysis(code)
        self._performance_analysis(code)
        self._maintainability_analysis(code)
        self._dead_code_analysis(code)
        
        # Generate summary
        return self._generate_report(filename)
    
    def _animate_analysis(self):
        """Simulate real-time analysis animation"""
        stages = [
            "🔍 Scanning for security vulnerabilities...",
            "🛠️  Analyzing code quality patterns...",
            "⚡ Checking performance bottlenecks...",
            "📊 Evaluating maintainability metrics...",
            "🧹 Detecting dead code and duplicates...",
            "🤖 Generating AI recommendations..."
        ]
        
        for stage in stages:
            print(f"{stage}")
            time.sleep(0.8)  # Simulate processing time
    
    def _security_analysis(self, code: str):
        """Detect security vulnerabilities"""
        security_patterns = {
            r"SELECT.*FROM.*WHERE.*=.*\+": {
                "type": "CRITICAL",
                "issue": "SQL Injection Vulnerability",
                "description": "Direct string concatenation in SQL query",
                "fix": "Use parameterized queries instead",
                "line_pattern": "cursor.execute.*\+"
            },
            r"open\([^)]*\)(?!\s*with)": {
                "type": "HIGH",
                "issue": "Resource Leak Risk",
                "description": "File opened without proper context manager",
                "fix": "Use 'with open()' statement for automatic cleanup"
            },
            r"password.*=.*[\"'][^\"']+[\"']": {
                "type": "CRITICAL",
                "issue": "Hardcoded Password",
                "description": "Sensitive credentials exposed in source code",
                "fix": "Use environment variables or secure vault"
            },
            r"api[_-]?key.*=.*[\"'][^\"']+[\"']": {
                "type": "CRITICAL",
                "issue": "Hardcoded API Key",
                "description": "API key exposed in source code",
                "fix": "Store in environment variables"
            }
        }
        
        lines = code.split('\n')
        for i, line in enumerate(lines, 1):
            for pattern, details in security_patterns.items():
                if re.search(pattern, line, re.IGNORECASE):
                    self.issues_found.append({
                        "category": "Security",
                        "severity": details["type"],
                        "line": i,
                        "issue": details["issue"],
                        "description": details["description"],
                        "suggestion": details["fix"],
                        "code_snippet": line.strip()
                    })
    
    def _quality_analysis(self, code: str):
        """Analyze code quality issues"""
        lines = code.split('\n')
        
        # Check for long functions
        current_function = None
        function_lines = 0
        in_function = False
        
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            
            # Detect function definitions
            if stripped.startswith('def '):
                if in_function and function_lines > 20:
                    self.issues_found.append({
                        "category": "Code Quality",
                        "severity": "MEDIUM",
                        "line": i - function_lines,
                        "issue": "Function Too Long",
                        "description": f"Function has {function_lines} lines (recommended: <20)",
                        "suggestion": "Consider breaking into smaller functions",
                        "code_snippet": current_function
                    })
                
                current_function = stripped
                function_lines = 0
                in_function = True
            elif in_function:
                function_lines += 1
        
        # Check for complex conditions
        for i, line in enumerate(lines, 1):
            if_count = line.count('if') + line.count('elif')
            and_or_count = line.count(' and ') + line.count(' or ')
            
            if if_count > 0 and and_or_count > 2:
                self.issues_found.append({
                    "category": "Code Quality",
                    "severity": "MEDIUM",
                    "line": i,
                    "issue": "Complex Condition",
                    "description": "Condition too complex, hard to understand",
                    "suggestion": "Break into multiple conditions or use helper functions",
                    "code_snippet": line.strip()
                })
        
        # Check for missing type hints
        for i, line in enumerate(lines, 1):
            if line.strip().startswith('def ') and '->' not in line and '__init__' not in line:
                self.issues_found.append({
                    "category": "Code Quality",
                    "severity": "LOW",
                    "line": i,
                    "issue": "Missing Type Hints",
                    "description": "Function lacks return type annotation",
                    "suggestion": "Add type hints for better code documentation",
                    "code_snippet": line.strip()
                })
    
    def _performance_analysis(self, code: str):
        """Detect performance issues"""
        lines = code.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Detect nested loops
            if 'for' in line and any('for' in lines[j] for j in range(max(0, i-5), min(len(lines), i+5)) if j != i-1):
                self.issues_found.append({
                    "category": "Performance",
                    "severity": "HIGH",
                    "line": i,
                    "issue": "Nested Loop Detected",
                    "description": "Potential O(n²) time complexity",
                    "suggestion": "Consider using hash maps or more efficient algorithms",
                    "code_snippet": line.strip()
                })
            
            # Detect string concatenation in loops
            if 'for' in line and ('+=' in line or '+' in line) and 'str' in line.lower():
                self.issues_found.append({
                    "category": "Performance", 
                    "severity": "MEDIUM",
                    "line": i,
                    "issue": "Inefficient String Concatenation",
                    "description": "String concatenation in loop is inefficient",
                    "suggestion": "Use list.join() or f-strings instead",
                    "code_snippet": line.strip()
                })
    
    def _maintainability_analysis(self, code: str):
        """Check maintainability factors"""
        lines = code.split('\n')
        
        # Check for code duplication
        line_counts = {}
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if len(stripped) > 20 and not stripped.startswith('#'):
                if stripped in line_counts:
                    line_counts[stripped].append(i)
                else:
                    line_counts[stripped] = [i]
        
        for line_text, occurrences in line_counts.items():
            if len(occurrences) > 1:
                self.issues_found.append({
                    "category": "Maintainability",
                    "severity": "MEDIUM",
                    "line": occurrences[0],
                    "issue": "Code Duplication",
                    "description": f"Identical code found on lines: {', '.join(map(str, occurrences))}",
                    "suggestion": "Extract common code into a function",
                    "code_snippet": line_text
                })
    
    def _dead_code_analysis(self, code: str):
        """Detect unused code"""
        # Simple heuristic for unused functions
        function_names = re.findall(r'def\s+(\w+)', code)
        
        for func_name in function_names:
            # Count occurrences (definition + calls)
            occurrences = len(re.findall(rf'\b{func_name}\b', code))
            
            # If only found once (just the definition), it's likely unused
            if occurrences == 1 and func_name not in ['__init__', '__str__', '__repr__']:
                lines = code.split('\n')
                for i, line in enumerate(lines, 1):
                    if f'def {func_name}' in line:
                        self.issues_found.append({
                            "category": "Dead Code",
                            "severity": "LOW",
                            "line": i,
                            "issue": "Unused Function",
                            "description": f"Function '{func_name}' is defined but never called",
                            "suggestion": "Remove unused function or add usage",
                            "code_snippet": line.strip()
                        })
                        break
    
    def _generate_report(self, filename: str) -> Dict[str, Any]:
        """Generate comprehensive analysis report"""
        # Count issues by severity
        severity_counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
        category_counts = {}
        
        for issue in self.issues_found:
            severity_counts[issue["severity"]] += 1
            category = issue["category"]
            category_counts[category] = category_counts.get(category, 0) + 1
        
        # Calculate metrics
        total_issues = len(self.issues_found)
        code_lines = len([line for line in filename.split('\n') if line.strip()])
        
        report = {
            "filename": filename,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_issues": total_issues,
            "severity_breakdown": severity_counts,
            "category_breakdown": category_counts,
            "issues": self.issues_found,
            "metrics": {
                "code_lines": code_lines,
                "issues_per_100_lines": round((total_issues / max(code_lines, 1)) * 100, 2),
                "security_score": max(0, 100 - (severity_counts["CRITICAL"] * 25 + severity_counts["HIGH"] * 10)),
                "quality_score": max(0, 100 - (total_issues * 5))
            }
        }
        
        return report
    
    def print_report(self, report: Dict[str, Any]):
        """Print formatted analysis report"""
        print("\n" + "="*60)
        print("📊 CODEANT AI ANALYSIS REPORT")
        print("="*60)
        
        print(f"File: {report['filename']}")
        print(f"Analysis Time: {report['timestamp']}")
        print(f"Total Issues Found: {report['total_issues']}")
        
        # Severity breakdown
        print("\n🚨 SEVERITY BREAKDOWN:")
        for severity, count in report['severity_breakdown'].items():
            if count > 0:
                icon = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🔵"}
                print(f"   {icon[severity]} {severity}: {count}")
        
        # Category breakdown  
        print("\n📋 CATEGORY BREAKDOWN:")
        for category, count in report['category_breakdown'].items():
            icons = {
                "Security": "🔒", "Performance": "⚡", "Code Quality": "✨",
                "Maintainability": "🔧", "Dead Code": "🧹"
            }
            icon = icons.get(category, "📌")
            print(f"   {icon} {category}: {count}")
        
        # Metrics
        print(f"\n📈 CODE METRICS:")
        print(f"   Security Score: {report['metrics']['security_score']}/100")
        print(f"   Quality Score: {report['metrics']['quality_score']}/100")
        print(f"   Issues per 100 lines: {report['metrics']['issues_per_100_lines']}")
        
        # Top issues
        print(f"\n🔍 TOP ISSUES FOUND:")
        critical_and_high = [issue for issue in report['issues'] 
                           if issue['severity'] in ['CRITICAL', 'HIGH']]
        
        for i, issue in enumerate(critical_and_high[:5], 1):
            severity_icon = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🔵"}
            print(f"\n   {i}. {severity_icon[issue['severity']]} {issue['issue']} (Line {issue['line']})")
            print(f"      Category: {issue['category']}")
            print(f"      Description: {issue['description']}")
            print(f"      Suggestion: {issue['suggestion']}")
            print(f"      Code: {issue['code_snippet']}")
        
        # AI Recommendations
        print(f"\n🤖 AI RECOMMENDATIONS:")
        if report['total_issues'] == 0:
            print("   ✅ Excellent! No issues found. Your code follows best practices.")
        else:
            recommendations = self._generate_ai_recommendations(report)
            for i, rec in enumerate(recommendations, 1):
                print(f"   {i}. {rec}")
    
    def _generate_ai_recommendations(self, report: Dict[str, Any]) -> List[str]:
        """Generate AI-powered recommendations"""
        recommendations = []
        
        if report['severity_breakdown']['CRITICAL'] > 0:
            recommendations.append("🚨 URGENT: Address critical security vulnerabilities immediately")
        
        if report['category_breakdown'].get('Security', 0) > 2:
            recommendations.append("🔒 Consider implementing a security-first development approach")
        
        if report['category_breakdown'].get('Performance', 0) > 1:
            recommendations.append("⚡ Profile your code to identify performance bottlenecks")
        
        if report['category_breakdown'].get('Dead Code', 0) > 0:
            recommendations.append("🧹 Remove unused code to improve maintainability")
        
        if report['metrics']['quality_score'] < 80:
            recommendations.append("✨ Implement code review process and coding standards")
        
        if not recommendations:
            recommendations.append("🎉 Great code quality! Consider adding more comprehensive tests")
        
        return recommendations

def run_demo():
    """Run the CodeAnt AI demo"""
    print("🚀 Welcome to CodeAnt AI Demo!")
    print("This demonstration shows how CodeAnt AI analyzes code in real-time")
    
    # Sample problematic code for demonstration
    sample_code = '''
def vulnerable_login(username, password):
    import sqlite3
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result is not None

DATABASE_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"

def complex_function(data, option, flag, mode, setting):
    if option == 1:
        if flag:
            if mode == "advanced":
                if setting > 5:
                    result = []
                    for item in data:
                        if item % 2 == 0:
                            if item > 10:
                                result.append(item * 2)
                            else:
                                result.append(item)
                        else:
                            if item < 50:
                                result.append(item + 1)
                    return result

def unused_function():
    print("This function is never used")
    return 42

def risky_file_operation(filename):
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content.upper()
'''
    
    # Initialize CodeAnt simulator
    codeant = CodeAntSimulator()
    
    # Run analysis
    report = codeant.analyze_code(sample_code, "demo_problems.py")
    
    # Print results
    codeant.print_report(report)
    
    print("\n" + "="*60)
    print("✨ This is just a small sample of CodeAnt AI's capabilities!")
    print("In real usage, CodeAnt AI:")
    print("• Integrates directly with your IDE and Git workflow")
    print("• Provides real-time feedback as you type")
    print("• Offers one-click fixes for many issues")
    print("• Learns from your codebase patterns")
    print("• Generates comprehensive security reports")
    print("="*60)

if __name__ == "__main__":
    run_demo()
