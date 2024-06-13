#!/usr/bin/env python

import shutil
import sys

required_commands = ["mash", "calc", "bc", "fmt", "datasets", "esummary", "xtract", "wget", "JolyTree.sh", "fastANI", "blastn", "bPTP.py"]

missing_commands = [cmd for cmd in required_commands if shutil.which(cmd) is None]

if missing_commands:
    print("**** Warning: The following commands are missing:", file=sys.stderr)
    print(", ".join(missing_commands), file=sys.stderr)
    print("Please install it, as it is a requirement to run GenomeScanner", file=sys.stderr)
    print("****\n", file=sys.stderr)
    sys.exit(1)
# ~ else:
    # ~ print("\nAll required commands are available\n")
