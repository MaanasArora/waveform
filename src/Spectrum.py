import numpy as np
from scipy.fft import fft, fftfreq


class Spectrum:
    def __init__(self, rate, frames, freqs):
        self.rate = rate
        self.frames = frames
        self.freqs = freqs

    @classmethod
    def create_from_wave(cls, spectrum_rate, wave):
        waveform = wave.waveform

        window_size = wave.rate // spectrum_rate
        num_windows = len(waveform) // window_size

        frames = np.array(
            fft(waveform[window_size * i:window_size * (i + 1)])
            for i in range(num_windows)
        )
        freqs = fftfreq(window_size, 1 / wave.rate)

        return Spectrum(spectrum_rate, frames, freqs)
