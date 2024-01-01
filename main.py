import pytesseract
import fitz
import json
import os
from PIL import Image

if __name__ == '__main__':
    path = "./img/"
    files = os.listdir(path)
    for file in files:
        filename = os.path.join(path, file)
        if file.endswith("pdf"):
            continue

        # 打开图片文件
        image = Image.open(filename)

        # 使用Tesseract进行文字识别
        text = pytesseract.image_to_string(image,lang="chi_sim")

        # 输出识别结果
        print(f"======={file} 识别结果输出如下：======")
        print(text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
