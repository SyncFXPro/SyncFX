import os
from utils.beat_detector import extract_beats
from utils.xml_generator import generate_xml

audio_file = "audio/track.mp3"
output_xml = "output/beat_markers.xml"

if not os.path.exists(audio_file):
    print("❌ Audio file not found!")
else:
    print("🎧 Analyzing audio...")
    beats = extract_beats(audio_file)
    print(f"✅ Found {len(beats)} beats.")

    print("📄 Generating XML...")
    generate_xml(beats, output_xml)
    print(f"✅ Done! File saved to: {output_xml}")