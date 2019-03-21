from PIL import Image, ImageDraw, ImageFont


def insert_image(img_path: str, background_path: str, output_path: str,
                 pos: (int, int) = None):
    """
    Insert image
    """
    img = Image.open(img_path, 'r')
    img_w, img_h = img.size
    background = Image.open(background_path, 'r')
    bg_w, bg_h = background.size
    if pos is None:
        pos = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img, pos)
    background.save(output_path)


def insert_text(img_path: str, label: str, output_path: str,
                font_path: str = None, pos: (int, int) = None):
    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    if font_path is not None:
        font = ImageFont.truetype(font_path, 16)
    else:
        font = None
    draw.text(pos, label, (255, 255, 255), font)
    img.save(output_path)


def ok(img_path):
    insert_image(img_path=img_path,
                 background_path='backgrounds/ok.png',
                 output_path='out.jpg')


ok('1.jpg')
