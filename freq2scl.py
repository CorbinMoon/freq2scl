import numpy as np
import matplotlib.pyplot as plt


d = 0.24
s_1 = 0.021
s_2 = 19
_a = -3.5
_b = -5.75


def dis(f, amp):
    idx = np.argsort(f)
    s_amp = np.asarray(amp)[idx]
    s_f = np.asarray(f)[idx]
    idx = np.transpose(np.triu_indices(len(s_f), 1))

    f_pairs = s_f[idx]
    amp_pairs = s_amp[idx]

    f_min = f_pairs[:, 0]
    s = d / (s_1 * f_min + s_2)
    x = s * (f_pairs[:, 1] - f_pairs[:, 0])

    v = np.prod(amp_pairs, axis=1)

    return np.sum(v * (np.exp(_a * x) - np.exp(_b * x)))


class Freq2Scl(object):

    def __init__(self):
        self.__data = None
        self.__alpharange = None

    def calc_dis(self, f, amp, n=2000, alpharange=2.1):
        data = np.zeros(n, dtype=np.float)
        a = np.concatenate((amp, amp))

        for i, alpha in enumerate(np.linspace(1, alpharange, n)):
            freq = np.concatenate((f, alpha * f))
            data[i] = dis(freq, a)

        self.__data = data
        self.__alpharange = alpharange

    def plot(self):
        plt.plot(np.linspace(1, self.__alpharange,
                             len(self.__data)), self.__data)
        plt.xlim(1, self.__alpharange)
        plt.xlabel('frequency ratio')
        plt.ylabel('sensory dissonance')
        plt.show()
