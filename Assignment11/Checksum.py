import hashlib

def hashfile(Dir_Path,blocksize =1024):
    File = open(Dir_Path, "rb")
    hasher = hashlib.md5()
    buf = File.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = File.read(blocksize)
    File.close()
    return hasher.hexdigest()