import os

from snapcat import image_recognition

script_dir = os.path.dirname(__file__)
rel_path = './resources/wakeupcat.jpg'
with open(os.path.join(script_dir, rel_path), mode='rb') as file:
    fileContent = file.read()
    assert image_recognition.is_cat(fileContent) is False
    assert image_recognition.has_label(fileContent, 'turtle') is True
