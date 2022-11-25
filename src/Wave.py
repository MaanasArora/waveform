import librosa
import soundfile


class Wave:
    def __init__(self, rate, waveform):
        self.rate = rate
        self.waveform = waveform

    @staticmethod
    def read(cls, filename):
        rate, waveform = librosa.load(filename)

        return Wave(rate, waveform)

    def write(self, filename):
        soundfile.write(filename, self.waveform, self.rate)

    def __len__(self):
        return len(self.waveform)
