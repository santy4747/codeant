# CodeAnt AI Demo Examples
# These examples demonstrate the types of issues CodeAnt AI can detect and fix

# Example 1: Security Vulnerability - SQL Injection

# Example 1 - FIXED VERSION (CodeAnt AI would suggest this)
def secure_login(username, password):
    """Fixed version using parameterized queries"""
    import sqlite3

    conn = sqlite3.connect('users.db')
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?", 
            (username, password)
        )
        result = cursor.fetchone()
    finally:
        conn.close()

    return result is not None

# Example 2: Code Quality Issues - Complex Function
def complex_function(data, option, flag, mode, setting):
    """
    Refactored to enhance readability and maintain the same behavior.
    """
    if option != 1:
        return data

    if not flag:
        return sorted(data)

    if mode != "advanced":
        return data[:10]

    if setting <= 5:
        return [x for x in data if x > 0]

    result = []
    for item in data:
        if item % 2 == 0:
            result.append(item * 2 if item > 10 else item)
        elif item < 50:
            result.append(item + 1)

    return result

# Example 2 - REFACTORED VERSION (CodeAnt AI would suggest improvements)
from typing import List, Literal

def process_numbers(
    numbers: List[int],
    operation: Literal["filter", "transform"] = "filter",
    use_advanced_mode: bool = False,
    threshold: int = 5
) -> List[int]:
    """
    Improved version with better structure and type hints
    """
    if operation == "filter":
        return _filter_numbers(numbers, use_advanced_mode, threshold)
    else:
        return _transform_numbers(numbers, use_advanced_mode, threshold)

def _filter_numbers(numbers: List[int], advanced: bool, threshold: int) -> List[int]:
    """Helper function for filtering logic"""
    if advanced and threshold > 5:
        return [num for num in numbers if num > 10 and num % 2 == 0]
    return [num for num in numbers if num > 0]

def _transform_numbers(numbers: List[int], advanced: bool, threshold: int) -> List[int]:
    """Helper function for transformation logic"""
    if advanced:
        return [num * 2 if num % 2 == 0 else num + 1 for num in numbers]
    return sorted(numbers)

# Example 3: Dead Code Detection
def unused_function():
    """
    This function is never called - CodeAnt AI would flag as dead code
    """
    print("This function is never used")
    return 42

def another_unused_function():
    """
    Another unused function
    """
    x = 10
    y = 20
    return x + y  # Simple calculation that's never used

# Example 4: Code Duplication
class UserManager:
    def create_admin_user(self, username, email):
        # Duplicate validation logic
        if not username or len(username) < 3:
            raise ValueError("Username must be at least 3 characters")
        if not email or "@" not in email:
            raise ValueError("Invalid email format")
        
        return {"username": username, "email": email, "role": "admin"}
    
    def create_regular_user(self, username, email):
        # Duplicate validation logic (CodeAnt AI would detect this)
        if not username or len(username) < 3:
            raise ValueError("Username must be at least 3 characters")
        if not email or "@" not in email:
            raise ValueError("Invalid email format")
        
        return {"username": username, "email": email, "role": "user"}

# Example 4 - REFACTORED VERSION
class ImprovedUserManager:
    def _validate_user_input(self, username: str, email: str) -> None:
        """Centralized validation logic"""
        if not username or len(username) < 3:
            raise ValueError("Username must be at least 3 characters")
        if not email or "@" not in email:
            raise ValueError("Invalid email format")
    
    def create_admin_user(self, username: str, email: str) -> dict:
        self._validate_user_input(username, email)
        return {"username": username, "email": email, "role": "admin"}
    
    def create_regular_user(self, username: str, email: str) -> dict:
        self._validate_user_input(username, email)
        return {"username": username, "email": email, "role": "user"}

# Example 5: Performance Issues
def inefficient_search(data, target):
    """
    Inefficient search algorithm - O(n²) complexity
    CodeAnt AI would suggest optimization
    """
    results = []
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] == target and i != j:
                results.append(i)
    return results

# Example 5 - OPTIMIZED VERSION
def efficient_search(data, target):
    """
    Optimized search - O(n) complexity
    """
    return [i for i, value in enumerate(data) if value == target]

# Example 6: Error Handling Issues
def risky_file_operation(filename):
    """
    Poor error handling - CodeAnt AI would flag this
    """
    file = open(filename, 'r')  # No error handling
    content = file.read()
    file.close()  # File might not close if error occurs
    return content.upper()

# Example 6 - IMPROVED VERSION
def safe_file_operation(filename):
    """
    Proper error handling and resource management
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content.upper()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

# Example 7: Memory Leak Potential
class ResourceLeaker:
    def __init__(self):
        self.connections = []
    
    def add_connection(self, conn):
        self.connections.append(conn)
        # Missing connection cleanup - potential memory leak
    
    def process_data(self):
        for conn in self.connections:
            # Process without proper cleanup
            pass

# Example 7 - FIXED VERSION
class ResourceManager:
    def __init__(self):
        self.connections = []
    
    def add_connection(self, conn):
        self.connections.append(conn)
    
    def cleanup_connections(self):
        """Proper resource cleanup"""
        for conn in self.connections:
            try:
                conn.close()
            except Exception as e:
                print(f"Error closing connection: {e}")
        self.connections.clear()
    
    def __del__(self):
        """Destructor for cleanup"""
        self.cleanup_connections()

# Example 8: Configuration Issues
# BAD: Hardcoded sensitive information
DATABASE_PASSWORD = "admin123"  # CodeAnt AI would flag as security risk
API_KEY = "sk-1234567890abcdef"  # Hardcoded API key

def connect_to_database():
    return f"Connecting with password: {DATABASE_PASSWORD}"

# GOOD: Using environment variables
import os
from typing import Optional

def get_database_password() -> Optional[str]:
    """Secure way to get database password"""
    return os.getenv('DATABASE_PASSWORD')

def get_api_key() -> Optional[str]:
    """Secure way to get API key"""
    return os.getenv('API_KEY')

def secure_database_connection() -> str:
    password = get_database_password()
    if not password:
        raise ValueError("Database password not found in environment variables")
    return f"Connecting securely..."

if __name__ == "__main__":
    # Demo the examples
    print("CodeAnt AI Demo Examples")
    print("=" * 40)
    
    # Test the improved functions
    print("1. Testing secure login (would need database setup)")
    print("2. Testing improved number processing:")
    
    numbers = [1, 2, 3, 4, 5, 10, 15, 20, 25]
    result = process_numbers(numbers, "filter", True, 6)
    print(f"   Filtered numbers: {result}")
    
    print("3. Testing improved user manager:")
    user_mgr = ImprovedUserManager()
    try:
        admin = user_mgr.create_admin_user("john_doe", "john@example.com")
        print(f"   Created admin: {admin}")
    except ValueError as e:
        print(f"   Validation error: {e}")
    
    print("4. Testing efficient search:")
    data = [1, 2, 3, 2, 4, 2, 5]
    indices = efficient_search(data, 2)
    print(f"   Found target at indices: {indices}")
    
    print("\nThese examples show the types of issues CodeAnt AI detects and fixes automatically!")
