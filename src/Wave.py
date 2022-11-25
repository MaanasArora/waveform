import librosa
import soundfile


class Wave:
    def __init__(self, rate, waveform):
        self.rate = rate
        self.waveform = waveform

    @classmethod
    def read(cls, filename):
        waveform, rate = librosa.load(filename)

        return Wave(rate, waveform)

    def write(self, filename):
        soundfile.write(filename, self.waveform, self.rate)

    def __len__(self):
        return len(self.waveform)
