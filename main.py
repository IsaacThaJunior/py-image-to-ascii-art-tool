from func_utils import load_images, preprocess_img

def main():

    loaded_image = load_images("images/photo_test.avif")
    preprocess_img(loaded_image, 5)
    


if __name__ == "__main__":
    main()
