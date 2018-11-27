import hashlib


def get_sha_256_from_str(str_input):
    m = hashlib.sha256()
    m.update(str_input.encode('utf-8'))
    return m.digest()


def get_sha_256_from_bytes(byte_input):
    m = hashlib.sha256()
    m.update(byte_input)
    return m.digest()


def get_ripemd_160_from_str(str_input):
    m = hashlib.ripemd160()
    m.update(str_input.encode('utf-8'))
    return m.digest()


def get_ripemd_160_from_bytes(byte_input):
    m = hashlib.ripemd160()
    m.update(byte_input)
    return m.digest()


def get_sha_1_from_str(str_input):
    m = hashlib.sha1()
    m.update(str_input.encode('utf-8'))
    return m.digest()


def get_sha_1_from_bytes(byte_input):
    m = hashlib.sha1()
    m.update(byte_input)
    return m.digest()


def get_hash_160_from_str(str_input):
    # Return RIPEMD160(SHA256(x)) hash
    r = hashlib.new('ripemd160')

    r.update(str_input.encode('utf-8'))
    s = hashlib.sha256()
    s.update(r.digest())
    return s.digest()


def get_hash_160_from_bytes(byte_input):
    # Return RIPEMD160(SHA256(x)) hash
    r = hashlib.new('ripemd160')
    r.update(byte_input)
    s = hashlib.sha256()
    s.update(r.digest())
    return s.digest()



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
    first = this.pop()
    second = this.pop()

    if first == second:
        this.push(1)
    else:
        this.push(0)
