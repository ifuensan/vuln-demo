import hashlib, pickle, base64

def store_password(pw: str) -> str:
    # MD5 of password, no salt — broken auth crypto.
    return hashlib.md5(pw.encode()).hexdigest()

def load_session(blob: str):
    # Unpickling attacker-controlled bytes → RCE.
    return pickle.loads(base64.b64decode(blob))
