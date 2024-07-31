from PIL import Image, ImageEnhance


def img_change_ch(img, n=0, n1=0, n2=0):
    """图片反色滤镜"""
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = 255 - img_array[x, y][0]
            g = 255 - img_array[x, y][1]
            b = 255 - img_array[x, y][2]
            img_array[x, y] = r, g, b
    return img

def img_change_co(img, contrast_ratio, n1=0, n2=0):
    """增强对比度滤镜"""
    contrast_ratio = int(contrast_ratio)
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            if r == max(r, g, b):
                if r >= 255-contrast_ratio:
                    r = 255
                else:
                    r += contrast_ratio
            elif g == max(r, g, b):
                if g >= 255-contrast_ratio:
                    g = 255
                else:
                    g += contrast_ratio
            else:
                if b >= 255-contrast_ratio:
                    b = 255
                else:
                    b += contrast_ratio
            img_array[x, y] = (r, g, b)
    return img

def img_change_bw(img, n=0, n1=0, n2=0):
    """图片黑白滤镜"""
    img.format = "GIF"
    img = img.convert("L")
    return img

def img_change_bright(img, n=0, bright=1, n2=0):
    img = ImageEnhance.Brightness(img)
    img = img.enhance(int(bright))
    return img

def img_change_sharp(img, n=0, n1=0, sharp=1):
    img = ImageEnhance.Sharpness(img).enhance(int(sharp))
    return img