import secrets

def generate_secret_key(length=32):
  """Generates a secure secret key of specified length (in bytes)."""
  return secrets.token_bytes(length)

# Example usage
secret_key = generate_secret_key()

# Convert to hex string for display
secret_key_hex = secret_key.hex()
print("Secret key (hex):", secret_key_hex)