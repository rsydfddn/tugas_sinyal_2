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
    
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

def fft2d(data):
    # FFT pada setiap baris
    rows = [fft(row) for row in data]
    # FFT pada setiap kolom
    cols = [fft([row[i] for row in rows]) for i in range(len(data[0]))]
    return cols

# Contoh penggunaan FFT 2D
if __name__ == "__main__":
    # Contoh data dua dimensi
    data = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    
    # Menghitung FFT dua dimensi
    fft_result = fft2d(data)

    # Menampilkan hasil FFT
    print("FFT Result:")
    for row in fft_result:
        print(row)
    
    # Membentuk grafik dari hasil FFT
    magnitude_spectrum = [[abs(x) for x in row] for row in fft_result]
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.show()
