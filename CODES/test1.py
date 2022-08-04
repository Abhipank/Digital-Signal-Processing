import soundfile as sf

from scipy import signal

#read .wav file
input_signal,fs = sf.read('Sound_Noise.wav')   
#signal time domain being discretized
print(len(input_signal),fs)
#sampling frequency of Input signal
sampl_freq=fs

#order of the filter
order=4

#cutoff frquency 4kHz
cutoff_freq=4000.0

#digital frequency
Wn=2*cutoff_freq/sampl_freq

# b and a are numerator and denominator polynomials respectively

b, a = signal.butter(order,Wn, 'low')

#filter the input signal with butterworth filter

output_signal = signal.filtfilt(b, a,input_signal)
#output signal = signal.lfilter(b, a,input_signal)

#write the output signal into .wav file
#sf.write('Sound With ReducedNoise.wav',output_signal,fs)




#spectrogram is 3D plot of amplitude of a signal wrt time and frequency.
#A “keystroke” is just any interaction you make with a button on your keyboard.Keystrokes are how you “speak” to your computers. Each keystroke transmits a signal that tells your computer programs what you want them to do.
#The order of a digital filter is the number of previous inputs (stored in the processor's memory) used to calculate the current output.
