from google.cloud import vision


def is_cat(image):
    return has_label(image, 'cat')


def has_label(image, label_desc):
    labels = get_labels_from_image(image)
    wanted_label = None
    for label in labels:
        if label.description == label_desc:
            wanted_label = label
    if not wanted_label:
        return False
    else:
        if wanted_label.score > 0.95:
            return True
        else:
            return False


def get_labels_from_image(image):
    vision_client = vision.Client()
    result = vision_client.image(content=image)
    return result.detect_labels()
