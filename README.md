# TimeLapse Screenshot to Video

This project lets you capture screenshots at regular intervals and combine them into a timelapse video.

## Structure

- `make_screenshots.py` — Captures screenshots at set intervals and saves them in the `screenshots/` folder.
- `make_video.py` — Combines the screenshots into a video file (`video.mp4`).
- `screenshots/` — Folder containing the captured screenshots.

## Usage

### 1. Capture Screenshots

Run:

```sh
python make_screenshots.py
```

This will save screenshots in the `screenshots/` folder.

### 2. Create Video

Run:

```sh
python make_video.py
```

This will generate `video.mp4` from the screenshots.

## Requirements

- Python 3
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [opencv-python](https://pypi.org/project/opencv-python/)

Install dependencies:

```sh
pip install pyautogui opencv-python
```

## License
