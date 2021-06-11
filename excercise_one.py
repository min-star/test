# -*- coding: utf-8 -*-
from PIL import Image
import matplotlib.pyplot as plt
import json
# 1.将json文件里面的name为'box_b'的'rectangle'字段打印出来

def print_rectangle(path):
    #path = './boxes.json'
    data = json.load(open(path))
    for dict_ele in data['boxes']:
        if dict_ele['name'] == 'box_b':
            #打印‘box_b’的'rectangle'字段
            print(dict_ele['rectangle'])
            return dict_ele['rectangle']['left_top'], dict_ele['rectangle']['right_bottom']

# 2.写一个小工具，可以将任意一张图像填充到另一张图像的box_b所指定的区域中。
def fill_image(path1, path2, left_up, right_bottom):
    im = Image.open(path1)
    im1 = Image.open(path2)
    width = right_bottom[0] - left_up[0]
    height = right_bottom[1] - left_up[1]
    new_size = (width, height)
    im = im.resize(new_size)
    im1.paste(im, (left_up[0], left_up[1], right_bottom[0], right_bottom[1]))
    plt.imshow(im1)
    plt.show()
if __name__ == '__main__':
    left_up, right_bottom = print_rectangle('./boxes.json')
    path1 = './base.jpg'
    path2 = './baseone.jpg'
    fill_image(path1, path2, left_up, right_bottom)