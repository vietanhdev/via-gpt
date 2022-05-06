from precise_runner import PreciseEngine, PreciseRunner
import speech_recognition as sr
import time

# Setup speech recognizer
speech_recognizer = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    speech_recognizer.adjust_for_ambient_noise(source)
trigger_voice = False

# Setup wake-word engine
wakeword_engine = PreciseEngine('./mycroft-precise/.venv/bin/precise-engine', 'pretrained_models/ok-via.pb')

def listen_and_respond():
    """Listen and response to user commands"""
    print("Listening...")
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = speech_recognizer.listen(source)

    text = None
    try:
        text = speech_recognizer.recognize_google(audio, language='vi-VN')
        print("==> " + text)    # recognize speech using Google Speech Recognition
    except LookupError:                            # speech is unintelligible
        print("Could not understand audio")

def trigger_wakeword():
    """Activate listening
    """
    global trigger_voice
    trigger_voice = True

# Run wakeword engine
wakeword_runner = PreciseRunner(wakeword_engine, on_activation=trigger_wakeword,
                    sensitivity = 0.8, trigger_level=10)
wakeword_runner.start()

# Main loop
while True:
    time.sleep(0.1)
    if trigger_voice:
        listen_and_respond()
        trigger_voice = False
