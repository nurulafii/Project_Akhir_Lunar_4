import speech_recognition
import playsound as ps
from gtts import gTTS
from audioplayer import AudioPlayer

recognizer = speech_recognition.Recognizer()
recognize_exit = ['stop', 'udahan', 'berhenti']

def dengerin():
  with speech_recognition.Microphone() as mic:
    recognizer.adjust_for_ambient_noise(mic, 0.2)
    audio = recognizer.listen(mic)
    text = recognizer.recognize_google(audio, language="id")
    print(text.lower())
  return text.lower()

def bilang(text):
  tts = gTTS(text=text, lang="id")
  filename = "rekaman.mp3"
  tts.save(filename)
  try:
    AudioPlayer(filename).play(block=True)
  except:
     print('Maaf lagi sariawan, gabisa ngomong dulu')