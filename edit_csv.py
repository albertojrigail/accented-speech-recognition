from csv import reader
from os.path import join
import pandas as pd
import speech_accent_archive_analysis

files = ["amazon_transcribe.csv", "google_speech_to_text.csv", "mozilla_deepspeech.csv"]
output_files = ["amazon_transcribe_key.csv", "google_speech_to_text_key.csv", "mozilla_deepspeech_key.csv"]
scores_dir = "asr_scores"

for i in range(len(files)):
    f = files[i]
    path = join(scores_dir, f)
    df = pd.read_csv(path)
    df = df[df['frequency'] > 15]
    output_f = output_files[i]
    output_path = join(scores_dir, output_f)
    df.to_csv(output_path, index=False)




