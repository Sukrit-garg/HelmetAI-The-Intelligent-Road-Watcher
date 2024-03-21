# HelmetAI-The-Intelligent-Road-Watcher

Welcome to my new project, HelmetAI.

**HelmetAI** is an intelligent system designed to monitor road users and detect riders without helmets. The system uses YOLOv8 for object detection and PaddleOCR for number plate recognition. It can detect four classes: rider, with helmet, without helmet, and number plate. When a rider without a helmet is detected, the system crops the corresponding number plate from the original image and performs OCR to retrieve the number plate text.

Getting Started
Follow these steps to set up and run the HelmetAI project on your local machine.

Prerequisites
- Python 3.6 or higher
- pip (Python package installer)
Installation
1. Create a virtual environment (recommended):

```bash
python -m venv myenv
```

2. Activate the virtual environment:
  - On Windows:
    ```bash
    myenv\Scripts\activate
    ```
  - On Unix or macOS:
```bash
source myenv/bin/activate
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```
4. Download the pre-trained YOLOv8 model weights (best.pt) for the custom dataset. You can find the model weights file here.
5. Update the paths to the best.pt file in the project code.
6. Running the Application
- Start the Django server:
```bash
python manage.py runserver
```
- Open your web browser and navigate to http://localhost:8000.
- Choose an image file containing riders and vehicles.
- The application will process the image, detect riders without helmets, and display the corresponding number plates.
Output
The application will display the processed image with bounding boxes around the detect#ed objects (riders, helmets, and number plates). For riders without helmets, the corresponding number plate text will be shown.

![image](https://github.com/Sukrit-garg/HelmetAI-The-Intelligent-Road-Watcher/assets/101797008/56777de5-9a6b-4db3-94ec-9ab9d075557d)

### Sample Image:

<img width="273" alt="72" src="https://github.com/Sukrit-garg/HelmetAI-The-Intelligent-Road-Watcher/assets/101797008/6cbee802-eb13-4374-a13e-c42cd0bfe7ba">

### Sample bounding boxes:

![image0](https://github.com/Sukrit-garg/HelmetAI-The-Intelligent-Road-Watcher/assets/101797008/272d9550-013e-4201-95ab-376c4a515ce3)

### Sample number plate output:

![image](https://github.com/Sukrit-garg/HelmetAI-The-Intelligent-Road-Watcher/assets/101797008/15d40a2e-a5b4-4a92-abc4-87d1c383d39e)



Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License.

Acknowledgments:
- YOLOv8 for object detection
- PaddleOCR for optical character recognition
- https://www.kaggle.com/datasets/aneesarom/rider-with-helmet-without-helmet-number-plate
