import sys
from .core import show

def main():

    if len(sys.argv)!=2:
        print("Usage: python3 -m microheaders <host>")
        return

    show(sys.argv[1])
