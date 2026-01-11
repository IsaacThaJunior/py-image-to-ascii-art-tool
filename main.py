from func_utils import load_images, preprocess_img, create_ascii_art

def main():
    
    # charset_to_use = "@%#*+=-:. " 
    charset_to_use = " .:-=+*#%@"

    loaded_image = load_images("images/photo_test.avif")
    pixel_list, width = preprocess_img(loaded_image, 100)
    create_ascii_art(pixel_list, width, charset_to_use)
    


if __name__ == "__main__":
    main()
