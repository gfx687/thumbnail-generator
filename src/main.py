import sys
from PIL import Image, ImageFont, ImageDraw


font = ImageFont.truetype('./assets/SourceCodePro-Bold.ttf', size=200)
font2 = ImageFont.truetype('./assets/SourceCodePro-Bold.ttf', size=160)

RESOLUTION = (2560, 1440)
THUMBNAIL_RES = (1280, 720)
ICON_SIZE_FRAME = 400
ICON_SIZE_MOD = 192

CLASSES = {
    'engineer': 'engineer_icon.png',
    'gunner': 'gunner_icon.png',
    'scout': 'scout_icon.png',
    'driller': 'driller_icon.png'
}

OVERCLOCKS = {
    'pgl_compact_rounds': ('Frame_Overclock_Balanced.png', 'Icon_Upgrade_Ammo.png'),
    'stubby_em_refire_booster': ('Frame_Overclock_Balanced.png', 'Icon_Upgrade_FireRate.png'),
    'hurricane_pbm': ('Frame_Overclock_Balanced.png', 'Icon_Upgrade_BulletPenetration.png'),
    'coilgun_umc': ('Frame_Overclock_Clean.png', 'Icon_Upgrade_Duration_V2.png')
}

DIFFICULTIES = [
    'Hazard 6x2EX',
    'Hazard Lx2'
]

MISSION_TYPES = [
    'Mining',
    'Egg Hunt'
]


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
    mod_icon_offset = ICON_SIZE_FRAME // 2 - ICON_SIZE_MOD // 2

    oc1_frame = Image.open('./assets/' + OVERCLOCKS[oc1][0])
    oc1_frame = oc1_frame.resize((ICON_SIZE_FRAME, ICON_SIZE_FRAME),
                                 resample=Image.BOX)

    oc1_mod = Image.open('./assets/' + OVERCLOCKS[oc1][1])
    oc1_mod = oc1_mod.resize((ICON_SIZE_MOD, ICON_SIZE_MOD),
                             resample=Image.BOX)

    oc2_frame = Image.open('./assets/' + OVERCLOCKS[oc2][0])
    oc2_frame = oc2_frame.resize((ICON_SIZE_FRAME, ICON_SIZE_FRAME),
                                 resample=Image.BOX)

    oc2_mod = Image.open('./assets/' + OVERCLOCKS[oc2][1])
    oc2_mod = oc2_mod.resize((ICON_SIZE_MOD, ICON_SIZE_MOD),
                             resample=Image.BOX)

    image.paste(oc1_frame, (1550, 100), oc1_frame)
    image.paste(oc1_mod,
                (1550 + mod_icon_offset, 100 + mod_icon_offset), oc1_mod)
    image.paste(oc2_frame, (2050, 100), oc2_frame)
    image.paste(oc2_mod,
                (2050 + mod_icon_offset, 100 + mod_icon_offset), oc2_mod)


image = Image.open('./input/input.png')

if image.size != RESOLUTION:
    print('ERROR: image is of unexpected resolution: {0}. Expected (2560, 1440)'.format(
        image.size))
    sys.exit()

image = add_gradient(image)

image_draw = ImageDraw.Draw(image)

image_draw.text((50, 50), "[VWA]", fill=(0, 0, 0), font=font2)
image_draw.text((50, 600), DIFFICULTIES[0], fill=(0, 0, 0), font=font)
image_draw.text((50, 850), MISSION_TYPES[1], fill=(0, 0, 0), font=font)
image_draw.text((50, 1100), "True Solo", fill=(0, 0, 0), font=font)

add_class_icon(image, 'engineer')
add_overclock_icons(image, 'stubby_em_refire_booster', 'pgl_compact_rounds')

image = image.convert('RGB')
image.thumbnail(THUMBNAIL_RES)
image.save('./output/output.jpg', 'JPEG')
