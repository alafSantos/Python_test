from gtts import gTTS #pip install gtts
from playsound import playsound #pip install playsound
import os

audio = 'falando.mp3'

text = "Bom dia, meu bebê"
language = 'pt'

sp = gTTS(text = text, lang = language, slow = False)

sp.save(audio)

print(text)
playsound(audio)

os.remove("falando.mp3")