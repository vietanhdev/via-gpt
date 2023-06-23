# VIA Voice - Voice interface for VIA

This project is still in early development. Features:
- Wake word detection
- Voice recognition
- Voice control for VIA robots

## I. Train your wake word detector

**VIA Voice** uses [Mycroft Precise](https://github.com/MycroftAI/mycroft-precise) as wake word detector. Instead of "Ok Google" or "Hey, Alexa", you can use "Ok VIA" or your custom keyword to wake up voice interface.

The source code are indented to support Linux systems (Ubuntu, Raspbian, ...). However, macOS / Windows Subsystem Linux can work also (not verified).

### 1. Setup the environment

Wake word detector Mycroft Precision requires **Python 3.7** because all Python >= 3.8 don't have a right Tensorflow version. You can use an Anaconda/Miniconda environment. Clone and run environment setup:

```
git clone https://github.com/makerhanoi/via-voice --recursive
cd via-voice/mycroft-precise
./setup.sh
```

From now on, use following commands in any Terminal to activate the **precise** environment:

```
source .venv/bin/activate
```

### 2. Train your own wake word detector

For training your custom wake word, use the instruction [here](https://github.com/MycroftAI/mycroft-precise/wiki/Training-your-own-wake-word#how-to-train-your-own-wake-word).

**Known error:** If you meet following error, reinstall `h5py` to version `2.10.0`.

Error:

```
model_config = json.loads(model_config.decode('utf-8'))
AttributeError: 'str' object has no attribute 'decode'
```

Resolve by reinstall `h5py`:

```
pip install h5py==2.10.0 --force-reinstall
```

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
