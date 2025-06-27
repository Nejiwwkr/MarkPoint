import re
from collections.abc import Callable
from io import BytesIO

import matplotlib
from PIL import Image
from pptx.slide import Slide
from pptx.util import Inches

matplotlib.use('Agg')
import matplotlib.pyplot as plt


def latex_to_png(latex_str):
    fig = plt.figure(figsize=(0.1, 0.1), facecolor='none')  # 设置figure背景为透明
    ax = plt.axes([0, 0, 1, 1], facecolor='none')  # 设置axes背景为透明
    ax.set_axis_off()  # 隐藏坐标轴

    # 添加LaTeX公式，颜色设置为黑色或其他你需要的颜色
    plt.text(0.5, 0.5, r'${}$'.format(latex_str),
             horizontalalignment='center',
             verticalalignment='center',
             fontsize=20,
             color='black',  # 可以根据需要调整颜色
             transform=ax.transAxes)

    # 保存为PNG文件，背景透明

    buf = BytesIO()
    plt.savefig(buf, dpi=300, bbox_inches='tight', pad_inches=0.1, transparent=True)
    plt.close()

    # 将BytesIO指针重置到开始位置，以便读取
    buf.seek(0)
    return buf

def add_formula(slide, formula, meta_data, top: float) -> (float, Callable[[None], None]):
    img_buffer = latex_to_png(formula)

    image = Image.open(img_buffer)
    # 获取图像的宽度和高度
    width, height = image.size

    # 定义放置图像的位置和大小
    formula_height: float = height/207 *0.6
    left = Inches((meta_data.w - (width / height) * formula_height) / 2)

    return formula_height, lambda: slide.shapes.add_picture(img_buffer, left, Inches(top), height=Inches(formula_height))


def merge_dollars_content(text):
    # 使用正则表达式匹配$$...$$之间的内容，并去除换行符
    pattern = r'\$\$(.*?)\$\$'
    # 使用lambda函数处理每个匹配到的内容
    merged_text = re.sub(pattern, lambda m: '$$' + m.group(1).replace('\n', '') + '$$', text, flags=re.DOTALL)
    return merged_text
