import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='A script to calculate the area of a rectangle.')

# Add arguments to the parser
parser.add_argument('--length', type=float, required=True, help='Length of the rectangle')
parser.add_argument('--width', type=float, required=True, help='Width of the rectangle')

# Parse the command line arguments
args = parser.parse_args()

# Perform the operation on the arguments
area = args.length * args.width

# Display the result
print("Area of rectangle with length {} and width {} is: {}".format(args.length, args.width, area))
