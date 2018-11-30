from music21 import converter, note


def melody():
    """
    Returns a list of note objects representing the melody voice.
    """

    DATA = []

    for f in FILES:
        piece = converter.parse(f)
        parts = [p for p in piece]
        part_pitches = [[] for p in parts]

        for i, p in enumerate(parts):
            for n in p:
                if type(n) == note.Note:
                    part_pitches[i].append(n.pitch.midi)

        averages = [sum(p)/len(p) for p in part_pitches]
        melody_voice = averages.index(max(averages))

        DATA.append([n for n in parts[melody_voice] if type(n) == note.Note])

    return DATA


def melody_durations():
    """
    Melodies written in the form of midi note and duration.
    Example: "72 0.5"
    """

    melodies = melody()

    DATA = []
    for m in melodies:
        data = []
        for n in m:
            data.append(str(n.pitch.midi) + ' ' + str(n.duration.quarterLength))
        DATA.append(data)

    return DATA


def melody_scale_degree_durations():
    """
    Melodies written in the form of scale degree and duration.
    Example: "4 0.5"
    """

    melodies = melody()

    DATA = []

    for m in melodies:
        data = []
        for n in m:
            data.append(str(n.pitch.midi%12) + ' ' + str(n.duration.quarterLength))
        DATA.append(data)

    return DATA


def melody_repetitions():
    """
    Represents notes as lists of numbers, stating whether it's the beginning, middle, or end
    of the note.
    Split up by 16th notes.
    Example: ['71 b', '71 c', '71 c', '71 c', '71 e']
    """

    melodies = melody()

    DATA = []

    for m in melodies:
        data = []
        for n in m:
            myNote = str(n.pitch.midi)
            repetitions = int(n.duration.quarterLength/0.25)
            for i in range(repetitions):
                if i == repetitions-1:
                    data.append(myNote + ' e')
                elif i == 0:
                    data.append(myNote + ' b')
                else:
                    data.append(myNote + ' c')
        DATA.append(data)

    return DATA


def melody_scale_degree_repetitions():
    """
    Represents scale degrees as lists of numbers, stating whether it's the beginning, middle, or end
    of the note.
    Split up by 16th notes.
    Example: ['11 b', '11 c', '11 c', '11 c', '11 e']
    """

    melodies = melody()

    DATA = []

    for m in melodies:
        data = []
        for n in m:
            myNote = str(n.pitch.midi%12)
            repetitions = int(n.duration.quarterLength/0.25)
            for i in range(repetitions):
                if i == repetitions-1:
                    data.append(myNote + ' e')
                elif i == 0:
                    data.append(myNote + ' b')
                else:
                    data.append(myNote + ' c')
        DATA.append(data)

    return DATA

