import argparse
import sys


def build_parser():
    p = argparse.ArgumentParser(prog="greet")
    p.add_argument("name", nargs="?", default="world")
    p.add_argument("--shout", action="store_true")
    p.add_argument("--version", action="version", version="greet 0.1.0")
    return p


def greet(name, shout=False):
    msg = f"Hello, {name}!"
    return msg.upper() if shout else msg


def main(argv=None):
    args = build_parser().parse_args(argv)
    print(greet(args.name, args.shout))
    return 0


if __name__ == "__main__":
    sys.exit(main())
