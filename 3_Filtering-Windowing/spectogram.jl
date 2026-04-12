using DSP
using Plots; gr()

fs = 44100
ts = range(0, stop=5, step=1/fs)
signal = @. sin(2π*1000*ts^2)
n = length(signal)
nw = n/50
spec = spectrogram(signal, nw, nw/2; fs=fs)
heatmap(spec.time, spec.frequ, spec.power, xguide="Time [s]", yguide="Frequency [Hz]")