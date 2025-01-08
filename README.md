# CTF-1-8-2025

## Description

This project is a simple **Steganography challenge** where we use the **Least Significant Bit (LSB)** technique to hide a flag in an image. The flag is encoded using a key and then embedded into an image. The image can then be shared, and participants can attempt to extract the hidden flag using the correct key. The solution involves working with image manipulation, binary data extraction, and the decoding process.

## Files

- `ctf.py`: This file contains the functions to generate an image, hide the flag in the image, and save it with metadata.
- `solve.py`: This file contains the function to extract the hidden flag from the image, given the correct key.

## Installation

Make sure you have Python 3 installed, along with the necessary libraries.

### Requirements

- numpy
- Pillow (PIL)

You can install the required libraries by running:

```
pip install numpy Pillow
```

## How to Run

### Step 1: Create and Hide the Flag in the Image (`ctf.py`)

In the `ctf.py` file, we generate an image with some text and embed the flag in it using the `hide` function.

1. Set the name, left_text, right_text, flag, and key as follows:

```python
name = 'GGH CTF'
left_text = 'Join @GGHAccepts_Bot'
right_text = 'By @superhexa'
flag = 'CTF{GGH_YOU_ARE_THE_CHAMPION}'
key = '8cp9wNaD'
```

2. Use the `generate_img` function to create the image:

```python
generate_img(name, left_text, right_text)
```

3. Then, call the `hide` function to embed the flag into the image:

```python
hide('img.png', flag, key)
```

This will create an image file named `ctf.png` with the flag embedded in it.

### Step 2: Extract the Flag from the Image (`solve.py`)

Once the image is created, you can use `solve.py` to extract the hidden flag.

1. Set the key in `solve.py`:

```python
key = '8cp9wNaD'
```

2. Call the `extract` function with the image file (`ctf.png`) and the key:

```python
print(extract('ctf.png', key))
```

This will print the hidden flag if the correct key is provided.

## Community

For discussions, challenges, and support, join our community: [@GGHAccepts_Bot](https://t.me/GGHAccepts_Bot).

## Contributing

Feel free to fork and contribute to the project. If you have any issues or suggestions, open an issue or pull request.

Happy Hacking! 👨‍💻👾
