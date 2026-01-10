from PIL import Image, ImageOps


def load_images(image_path):
    # check that the image is a real one by checking if the extension
    # ends with JPG, PNG or JPEG
    try:
        return Image.open(image_path)

    except Exception as e:
        print("Error:", e)


def preprocess_img(img_object, target_width):
    to_greyscale = ImageOps.grayscale(img_object)
    aspect_ratio = to_greyscale.height / to_greyscale.width
    new_height = target_width * aspect_ratio * 0.45
    resize_image = to_greyscale.resize((target_width, int(new_height)))
