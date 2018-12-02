from data_processing.get_data import DataParser
from models.lstm import LSTMLabels
from music21 import stream, midi

dp = DataParser('mini', 'melody_repetitions', 'full_chord_repetitions')
X, Y = dp.parse()

l = LSTMLabels(X[:-1], Y[:-1])
l.train(32, 10)
y = l.generate(X[-1])


s = dp.make_song(X[-1], y, 'models/midi')
# sp = midi.realtime.StreamPlayer(s)
# sp.play()