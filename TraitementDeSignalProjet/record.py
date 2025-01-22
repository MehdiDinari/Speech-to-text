import sounddevice as sd
import scipy.io.wavfile as wav

def Record():
    # Set the desired sampling rate
    sampling_rate = 16000

    # Set the duration of the recording in seconds
    duration = 1

    # Record audio
    print("Recording audio...")
    audio = sd.rec(int(duration * sampling_rate), samplerate=sampling_rate, channels=1)
    sd.wait()  # Wait until the recording is complete

    # Save the recorded audio to a WAV file
    wav.write("recorded_audio.wav", sampling_rate, audio)

    print("Recording saved as 'recorded_audio.wav'")
