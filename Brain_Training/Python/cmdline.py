import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Advanced argparse example.")

# Add arguments
parser.add_argument("filename", type=str, help="The file to process")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
parser.add_argument("--lines", type=int, default=10, help="Number of lines to read (default: 10)")

# Parse the arguments
args = parser.parse_args()

# Use the arguments
if args.verbose:
    print(f"Processing file: {args.filename}")
print(f"Reading {args.lines} lines from {args.filename}")