from PIL import Image, ImageEnhance, ImageFilter
import os, sys


def open_image(path):
    im = Image.open(path)
    print(im.format, im.size, im.mode)
    return im


# 创建缩略图
def create_thumbnail(path, px=128):
    size = (px, px)
    try:
        with Image.open(path) as im:
            f, e = os.path.splitext(path)
            outfile = f + "_thumbnail" + ".jpg"
            im.thumbnail(size)
            im.save(outfile, "JPEG")
    except OSError:
        print("cannot create thumbnail for", path)


# 处理一系列图片
def create_thumbnails(lists, px=128):
    for infile in lists:
        create_thumbnail(infile, px)


# 图像平移
def roll(path, delta):
    """Roll an image sideways."""
    image = Image.open(path)
    xsize, ysize = image.size
    print(image.size)

    delta = delta % xsize
    print(delta)
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part1, (xsize - delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize - delta, ysize))

    return image


# 变成黑白
def change_color(path):
    with Image.open(path) as im:
        im = im.convert('L')
    return im


# 增加对比度
def enhance_contrast(path, delta=1.3):
    enh = ImageEnhance.Contrast(Image.open(path))
    enh.enhance(delta).show("30% more contrast")


# 图片大小调整
def image_resize(path, scale=1):
    im = Image.open(path)
    return im.resize((int(im.size[0] * scale), int(im.size[1] * scale)))


# 打包exe直接拖入cmd，获得文件列表
def get_list():
    aa = sys.argv[1:]
    print(aa)

# 滤镜
def pic_filter(path):
    with Image.open(path) as im:
        # 高斯模糊
        # im1 = im.filter(ImageFilter.GaussianBlur)
        # 普通模糊
        # im2 = im.filter(ImageFilter.BLUR)
        # 边缘增强
        # im2 = im.filter(ImageFilter.EDGE_ENHANCE)
        # 找到边缘
        im1 = im.filter(ImageFilter.FIND_EDGES)
        # 浮雕
        # im.filter(ImageFilter.EMBOSS)
        # 轮廓
        # im3 = im.filter(ImageFilter.CONTOUR)
        # 锐化
        # im.filter(ImageFilter.SHARPEN)
        # 平滑
        # im.filter(ImageFilter.SMOOTH)
        # 细节
        # im.filter(ImageFilter.DETAIL)
        # im1.show()
        aa = im.histogram()
        im1.show()
        print(aa)



if __name__ == '__main__':
    # src = 'C:/Users/sunzhongshan-pc/Desktop/image1.jpg'
    # lists = [src]
    # create_thumbnails(lists, 600)
    # pic_filetr(src)
    print('图片处理')