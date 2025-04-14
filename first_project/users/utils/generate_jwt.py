import base64
import hmac
import hashlib
import json
import time
from django.conf import settings

def base64_url_encode(data):
    """Encodes JSON to Base64 URL-safe string (without padding)."""
    return base64.urlsafe_b64encode(json.dumps(data).encode()).rstrip(b'=').decode()

def base64_url_decode(data):
    """Decodes Base64 URL-safe string back to JSON."""
    padding = "=" * (4 - len(data) % 4)  # Add padding if needed
    return json.loads(base64.urlsafe_b64decode(data + padding).decode())

def generate_jwt(user):
    """Creates a JWT manually."""
    header = {"alg": "HS256", "typ": "JWT"}
    payload = {
        "id": user.id,
        "username": user.username,
        "exp": int(time.time()) + 86400,  # Token expires in 24 hours
        "iat": int(time.time()),
    }

    secret_key = settings.SECRET_KEY.encode()  # Use settings.SECRET_KEY

    # Encode header & payload
    encoded_header = base64_url_encode(header)
    encoded_payload = base64_url_encode(payload)

    # Create signature (HMAC-SHA256)
    signature = hmac.new(secret_key, f"{encoded_header}.{encoded_payload}".encode(), hashlib.sha256).digest()
    encoded_signature = base64.urlsafe_b64encode(signature).rstrip(b'=').decode()

    return f"{encoded_header}.{encoded_payload}.{encoded_signature}"

def decode_jwt(token):
    """Validates and decodes JWT manually."""
    try:
        # Split token into parts
        encoded_header, encoded_payload, encoded_signature = token.split(".")

        # Decode header & payload
        header = base64_url_decode(encoded_header)
        payload = base64_url_decode(encoded_payload)

        # Verify expiration
        if payload.get("exp") < int(time.time()):
            return None  # Token expired

        # Recreate signature and compare
        secret_key = settings.SECRET_KEY.encode()
        expected_signature = hmac.new(secret_key, f"{encoded_header}.{encoded_payload}".encode(), hashlib.sha256).digest()
        expected_signature_encoded = base64.urlsafe_b64encode(expected_signature).rstrip(b'=').decode()

        if encoded_signature != expected_signature_encoded:
            return None  # Invalid signature

        return payload  # Return decoded data if valid
    except Exception:
        return None  # Invalid token
