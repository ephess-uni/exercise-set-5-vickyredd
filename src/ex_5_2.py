""" ex_5_2.py
This module contains an entry point that

- loads data from a file `ex_5_2-data.csv` into a numpy array
- shifts and scales the data such that the resulting mean
        is 0 and the standard deviation is 1.
- writes the processed data to a file called `ex_5_2-processed.csv`
"""
import numpy as np # type: ignore

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root


if __name__ == "__main__":

    # Use these predefined input / output files
    root_dir = get_repository_root()
    INFILE = root_dir / "data" / "ex_5_2-data.csv"
    OUTFILE = root_dir / "outputs" / "ex_5_2-processed.csv"

    # Load the data from the input file
    data = np.loadtxt(INFILE, delimiter=",")

    # Shift and scale the data to have a mean of 0 and standard deviation of 1
    data_mean = np.mean(data)
    data_std = np.std(data)
    processed = (data - data_mean) / data_std

    # Save the processed data to the output file
    np.savetxt(OUTFILE, processed, delimiter=",")