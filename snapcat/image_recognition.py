from google.cloud import vision


def is_cat(image_content):
    return has_label(image_content, 'cat')


def has_label(image_content, label_desc):
    labels = get_labels_from_image(image_content)
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


def get_labels_from_image(image_content):
    vision_client = vision.Client()
    image = vision_client.image(content=image_content)
    labels = image.detect_labels()
    return labels
