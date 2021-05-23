import pyaudio
import wave
from keyboard import is_pressed
from time import sleep

STOP = "s"
i = 0

audio_rec = pyaudio.PyAudio()

stream = audio_rec.open(channels=1, rate=44100, format=pyaudio.paInt16, input=True, frames_per_buffer=1024)

frames = []



print(f"You can stop recording by Pressing: {STOP}")
input("press Enter To start recording: ")


try:
    while True:
        data = stream.read(1024)
        frames.append(data)
        i += 1
        print(f"- reading - Sec: {i}")

        if is_pressed(STOP):
            stream.stop_stream()
            stream.close()
            audio_rec.terminate()
            break
except KeyboardInterrupt:
    pass

    
file_name = input("Enter Audio-File name: ")
sound_file = wave.open(f"{file_name}.wav", "wb")

sound_file.setnchannels(1)
sound_file.setsampwidth(audio_rec.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()
