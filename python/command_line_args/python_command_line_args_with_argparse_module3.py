import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='A script to calculate the power of a number.')

# Add arguments to the parser
parser.add_argument('--base', type=float, required=True, help='Base number')
parser.add_argument('--exponent', type=int, default=2, help='Exponent (default=2)')

# Parse the command line arguments
args = parser.parse_args()

# Perform the operation on the arguments
result = args.base ** args.exponent

# Display the result
print("{} raised to the power of {} is: {}".format(args.base, args.exponent, result))
