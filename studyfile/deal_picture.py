from PIL import Image, ImageEnhance, ImageFilter
import os, sys
import json


def open_image(path):
    im = Image.open(path)
    print(im.format, im.size, im.mode)
    return im


# 创建缩略图
def create_thumbnail(path, outpath='', px=128):
    size = (px, px)
    file_name, file_suffix = os.path.splitext(os.path.basename(path))
    outfile = outpath + '/' + file_name + "_thumbnail" + ".jpg"
    try:
        with Image.open(path) as im:
            im.thumbnail(size)
            im = im.convert("RGB") # JPG压缩,尺寸更小
            im.save(outfile, "JPEG")
            return outfile
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


###################################################################################################

# 获得路径下所有文件及路径
def get_all_file(filepath):
    lists = []
    for root, dirs, files in os.walk(filepath, topdown=False):
        for name in files:
            lists.append(root + '/' + name)
        # for name in dirs:
        #     print(os.path.join(root, name))
    # print(f'####{lists}')
    return lists


# 1、将当下路径中origin文件夹下所有文件复制到 origin_thumbnail
# 2、同时将源文件路径和新文件路径添加到dict写入list,保存到data.txt文件
def from_raw_to_thumbnail(outputfilename='origin_thumbnail', thumbnail_px=2000):
    datum = []
    basepath = os.path.split(sys.argv[0])[0] + '/'
    origin_path = os.path.join(basepath, 'origin/')
    if not os.path.isdir(origin_path):
        os.mkdir(origin_path)
    print('当前路径:' + basepath)
    file_lists = get_all_file(origin_path)  # 获得路径下所有文件
    count_file_lists = len(file_lists)
    # 如果列表不为空
    if count_file_lists:
        # 判断是否有导出文件夹目录
        outpath = os.path.join(basepath, outputfilename)
        if not os.path.isdir(outpath):
            os.mkdir(outpath)
        for inpath in file_lists:
            outfilename = create_thumbnail(inpath, outpath, thumbnail_px)
            datum.append((inpath, outfilename))
        print(f"照片已压缩,共 {count_file_lists} 张")
        File_W_R(basepath).write_file(str(init_pic_lists(datum)))
    else:
        print("请将照片复制到origin文件夹下,再重新运行软件")
        os.startfile(origin_path)


# 文件读写
class File_W_R:
    def __init__(self, base_path, filename='data.txt', ):
        self.base_path = base_path
        self.filename = filename
        self.file_path = self.base_path + self.filename
        self.encoding = 'gbk'
        self.creat_empty_file()

    def show_path(self):
        print(self.base_path)

    def creat_empty_file(self):
        if not os.path.isfile(self.file_path):
            print('Create New')
            self.write_file('')
        else:
            self.read_file()

    def read_file(self):
        with open(self.file_path, 'r', encoding=self.encoding) as f:
            self.data = f.read()
            # return data

    def write_file(self, data):
        self.data = data
        with open(self.file_path, 'w', encoding=self.encoding) as f:
            f.write(str(self.data))
            print(f'已写入 {self.filename}')

    def show_data(self):
        print(self.data)


# 初始化图片列表，添加原始路径，添加压缩图片路径
def init_pic_lists(datum):
    pic_lists = []

    def add_item(origin_path, thumbnail_path):
        pic_item = {
            'origin_path': origin_path,
            'thumbnail_path': thumbnail_path,
            'sort_tags': '',
            'update_time': '',
            'useless': False
        }
        return pic_item

    for origin_path, thumbnail_path in datum:
        pic_lists.append(add_item(origin_path=origin_path, thumbnail_path=thumbnail_path))
    # print(f'数量：{len(pic_lists)}')
    # print(pic_lists)
    print(f'已创建 {len(pic_lists)} 条记录')
    return pic_lists


if __name__ == '__main__':
    from_raw_to_thumbnail()
    # TODO 所有照片都会被重新压缩，暂时不做处理，不能保证不会用同名同大小的文件被替换,或者读取exif数据，再讨论
    input('')
