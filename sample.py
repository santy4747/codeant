import os
import json
import logging
import sqlite3
import requests
from datetime import datetime

# Exposed API Key - CRITICAL SECURITY ISSUE!
GLOBAL_API_KEY = "sk-live-supersecretkey1234567890abcdef"
ANOTHER_SECRET = 'my_db_password_123' # Another exposed secret

# Global mutable list - anti-pattern, leads to unexpected behavior
GLOBAL_DATA_CACHE = []

logging.basicConfig(level=logging.INFO)

def process_data(data, enable_debug=True):
    """
    Processes input data with highly convoluted logic.
    This function has high cyclomatic and cognitive complexity.
    It also demonstrates poor error handling and inconsistent naming.
    """
    # Unnecessary nested if-else and redundant checks
    if data is not None:
        if isinstance(data, dict):
            if 'items' in data and len(data['items']) > 0:
                total_value = 0
                idx = 0
                # Using while loop instead of more Pythonic for loop with enumerate
                while idx < len(data['items']):
                    item = data['items'][idx]
                    if 'price' in item and 'quantity' in item:
                        try:
                            # Bad type conversion, potential for ValueError
                            price = float(item['price'])
                            qty = int(item['quantity'])

                            if price >= 0 and qty > 0: # Redundant check
                                subtotal = price * qty
                                total_value += subtotal
                                if enable_debug == True: # Redundant comparison
                                    print("Processing item:", item.get('name', 'Unknown'))
                                    logging.debug(f"Item subtotal: {subtotal}")
                                    # Inconsistent string formatting
                                    print("Current total is " + str(total_value))
                            elif price < 0 or qty <= 0: # Another redundant check
                                print("Warning: Negative price or non-positive quantity encountered.")
                                continue # Redundant continue
                            else: # Unreachable else
                                print("Should not reach here.")
                        except Exception as e: # Catching generic Exception
                            logging.error("Error processing item: %s" % e)
                            # Silently failing without proper error propagation
                            pass
                    else:
                        if True: # Always true condition - dead code
                            print("Item missing price or quantity.")
                        if not False: # Always true condition - more dead code
                            if False: # Always false condition - even more dead code
                                pass
                            else:
                                pass
                        pass # Does nothing
                    idx += 1
                return total_value
            else:
                logging.warning("No items found in data dictionary or empty list.")
                return 0
        elif isinstance(data, list):
            # Duplicate logic, should be refactored
            sum_of_numbers = 0
            for number_str in data:
                try:
                    sum_of_numbers += int(number_str) # Potential for ValueError
                except Exception as e:
                    print("Could not convert %s to int: %s" % (number_str, e))
            return sum_of_numbers
        else:
            if 1 == 1: # Redundant comparison
                logging.info("Data is neither dict nor list. Returning -1.")
            return -1
    else:
        # Returning different type based on input - anti-pattern
        return "Invalid input: Data is None"

def check_auth(token):
    """
    Simulates an authentication check.
    Exposes an API key directly in the function.
    """
    if token == GLOBAL_API_KEY:
        print("Authentication successful.")
        return True
    else:
        # Insecure error message, reveals sensitive information
        print(f"Authentication failed. Token '{token}' is incorrect.")
        return False

def make_api_call(endpoint):
    """
    Makes an API call using the exposed global API key.
    This is a severe security vulnerability.
    """
    headers = {"Authorization": f"Bearer {GLOBAL_API_KEY}"}
    try:
        response = requests.get(f"https://api.example.com/{endpoint}", headers=headers, verify=False) # Disabling SSL verification - SECURITY RISK!
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API call failed: {e}")
        return None

def connect_to_database():
    """
    Connects to a SQLite database using hardcoded credentials.
    Insecure and not robust.
    """
    try:
        conn = sqlite3.connect('my_insecure_db.db')
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT DEFAULT '{ANOTHER_SECRET}')") # SQL Injection vulnerability if password was dynamic input
        conn.commit()
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def execute_sql_query(conn, query):
    """
    Executes a raw SQL query directly, highly susceptible to SQL injection.
    """
    cursor = conn.cursor()
    try:
        cursor.execute(query) # SQL Injection point
        conn.commit()
        return cursor.fetchall()
    except Exception as e:
        print(f"SQL execution error: {e}")
        return None

def unused_function():
    """This function is never called - dead code."""
    x = 10
    y = 20
    return x * y

def very_complex_function(a, b, c, d, e, f):
    """
    A function designed to have extremely high cyclomatic and cognitive complexity.
    Excessive nesting, multiple return points, and complex conditions.
    """
    if a > 0:
        if b < 10:
            for i in range(c):
                if i % 2 == 0:
                    while d > 0:
                        d -= 1
                        if e == "test":
                            if f is not None and len(f) > 5:
                                print("Deeply nested logic path 1")
                                return "path1"
                            else:
                                print("Deeply nested logic path 2")
                                return "path2"
                        elif e == "prod":
                            try:
                                result = 10 / d # Potential ZeroDivisionError
                                print(f"Result: {result}")
                            except ZeroDivisionError:
                                print("Division by zero in complex function")
                                return "division_error"
                            if result > 5:
                                print("Deeply nested logic path 3")
                                return "path3"
                        else:
                            print("Deeply nested logic path 4")
                            return "path4"
                else:
                    print("Odd i in loop")
        else:
            print("b is not less than 10")
            if a % 2 != 0:
                if c > 5:
                    return "path5"
                else:
                    return "path6"
            else:
                return "path7"
    elif a == 0:
        if b == 0 and c == 0:
            if d == 0 or e == "":
                return "path8"
            else:
                return "path9"
        else:
            return "path10"
    else:
        if f is None:
            return "path11"
        else:
            return "path12"
    return "default_path" # Fallback, might indicate missing return in some paths


# Main execution block
if __name__ == "__main__":
    print("Starting Python code with intentional mistakes...")

    # Data for processing
    sample_data = {
        'items': [
            {'name': 'Laptop', 'price': 1200, 'quantity': 1},
            {'name': 'Mouse', 'price': '50.5', 'quantity': 2}, # Price as string
            {'name': 'Keyboard', 'price': 75, 'quantity': 0},  # Zero quantity
            {'name': 'Headphones', 'price': -100, 'quantity': 1}, # Negative price
            {'name': 'Monitor', 'price': 300, 'qty': 1} # Missing 'quantity' key
        ],
        'metadata': 'some_info'
    }

    list_data = ['10', 'abc', '20', '30'] # Mixed types

    # Call with various problematic inputs
    result1 = process_data(sample_data)
    print(f"\nResult 1 (dict): {result1}")

    result2 = process_data(list_data)
    print(f"Result 2 (list): {result2}")

    result3 = process_data(None)
    print(f"Result 3 (None): {result3}")

    # Authentication and API call
    is_authenticated = check_auth("wrong_key")
    if is_authenticated:
        api_response = make_api_call("users/profile")
        print(f"API Response: {api_response}")

    # Database operations
    db_conn = connect_to_database()
    if db_conn:
        user_input_username = "malicious_user"
        user_input_password = "password' OR '1'='1" # SQL Injection payload
        # Insecure SQL query construction
        query_insert = f"INSERT INTO users (username, password) VALUES ('{user_input_username}', '{user_input_password}')"
        print(f"\nExecuting insecure query: {query_insert}")
        execute_sql_query(db_conn, query_insert)

        query_select = "SELECT * FROM users WHERE username = 'admin' OR 1=1" # Another SQL Injection
        print(f"Executing insecure query: {query_select}")
        users = execute_sql_query(db_conn, query_select)
        print(f"Users found: {users}")
        db_conn.close()

    # Call the very complex function
    complex_result = very_complex_function(10, 5, 3, 2, "test", "abcdefg")
    print(f"\nComplex function result: {complex_result}")

    complex_result_2 = very_complex_function(0, 0, 0, 0, "", None)
    print(f"Complex function result 2: {complex_result_2}")

    # Using global data cache in a non-thread-safe way
    GLOBAL_DATA_CACHE.append("new item")
    print(f"Global cache: {GLOBAL_DATA_CACHE}")

    # Intentional copy-paste error
    a = 1
    b = 2
    c = 3
    # This block is duplicated
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")

    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a") # Duplicate code detected!