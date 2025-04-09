# SyncFx™

A Premiere Pro plugin that syncs cuts, effects, and markers to music automatically.

## Folder Structure
- `plugin/` - the Premiere Pro panel (HTML/JS)
- `engine/` - Python script for beat detection
- `bridge/` - communication between frontend and backend

## Getting Started
1. Clone the repo or unzip this project
2. Open in VS Code
3. Run `engine/beat_detector.py` with an MP3 file to test beat detection
4. Set up CEP plugin panel for Premiere Pro using the files in `plugin/`
