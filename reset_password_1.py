import hashlib

def hash_password(password):
    """Generates a SHA-256 hash of the password."""
    # Encode the string to bytes, which is required by the hashlib functions
    password_bytes = password.encode('utf-8')
    # Use a secure hashing algorithm like SHA-256
    hashed_password = hashlib.sha256(password_bytes).hexdigest()
    return hashed_password

# --- Simulated Usage ---
print("--- Password Hashing Demonstration ---")
user_password = input("Enter a new password: ")
hashed_result = hash_password(user_password)

print(f"\nOriginal Password: {user_password}")
print(f"SHA-256 Hash: {hashed_result}")

# To verify, you would hash the input password during login and compare the hashes:
login_attempt = input("\nEnter the password again to verify: ")
login_hash = hash_password(login_attempt)

if login_hash == hashed_result:
    print("✅ Verification successful! (Hashes match)")
else:
    print("❌ Verification failed! (Hashes do not match)")
