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
    get_brightness_pixels = list(resize_image.getdata())

    return get_brightness_pixels, target_width


def create_ascii_art(pixels, width, charset):
    if not pixels:
        raise Exception("Pixel List is empty")
    if not width:
        raise Exception("Width cannot be zero or less than")
    if not charset:
        raise Exception("You must pass in a charset for the ascii art")

    pixel_list_length = len(pixels)
    charset_length = len(charset)
    height = int(pixel_list_length / width)

    ascii_chars = []

    for brightness_value in pixels:
        get_decimal_value = brightness_value / 255
        char_index = int(get_decimal_value * (charset_length - 1))
        if char_index >= charset_length:
            char_index = charset_length - 1
        charset_to_use = charset[char_index]
        ascii_chars.append(charset_to_use)

    ascii_rows = []

    for row in range(height):
        start_index = row * width
        end_index = start_index + width

        row_chars = ascii_chars[start_index:end_index]
        row_string = "".join(row_chars)
        ascii_rows.append(row_string)

    ascii_art = "\n".join(ascii_rows)
    print("Here is the ascii art:", ascii_art)

    return ascii_art
