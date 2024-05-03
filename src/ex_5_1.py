import argparse
from ex_5_0 import line_count


def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program prints the number of lines in infile.")
    parser.add_argument("infile", help="Input file to count lines from")
    args = parser.parse_args()
    
    main(args.infile)
    
