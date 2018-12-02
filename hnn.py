from data_processing.get_data import DataParser
from models.lstm import LSTMLabels, LSTMGenerate
import random
import sys
import os

# learn chords from Bach chorales and try to generate sequences of different lengths
path_name = 'pickle/full_chords_christmas/'

if os.path.exists(path_name):
    i = raw_input('This path already exists and some files might get written over. Continue? [y/n] ')
    if i == 'y':
        pass
    else:
        sys.exit()
else:
    os.mkdir(path_name)
    os.mkdir(path_name + 'midi')

print 'parsing'
dp = DataParser('christmas', 'full_chords')
X = dp.parse()
dp.save(path_name)

print 'lstm'

l = LSTMGenerate(X)
l.train()
l.save(path_name+'model')

print 'generate'

options = []
for k in dp.X_dict.keys():
    ks = k.split(' ')
    if list(set(sorted([int(a)%12 for a in ks[:-1] if a != 'r']))) == [0, 4, 7]:
        options.append(dp.X_dict[k])

y = l.generate([random.choice(options)], 4)
s = dp.make_song(path_name + 'midi/4_notes', x=y)

y = l.generate([random.choice(options)], 8)
s = dp.make_song(path_name + 'midi/8_notes', x=y)

y = l.generate([random.choice(options)], 16)
s = dp.make_song(path_name + 'midi/16_notes', x=y)

y = l.generate([random.choice(options)], 48)
s = dp.make_song(path_name + 'midi/48_notes', x=y)
