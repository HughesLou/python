#!/usr/local/bin/python3

# -*-coding:utf-8-*-

# @Author: hugheslou
# @Time: 2018/9/16 13:09

"""
将一张图片填充为正方形后切为9张图
"""
from PIL import Image


# 将图片填充为正方形
def fill_image(image):
    width, height = image.size
    # 选取长和宽中较大值作为新图片的
    new_image_length = width if width > height else height
    # 生成新图片[白底]
    new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')
    # 将之前的图粘贴在新图上，居中
    if width > height:  # 原图宽大于高，则填充图片的竖直维度
        new_image.paste(image, (0, int((new_image_length - height) / 2)))  # (x,y)二元组表示粘贴上图相对下图的起始位置
    else:
        new_image.paste(image, (int((new_image_length - width) / 2), 0))
    return new_image


# 将图片调整为正方形
def crop_image(image):
    width, height = image.size
    # 选取长和宽中较小值作为新图片的
    new_length = min(width, height)
    # 生成新图片
    # new_image = Image.new(image.mode, (new_length, new_length))
    # 将之前的图粘贴在新图上，居中
    if width > height:  # 原图宽大于高，则填充图片的竖直维度
        return image.crop((int((width - new_length) / 2), 0, int((width + new_length) / 2), new_length))
        # new_image.paste(image, (0, int((new_length - height) / 2)))  # (x,y)二元组表示粘贴上图相对下图的起始位置
    else:
        return image.crop((0, int((height - new_length) / 2), new_length, int((height + new_length) / 2)))
        # new_image.paste(image, (int((new_length - width) / 2), 0))
    # return new_image


# 切图
def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0, 3):
        for j in range(0, 3):
            # print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)

    return [image.crop(box) for box in box_list]


# 保存
def save_images(image_list):
    index = 1
    for image in image_list:
        image.save('../result/p' + str(index) + '.png', 'PNG')
        index += 1


if __name__ == '__main__':
    file_path = "pp.jpg"
    image = Image.open(file_path)
    # image.show()
    # image = fill_image(image)
    image = crop_image(image)
    image_list = cut_image(image)
    save_images(image_list)
