from data_processing.get_data import DataParser
import pickle


dp = DataParser('joplin', 'melody_repetitions', 'full_chord_repetitions')
X,Y = dp.parse()

pickle.dump(X, open('pickle/data/joplin/X.p', 'wb'))
pickle.dump(Y, open('pickle/data/joplin/Y.p', 'wb'))
dp.save('pickle/data/joplin')

