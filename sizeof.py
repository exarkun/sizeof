from sys import argv

from cffi import FFI

ffi = FFI()
ffi.cdef("""
static const int thesize;
""")
lib = ffi.verify("""
#include <%s>
const int thesize = sizeof(%s);
""" % (argv[1], argv[2]))
print lib.thesize


