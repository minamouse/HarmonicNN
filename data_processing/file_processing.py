from music21 import converter, note, chord
import os


FILES = []
X = []
Y = []


def list_files(path):

    for p in os.listdir(path):
        if p.split('.')[-1] == 'mid':
            FILES.append


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


def full_chords():
    """
    Sorted midi pitches with repetitions removed.
    Duration included.
    Example: "50 60 66 69 0.5"
    """

    DATA = []

    for i, f in enumerate(FILES):
        data = []
        piece = converter.parse(f)
        chordified = piece.chordify()
        for c in chordified:
            if type(c) == chord.Chord:
                pitches = sorted(list(set([p.midi for p in c.pitches])))
                pitches.append(c.duration.quarterLength)
                data.append(' '.join([str(p) for p in pitches]))
        DATA.append(data)

    return DATA


def scale_degree():
    """
    Sorted scale degrees with repetitions removed.
    Duration included.
    Example: "0 2 6 9 0.5"
    """

    DATA = []

    for i, f in enumerate(FILES):
        data = []
        piece = converter.parse(f)
        chordified = piece.chordify()
        for c in chordified:
            if type(c) == chord.Chord:
                pitches = sorted(list(set([p.midi%12 for p in c.pitches])))
                pitches.append(c.duration.quarterLength)
                data.append(' '.join([str(p) for p in pitches]))
        DATA.append(data)

    return DATA


def full_chord_repetitions():
    """
    Sorted midi pitches with repetitions removed.
    Duration included.
    Example: "50 60 66 69 0.5"
    """

    DATA = []

    for i, f in enumerate(FILES):
        data = []
        piece = converter.parse(f)
        chordified = piece.chordify()
        for c in chordified:
            if type(c) == chord.Chord:
                pitches = sorted(list(set([p.midi for p in c.pitches])))
                chord_notes = ' '.join([str(p) for p in pitches])
                repetitions = int(c.duration.quarterLength/0.25)
                for j in range(repetitions):
                    if j == repetitions-1:
                        data.append(chord_notes + ' e')
                    elif j == 0:
                        data.append(chord_notes + ' b')
                    else:
                        data.append(chord_notes + ' c')
        DATA.append(data)

    return DATA


def scale_degree_repetitions():
    """
    Sorted midi pitches with repetitions removed.
    Duration included.
    Example: "50 60 66 69 0.5"
    """

    DATA = []

    for i, f in enumerate(FILES):
        data = []
        piece = converter.parse(f)
        chordified = piece.chordify()
        for c in chordified:
            if type(c) == chord.Chord:
                pitches = sorted(list(set([p.midi for p in c.pitches])))
                chord_notes = ' '.join([str(p) for p in pitches])
                repetitions = int(c.duration.quarterLength/0.25)
                for j in range(repetitions):
                    if j == repetitions-1:
                        data.append(chord_notes + ' e')
                    elif j == 0:
                        data.append(chord_notes + ' b')
                    else:
                        data.append(chord_notes + ' c')
        DATA.append(data)

    return DATA



# option 1
# melody_repetitions()
# full_chord_repetitions()

# option 2
# melody_scale_degree_repetitions()
# scale_degree_repetitions()

# option 3
# full_chords()

# option 4
# scale_degree()

# option 5
# melody_durations()

# option 6
# melody_scale_degree_durations()






