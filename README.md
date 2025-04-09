# SyncFX

SyncFX detects beats in an audio file and generates a timeline XML file with markers for Adobe Premiere.

## How to use

1. Put your `.mp3` or `.wav` file into the `audio/` folder and name it `track.mp3`
2. Run:
```bash
python app.py
```
3. Beat markers will be saved as `beat_markers.xml` in the `output/` folder
4. Import that XML file into Adobe Premiere to see the markers

## Install dependencies
```bash
pip install -r requirements.txt
```