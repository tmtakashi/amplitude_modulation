import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

fs = 48000
t = 3

n = np.arange(t * fs)

#変調周波数
fmod = 20
#搬送周波数
fc = 500

#振幅
A = 1
Am = 3
#周期的振幅変調音
AM = A * (1 + Am * np.cos(2*np.pi*fc*n/fs) + 1/2 * Am*np.cos(2*np.pi*(fc-fmod)*n/fs) + 1/2 * Am*np.cos(2*np.pi*(fc+fmod)*n/fs))
# AM = A*Am*np.cos(2*np.pi*fmod*n/fs)*np.cos(2*np.pi*fc*n/fs)

plt.plot(n / fs, AM, label='fmod={0}[Hz], fc={1}[Hz]'.format(fmod, fc))
plt.xlabel('time[s]')
plt.xlim(0, 0.1)
plt.legend(loc='lower right')
plt.savefig("AM.png",format = 'png', dpi=300)
plt.show()

sf.write("AM.wav", AM, fs)
