import contextlib
import wave

fname = 'Audio.wav'
with contextlib.closing(wave.open(fname, 'r')) as f:
  frames = f.getnframes()
  rate = f.getframerate()
  duration = frames / float(rate)
  print(duration)
