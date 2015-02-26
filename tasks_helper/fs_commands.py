import os, errno


def mkdirp(path):
    """\
    Equivalent of mkdir -p from the commandline.
    """
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

