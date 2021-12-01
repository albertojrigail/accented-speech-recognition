from csv import reader
from os.path import join
import pandas as pd

files = ["amazon_transcribe_old.csv", "google_speech_to_text_old.csv", "mozilla_deepspeech.csv"]
scores_dir = "asr_scores"

for f in files:
    path = join(scores_dir, f)
    df = pd.read_csv(path)
    for i in range(len(df['number'])):
        df['number'][i] = i
    print(df['number'])
    df.to_csv(path, index=False)




