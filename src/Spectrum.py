import numpy as np
from scipy.fft import fft, fftfreq


class Spectrum:
    def __init__(self, rate, frames, freqs):
        self.rate = rate
        self.frames = frames
        self.freqs = freqs

    @staticmethod
    def create_from_wave(cls, spectrum_rate, wave):
        waveform = wave.waveform

        window_size = spectrum_rate // wave.rate
        num_windows = len(waveform) // window_size

        frames = []
        for i in range(len(waveform) // num_windows):
            win_start = window_size * i
            win_end = window_size * (i + 1)

            window = waveform[win_start:win_end]
            frames.append(fft(window))
        frames = np.array(frames)

        freqs = fftfreq(window_size, 1 / wave.rate)

        return Spectrum(spectrum_rate, frames, freqs)