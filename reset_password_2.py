# Simulated 'database' of users: username maps to a placeholder password
USER_DB = {
    "alice": "pass123",
    "bob": "secret456",
    "charlie": "mysecurepass"
}

def authenticate_user(username, password):
    """Checks if the provided username and password match the stored data."""
    if username in USER_DB and USER_DB[username] == password:
        return True
    return False

# --- Simulated Usage ---
print("--- Basic Login Validation ---")
user_input = input("Username: ")
pass_input = input("Password: ")

if authenticate_user(user_input, pass_input):
    print(f"Welcome, {user_input}! Login successful.")
else:
    print("Invalid username or password.")
