from src.cryptography import *
from src.blockchain.transaction import create_locking_script, hash_locking_script
from src.cryptography.cryptography import *
from src.cryptography.signature import verify_signature_from_public_key


def op_ripemd160(this):
    temp = this.pop()
    temp = get_ripemd_160_from_str(temp)
    this.push(temp)

def op_sha1(this):
    temp = this.pop()
    temp = get_sha_1_from_str(temp)
    this.push(temp)

def op_sha256(this):
    temp = this.pop()
    temp = get_sha_256_from_str(temp)
    this.push(temp)

def op_hash160(this):
    temp = this.pop()
    temp = get_hash_160_from_str(temp)
    this.push(temp)

def op_check_sig(this):
    pub_key = this.pop()
    trans_signature = this.pop()

    print(pub_key)

    print(trans_signature)


    reconstructed_message = create_locking_script(pub_key)
    reconstructed_message = hash_locking_script(reconstructed_message)

    ver = verify_signature_from_public_key(trans_signature, pub_key, reconstructed_message)

    print(ver)

    if ver:
        this.push(1)
    else:
        this.push(0)
