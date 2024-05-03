""" ex_5_3.py
This module contains an entry point that:

- creates a CLI that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np # type: ignore
from argparse import ArgumentParser

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root

def process_data(infile, outfile):
    """
    Load data from infile, apply standard scale transform, and write to outfile.
    """
    # Load the data from the input file
    data = np.loadtxt(infile, delimiter=",")

    # Shift and scale the data to have a mean of 0 and standard deviation of 1
    data_mean = np.mean(data)
    data_std = np.std(data)
    processed = (data - data_mean) / data_std

    # Save the processed data to the output file
    np.savetxt(outfile, processed, delimiter=",")

if __name__ == "__main__":
    parser = ArgumentParser(description="This program applies a standard scale transform to the data in infile and writes it to outfile.")
    parser.add_argument("infile", help="Input filename")
    parser.add_argument("outfile", help="Output filename")
    args = parser.parse_args()

    # Use the predefined input/output files if running from the command line
    root_dir = get_repository_root()
    infile = root_dir / "data" / args.infile
    outfile = root_dir / "outputs" / args.outfile

    process_data(infile, outfile)