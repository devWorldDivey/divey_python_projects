import speech_recognition_python as sr
listener = sr.Recognizer()
#try:
with sr.Microphone() as source:
    print("Listening...")
    voice = listener.listen(source)
    command = listener.recognize_google_cloud(voice)
    print(command)
#except:
    #print("Error")
