#!/bin/sh

# This script makes a GET request to the Advent of Code input URL for the specified day
# and writes the output to a file. The request includes a "cookie" HTTP header with the
# value read from the file "./token.txt"

# Usage: ./get_request.sh <day> <output_file>

# Make sure a day is specified
if [ -z "$1" ]; then
    echo "Error: No day specified"
    exit 1
fi

# Check if the "./token.txt" file exists
if [ ! -f "./token.txt" ]; then
    echo "Error: Token file not found"
    exit 1
fi

# Check if the "./token.txt" file exists
if [ ! -d "./$1" ]; then
    $(mkdir $1)
fi

cp "./template.py" "$1/part1.py"
cp "./template.py" "$1/part2.py"
touch "$1/test-input.txt"

# Read the value of the "cookie" header from the file "./token.txt"
cookie=$(cat "./token.txt")

# Build the input URL for the specified day
input_url="https://adventofcode.com/2022/day/$1/input"

# Make the GET request with the "cookie" header and write the output to the specified file
curl -X GET -H "cookie: $cookie" "$input_url" > "$1/data.txt"
