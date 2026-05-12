import numpy as np
import pandas as pd
import os
for dirname, _, filenames in os.walk('./Dataset'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_hub as hub
from keras.layers import Dense, Flatten, Lambda, Dense, Flatten
from keras.models import Sequential, Model
from keras.applications.vgg16 import VGG16
from keras.src.legacy.preprocessing.image import ImageDataGenerator
from keras.utils import load_img  # Correct import
import ssl
ssl._create_default_https_context = ssl._create_unverified_context  # Bypass SSL verification
from keras.preprocessing import image
import cv2
import os
import PIL.Image as Image
from glob import glob
IMAGE_SIZE = [224, 224]
train_path = './Dataset'
vgg16 = VGG16(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)
for layer in vgg16.layers:
    layer.trainable = False
folders = glob('./Dataset/*')
print (len(folders))
x = Flatten()(vgg16.output)
prediction=Dense(len(folders), activation='softmax')(x)
model=Model(inputs=vgg16.input, outputs=prediction)
model.summary()
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)
train_datagen = ImageDataGenerator(rescale = 1./255, shear_range =  0.2, zoom_range = 0.2, horizontal_flip = True)
train_set = train_datagen.flow_from_directory('./Dataset', target_size = (224, 224),
                                            batch_size = 32, class_mode = 'categorical')
r = model.fit(train_set, epochs = 10, steps_per_epoch = len(train_set))
from IPython import display
#display.set_matplotlin_formats('svg')
#plt.style.use('seaborn-pastel')
plt.plot(r.history['loss'],label='train loss')
plt.legend()
plt.show()
plt.savefig('loss.png')
plt.accuracy.plot(r.history['accuracy'],label='train accuracy')
plt.legend()
plt.show()
plt.savefig('Accuracy.png')
plt.tight_layout()
model.save('model_vgg16.h5')