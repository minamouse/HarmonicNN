from models.lstm import LSTMGenerate
from data_processing.get_data import DataParser

starting_point = 'begin'
stopping_point = 'end'

for epoch in [100, 200, 400]:

    # chordified
    path = 'pickle/final/full_chords/' + str(epoch) + '/'

    dp = DataParser('chorales', 'full_chords')
    X = dp.parse()
    dp.save(path)

    l = LSTMGenerate(X)
    l.train(epochs=epoch)
    l.save(path+'model')


    generated = l.generate([dp.X_dict[starting_point]], dp.X_dict[stopping_point])
    dp.make_song(path+'1', generated)

    generated = l.generate([dp.X_dict[starting_point]], dp.X_dict[stopping_point])
    dp.make_song(path+'2', generated)

    generated = l.generate([dp.X_dict[starting_point]], dp.X_dict[stopping_point])
    dp.make_song(path+'3', generated)


    # chordified without durations
    path = 'pickle/final/full_chords_no_durations/' + str(epoch) + '/'

    dp = DataParser('chorales', 'full_chords_no_duration')
    X = dp.parse()
    dp.save(path)

    l = LSTMGenerate(X)
    l.train(epochs=epoch)
    l.save(path+'model')

    generated = l.generate([dp.X_dict[starting_point]])
    dp.make_song(path+'1', generated)

    generated = l.generate([dp.X_dict[starting_point]])
    dp.make_song(path+'2', generated)

    generated = l.generate([dp.X_dict[starting_point]])
    dp.make_song(path+'3', generated)



    # scale degrees
    path = 'pickle/final/scale_degree_chords/' + str(epoch) + '/'

    dp = DataParser('chorales', 'scale_degree_chord')
    X = dp.parse()
    dp.save(path)

    l = LSTMGenerate(X)
    l.train(epochs=epoch)
    l.save(path+'model')

    generated = l.generate([dp.X_dict[starting_point]])
    dp.make_song(path+'1', generated)

    generated = l.generate([dp.X_dict[starting_point]])
    dp.make_song(path+'2', generated)

    generated = l.generate([dp.X_dict[starting_point]])
    dp.make_song(path+'3', generated)


    # scale degrees without durations
    path = 'pickle/final/scale_degree_no_duration/' + str(epoch) + '/'

    dp = DataParser('chorales', 'scale_degree_chord_no_duration')
    X = dp.parse()
    dp.save(path)

    l = LSTMGenerate(X)
    l.train(epochs=epoch)
    l.save(path+'model')

    generated = l.generate([dp.X_dict[starting_point]])
    dp.make_song(path+'1', generated)

    generated = l.generate([dp.X_dict[starting_point]])
    dp.make_song(path+'2', generated)

    generated = l.generate([dp.X_dict[starting_point]])
    dp.make_song(path+'3', generated)

