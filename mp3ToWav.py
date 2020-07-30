#comandos de todas as dependencias que s]ao necess[arias para  biblioteca funcionar no Ubuntu
#apt-get install ffmpeg
#apt-get install swig
#apt-get install libpulse-dev
#apt-get install libasound2-dev

from os import path
from pydub import AudioSegment
import speech_recognition as sr
from pocketsphinx import AudioFile
r = sr.Recognizer()

def convert():
    src = "audio.mp3" #arquivo de origem
    dst = "test.wav" #arquivo final

    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src) #caso o arquivo não seja mp3, consultar a biblioteca para outras posibilidades e mudar a função
    sound.export(dst, format="wav") #salvando em .wav

convert()
teste = sr.AudioFile('test.wav')
with teste as source:
    audio = r.record(source) #abrindo o arqiovo de audio

audioT = r.recognize_sphinx(audio) #transformando o audio em texto para ser printado na tela

print(audioT)


