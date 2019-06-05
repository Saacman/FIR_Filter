import os
import numpy as np
import soundfile as sf
from scipy.signal import firwin, butter

size = 8
type = 'lowpass'
freq = 723
data, sample_rate = sf.read('chorwat_c3.wav')


cutoff = 2 * np.pi * (freq / sample_rate)
b, a= butter(size, cutoff, type)

print(a)
print(b)
data_len = len(data)
b_len = len(b)
a_len = len(a)
y = np.zeros((data_len + b_len -1), dtype = float)

y_len = len(y)

for k in range(y_len):
    for i in range(k+1):
        #y[k] += b[k] * data[y_len-k-1] - a[k] * y[y_len-k-1]
        y[k] += data[i] * b[k-i] if((k-i)<b_len and i<data_len) else 0
        y[k] -= data[i+1] * a[k-(i+1)] if((k-(i+1))<a_len and (i+1)<data_len) else 0
    os.system("clear")
    print("{0:.1f}%".format((k/y_len)*100.0))

sf.write('output_IIR.wav', y, sample_rate)
