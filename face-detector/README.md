# Face Detector

This project is a simple face detection application using Python. It utilizes OpenCV and other libraries to detect faces in images or video streams.

## Features

- Detect faces in images
- Detect faces in video streams
- Save detected faces as separate images

## Requirements

- Python 3.x
- OpenCV
- NumPy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/face-detector.git
    cd face-detector
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Detect Faces in an Image

```bash
python detect_faces.py --image path/to/your/image.jpg
```

### Detect Faces in a Video Stream

```bash
python detect_faces.py --video path/to/your/video.mp4
```

### Save Detected Faces

```bash
python detect_faces.py --image path/to/your/image.jpg --save
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenCV
- NumPy
