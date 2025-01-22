import os
import librosa
import numpy as np
from keras.layers import Dense, Dropout, Flatten, Conv1D, Input, MaxPooling1D
from keras.models import Model
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import backend as K
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
import tensorflow as tf

# Set the path for the audio files
train_audio_path = r"C:\Users\Fddkk\Downloads\TS\TraitementDeSignalProjet\trainingInputs"
labels = os.listdir(train_audio_path)

# Initialize lists to hold wave data and labels
all_wave = []
all_label = []

# Load and process the audio files
for label in labels:
    print(label)
    label_path = os.path.join(train_audio_path, label)
    waves = [f for f in os.listdir(label_path) if f.endswith('.wav')]

    for wav in waves:
        file_path = os.path.join(label_path, wav)
        samples, sample_rate = librosa.load(file_path, sr=16000)
        samples = librosa.resample(samples, orig_sr=sample_rate, target_sr=8000)

        if len(samples) == 8000:
            all_wave.append(samples)
            all_label.append(label)

# Encode the labels
le = LabelEncoder()
y = le.fit_transform(all_label)
y = to_categorical(y, num_classes=len(labels))

# Reshape the wave data
all_wave = np.array(all_wave).reshape(-1, 8000, 1)

# Split the data into training and validation sets
x_tr, x_val, y_tr, y_val = train_test_split(all_wave, y, stratify=y, test_size=0.2, random_state=777, shuffle=True)

# Clear previous models from memory
tf.compat.v1.reset_default_graph()
K.clear_session()

# Define the model architecture
inputs = Input(shape=(8000, 1))

# First Layer
conv = Conv1D(8, 13, padding='valid', activation='relu', strides=1)(inputs)
conv = MaxPooling1D(3)(conv)
conv = Dropout(0.3)(conv)

# Second Layer
conv = Conv1D(16, 11, padding='valid', activation='relu', strides=1)(conv)
conv = MaxPooling1D(3)(conv)
conv = Dropout(0.3)(conv)

# Third Layer
conv = Conv1D(32, 9, padding='valid', activation='relu', strides=1)(conv)
conv = MaxPooling1D(3)(conv)
conv = Dropout(0.3)(conv)

# Fourth Layer
conv = Conv1D(64, 7, padding='valid', activation='relu', strides=1)(conv)
conv = MaxPooling1D(3)(conv)
conv = Dropout(0.3)(conv)

# Fifth Layer
conv = Conv1D(128, 5, padding='valid', activation='relu', strides=1)(conv)
conv = MaxPooling1D(3)(conv)
conv = Dropout(0.3)(conv)

# Sixth Layer
conv = Conv1D(256, 3, padding='valid', activation='relu', strides=1)(conv)
conv = MaxPooling1D(3)(conv)
conv = Dropout(0.3)(conv)

# Flatten Layer
conv = Flatten()(conv)

# Dense Layer 1
conv = Dense(256, activation='relu')(conv)
conv = Dropout(0.3)(conv)

# Dense Layer 2
conv = Dense(128, activation='relu')(conv)
conv = Dropout(0.3)(conv)

# Output Layer
outputs = Dense(len(labels), activation='softmax')(conv)

# Compile the model
model = Model(inputs, outputs)
model.summary()
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Define callbacks
es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=10, min_delta=0.0001)
mc = ModelCheckpoint(filepath='best_model2.keras', monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')

# Train the model
history = model.fit(x_tr, y_tr, epochs=100, callbacks=[es, mc], batch_size=32, validation_data=(x_val, y_val))

# Plot the training history
plt.plot(history.history['accuracy'])