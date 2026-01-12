from PIL import Image


class Image_To_Ascii:
    def __init__(self, image_path, target_width) -> None:
        self.image_path = image_path
        self.target_width = target_width
        self.charset = (
            r" .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
        )
        self.default_number_for_terminal = 0.45

    def load_images(self):
        """
        This method is just responsible for loading the image
        """
        # takes the image path and loads the image
        try:
            return Image.open(self.image_path)

        except Exception as e:
            print("An error occured here")
            print("Error:", e)

    def turn_image_to_greyscale_and_get_aspect_ratio(self):
        """
        Method that turns the image to greyscale and gets the aspect ratio
        """

        # first we get the image from load images
        get_image = self.load_images()

        # turn the image to l mode i think
        to_grayscale = get_image.convert("L")

        # get the aspect ratio of the image
        aspect_ratio = to_grayscale.height / to_grayscale.width
        return to_grayscale, aspect_ratio

    def get_complete_vals_for_art(self) -> list:
        """
        This method is responsible for drawing the ascii art
        """
        greyscale_image, aspect_ratio = (
            self.turn_image_to_greyscale_and_get_aspect_ratio()
        )
        terminal_image_height = (
            self.target_width * aspect_ratio * self.default_number_for_terminal
        )
        resize_image = greyscale_image.resize(
            (self.target_width, int(terminal_image_height))
        )
        get_brightness_pixels = list(resize_image.getdata())
        return get_brightness_pixels

    def draw_ascii_image(self):
        """
        This method is responsible for drawing the ascii art
        """

        pixel_list = self.get_complete_vals_for_art()
        pixel_list_length = len(pixel_list)
        charset_length = len(self.charset)
        height = int(pixel_list_length / self.target_width)
        ascii_char = []
        ascii_rows = []

        for pixel in pixel_list:
            # get each pixel as a value from 0 - 1
            get_decimal_value = pixel / 255

            # multiply the decimal value by the length of the charset to know which charset to use for each pixel
            # We are minusing 1 to accomodate the list indices when we start looping
            char_index = int(get_decimal_value * (charset_length - 1))
            # print(pixel, get_decimal_value, self.charset[char_index], char_index)

            charset_to_use = self.charset[char_index]
            ascii_char.append(charset_to_use)

        for num in range(height):
            start_row = num * self.target_width
            end_row = start_row + self.target_width

            row_chars = ascii_char[start_row:end_row]
            row_string = "".join(row_chars)
            ascii_rows.append(row_string)

        ascii_art = "\n".join(ascii_rows)
        print(ascii_art)

        return ascii_art
