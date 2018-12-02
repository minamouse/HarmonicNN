from music21 import chord, stream


class ChordParser:

    data = []
    pieces = []
    parsing_options = ['full_chords',
                       'scale_degree',
                       'full_chord_repetitions',
                       'scale_degree_repetitions']


    def __init__(self, pieces, parsing_option, shortestNote=0.25):

        if parsing_option not in self.parsing_options:
            raise ValueError('Invalid melody parsing option.')

        self.pieces = pieces
        self.parsing_option = parsing_option
        self.shortestNote = shortestNote


    def parse(self):

        for piece in self.pieces:
            chordified = piece.chordify()
            if self.parsing_option == 'full_chords':
                self.data.append(self.full_chords(chordified))
            elif self.parsing_option == 'scale_degree_chord':
                self.data.append(self.scale_degree_chord(chordified))
            elif self.parsing_option == 'full_chord_repetitions':
                self.data.append(self.full_chord_repetitions(chordified))
            elif self.parsing_option == 'scale_degree_chord_repetitions':
                self.data.append(self.scale_degree_chord_repetitions(chordified))

        return self.data


    def full_chords(self, chordified):
        """
        Sorted midi pitches with repetitions removed.
        Duration included.
        Example: "50 60 66 69 0.5"
        """

        chords = []

        for c in chordified:
            if type(c) == chord.Chord:
                pitches = sorted(list(set([p.midi for p in c.pitches])))
                pitches.append(c.duration.quarterLength)
                chords.append(' '.join([str(p) for p in pitches]))

        return chords


    def undo_full_chords(self, chords):

        part = stream.Part()

        for c in chords:
            if c != 'r':
                pitches = c.split(' ')
                newChord = chord.Chord([int(p) for p in pitches[-1]])
                newChord.duration.quarterLength = float(pitches[-1])
                part.append(newChord)

        return part


    def scale_degree_chord(self, chordified):
        """
        Sorted scale degrees with repetitions removed.
        Duration included.
        Example: "0 2 6 9 0.5"
        """

        chords = []

        for c in chordified:
            if type(c) == chord.Chord:
                pitches = sorted(list(set([p.midi%12 for p in c.pitches])))
                pitches.append(c.duration.quarterLength)
                chords.append(' '.join([str(p) for p in pitches]))

        return chords


    def full_chord_repetitions(self, chordified):
        """
        Sorted midi pitches with repetitions removed.
        Duration included.
        Example: "50 60 66 69 0.5"
        """

        chords = []

        for c in chordified:
            if type(c) == chord.Chord:
                pitches = sorted(list(set([p.midi for p in c.pitches])))
                chord_notes = ' '.join([str(p) for p in pitches])
                repetitions = int(c.duration.quarterLength/self.shortestNote)
                for i in range(repetitions):
                    if i == repetitions-1:
                        chords.append(chord_notes + ' e')
                    elif i == 0:
                        chords.append(chord_notes + ' b')
                    else:
                        chords.append(chord_notes + ' c')

        return chords


    def undo_full_chord_repetitions(self, chords):

        part = stream.Part()
        
        pitches = []
        durations = []
        inc = -1
        for c in chords:
            if c != 'r':
                notes = m.split(' ')

                if notes[-1] == 'b':
                    inc += 1
                    durations.append(self.shortestNote)
                    pitches.append(notes[:-1])
                else:
                    durations[inc] += self.shortestNote

        for i in range(len(pitches)):
            newChord = chord.Chord([int(p) for p in pitches[i]])
            newChord.duration.quarterLength = float(durations[i])
            part.append(newChord)

        return part


    def scale_degree_chord_repetitions(self, chordified):
        """
        Sorted midi pitches with repetitions removed.
        Duration included.
        Example: "50 60 66 69 0.5"
        """

        chords = []

        for c in chordified:
            if type(c) == chord.Chord:
                pitches = sorted(list(set([p.midi for p in c.pitches])))
                chord_notes = ' '.join([str(p) for p in pitches])
                repetitions = int(c.duration.quarterLength/self.shortestNote)
                for i in range(repetitions):
                    if i == repetitions-1:
                        chords.append(chord_notes + ' e')
                    elif i == 0:
                        chords.append(chord_notes + ' b')
                    else:
                        chords.append(chord_notes + ' c')

        return chords


    def make_stream(self, chords):

        if self.parsing_option == 'full_chords' or self.parsing_option == 'scale_degree_chord':
            return self.undo_full_chords(chords)
        elif self.parsing_option == 'full_chord_repetitions' or self.parsing_option == 'scale_degree_chord_repetitions':
            return self.undo_full_chord_repetitions(chords)

