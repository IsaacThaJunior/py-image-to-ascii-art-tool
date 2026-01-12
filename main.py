from draw import Image_To_Ascii
import argparse
import os


def main():
    parser = argparse.ArgumentParser(
        description="Convert an image to ascii art",
        epilog="Example: ascii_art.py image.jpg --width 100 --format html",
    )
    parser.add_argument(
        "image",
        help="The image to convert to ascii art",
    )
    parser.add_argument(
        "width",
        type=int,
        default=100,
        help="The width of the ascii art. If you want clear and photorealistic image then width should be greater than 100. The greater the better",
    )
    # parser.add_argument(
    #     "--format",
    #     "-f",
    #     type=str,
    #     default="html",
    #     help="The format of the ascii art",
    # )
    args = parser.parse_args()

    if not os.path.exists(args.image):
        parser.error(f"No file as {args.image} exists")
    if not os.path.isfile(args.image):
        parser.error(f"{args.image} exists but is not a file")

    if args.width < 50:
        parser.error("Width must be greater than 50")

    img = Image_To_Ascii(args.image, args.width)
    img.draw_ascii_image()


if __name__ == "__main__":
    main()
