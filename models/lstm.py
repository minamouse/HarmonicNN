import numpy as np
from keras.models import Model, Input
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding, Dropout, Bidirectional, LSTM, TimeDistributed, Dense


class LSTMLabels():

    X = []
    Y = []

    model = None
    input = None
    out = None

    max_len = 0
    padding_x = 0
    padding_y = 0

    n_x = 0
    n_y = 0


    def __init__(self, X, Y):

        self.max_len = max([len(x) for x in X])
        self.padding_x = max([max(x) for x in X]) + 1
        self.padding_y = max([max(y) for y in Y]) + 1

        self.n_x = self.padding_x + 1
        self.n_y = self.padding_y + 1

        self.X = pad_sequences(maxlen=self.max_len, sequences=X, padding='post', value=self.padding_x)
        self.Y = pad_sequences(maxlen=self.max_len, sequences=Y, padding='post', value=self.padding_y)
        self.Y = [to_categorical(i, num_classes=self.n_y) for i in self.Y]

        self.input = Input(shape=(self.max_len,))
        self.model = Embedding(input_dim=self.n_x, output_dim=50, input_length=self.max_len)(self.input)
        self.model = Dropout(0.1)(self.model)
        self.model = Bidirectional(LSTM(units=100, return_sequences=True, recurrent_dropout=0.1))(self.model)

        self.out = TimeDistributed(Dense(self.n_y, activation="softmax"))(self.model)
        self.model = Model(self.input, self.out)

        self.model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])


    def train(self, batch_size=32, epochs=100):
        
        history = self.model.fit(self.X, np.array(self.Y), batch_size=batch_size, epochs=epochs, validation_split=0.1, verbose=1)


    def load(self, path):
        
        self.model.load_weights(path)


    def save(self, path):
        
        self.model.save_weights(path)


    def generate(self, X):
        X = pad_sequences(maxlen=self.max_len, sequences=[X], padding='post', value=self.padding_x)
        p = self.model.predict(np.array(X))
        p = np.argmax(p, axis=-1)

        return list(p[0])

