# This is a sample Python script.
import struct

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from scipy.fftpack import fft
import numpy as np
import pyaudio
import matplotlib.pyplot as plt


class Test(object):

    def __init__(self):
        # stream constants
        self.CHUNK = 2048 * 2
        self.FORMAT = pyaudio.paInt32
        self.CHANNELS = 1
        self.RATE = 44100
        self.pause = False

        # stream object
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK,
        )

        self.seenvalues = set()

    # goal: returns the max frequency of waveform
    def get_fundamental_frequency(self, audio_waveform):
        spectrum = fft(audio_waveform)

        # scale the spectrum
        scaled_spectrum = np.abs(spectrum[0:self.CHUNK]) / (128 * self.CHUNK)

        # clean the nullish first and last values
        cleaned_scaled_spectrum = scaled_spectrum[10:-10]

        # get the index of the max
        np_max = max(cleaned_scaled_spectrum)
        max_index = np.where(scaled_spectrum == np_max)[0][0]

        # the index corresponds to the following linspace
        index_to_freq = np.linspace(0, self.RATE, self.CHUNK)
        return index_to_freq[max_index], scaled_spectrum

    def read_audio_stream(self):
        data = self.stream.read(self.CHUNK, exception_on_overflow=False)
        data_int = struct.unpack(str(4 * self.CHUNK) + 'B', data)
        return data_int

    def open_loop(self, graphics=True):
        self.init_plots()
        while not self.pause:
            waveform = self.read_audio_stream()
            freq_max, scaled_spectrum = self.get_fundamental_frequency(waveform)
            if 250 < freq_max < 550:
                if freq_max not in self.seenvalues:
                    print(freq_max)
                self.seenvalues.add(freq_max)

            # update figure canvas if wanted
            if graphics:
                # set top graph
                data_np = np.array(waveform, dtype='b')[::4] + 128
                self.line.set_ydata(data_np)
                # set bottom graph
                self.line_fft.set_ydata(scaled_spectrum)

                # update figures
                self.fig.canvas.draw()
                self.fig.canvas.flush_events()

    def init_plots(self):

        # x variables for plotting
        x = np.arange(0, 2 * self.CHUNK, 2)
        xf = np.linspace(0, self.RATE, self.CHUNK)

        # create matplotlib figure and axes
        self.fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 7))

        # create a line object with random data
        self.line, = ax1.plot(x, np.random.rand(self.CHUNK), '-', lw=2)

        # create semilogx line for spectrum
        self.line_fft, = ax2.semilogx(
            xf, np.random.rand(self.CHUNK), '-', lw=2)

        # format waveform axes
        ax1.set_title('AUDIO WAVEFORM')
        ax1.set_xlabel('samples')
        ax1.set_ylabel('volume')
        ax1.set_ylim(0, 255)
        ax1.set_xlim(0, 2 * self.CHUNK)
        plt.setp(
            ax1, yticks=[0, 128, 255],
            xticks=[0, self.CHUNK, 2 * self.CHUNK],
        )
        plt.setp(ax2, yticks=[0, 1], )

        # format spectrum axes
        ax2.set_xlim(20, self.RATE / 2)

        # show axes
        thismanager = plt.get_current_fig_manager()
        # thismanager.window.setGeometry(5, 120, 1910, 1070)
        plt.show(block=False)


if __name__ == '__main__':
    t = Test()
    t.open_loop()
