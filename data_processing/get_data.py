from melodies import MelodyParser
from chords import ChordParser
from music21 import converter, stream
import pickle
import os


class DataParser():


    path_directory = 'data/'
    X = []
    Y = []
    X_dict = {}
    reverse_X = {}
    Y_dict = {}
    reverse_Y = {}
    pieces = []

    x_parser = None
    y_parser = None


    def __init__(self, path, X_option=None, Y_option=None):

        self.path = self.path_directory + path
        self.X_option = X_option
        self.Y_option = Y_option


    def parse(self):
        
        self.files_to_pieces()

        if self.X_option:
            if 'chord' in self.X_option:
                self.x_parser = ChordParser(self.pieces, self.X_option)
                self.X = self.x_parser.parse()
            elif 'melody' in self.X_option:
                self.x_parser = MelodyParser(self.pieces, self.X_option)
                self.X = self.x_parser.parse()

        if self.Y_option:
            if 'chord' in self.Y_option:
                self.y_parser = ChordParser(self.pieces, self.Y_option)
                self.Y = self.y_parser.parse()
            elif 'melody' in self.Y_option:
                self.y_parser = MelodyParser(self.pieces, self.Y_option)
                self.Y = self.y_parser.parse()


        self.data_to_dict()
        self.to_numerical()

        if self.X_option and self.Y_option:
            return self.X_n, self.Y_n
        elif self.X_option:
            return self.X_n
        elif self.Y_option:
            return self.Y_n
        else:
            return None


    def parse_new(self, path):

        self.path = self.path_directory + path
        self.files_to_pieces()

        all_data = []
        print self.X_dict

        for i, p in enumerate(self.pieces):
            data = self.x_parser.parse_new(p)
            piece = []
            for d in data:
                if d in self.X_dict:
                    piece.append(self.X_dict[d])
                else:
                    print d
                    piece.append(-1)
            if -1 in piece:
                print 'didn\'t work'
            else:
                all_data.append(piece)

        return all_data


    def save(self, path):

        if self.X_dict:
            pickle.dump(self.X_dict, open(path+'X_dict.p', 'wb'))
            pickle.dump(self.reverse_X, open(path+'/reverse_X.p', 'wb'))
        if self.Y_dict:
            pickle.dump(self.Y_dict, open(path+'Y_dict.p', 'wb'))
            pickle.dump(self.reverse_Y, open(path+'/reverse_Y.p', 'wb'))


    def files_to_pieces(self):

        self.pieces = []

        for p in os.listdir(self.path):
            if p.split('.')[-1] == 'mid':
                print p
                self.pieces.append(converter.parse(self.path + '/' + p))


    def data_to_dict(self):

        if self.X:
            all_data = []
            for d in self.X:
                all_data.extend(d)

            all_data = list(set(all_data))

            self.X_dict = {w: i for i, w in enumerate(all_data)}
            self.reverse_X = {i: w for i, w in enumerate(all_data)}

        if self.Y:
            all_data = []
            for d in self.Y:
                all_data.extend(d)

            all_data = list(set(all_data))

            self.Y_dict = {w: i for i, w in enumerate(all_data)}
            self.reverse_Y = {i: w for i, w in enumerate(all_data)}


    def to_numerical(self):

        if self.X_dict:
            self.X_n = [[self.X_dict[x] for x in X] for X in self.X]

        if self.Y_dict:
            self.Y_n = [[self.Y_dict[y] for y in Y] for Y in self.Y]


    def make_song(self, song_path, x=None, y=None):

        piece = stream.Stream()

        if x:
            x_strings = []
            for i in x:
                if i in self.reverse_X:
                    x_strings.append(self.reverse_X[i])
                else:
                    x_strings.append('r')

            part_x = self.x_parser.make_stream(x_strings)
            piece.append(part_x)

        if y:
            y_strings = []

            for i in y:
                if i in self.reverse_Y:
                    y_strings.append(self.reverse_Y[i])
                else:
                    y_strings.append('r')

            part_y = self.y_parser.make_stream(y_strings)
            piece.append(part_y)

        fp = piece.write('midi', fp=song_path+'.mid')

