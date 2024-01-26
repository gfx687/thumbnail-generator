import sys
from PIL import Image, ImageFont, ImageDraw
from constants import DIFFICULTIES, MISSION_TYPES
from draw import RESOLUTION, add_class_icon, add_overclock_icons, add_gradient

THUMBNAIL_RES = (1280, 720)
font = ImageFont.truetype('./assets/SourceCodePro-Bold.ttf', size=200)
font_small = ImageFont.truetype(
    './assets/SourceCodePro-Bold.ttf', size=160)
font_color = (0, 0, 0)

# check that OC's icon is configured in src/constants.py
inputs = {
    'class': 'engineer',
    'oc1': 'stubby_em_refire_booster',
    'oc2': 'pgl_compact_rounds',
    'mission_type': MISSION_TYPES[1],
    'difficulty': DIFFICULTIES[1],
    'is_vwa': True
}

if __name__ == '__main__':
    image = Image.open('./input/input.png')

    if image.size != RESOLUTION:
        print(f'ERROR: image is of unexpected resolution: {
              image.size}. Expected (2560, 1440)')
        sys.exit()

    image = add_gradient(image)

    image_draw = ImageDraw.Draw(image)

    image_draw.text((50, 600), inputs['difficulty'],
                    fill=font_color, font=font)
    image_draw.text((50, 850), inputs['mission_type'],
                    fill=font_color, font=font)
    image_draw.text((50, 1100), "True Solo", fill=font_color, font=font)

    if inputs['is_vwa']:
        image_draw.text((50, 50), "[VWA]", fill=font_color, font=font_small)

    add_class_icon(image, inputs['class'])
    add_overclock_icons(image, inputs['oc1'], inputs['oc2'])

    image = image.convert('RGB')
    image.thumbnail(THUMBNAIL_RES)
    image.save('./output/output.jpg', 'JPEG')
