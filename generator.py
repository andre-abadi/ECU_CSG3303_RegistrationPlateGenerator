"""ECU CSG3303 Assignment - Photometer - Random License Plate Generator"""
import random

"""
This program generates a text file of random vehicle registration plate
combinations that are valid in Western Australia. The scope of generation
is limited to standard aluminium plates with the blue Western Australia
top-bar. Plates are either custom, which is between 3 and 7 characters
with the leading character not being a space, or a standard plate.
Standard plates are generated according to contsraints known at the time
of this program being made, and commented accordingly. Global variables
are used to limit number of combinations generated, specify output file
and define the maximum possible length of a combination.
"""


# numerals 0-9
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# letters A-Z in uppercase
LETTERS = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
# make a superset all allowable characters
ALLOWABLE = NUMBERS + LETTERS
# add space to it because space is also allowed
ALLOWABLE.append(" ")
# make a special set for all allowable leading characters
LEADING = NUMBERS + LETTERS


def generate_custom():
    """ generate a random allowable custom WA plate """
    # maximum allowed on an aluminium plate is 7 characters
    max_length = 7
    # start the generation with an empty string
    permutation = ""
    random_length = random.randrange(3, max_length, 1)
    # start the instance with a character that is not a space
    permutation = random.choice(LEADING)
    # start increment at 1 because we already have a non-space leading char
    i = 1
    while i < random_length:
        single = random.choice(ALLOWABLE)
        # don't count spaces towards minimum printable characters
        if single == " ":
            i -= 1
        permutation += single
        i += 1
    return permutation


def generate_standard():
    """generate a random allowable standard WA plate"""
    permutation = ""
    # start with 1
    permutation += "1"
    # add a letter between A and G with F skipped
    first_letter = ["A", "B", "C", "D", "E", "G"]
    permutation += random.choice(first_letter)
    # add two random letters
    permutation += random.choice(LETTERS)
    permutation += random.choice(LETTERS)
    # add 3 random numbers
    permutation += random.choice(NUMBERS)
    permutation += random.choice(NUMBERS)
    permutation += random.choice(NUMBERS)
    return permutation


def main():
    """main program logic"""
    default_limit = 5
    default_filename = "output.txt"
    try:
        print("Random Registration Plate Generator for Blue WA Plates.")
        # check how many plates to generate
        limit = input("How many plates? Default is " + str(default_limit) + ": ")
        if not limit:
            limit = default_limit
        else:
            limit = limit.strip()
            limit = int(limit)
        print("Using: " + str(limit) + ".\n")
        # check filename to output to
        filename = input(
            "Which file to write to? Default is " + default_filename + ": "
        )
        if not filename:
            filename = "output.txt"
        else:
            filename = filename.strip()
        print("Using: " + filename + ".\n")
        selector = input("Standard (1) or Custom (2)? Default is 1: ")
        if not selector:
            selector = 1
        else:
            selector = int(selector)
        print("Using: " + str(selector) + ".\n")
        # open the file in text overWrite mode
        output = open(filename, "wt")
        # counter for the while loop
        counter = 0
        while counter < limit:
            instance = ""
            if selector == 1:
                instance = generate_standard()
            elif selector == 2:
                instance = generate_custom()
            # write the instance to the output file
            output.write(instance)
            # add a carriage return so it's one line per instance
            output.write("\n")
            # print(instance)
            counter += 1
        # close the file for neatness
        output.close()
        # tell the user how long the program took
        print(str(counter) + " plates to " + filename + ".\n")
    except KeyboardInterrupt:
        quit()


# standard python main function caller/wrapper
if __name__ == "__main__":
    main()
