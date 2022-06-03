import speech_recognition as sr
import pyttsx3
def bob_speaks(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def bob_stopping_detection(text):
    key_stopping_words = ["stop", "thank you", "goodbye", "merci", "salut", "arrete"]
    for elements in key_stopping_words:
        if elements in text:
            return True
    else:
        return(False)

def interaction_mode():
    stop_interaction = False
    while not stop_interaction:
        text = activate_speech_recon()
        stop_interaction = bob_stopping_detection(text)
        if "can you" in text:
            bob_speaks("of course i can")

def activate_speech_recon():
    r = sr.Recognizer()
    with sr.Microphone() as source2:
            audio2 = r.listen(source2)
            text = r.recognize_google(audio2)
    return text

def definitive_answer(conditionnal_string):
    while True:
        try:
            text = activate_speech_recon()
            print(text)
            for elements in conditionnal_string.split():
                if elements in text:
                    return elements
        except:
            bob_speaks("Master, that option is not available")

