# Setup

Create environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Verify OpenCV:

python -c "import cv2; print(cv2.__version__)"
