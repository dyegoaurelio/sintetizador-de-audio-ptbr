import pyttsx3

speaker = pyttsx3.init()
speaker.setProperty('voice', 'brazil') 
speaker.setProperty('rate', 150)

texto = open('texto.txt','r').read()

speaker.save_to_file(texto, 'output.mp3')
speaker.say(texto)
speaker.runAndWait()
