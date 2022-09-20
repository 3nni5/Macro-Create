from PIL import Image
import numpy as np

def create(pic):
    # 画像の読み込み
    img = Image.open(pic)
    # 画像の幅と高さを取得
    width, height = img.size
    # 画像情報の配列化
    img_pixels = np.array([[img.getpixel((i,j)) for j in range(height)] for i in range(width)])
    # マクロ生成
    macro = ''
    for i in range(width):
        # 縦一列のドット打ち
        for j in range(height):
            if all(img_pixels[i][j] == [0, 0, 0]):
                # black
                macro += 'Press(A, 0.10)\nPress(DOWN, 0.10)\n'
            else:
                # white
                macro += 'Wait(0.10)\nPress(DOWN, 0.10)\n'
        # 次の列に移動
        macro += 'Wait(0.10)\nPress(RIGHT, 0.10)\nPress(UP_L, 3)\nWait(0.10)\n'
    # txt出力
    f = open('macro.txt', 'w')
    f.write(macro)
    f.close()


if __name__ == '__main__':
    # 320×120のモノクロ(2値)画像をcreateに渡す
    create('picture.bmp')