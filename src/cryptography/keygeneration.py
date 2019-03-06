##############################################################
###
### This file handles all key generation for the blockchain
### That is it goes from generating a public/private
### key pair all the way to generating blockchain addresses.
###
###
### A nice tutorial of how the public address is generated can be found at:
### https://medium.com/coinmonks/elliptic-curve-cryptography-6de8fc748b8b
###
### Also this reddit thread was heavily used:
### https://www.reddit.com/r/Bitcoin/comments/7tzq3w/generate_your_own_private_key_5_lines_of_python/
###
##############################################################


##############################################################
# Imports
##############################################################
import codecs
import os, binascii, hashlib, base58, ecdsa


##############################################################
# Functions
##############################################################

def ripemd160(x):
    d = hashlib.new('ripemd160')
    d.update(x)
    return d


def recreate_public_key(private_key):

    private_key = base58.b58decode(private_key)

    private_key = binascii.hexlify(private_key)
    private_key = private_key[:-8]
    private_key = private_key[2:]
    private_key = binascii.unhexlify(private_key)

    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    public_key = '04' + binascii.hexlify(vk.to_string()).decode()

    return public_key


def generate_keypair():
    # generate private key , uncompressed WIF starts with "5" (that is 0x80)
    priv_key = os.urandom(32)
    fullkey = '80' + binascii.hexlify(priv_key).decode()
    sha256a = hashlib.sha256(binascii.unhexlify(fullkey)).hexdigest()
    sha256b = hashlib.sha256(binascii.unhexlify(sha256a)).hexdigest()
    temp = binascii.unhexlify(fullkey + sha256b[:8])
    WIF = base58.b58encode(temp)

    # Generate public key, The uncompressed address starts with "1"
    sk = ecdsa.SigningKey.from_string(priv_key, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    pub_key = '04' + binascii.hexlify(vk.to_string()).decode()

    return WIF, pub_key


def generate_public_address(pub_key):
    '''
    '''

    hash160 = ripemd160(hashlib.sha256(binascii.unhexlify(pub_key)).digest()).digest()
    publ_addr_a = b"\x00" + hash160
    checksum = hashlib.sha256(hashlib.sha256(publ_addr_a).digest()).digest()[:4]
    publ_addr_b = base58.b58encode(publ_addr_a + checksum)

    return publ_addr_b


##############################################################
# Driver code to test this file
##############################################################


if __name__ == '__main__':
    pri, pub = generate_keypair()
    public_address = generate_public_address(pub)

    print("Private Key     : " + pri.decode())
    print("Public Key     ,: " + pub)
    print("Bitcoin Address,: " + public_address.decode())


    recreated = recreate_public_key(pri)


    print("Recreated Public Key: " + recreated)
