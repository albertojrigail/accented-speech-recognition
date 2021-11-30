# accented-speech-recognition
This project has two phases:
1. Assessing Amazon Transcribe, Google Speech-to-text, and Mozilla Deep Speech on accented English speech. We use the [JiWER](https://github.com/jitsi/jiwer) library to compute WER score, and the Speech Accent Archive [dataset](https://www.kaggle.com/rtatman/speech-accent-archive).
2. Re-training of Mozilla Deep Speech with foreign accents using Mozilla's training [API](https://deepspeech.readthedocs.io/en/r0.9/TRAINING.html).
