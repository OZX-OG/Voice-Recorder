#import libraries
# Code Changed, Optimized And Commented By: OZX-OG

import pyaudio
import wave
import colorama
from keyboard import is_pressed
from time import sleep
from colorama import Fore

#Color
colorama.init(autoreset=True)

#You Know ;)
print(f"{Fore.YELLOW}--{Fore.GREEN} Voice Recorder By: OZX-OG {Fore.YELLOW} --")

#var
STOP = "s"
i = 0

#settings
audio_rec = pyaudio.PyAudio()

stream = audio_rec.open(channels=1, rate=44100, format=pyaudio.paInt16, input=True, frames_per_buffer=1024)

frames = []

#print info
print(f"You can stop recording by Pressing: {STOP}")
input("press Enter To start recording: ")

#clear cmd
if name == 'nt': system('cls')
else: system("clear") 

print(f"-{Fore.RED} s {Fore.WHITE}- to stop")
print(f"{Fore.YELLOW}-{Fore.GREEN} iS Recording... {Fore.YELLOW}-")

#rec
while True:
    data = stream.read(1024)
    frames.append(data)
    i += 1

    if is_pressed(STOP):
        #end rec
        stream.stop_stream()
        stream.close()
        audio_rec.terminate()
        print(f"{Fore.RED}- End Record -")
        break


#settings audio file
file_name = input("Enter Audio-File name: ")
sound_file = wave.open(f"{file_name}.wav", "wb")

sound_file.setnchannels(1)
sound_file.setsampwidth(audio_rec.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()
