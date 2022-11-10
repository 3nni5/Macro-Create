# Macro-Create
Splatoonの自動ドット打ちをNX Macro Controller ver.2で行うために、320×120のモノクロ画像からNX Macro Controller用の実行コードを生成するPythonのプログラムです。


2022/11/11
多くの方に見ていただきご連絡もいただいております．
そのため，個人的におすすめの実行手順を紹介します．

#### 動作環境
OS: Windows 10 Home
Python version: Python 3.6.7
CLI操作: PowerShell7

#### 手順
GUI操作：
githubからダウンロードしたフォルダに画像(picture.bmp)を移動させる．

CLI操作：
githubからダウンロードしたフォルダに移動
cd .\Downloads\Macro-Create-main\
仮想環境を構築
python -m venv venv
仮想環境のアクティベート
.\venv\Scripts\activate
pipのアプデ
python -m pip install --upgrade pip
必要なライブラリのインストール
pip install -r requirements.txt
プログラムを実行
python main.py

GUI操作：
macro.txtを確認


#### 画像について
画像はモノクロビットマップのものをご用意ください．
