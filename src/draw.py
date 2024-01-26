from PIL import Image
from constants import CLASSES, OVERCLOCKS

RESOLUTION = (2560, 1440)
ICON_SIZE_FRAME = 400
ICON_SIZE_MOD = 192
ICON_MOD_OFFSET = ICON_SIZE_FRAME // 2 - ICON_SIZE_MOD // 2


def add_gradient(image: Image.Image) -> Image.Image:
    if image.mode != 'RGBA':
        image = image.convert('RGBA')

    gradient_alpha = Image.linear_gradient('L').rotate(-90).resize(image.size)

    gamma = 2
    gradient_alpha = gradient_alpha.point(
        lambda f: int((f / 255.0)**(1/gamma)*255))

    gradient_image = Image.new('RGBA', image.size, (255, 255, 255, 0))
    gradient_image.putalpha(gradient_alpha)

    return Image.alpha_composite(image, gradient_image)


def add_class_icon(image: Image.Image, char_class: str):
    class_icon = Image.open('./assets/' + CLASSES[char_class])
    class_icon = class_icon.resize(
        (ICON_SIZE_FRAME, ICON_SIZE_FRAME), resample=Image.BOX)

    image.paste(class_icon, (1800, 500), class_icon)


def add_overclock_icons(image: Image.Image, oc1: str, oc2: str):
    # Overclock icons consist of 2 images - frame and mod. Combine them here

    oc1_frame = Image.open('./assets/' + OVERCLOCKS[oc1][0])
    oc1_frame = oc1_frame.resize((ICON_SIZE_FRAME, ICON_SIZE_FRAME),
                                 resample=Image.BOX)

    oc1_icon = Image.open('./assets/' + OVERCLOCKS[oc1][1])
    oc1_icon = oc1_icon.resize((ICON_SIZE_MOD, ICON_SIZE_MOD),
                               resample=Image.BOX)

    oc2_frame = Image.open('./assets/' + OVERCLOCKS[oc2][0])
    oc2_frame = oc2_frame.resize((ICON_SIZE_FRAME, ICON_SIZE_FRAME),
                                 resample=Image.BOX)

    oc2_icon = Image.open('./assets/' + OVERCLOCKS[oc2][1])
    oc2_icon = oc2_icon.resize((ICON_SIZE_MOD, ICON_SIZE_MOD),
                               resample=Image.BOX)

    image.paste(oc1_frame, (1550, 100), oc1_frame)
    image.paste(oc1_icon,
                (1550 + ICON_MOD_OFFSET, 100 + ICON_MOD_OFFSET), oc1_icon)
    image.paste(oc2_frame, (2050, 100), oc2_frame)
    image.paste(oc2_icon,
                (2050 + ICON_MOD_OFFSET, 100 + ICON_MOD_OFFSET), oc2_icon)
