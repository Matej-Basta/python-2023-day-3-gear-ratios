import argparse

def main():
    parser = argparse.ArgumentParser(description="This program solves day 3 challenge from Advent of Code 2023.")
    parser.add_argument("input_file", metavar="input_file", type=str, help="enter the input file")
    parser.add_argument("output_file", metavar="output_file", type=str, help="enter the output file")
    args = parser.parse_args()

    try:
        with open(args.input_file, "r") as input_file:
            with open(args.output_file, "w") as output_file:
                # creating a list of lines + adding boundaries, so there's no need to check for edge cases
                lines = []
                for line in input_file:
                    lines.append("." + line.rstrip("\n") + ".")
                boundary_line = "." * len(lines[0])
                lines.append(boundary_line)
                lines.insert(0, boundary_line)

                sum = 0
                for line_index, line in enumerate(lines):
                    is_in_number = False
                    number = 0
                    start_index = 0
                    end_index = 0
                    for index, ch in enumerate(line):
                        if ch.isdigit():
                            if not is_in_number:
                                start_index = index
                                is_in_number = True
                            number = number*10 + int(ch)
                        elif is_in_number:
                            end_index = index - 1
                            is_in_number = False
                            if has_adjacent_special_character(line_index, start_index, end_index, lines):
                                print(number)
                                sum += number
                            number = 0
                output_file.write(str(sum))

                            
    except FileNotFoundError:
        print("The file does not exist!")
    except:
        print("Something went wrong")


def is_special_character(ch):
    return not ch.isdigit() and ch != "."

def has_adjacent_special_character(line_index, start_index, end_index, lines):
    for i in range(line_index-1, line_index+2):
        for j in range(start_index-1, end_index+2):
            if is_special_character(lines[i][j]):
                return True
    return False


if __name__ == "__main__":
    main()