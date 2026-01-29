import os
import glob
from pydub import AudioSegment

def get_total_duration(directory):
    total_duration_ms = 0
    wav_files = glob.glob(os.path.join(directory, "*.wav"))

    for wav_file in wav_files:
        try:
            audio = AudioSegment.from_wav(wav_file)
            total_duration_ms += len(audio)  # duration in milliseconds
        except Exception as e:
            print(f"Error reading {wav_file}: {e}")

    total_seconds = total_duration_ms / 1000

    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    print(f"Total duration: {hours:02d}:{minutes:02d}:{seconds:02d} (HH:MM:SS)")
    print(f"Total duration in seconds: {total_seconds:.2f}")

if __name__ == "__main__":
    target_directory = "./dataset/h.nakamura_20250719"  # カレントディレクトリ
    get_total_duration(target_directory)
