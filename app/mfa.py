import pyotp

def generate_mfa_secret():
    return pyotp.random_base32()

def get_mfa_uri(username, secret):
    return pyotp.totp.TOTP(secret).provisioning_uri(username, issuer_name="SOC Automation")

def verify_mfa(secret, otp):
    totp = pyotp.TOTP(secret)
    return totp.verify(otp)
