from __future__ import print_function

import keras
from keras.datasets import mnist



(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
#攤平資料

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train /= 255
x_test /= 255
#Preprocessing Character Images

print(x_train.shape[0], x_test.shape[0])
#印出資料大小 

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
#ont-hot coding