from music21 import converter, chord


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

