VERSION = ['0', '1', '0']
FINAL=False
RELEASE="Shell Ninja"
SNAPTAG=None

def release_string():
    return RELEASE

def version_string():
    if FINAL:
        return '.'.join(filter(None, VERSION))
    else:
        return '.'.join(filter(None, VERSION))+"dev{0}".format(SNAPTAG)

