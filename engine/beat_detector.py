import librosa

def detect_beats(audio_path):
    y, sr = librosa.load(audio_path)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    times = librosa.frames_to_time(beats, sr=sr)
    return times

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "sample.mp3"
    beat_times = detect_beats(path)
    for t in beat_times:
        print(f"{t:.2f}")