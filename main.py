from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 1, 500)
triangle = signal.sawtooth(2 * np.pi * 20 * t)
plt.plot(t, triangle)
plt.xlabel('Частоты')
plt.ylabel('Амплитуда')

from scipy.fft import fft, ifft, fftfreq
fft_result = fft(triangle)
amplitude_spectrum = np.abs(fft_result)
frequencies = fftfreq(500, 1/500)
plt.plot(frequencies, amplitude_spectrum)
plt.xlabel('Частоты')
plt.ylabel('Амплитуда')
plt.xlim(0,100)

reconstructed = ifft(fft_result).real
plt.plot(t, reconstructed, label='Исходный')
plt.plot(t, triangle, label='Восстановленный', linestyle='--')
plt.xlabel('Частоты')
plt.ylabel('Амплитуда')
plt.legend(loc="lower right")

fft_result_reconstructed_triangle = fft(reconstructed)
amplitude_spectrum_reconstructed_triangle = np.abs(fft_result_reconstructed_triangle)
plt.plot(frequencies, amplitude_spectrum, label='Исходный')
plt.plot(frequencies,amplitude_spectrum_reconstructed_triangle, label='Восстановленный', linestyle='--')
plt.legend(loc="lower right")
plt.xlim(0,100)

from scipy.io.wavfile import write
sampling_rate = 500
write('triangle_signal.wav', sampling_rate, (triangle * 32767).astype(np.int16))

t = np.linspace(0, 1, 500)
square = signal.square(2 * np.pi * 20 * t)
plt.plot(t, square)
plt.title('Прямоугольный сигнал')
plt.xlabel('Частоты')
plt.ylabel('Амплитуда')

fft_result = fft(square)
amplitude_spectrum = np.abs(fft_result)
plt.plot(frequencies, amplitude_spectrum)
plt.xlabel('Частоты')
plt.ylabel('Амплитуда')
plt.xlim(0,200)

fft_result_reconstructed_square = fft(reconstructed)
amplitude_spectrum_reconstructed_square = np.abs(fft_result_reconstructed_square)
plt.plot(frequencies, amplitude_spectrum, label='Исходный')
plt.plot(frequencies, amplitude_spectrum_reconstructed_square, label='Восстановленный', linestyle='--')
plt.legend(loc="lower right")
plt.xlim(0,100)

write('square_signal.wav', sampling_rate, (square * 32767).astype(np.int16))