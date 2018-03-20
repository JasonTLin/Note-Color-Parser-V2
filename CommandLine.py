import sys


def note_color_parser(note):

    color = "white"

    dict = {'a': 'red', 'b': 'blue', 'c': 'green', 'd': 'purple', 'e': 'orange', 'f': 'gray', 'g': 'pink'}

    color = dict[note]

    return color


def main():

    color = note_color_parser(sys.argv[1].lower())

    print(color)


main()



