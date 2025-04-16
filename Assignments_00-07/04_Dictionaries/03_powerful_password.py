import hashlib

def hash_password(password):
    """Returns the SHA-256 hash of the given password."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Verifies if the hashed password matches the stored hash for the given email.
    Returns True if login is successful, else False.
    """
    email = email.strip()
    password_to_check = password_to_check.strip()
    
    if email in stored_logins:
        return stored_logins[email] == hash_password(password_to_check)
    return False

def main():
    # Simulated stored logins (email -> hashed password)
    stored_logins = {
        "user@example.com": hash_password("securepassword123"),
        "kaladi@dev.com": hash_password("mysecretpass"),
    }

    print("\n🔐 Welcome to Secure Login Portal 🔐")
    print("------------------------------------")

    email = input("📧 Enter your email: ").strip()
    password = input("🔑 Enter your password: ").strip()

    if login(email, password, stored_logins):
        print("\n✅ Login successful! Welcome back.")
    else:
        print("\n❌ Login failed! Incorrect email or password.")

if __name__ == '__main__':
    main()
