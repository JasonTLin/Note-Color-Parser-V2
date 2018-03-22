import sys, winsound


def note_color_parser(note):

    color = "white"

    dict = {'a': 'red', 'b': 'blue', 'c': 'green', 'd': 'purple', 'e': 'orange', 'f': 'gray', 'g': 'pink'}

    if note in dict:
        color = dict[note]

    return color


def note_to_sound(note):

    dict = {'a': 220, 'b': 247, 'c': 262, 'd': 294, 'e': 330, 'f': 349, 'g': 392}

    if note in dict:
        sound = dict[note]
        winsound.Beep(sound, 500)


def main():

    color = note_color_parser(sys.argv[1].lower())

    print(color)

    note_to_sound(sys.argv[1].lower())


main()




