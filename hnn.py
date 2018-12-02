from data_processing.get_data import DataParser
from models.lstm import LSTMLabels, LSTMGenerate
from music21 import stream, midi

dp = DataParser('mini', 'melody_durations')
X = dp.parse()

l = LSTMGenerate(X)

l.train(32, 10)
y = l.generate([5, 23, 27, 7, 0], 20)

print y
# s = dp.make_song(X[-1], y, 'models/midi')

