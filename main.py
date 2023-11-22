# Notes and questions:
# 1) convert input into thumbnail format? JPG?
# 2) magic numbers

import sys
from PIL import Image, ImageFont, ImageDraw


font = ImageFont.truetype('./assets/SourceCodePro-Bold.ttf', size=200)
font2 = ImageFont.truetype('./assets/SourceCodePro-Bold.ttf', size=160)


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


def add_class_icon(image: Image.Image):
    class_icon = Image.open('./assets/engineer_icon.png')
    class_icon = class_icon.resize((400, 400), resample=Image.BOX)

    image.paste(class_icon, (1800, 500), class_icon)


# frame = 100x100, mod = 48x48
def add_overclock_icons(image: Image.Image):
    oc1_frame = Image.open('./assets/Frame_Overclock_Balanced.png')
    oc1_frame = oc1_frame.resize((400, 400), resample=Image.BOX)
    image.paste(oc1_frame, (1550, 100), oc1_frame)

    oc1_mod = Image.open('./assets/Icon_Upgrade_FireRate.png')
    oc1_mod = oc1_mod.resize((192, 192), resample=Image.BOX)
    image.paste(oc1_mod, (1550 + 400 // 2 - 96, 100 + 400 // 2 - 96), oc1_mod)

    oc1_frame = Image.open('./assets/Frame_Overclock_Balanced.png')
    oc1_frame = oc1_frame.resize((400, 400), resample=Image.BOX)
    image.paste(oc1_frame, (2050, 100), oc1_frame)

    oc1_mod = Image.open('./assets/Icon_Upgrade_Ammo.png')
    oc1_mod = oc1_mod.resize((192, 192), resample=Image.BOX)
    image.paste(oc1_mod, (2050 + 400 // 2 - 96, 100 + 400 // 2 - 96), oc1_mod)



image = Image.open('./input/input.png')

if image.size != (2560, 1440):
    print('ERROR: image is of unexpected resolution: {0}. Expected (2560, 1440)'.format(
        image.size))
    sys.exit()

image = add_gradient(image)

image_draw = ImageDraw.Draw(image)

image_draw.text((50, 50), "[VWA]", fill=(0, 0, 0), font=font2)
image_draw.text((50, 600), "Hazard 6x2EX", fill=(0, 0, 0), font=font)
image_draw.text((50, 850), "Egg Hunt", fill=(0, 0, 0), font=font)
image_draw.text((50, 1100), "True Solo", fill=(0, 0, 0), font=font)

add_class_icon(image)
add_overclock_icons(image)

thumbnail_size = (1280, 720)
image = image.convert('RGB')
image.thumbnail(thumbnail_size)
# image.save('./output/output.png')
image.save('./output/output.jpg', 'JPEG')
