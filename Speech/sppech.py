# -*- coding: utf-8 -*-
"""Sppech.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_MeugfOI5BVU16aijbnqwkLf_5wXFyTx
"""

import librosa
import matplotlib.pyplot as plt
import numpy as np
import scipy
import soundfile as sf
# 1) Load and play an audio file
filename = "file_example_WAV_5MG.wav"
#y, sr = librosa.load(filename)
#librosa.output.write_wav('output.wav', y, sr)
y, sr = librosa.load(filename)
sf.write('output.wav', y, sr)

# 2) Compute power, pitch, and energy
D = np.abs(librosa.stft(y))**2
power = np.sum(D)
pitch = librosa.pitch_tuning(D)
energy = np.sum(D**2)/np.float64(len(y))

print(f'Power: {power}, Pitch: {pitch}, Energy: {energy}')

# 3) Plot the spectrogram
plt.figure(figsize=(12, 8))
D_db = librosa.amplitude_to_db(D, ref=np.max)
librosa.display.specshow(D_db, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.show()

# 4) Compute and display the cepstrum
cepstrum = np.real(scipy.fft.ifft(np.log(np.abs(scipy.fft.fft(y)))))
time = np.linspace(0, len(y)/sr, num=len(y))

plt.figure(figsize=(12, 8))
plt.plot(time, cepstrum)
plt.title('Cepstrum')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
