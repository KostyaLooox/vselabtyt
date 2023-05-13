from pydub import AudioSegment

s = AudioSegment.from_file("234.wav")
sf = s.speedup(1.5)
sf.export('1.wav', format="wav")