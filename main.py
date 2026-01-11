from draw import Image_To_Ascii


def main():
    img = Image_To_Ascii("images/photo_test.avif")
    img.draw_ascii_image()


if __name__ == "__main__":
    main()
