import argparse

from markpoint import markpoint


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--original", help="the .mp to render")
    parser.add_argument("--target", help="the path to export")
    parser.add_argument("--type", help="the target output type")
    args = parser.parse_args()
    markpoint.render(args.original, args.target, args.type)

if __name__ == "__main__":
    main()