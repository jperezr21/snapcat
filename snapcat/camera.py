from time import sleep
from picamera import PiCamera


def take_picture(path):
    camera = PiCamera()
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture(path)
    camera.close()
