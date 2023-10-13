import cmath
import math
import matplotlib.pyplot as plt

def fft2d(matrix):
    # Menghitung FFT dalam dimensi pertama (baris)
    rows = [fft(row) for row in matrix]
    
    # Menghitung FFT dalam dimensi kedua (kolom)
    cols = [fft([row[i] for row in rows]) for i in range(len(rows[0]))]
    
    return cols

def fft(signal):
    N = len(signal)
    if N <= 1:
        return signal
    even = fft(signal[0::2])
    odd = fft(signal[1::2])
    T = [cmath.exp(-2j * math.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + \
           [even[k] - T[k] for k in range(N // 2)]

# Contoh penggunaan FFT 2D
if _name_ == "_main_":
    # Contoh matriks 2D (citra)
    matrix = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]
    ]
    
    # Menghitung FFT 2D
    fft_result = fft2d(matrix)
    
    # Menampilkan hasil FFT
    print("FFT Result:")
    for row in fft_result:
        print(row)
    
    # Membentuk grafik dari hasil FFT
    magnitude_spectrum = [[abs(x) for x in row] for row in fft_result]
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum (FFT Result)')
    plt.colorbar()
    plt.show()