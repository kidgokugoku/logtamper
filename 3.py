from time import strptime, mktime
import struct
from pathlib import Path
import sys

LASTLOGFILE = Path("/var/log/lastlog")
LAST_STRUCT = "I32s256s"
LAST_STRUCT_SIZE = struct.calcsize(LAST_STRUCT)

if not sys.argv[1]:
    quit
timestamp = 0
try:
    str2time = strptime(sys.argv[1], "%Y:%m:%d:%H:%M:%S")
    timestamp = int(mktime(str2time))
except Exception:
    print("Time format err.")
    quit
data = struct.pack(LAST_STRUCT, timestamp, b"pts/0", "localhost")
try:
    fp = open(LASTLOGFILE, "wb")
    fp.write(data)
except Exception:
    print(f"Cannot open file: {LASTLOGFILE}")
finally:
    fp.close()
