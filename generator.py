"""ECU CSG3303 Assignment - Photometer - Random License Plate Generator"""
import random
from datetime import datetime

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


# main reference was this article on random number generation
#   https://pynative.com/python-random-module/


# start timing how long the program takes
START = datetime.now()

# global limit for number of generated permutations
LIMIT = 500000
# counter for main program logic
FILENAME = "output.txt"
# maximum length of a license plate
MAX_LENGTH = 7

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
    permutation = ""
    # calculate a random instance length, between the minimum(3) and maximum
    random_length = random.randrange(3, MAX_LENGTH, 1)
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
    counter = 0
    # open the file in text overWrite mode
    output = open(FILENAME, "wt")
    while counter < LIMIT:
        instance = ""
        print(str(counter))
        # a selector to choose between 0 and 1
        selector = random.choice([0, 1])
        # based on selector do either a custom or standard plate instance
        if selector == 0:
            instance = generate_custom()
        elif selector == 1:
            instance = generate_standard()
        # write the instance to the output file
        output.write(instance)
        # add a carriage return so it's one line per instance
        output.write("\n")
        # print the instance to the screen
        # print(instance)
        # increment counter
        counter += 1
    # close the file for neatness
    output.close()
    # tell the user how long the program took
    print(
        "\n"
        + "It took "
        + str(datetime.now() - START)
        + " seconds to print "
        + str(LIMIT)
        + " random allowable license plate permutations to: "
        + FILENAME
        + "."
    )
