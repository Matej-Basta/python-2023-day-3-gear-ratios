try:
    with open("test.txt", "r") as input_file:
        with open("output_file.txt", "w") as output_file:
            print("here")
except FileNotFoundError:
    print("The file does not exist!")
except:
    print("Something went wrong")