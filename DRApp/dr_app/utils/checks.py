import hashlib


def check_md5(doc, checksum):

    m = hashlib.md5()
    m.update(str(doc))
    print m.hexdigest()
    if m.hexdigest() == checksum:
        return True
    else:
        return False
