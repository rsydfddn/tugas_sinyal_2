# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 19:43:05 2023

@author: Rasyid
"""

import cmath
import math
import matplotlib.pyplot as plt

def fft(signal):
    N = len(signal)
    if N <= 1:
        return signal
    even = fft(signal[0::2])
    odd = fft(signal[1::2])
    T = [cmath.exp(-2j * math.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + \
           [even[k] - T[k] for k in range(N // 2)]

# Contoh penggunaan FFT
if __name__ == "__main__":
    # Contoh sinyal 1D
    signal = [0, 1, 2, 3, 4, 5, 6, 7]
    
    # Menghitung FFT
    fft_result = fft(signal)
    
    # Menampilkan hasil FFT
    print("FFT Result:")
    print(fft_result)
    
    # Membentuk grafik dari hasil FFT
    magnitude_spectrum = [abs(x) for x in fft_result]
    plt.figure(figsize=(8, 6))
    plt.plot(magnitude_spectrum, marker='o')
    plt.title('Magnitude Spectrum (FFT Result)')
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()
z