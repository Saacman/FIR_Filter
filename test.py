import numpy as np
import soundfile as sf
from scipy.signal import firwin

size = 8
type = 'lowpass'
freq = 723

data, sample_rate = sf.read('chorwat_c3.wav')
cutoff = 2 * np.py * (freq / sample_rate)
b = firwin(size, 0.284, pass_zero = type)

data_len = len(data)
b_len = len(b)

y = np.zeros((data_len + b_len -1), dtype = float)

y_len = len(y)

for k in range(y_len):
    for i in range(k+1):
        y[k] += data[i] * b[k-i] if((k-i)<b_len and i<data_len) else 0
    print("{0:.1f}%".format((k/y_len)*100.0))

sf.write('output.wav', y, sample_rate)
