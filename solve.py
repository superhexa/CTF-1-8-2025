import numpy as np
from PIL import Image

def decode(msg, key):
    key = (key * (len(msg) // len(key) + 1))[:len(msg)]
    return ''.join(chr(((ord(m) - (65 if m.isupper() else 97) - (ord(k) - (65 if k.isupper() else 97)) + 26) % 26) + (65 if m.isupper() else 97)) if m.isalpha() else m for m, k in zip(msg, key))

def extract(img_path, key):
    img = np.array(Image.open(img_path))
    flag_bin = ''
    for i in range(0, img.shape[0], 2):
        for j in range(0, img.shape[1], 2):
            block = img[i:i+2, j:j+2]
            lsb = block[0, 0, 0] & 1
            flag_bin += str(lsb)
    flag = ''.join(chr(int(flag_bin[i:i+8], 2)) for i in range(0, len(flag_bin), 8))
    return decode(flag, key)

key = '8cp9wNaD'
print(extract('ctf.png', key))
