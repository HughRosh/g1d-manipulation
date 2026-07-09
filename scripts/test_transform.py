#!/usr/bin/env python3

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from geometry.transform import Transform

T = Transform.identity()

print(T)
print(T.as_matrix())
