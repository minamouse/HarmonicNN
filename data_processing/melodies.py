from music21 import note, stream


class MelodyParser:

    data = []
    parsing_options = ['melody_durations',
                       'melody_scale_degree_durations',
                       'melody_repetitions',
                       'melody_scale_degree_repetitions']
    pieces = []


    def __init__(self, pieces, parsing_option, shortestNote=0.25):

        if parsing_option not in self.parsing_options:
            raise ValueError('Invalid melody parsing option.')

        self.pieces = pieces
        self.parsing_option = parsing_option
        self.shortestNote = shortestNote


    def parse(self):

        for piece in self.pieces:
            melody = self.melody(piece)
            if self.parsing_option == 'melody_durations':
                self.data.append(self.melody_durations(melody))
            elif self.parsing_option == 'melody_scale_degree_durations':
                self.data.append(self.melody_scale_degree_durations(melody))
            elif self.parsing_option == 'melody_repetitions':
                self.data.append(self.melody_repetitions(melody))
            elif self.parsing_option == 'melody_scale_degree_repetitions':
                self.data.append(self.melody_scale_degree_repetitions(melody))

        return self.data


    def parse_new(self, piece):

        melody = self.melody(piece)

        if self.parsing_option == 'melody_durations':
            return self.melody_durations(melody)
        elif self.parsing_option == 'melody_scale_degree_durations':
            return self.melody_scale_degree_durations(melody)
        elif self.parsing_option == 'melody_repetitions':
            return self.melody_repetitions(melody)
        elif self.parsing_option == 'melody_scale_degree_repetitions':
            return self.melody_scale_degree_repetitions(melody)


    def melody(self, piece):
        """
        Returns a list of note objects representing the melody voice.
        """

        parts = [p for p in piece]
        part_pitches = [[] for p in parts]

        for i, p in enumerate(parts):
            for n in p:
                if type(n) == note.Note:
                    part_pitches[i].append(n.pitch.midi)

        averages = [sum(p)/len(p) for p in part_pitches]
        melody_voice = averages.index(max(averages))

        return [n for n in parts[melody_voice] if type(n) == note.Note or type(n) == note.Rest]


    def melody_durations(self, melody):
        """
        Melodies written in the form of midi note and duration.
        Example: "72 0.5"
        """

        string_melody = []

        for n in melody:
            if type(n) == note.Note:
                string_melody.append(str(n.pitch.midi) + ' ' + str(n.duration.quarterLength))
            elif type(n) == note.Rest:
                string_melody.append(str('r ' + str(n.duration.quarterLength)))

        return string_melody


    def undo_melody_durations(self, melody):

        part = stream.Part()

        for n in melody:
            if n == 'r':
                pass
            else:
                p, l = n.split(' ')
                if p == 'r':
                    newNote = note.Rest()
                else:
                    newNote = note.Note(int(p))

                newNote.duration.quarterLength = float(l)
                part.append(newNote)

        return part


    def melody_scale_degree_durations(self, melody):
        """
        Melodies written in the form of scale degree and duration.
        Example: "4 0.5"
        """

        string_melody = []

        for n in melody:
            if type(n) == note.Note:
                string_melody.append(str(n.pitch.midi%12) + ' ' + str(n.duration.quarterLength))
            elif type(n) == note.Rest:
                string_melody.append(str('r ' + str(n.duration.quarterLength)))

        return string_melody


    def melody_repetitions(self, melody):
        """
        Represents notes as lists of numbers, stating whether it's the beginning, middle, or end
        of the note.
        Split up by 16th notes.
        Example: ['71 b', '71 c', '71 c', '71 c', '71 e']
        """

        new_melody = []

        for n in melody:
            if type(n) == note.Note:
                myNote = str(n.pitch.midi)
            else:
                myNote = 'r'
            repetitions = int(n.duration.quarterLength/self.shortestNote)
            for i in range(repetitions):
                if i == repetitions-1:
                    new_melody.append(myNote + ' e')
                elif i == 0:
                    new_melody.append(myNote + ' b')
                else:
                    new_melody.append(myNote + ' c')

        return new_melody


    def undo_melody_repetitions(self, melody):

        part = stream.Part()

        notes = []
        durations = []
        inc = -1
        for m in melody:
            if m != 'r':
                n, pos = m.split(' ')

                if pos == 'b':
                    inc += 1
                    durations.append(self.shortestNote)
                    notes.append(n)
                else:
                    if inc == -1:
                        pass
                    else:
                        durations[inc] += self.shortestNote

        for i in range(len(notes)):
            n = notes[i]
            if n == 'r':
                newNote = note.Rest()
            else:
                newNote = note.Note(int(n))
            newNote.duration.quarterLength = float(durations[i])
            part.append(newNote)

        return part


    def melody_scale_degree_repetitions(self, melody):
        """
        Represents scale degrees as lists of numbers, stating whether it's the beginning, middle, or end
        of the note.
        Split up by 16th notes.
        Example: ['11 b', '11 c', '11 c', '11 c', '11 e']
        """

        new_melody = []
        for n in melody:
            if type(n) == note.Note:
                myNote = str(n.pitch.midi%12)
            else:
                myNote = 'r'
            repetitions = int(n.duration.quarterLength/self.shortestNote)
            for i in range(repetitions):
                if i == repetitions-1:
                    new_melody.append(myNote + ' e')
                elif i == 0:
                    new_melody.append(myNote + ' b')
                else:
                    new_melody.append(myNote + ' c')

        return new_melody


    def make_stream(self, melody):

        if self.parsing_option == 'melody_durations' or self.parsing_option == 'melody_scale_degree_durations':
            return self.undo_melody_durations(melody)
        elif self.parsing_option == 'melody_repetitions' or self.parsing_option == 'melody_scale_degree_repetitions':
            return self.undo_melody_repetitions(melody)


