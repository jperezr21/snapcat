import logging
from time import sleep

from gpiozero import MotionSensor

from snapcat import camera, image_recognition, twitter_client

PICTURE_PATH = '/tmp/picture.jpeg'


def main():
    logger = logging.getLogger()
    pir = MotionSensor(4)
    while True:
        if pir.motion_detected:
            logger.info('Motion detected')
            camera.take_picture(PICTURE_PATH)
            logger.info('Took picture')
            picture = open(PICTURE_PATH, 'rb').read()
            if image_recognition.is_cat(picture):
                logger.info('Cat recognized')
                twitter_client.upload_image(PICTURE_PATH)
                logger.info('Cat picture uploaded')
                sleep(10 * 60)
            else:
                logger.info('Not a cat')
                sleep(10)


if __name__ == "__main__":
    main()
