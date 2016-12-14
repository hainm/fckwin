import os, sys

if sys.platform.startswith('win'):
    # set PATH to find libcpptraj.lib
    # we copy it (libcpptraj.lib) to pytraj folder during installation.
    os.environ['PATH'] = os.path.dirname(os.path.abspath(__file__)) + ';' + os.environ['PATH']
    msys_bin = '/c/msys64/mingw64/bin/'
    msys_lib = '/c/msys64/mingw64/lib/'
    os.environ['PATH'] = ';'.join((os.environ['PATH'], msys_bin, msys_lib))
    print('PATH', os.environ['PATH'])

import pytraj
