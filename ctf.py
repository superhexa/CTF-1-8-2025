import numpy as np
from PIL import Image, ImageDraw, ImageFont
from PIL.PngImagePlugin import PngInfo
import random

def encode(msg, key):
    key = (key * (len(msg) // len(key) + 1))[:len(msg)]
    return ''.join(chr(((ord(m) - (65 if m.isupper() else 97) + (ord(k) - (65 if k.isupper() else 97))) % 26) + (65 if m.isupper() else 97)) if m.isalpha() else m for m, k in zip(msg, key))

def hide(img_path, flag, key):
    img = np.array(Image.open(img_path), dtype=np.uint8)
    flag = encode(flag, key)
    flag_bin = ''.join(format(ord(c), '08b') for c in flag)
    idx = 0
    for i in range(0, img.shape[0], 2):
        for j in range(0, img.shape[1], 2):
            block = img[i:i+2, j:j+2]
            if idx < len(flag_bin):
                bit = int(flag_bin[idx])
                block[0, 0, 0] = (block[0, 0, 0] & ~1) | bit
                idx += 1
            if random.random() < 0.10:
                for _ in range(random.randint(1, 6)):
                    noise = random.randint(0, 255)
                    x, y = random.randint(0, 1), random.randint(0, 1)
                    channel = random.randint(0, 2)
                    block[x, y, channel] = (block[x, y, channel] + noise) % 256
            img[i:i+2, j:j+2] = block
    img = np.clip(img, 0, 255).astype(np.uint8)
    pil_img = Image.fromarray(img)
    metadata = PngInfo()
    metadata.add_text("key", key)
    pil_img.save('ctf.png', pnginfo=metadata)

def generate_img(text, bottom_left, bottom_right):
    img = Image.new('RGB', (800, 600), color=(30, 50, 90))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 100)
    except IOError:
        font = ImageFont.load_default()
    big_font = font
    text_bbox = draw.textbbox((0, 0), text, font=big_font)
    position = ((img.width - (text_bbox[2] - text_bbox[0])) // 2, (img.height - (text_bbox[3] - text_bbox[1])) // 2)
    shadow_offset = (10, 10)
    draw.text((position[0] + shadow_offset[0], position[1] + shadow_offset[1]), text, font=big_font, fill=(0, 0, 0))
    gradient_color = (255, 165, 0)
    draw.text((position[0], position[1]), text, font=big_font, fill=gradient_color, stroke_width=4, stroke_fill=(255, 165, 0))
    dark_shade = (180, 140, 50)
    draw.text((position[0] - 4, position[1] - 4), text, font=big_font, fill=dark_shade, stroke_width=4, stroke_fill=(255, 215, 85))
    small_font = ImageFont.load_default()
    left_bbox = draw.textbbox((0, 0), bottom_left, font=small_font)
    left_position = (20, img.height - (left_bbox[3] - left_bbox[1]) - 20)
    draw.text((left_position[0] + 1, left_position[1]), bottom_left, font=small_font, fill=(255, 215, 85))
    draw.text(left_position, bottom_left, font=small_font, fill=(255, 215, 85))
    right_bbox = draw.textbbox((0, 0), bottom_right, font=small_font)
    right_position = (img.width - (right_bbox[2] - right_bbox[0]) - 20, img.height - (right_bbox[3] - right_bbox[1]) - 20)
    draw.text((right_position[0] + 1, right_position[1]), bottom_right, font=small_font, fill=(255, 215, 85))
    draw.text(right_position, bottom_right, font=small_font, fill=(255, 215, 85))
    img.save('img.png')

name = 'GGH CTF'
left_text = 'Join @GGHAccepts_Bot'
right_text = 'By @superhexa'
flag = 'CTF{GGH_YOU_ARE_THE_CHAMPION}'
key = '8cp9wNaD'
generate_img(name, left_text, right_text)
hide('img.png', flag, key)

