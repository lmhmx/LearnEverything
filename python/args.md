# argparse

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--robot", type=str, help="help", default="robot")
args = parser.parse_args()
```