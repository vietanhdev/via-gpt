from precise_runner import PreciseEngine, PreciseRunner
import speech_recognition as sr
from gtts import gTTS
import playsound
from vnm_utils import check_pattern_in_text, standardize_tone
import time

# Setup speech recognizer
speech_recognizer = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    speech_recognizer.adjust_for_ambient_noise(source)
trigger_voice = False

# Setup wake-word engine
wakeword_engine = PreciseEngine('./mycroft-precise/.venv/bin/precise-engine', 'pretrained_models/ok-via.pb')

def play_audio_from_text(text):
    """Play audio from text"""
    tts = gTTS(text, lang='vi')
    tts.save("output.mp3")
    playsound.playsound('output.mp3', True)

def listen_and_respond():
    """Listen and response to user commands"""
    print("Listening...")
    playsound.playsound("activate.wav", True)
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = speech_recognizer.listen(source)

    text = None
    try:
        text = speech_recognizer.recognize_google(audio, language='vi-VN')
        print("==> " + text)    # recognize speech using Google Speech Recognition
    except LookupError:                            # speech is unintelligible
        print("Could not understand audio")

    # Process text
    text = text.lower()
    text = standardize_tone(text)
    if "chào" in text:
        response = "Xin chào, tôi là VIA, tôi có thể giúp gì cho bạn?"
        print(response)
        play_audio_from_text(response)
    elif check_pattern_in_text("bật điều hoà", text):
        response = "Bật điều hoà thành công"
        print(response)
        play_audio_from_text(response)
    elif check_pattern_in_text("tắt điều hoà", text):
        response = "Tắt điều hoà thành công"
        print(response)
        play_audio_from_text(response)


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
