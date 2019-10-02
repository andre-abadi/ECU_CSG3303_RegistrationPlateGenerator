# Introduction
This program generates a text file of random vehicle registration plate combinations that are valid in Western Australia. The scope of generation is limited to standard aluminium plates with the blue Western Australia top-bar. Plates are either custom, which is between 3 and 7 characters with the leading character not being a space, or a standard plate. Standard plates are generated according to contsraints known at the time of this program being made, and commented accordingly. Global variables are used to limit number of combinations generated, specify output file and define the maximum possible length of a combination.

# Installation
1. `sudo apt install python3 git`
2. `git clone git@github.com:dancingborg/ECU_CSG3303_RegistrationPlateGenerator.git generator`

# Usage
1. `How many plates? Default is 5:` Enter the number of plates to be generated.
2. `Which file to write to? Default is output.txt:` Enter the desired file to be written by the program.
3. `Plate type to generate? Default is 1:` Enter the plate type to be generated.

## Plate Types
At this time the interactivity of plate type selection is rudimentary. The user should read `generator.py` but a summary is provided below:
1. Standard WA plate in the format 1ABC123
    - Number 1
    - Letter A-G
    - 2 random letters
    - 3 random numbers
2. Custom WA plate in the format ABCDEFG
    - Minimum length of 3 characters
    - Spaces do not count towards minimum characters
    - Maximum of 7 characters
    - May not start with a space
3. First half of standard WA plate in the format 1ABC
4. Second half of standard WA plate in the format 123
