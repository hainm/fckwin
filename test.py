import os, sys

if sys.platform.startswith('win'):
    # set PATH to find libcpptraj.lib
    # we copy it (libcpptraj.lib) to pytraj folder during installation.
    os.environ['PATH'] = os.path.dirname(os.path.abspath(__file__)) + ';' + os.environ['PATH']
    msys = '/c/msys64/mingw64/bin/'
    os.environ['PATH'] = os.environ['PATH'] + ';' + msys
    print('PATH', os.environ['PATH'])

import pytraj
