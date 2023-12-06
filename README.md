# VIA GPT - Talk with VIA

This project is still in early development. Features:

- Wake word detection
- Voice recognition
- Voice chat with ChatGPT

```
sudo apt install flac
```

## I. Train your wake word detector

Train your custom wake word detector using online service from <https://console.picovoice.ai/>.

## II. Run VIA voice example

After setting up the environment as the instruction in I., install requirements for VIA assistant:

```
source mycroft-precise/.venv/bin/activate
cd via-voice
pip install -r requirements.txt
```

Run the example:

```
python via_assistant.py
```
