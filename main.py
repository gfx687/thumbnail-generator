# Notes and questions:
# 1) convert input into thumbnail format? JPG?
# 2) validate image size so text is placed correctly

from PIL import Image, ImageFont, ImageDraw


font = ImageFont.truetype(
    '/usr/share/fonts/truetype/firacode/FiraCode-SemiBold.ttf', size=200)


def print_image_info_by_path(path: str) -> None:
    """Print basic info about provided image"""
    image = Image.open(path)
    print(image.format, image.size, image.mode)


def add_gradient(image: Image.Image) -> Image.Image:
    """Creates copy of provided image and returns it with added white gradient"""
    if image.mode != 'RGBA':
        image = image.convert('RGBA')

    gradient_alpha = Image.linear_gradient('L').rotate(-90).resize(image.size)
    # gradient_alpha.save('./output/DEBUG-alpha.png')

    gradient_image = Image.new('RGBA', image.size, (255, 255, 255, 0))
    gradient_image.putalpha(gradient_alpha)
    # gradient_image.save('./output/DEBUG-gradient.png')

    return Image.alpha_composite(image, gradient_image)


image = Image.open('./input/input.png')
image = add_gradient(image)

image_draw = ImageDraw.Draw(image)

image_draw.text((image.size[0] - 600, 20), "test", fill=(255, 0, 0), font=font)

image.save('./output/output.png')
