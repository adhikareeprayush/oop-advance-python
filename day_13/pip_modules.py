import sys

print("Python module search path (sys.path):")
for path in sys.path:
    print("-", path)

try:
    import urllib3
    print("Module 'urllib3' is available!")
except ImportError:
    print("Module not found. Install via terminal: pip install urllib3")
