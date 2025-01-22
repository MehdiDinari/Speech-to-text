import librosa
import IPython.display as ipd
import numpy as np
from keras.models import load_model
import os


def Test():
    train_audio_path = r"C:\Users\Fddkk\Downloads\TS\TraitementDeSignalProjet\trainingInputs"
    classes = os.listdir(train_audio_path)

    model = load_model('best_model2.hdf5')

    def predict(audio):
        prob = model.predict(audio.reshape(1, 8000, 1))
        print(prob[0])
        index = np.argmax(prob[0])
        return classes[index]

    samples, sample_rate = librosa.load(r"C:\Users\Fddkk\Downloads\TS\TraitementDeSignalProjet\recorded_audio.wav",
                                        sr=16000)

    # Resample the audio to the target sample rate
    samples = librosa.resample(samples, orig_sr=sample_rate, target_sr=8000)

    # Adjust the size of the audio array to match the expected shape
    desired_size = 8000
    if len(samples) < desired_size:
        padding = np.zeros((desired_size - len(samples),))
        samples = np.concatenate((padding, samples, padding))
    elif len(samples) > desired_size:
        samples = samples[:desired_size]

    ipd.Audio(samples, rate=8000)
    print(predict(samples))
    return predict(samples)