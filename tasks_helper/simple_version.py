import os
from time import strftime

def get_major_version():
    """\
    The major version should always reside within the repository and should
    be incremended when major releases are made.
    """
    major_version = 0
    with open("configs/.major_version", "a+b") as f:
        try:
            major_version = int(f.read())
        except:
            major_version = 0
            f.seek(0)
            f.write(str(major_version))
            f.truncate()
    return major_version


def get_minor_version():
    """\
    Since the deployment process will be highly automated minor version
    numbers will be based on date and time. This causes problems when
    servers have different time zones.
    """
    return strftime("%Y%m%d~%H%M%S")


def get_minor_version_with_increment(domain):
    """\
    A file based approach for minor version numbers that just increments the
    value of a hidden file. This can't be used for automatics deployment,
    since version files can't be guaranteed to be up-to-date in the VCS.
    """
    minor_version = 0
    path_to_version = "configs/.%(domain)s.minor_version" % { "domain": domain }
    if not os.path.exists(path_to_version):
        with open(path_to_version, "w+b") as f:
            f.write("")
    with open(path_to_version, "rw+b") as f:
        try:
            minor_version = int(f.read())
            minor_version += 1
            f.seek(0)
            f.write(str(minor_version))
            f.truncate()
        except:
            minor_version = 0
            f.seek(0)
            f.write(str(minor_version))
            f.truncate()
    return minor_version
