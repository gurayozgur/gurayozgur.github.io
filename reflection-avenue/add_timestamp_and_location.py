def add_timestamp_and_location():
    from PIL import Image, ImageDraw, ImageFont
    location = input("Enter the location: ")
    timestamp = input("Enter the timestamp: ")
    q = input("url or path: ")
    if q == "url":
        img_url = input("Enter the URL of the image: ")
        import urllib.request
        urllib.request.urlretrieve(img_url,"image_with_timestamp.jpg")
        image = Image.open("image_with_timestamp.jpg")
    else:
        img_pth = input("Enter the path of the image: ")
        image = Image.open(img_pth)
    image = crop_center_square(image)
    # Resize image to 1080x1080
    image = image.resize((1080, 1080))
    draw = ImageDraw.Draw(image)
    # Use Lato Light 300 font
    font = ImageFont.truetype('LatoTR-Light.ttf', size=40)
    # Get width and height of the image
    width, height = image.size
    # Measure the size of the text
    timestamp_size = draw.textsize(timestamp, font)
    location_size = draw.textsize(location, font)
    # Add timestamp and location to the bottom right corner
    draw.text((width - timestamp_size[0]-location_size[0]-30, height - 60), timestamp+", "+location, font=font, fill=(255, 255, 255))
    # Save image
    image.save(timestamp+"_"+location+'.jpg')

def crop_center_square(image):
    width, height = image.size
    size = min(width, height)
    left = (width - size) // 2
    top = (height - size) // 2
    right = (width + size) // 2
    bottom = (height + size) // 2
    image = image.crop((left, top, right, bottom))
    return image

add_timestamp_and_location()
