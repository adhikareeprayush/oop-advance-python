import sys
# sys gives access to functions/variables maintained by interpreter eg: sys.version, sys.executable
import platform
# platform gives info about os eg: platform.system(), platform.release()

print("Python Version:", sys.version)
print("Platform/OS:", platform.system())
print("Executable Path (Python):", sys.executable)
print("Platform Machine (Architecture):", platform.machine())
print("Platform Node (Hostname):", platform.node())
print("Platform Processor (Type):", platform.processor())
print("Platform Release (Version):", platform.release())