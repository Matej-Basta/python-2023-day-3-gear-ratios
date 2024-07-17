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

                

    except FileNotFoundError:
        print("File does not exist.")
    except:
        print("Something went wrong.")

if __name__ == "__main__":
    main()