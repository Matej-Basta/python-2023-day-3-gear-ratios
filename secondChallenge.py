import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    try:
        with open(args.input_file, "r") as input_file:
            with open(args.output_file, "w") as output_file:
                lines = []
                for line in input_file.readlines():
                    lines.append("." + line.strip("\n") + ".")
                boundary_line = "." * len(lines[0])
                lines.insert(0, boundary_line)
                lines.append(boundary_line)

                sum = 0
                number_storage = {}
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
                            if gear := get_adjacent_gear(line_index, start_index, end_index, lines):
                                if prev_number := number_storage.get(gear):
                                    sum += number * prev_number
                                else:
                                    number_storage[gear] = number
                            number = 0
                print(sum)
                output_file.write(str(sum))

    except FileNotFoundError:
        print("File does not exist.")
    except:
        print("Something went wrong.")

def is_gear(ch):
    return ch == "*"

def get_adjacent_gear(line_index, start_index, end_index, lines):
    for i in range(line_index-1, line_index+2):
        for j in range(start_index-1, end_index+2):
            if is_gear(lines[i][j]):
                return (i, j)
    return None

if __name__ == "__main__":
    main()