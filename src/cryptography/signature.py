################################################################
# Contains functions that are used to sign and verify signatures
################################################################
import ecdsa
import base58
import binascii


def create_signature(message, secret_key):
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
    public_key = public_key[2:]  # The first byte is some contorll byte

    print(signature)
    print(public_key)

    verifying_key = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)

    if isinstance(message, str):
        message = binascii.hexlify(message.encode('utf-8'))

    if isinstance(signature, str):
        signature = bytes.fromhex(signature)

    result = verifying_key.verify(signature, message)  # True

    return result


mes = 'hej'
key = '5KZgGoqV1XCxx25m6ZiPKnGzzZvAwiA9jDSV82rBYGfYSHJMHMc'
public = '04b7761ef5e31b46fa7549e8cbd4e1027fec33ccee9c3df1e2f51d29e3e332c4c8e0859e76587491ca38761067c4fa1a6c188604e0fea8a7d089dfda25ea437be4'
signature = create_signature(mes, key)

a = verify_signature_from_public_key(signature, public, mes)

print(a)

mes = 'hej'
key = '5KZgGoqV1XCxx25m6ZiPKnGzzZvAwiA9jDSV82rBYGfYSHJMHMc'
public = '04b7761ef5e31b46fa7549e8cbd4e1027fec33ccee9c3df1e2f51d29e3e332c4c8e0859e76587491ca38761067c4fa1a6c188604e0fea8a7d089dfda25ea437be4'
signature = create_signature(mes, key)

mes = 'hej'
public = '04c7761ef5e31b46fa7549e8cbd4e1027fec33ccee9c3df1e2f51d29e3e332c4c8e0859e76587491ca38761067c4fa1a6c188604e0fea8a7d089dfda25ea437be4'
a = verify_signature_from_public_key(signature, public, mes)

print(a)
