# -*- coding =utf-8 -*-
# @time : 2021/5/17 14:32
# @Author : Rov
# @File : zhengli.py
# @Software : PyCharm
from PIL import Image
import os
print('此程序把文件夹内所有图片转换为一个pdf文档（图片需按顺序命名）！')
path = r"./pic"
# imgList = os.listdir(path)
# imgList.sort(key=lambda x: int(x.split('.')[0]))
name = "电力系统分析笔记"
img_open_list = []                                 # 创建打开后的图片列表
for root, dirs, files in os.walk(path):
    for i in files:
        file = os.path.join(root, i)               # 遍历所有图片，带绝对路径
        img_open = Image.open(file)                # 打开所有图片
        if img_open.mode != 'RGB':
            img_open = img_open.convert('RGB')     # 转换图像模式
        img_open_list.append(img_open)             # 把打开的图片放入列表
pdf_name = name + '.pdf'                           # pdf文件名
img_1 = img_open_list[0]                           # 打开的第一张图片
# 把img1保存为PDF文件,将另外的图片添加进来，列表需删除第一张图片，不然会重复
img_open_list = img_open_list[1:]
img_1.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=img_open_list)
print('转换成功！pdf文件在当前程序目录下！')