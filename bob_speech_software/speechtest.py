import speech_recognition as sr
import pyttsx3
import speech_library as sp
import requests
"""def error_decorator(fun_def):
    try:
        fun_def()
    except:
        sp.bob_speaks("bob is confused, would you like some help?")
        ## integrate reinitialization function"""

class Bob():
    def __init__(self):
        self.name = "Bob"
        self.serial_number = "1"
        self.model_number = "grasp_1"
        self.personality = "polite_nice"
        self.special_speech_start = ["bob"]
        self.special_speech_stop = ["thank you"]
        self.manual_control_sensor = "speech"
        self.network_connection_dict = {}
        self.connected_modules = {}
        self.positional_data = 0

    def idle(self):
        while True:
            try:
                print("I am ready")
                if self.key_start_detector(self.manual_control_sensor):
                    r = requests.post("http://192.168.146.146", data = "turn on")
                    return True
            except:
                pass

    def key_start_detector(self, current_sensor):
        if current_sensor == "speech":
            speech = sp.activate_speech_recon()
            print(speech)
            for elements in self.special_speech_start:
                if elements in speech.lower():
                    return True

    def manual_mode(self):
        sp.bob_speaks("Hi master, please give me instructions")
        while True:
            try:
                print("ready for instructions")
                text = sp.activate_speech_recon()

                for elements in self.special_speech_stop:
                    if elements in text:
                        sp.bob_speaks("Goodbye master. Call me when you need me")
                        r = requests.post("http://192.168.146.146", data = "turn off")
                        return 
                sp.bob_speaks(f"of course I can {text} for you")

            except:
                sp.bob_speaks("instructions unclear")

bob = Bob()
while True:
    if bob.idle():
        bob.manual_mode()







