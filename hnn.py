from data_processing.get_data import DataParser
from models.lstm import LSTMLabels, LSTMGenerate
import random
import sys
import os


#######################################################################################
# Bach generate chords
#######################################################################################

# path_name = 'pickle/full_chords_bach/'

# os.mkdir(path_name)
# os.mkdir(path_name + 'midi')

# print 'parsing bach'
# dp = DataParser('chorales', 'full_chords')
# X = dp.parse()
# dp.save(path_name)

# print 'lstm bach'

# l = LSTMGenerate(X)
# l.train()
# l.save(path_name+'model')

# print 'generate bach'

# options = []
# for k in dp.X_dict.keys():
#     ks = k.split(' ')
#     if list(set(sorted([int(a)%12 for a in ks[:-1] if a != 'r']))) == [0, 4, 7]:
#         options.append(dp.X_dict[k])

# y = l.generate([random.choice(options)], 4)
# s = dp.make_song(path_name + 'midi/4_notes1', x=y)
# y = l.generate([random.choice(options)], 4)
# s = dp.make_song(path_name + 'midi/4_notes2', x=y)

# y = l.generate([random.choice(options)], 8)
# s = dp.make_song(path_name + 'midi/8_notes1', x=y)
# y = l.generate([random.choice(options)], 8)
# s = dp.make_song(path_name + 'midi/8_notes2', x=y)

# y = l.generate([random.choice(options)], 16)
# s = dp.make_song(path_name + 'midi/16_notes1', x=y)
# y = l.generate([random.choice(options)], 16)
# s = dp.make_song(path_name + 'midi/16_notes2', x=y)

# y = l.generate([random.choice(options)], 48)
# s = dp.make_song(path_name + 'midi/48_notes1', x=y)
# y = l.generate([random.choice(options)], 48)
# s = dp.make_song(path_name + 'midi/48_notes2', x=y)


# #######################################################################################
# # Christmas generate chords
# #######################################################################################

# path_name = 'pickle/full_chords_christmas/'

# os.mkdir(path_name)
# os.mkdir(path_name + 'midi')

# print 'parsing christmas'
# dp = DataParser('christmas', 'full_chords')
# X = dp.parse()
# dp.save(path_name)

# print 'lstm christmas'

# l = LSTMGenerate(X)
# l.train()
# l.save(path_name+'model')

# print 'generate christmas'

# options = []
# for k in dp.X_dict.keys():
#     ks = k.split(' ')
#     if list(set(sorted([int(a)%12 for a in ks[:-1] if a != 'r']))) == [0, 4, 7]:
#         options.append(dp.X_dict[k])

# y = l.generate([random.choice(options)], 4)
# s = dp.make_song(path_name + 'midi/4_notes1', x=y)
# y = l.generate([random.choice(options)], 4)
# s = dp.make_song(path_name + 'midi/4_notes2', x=y)

# y = l.generate([random.choice(options)], 8)
# s = dp.make_song(path_name + 'midi/8_notes1', x=y)
# y = l.generate([random.choice(options)], 8)
# s = dp.make_song(path_name + 'midi/8_notes2', x=y)

# y = l.generate([random.choice(options)], 16)
# s = dp.make_song(path_name + 'midi/16_notes1', x=y)
# y = l.generate([random.choice(options)], 16)
# s = dp.make_song(path_name + 'midi/16_notes2', x=y)

# y = l.generate([random.choice(options)], 48)
# s = dp.make_song(path_name + 'midi/48_notes1', x=y)
# y = l.generate([random.choice(options)], 48)
# s = dp.make_song(path_name + 'midi/48_notes2', x=y)


# #######################################################################################
# # Joplin generate chords
# #######################################################################################

# path_name = 'pickle/full_chords_joplin/'

# os.mkdir(path_name)
# os.mkdir(path_name + 'midi')

# print 'parsing joplin'
# dp = DataParser('joplin', 'full_chords')
# X = dp.parse()
# dp.save(path_name)

# print 'lstm joplin'

# l = LSTMGenerate(X)
# l.train()
# l.save(path_name+'model')

# print 'generate joplin'

# options = []
# for k in dp.X_dict.keys():
#     ks = k.split(' ')
#     if list(set(sorted([int(a)%12 for a in ks[:-1] if a != 'r']))) == [0, 4, 7]:
#         options.append(dp.X_dict[k])

# y = l.generate([random.choice(options)], 4)
# s = dp.make_song(path_name + 'midi/4_notes1', x=y)
# y = l.generate([random.choice(options)], 4)
# s = dp.make_song(path_name + 'midi/4_notes2', x=y)

# y = l.generate([random.choice(options)], 8)
# s = dp.make_song(path_name + 'midi/8_notes1', x=y)
# y = l.generate([random.choice(options)], 8)
# s = dp.make_song(path_name + 'midi/8_notes2', x=y)

# y = l.generate([random.choice(options)], 16)
# s = dp.make_song(path_name + 'midi/16_notes1', x=y)
# y = l.generate([random.choice(options)], 16)
# s = dp.make_song(path_name + 'midi/16_notes2', x=y)

# y = l.generate([random.choice(options)], 48)
# s = dp.make_song(path_name + 'midi/48_notes1', x=y)
# y = l.generate([random.choice(options)], 48)
# s = dp.make_song(path_name + 'midi/48_notes2', x=y)


#######################################################################################
# Bach harmonize
#######################################################################################

path_name = 'pickle/full_chords_accompaniment_bach/'

os.mkdir(path_name)
os.mkdir(path_name + 'midi')

print 'parsing bach'
dp = DataParser('chorales', 'melody_repetitions', 'full_chord_repetitions')
X, Y = dp.parse()
dp.save(path_name)

print 'lstm bach'

l = LSTMLabels(X, Y)
l.train()
l.save(path_name+'model')

print 'generate bach'

melodies = dp.parse_new('melodies')

for i, m in enumerate(melodies):
    y = l.generate(m)
    s = dp.make_song(path_name + 'midi/' + str(i), x=m, y=y)


#######################################################################################
# Christmas harmonize
#######################################################################################

path_name = 'pickle/full_chords_accompaniment_christmas/'

os.mkdir(path_name)
os.mkdir(path_name + 'midi')

print 'parsing christmas'
dp = DataParser('christmas', 'melody_repetitions', 'full_chord_repetitions')
X, Y = dp.parse()
dp.save(path_name)

print 'lstm christmas'

l = LSTMLabels(X, Y)
l.train()
l.save(path_name+'model')

print 'generate christmas'

melodies = dp.parse_new('melodies')

for i, m in enumerate(melodies):
    y = l.generate(m)
    s = dp.make_song(path_name + 'midi/' + str(i), x=m, y=y)


#######################################################################################
# Joplin harmonize
#######################################################################################

path_name = 'pickle/full_chords_accompaniment_joplin/'

os.mkdir(path_name)
os.mkdir(path_name + 'midi')

print 'parsing joplin'
dp = DataParser('joplin', 'melody_repetitions', 'full_chord_repetitions')
X, Y = dp.parse()
dp.save(path_name)

print 'lstm joplin'

l = LSTMLabels(X, Y)
l.train()
l.save(path_name+'model')

print 'generate joplin'

melodies = dp.parse_new('melodies')

for i, m in enumerate(melodies):
    y = l.generate(m)
    s = dp.make_song(path_name + 'midi/' + str(i), x=m, y=y)



