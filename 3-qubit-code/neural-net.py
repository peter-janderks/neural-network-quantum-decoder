import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

"""
3-qubit 
00 do nothing
01 apply σx to third qubit
10 apply σx to second qubit
11 apply σx to first qubit
"""

def generate_data(train_dataset_size,test_dataset_size):
    train_inputs = np.stack([np.random.choice(2,size=2) 
                             for i in range(train_dataset_size)])

    train_labels = np.zeros(shape=(1,train_dataset_size))
    train_labels = [1 if np.array_equal(train_inputs[s],[1,1]) 
                    else 2 if np.array_equal(train_inputs[s],[1,0])
                    else 3 if np.array_equal(train_inputs[s],[0,1])
                    else 0
                    for s in range(train_dataset_size)]
    
    test_inputs = np.stack([np.random.choice(2,size=2) 
                            for i in range(test_dataset_size)])

    test_labels = [1 if np.array_equal(test_inputs[s],[1,1])
                    else 2 if np.array_equal(test_inputs[s],[1,0])
                    else 3 if np.array_equal(test_inputs[s],[0,1])
                    else 0
                    for s in range(test_dataset_size)]

    return(train_inputs, train_labels, test_inputs, test_labels)

train_inputs, train_labels, test_inputs, test_labels = (generate_data(10000,100))

model = keras.Sequential([
    keras.layers.InputLayer(input_shape=(2)),
    keras.layers.Dense(4, activation=tf.nn.softmax),
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_inputs, train_labels, epochs=10)
test_loss, test_acc = model.evaluate(test_inputs, test_labels)

model.summary()

print(test_acc,'final test accuracy')

