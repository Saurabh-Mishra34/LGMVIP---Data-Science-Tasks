import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import tensorflow as tf


# mnist = tf.keras.datasets.mnist
# (x_train,y_train), (x_test,y_test)= mnist.load_data()
#
# x_train = tf.keras.utils.normalize(x_train,axis=1)
# x_test = tf.keras.utils.normalize(x_test,axis=1)

# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# model.add(tf.keras.layers.Dense(128, activation = 'relu'))
# model.add(tf.keras.layers.Dense(128, activation = 'relu'))
# model.add(tf.keras.layers.Dense(10, activation = 'softmax'))
#
# model.compile(optimizer = 'adam' , loss = 'sparse_categorical_crossentropy' , metrics=['accuracy'])
#
# model.fit(x_train,y_train, epochs = 10)
#
# model.save('handwritten2.model')

model = tf.keras.models.load_model('handwritten.model')



image_number = 11
while image_number>=0:
    try:
        img = cv2.imread(f"digit{image_number}.jpg")[:,:,0]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)
        print(f"This digit is probably a {np.argmax(prediction)}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
    except:
        print("Eroor!")
    finally:
        image_number-=1