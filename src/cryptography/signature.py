################################################################
# Contains functions that are used to sign and verify signatures
################################################################
import ecdsa
import base58
import binascii

from ecdsa.keys import BadSignatureError


def create_signature(secret_key, message):
    # SECP256k1 is the Bitcoin elliptic curve

    secret_key = base58.b58decode(secret_key)

    secret_key = secret_key[1:]  # Remove first byte for version
    secret_key = secret_key[:-4]  # Remove last 4 bytes for checksum

    signing_key = ecdsa.SigningKey.from_string(secret_key, curve=ecdsa.SECP256k1)

    if isinstance(message, str):
        message = binascii.hexlify(message.encode('utf-8'))

    signature = signing_key.sign(message)
    return signature


def verify_signature_from_public_key(signature, public_key, message):
    public_key = public_key[2:]  # The first byte is some control byte

    try:
        verifying_key = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)
    except AssertionError:
        return False

    if isinstance(message, str):
        message = binascii.hexlify(message.encode('utf-8'))

    if isinstance(signature, str):
        signature = bytes.fromhex(signature)

    try:
        result = verifying_key.verify(signature, message)  # True
    except BadSignatureError:
        return False

    return result

