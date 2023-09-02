import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='A simple script to add two numbers.')

# Add arguments to the parser
parser.add_argument('num1', type=int, help='The first number')
parser.add_argument('num2', type=int, help='The second number')

# Parse the command line arguments
args = parser.parse_args()

# Perform the operation on the arguments
result = args.num1 + args.num2

# Display the result
print("Sum of {} and {} is: {}".format(args.num1, args.num2, result))
