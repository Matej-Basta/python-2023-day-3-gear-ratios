import argparse

parser = argparse.ArgumentParser(description="This program solves day 3 challenge from Advent of Code 2023.")
parser.add_argument("input_file", metavar="input_file", type=str, help="enter the input file")
parser.add_argument("output_file", metavar="output_file", type=str, help="enter the output file")
args = parser.parse_args()

try:
    with open(args.input_file, "r") as input_file:
        with open(args.output_file, "w") as output_file:
            lines = []
            for line in input_file:
                lines.append(line.rstrip("\n"))
            print(lines)
            for index_line, line in enumerate(input_file):
                for index_character, character in enumerate(line):
                    if character.isdigit():
                        previous_line_index = index_line - 1 if 0 <= index_line - 1 < len(lines) else None
                        previous_character_index = line[index_character - 1] if 0 <= index_character - 1 < len(line) else None

except FileNotFoundError:
    print("The file does not exist!")
except:
    print("Something went wrong")