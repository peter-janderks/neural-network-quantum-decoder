import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

def create_syndrome_table():
    H = np.array([[1,0,0,0,1,1,1,0,0,0,0,0,0,0],
                  [0,1,0,1,0,1,1,0,0,0,0,0,0,0],
                  [0,0,1,1,1,1,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,1,0,1,1,0,0,1],
                  [0,0,0,0,0,0,0,0,1,1,0,1,0,1],
                  [0,0,0,0,0,0,0,1,1,1,0,0,1,0]])

    errors = np.zeros((14,14))
    np.fill_diagonal(errors, 1)
    syndrome_table = np.matmul(H,errors.T).T

    return(syndrome_table)

def create_data(size_data, syndrome_table):
    error_number = np.random.randint(6, size=size_data)
    syndromes = syndrome_table[error_number]
    return (syndromes,error_number)

syndrome_table = create_syndrome_table()
train_inputs, train_labels = create_data(10000,syndrome_table)

model = keras.Sequential([
        keras.layers.InputLayer(input_shape=(6)),
        keras.layers.Dense(10,activation=tf.nn.relu),
        keras.layers.Dense(6,activation=tf.nn.softmax),
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_inputs,train_labels,epochs=10)

model.summary()