# Macro-Create
Splatoonの自動ドット打ちをNX Macro Controller ver.2で行うために，320×120のモノクロ画像からNX Macro Controller用の実行コードを生成するPythonのプログラムです．


## 2022/11/11
多くの方に見ていただきご連絡もいただいております．  
そこで，個人的におすすめの実行手順を紹介します．  

### 動作環境
OS: Windows 10 Home  
Python version: Python 3.6.7  
CLI操作: PowerShell7  

### 手順
GUI操作：  
githubからダウンロードしたフォルダに画像(picture.bmp)を移動させる．  
  
CLI操作：  
githubからダウンロードしたフォルダに移動  
```bash
cd .\Downloads\Macro-Create-main\
```
仮想環境を構築  
```bash
python -m venv venv
```
仮想環境のアクティベート  
```bash
.\venv\Scripts\activate  
```
pipのアプデ  
```bash
python -m pip install --upgrade pip  
```
必要なライブラリのインストール  
```bash
pip install -r requirements.txt  
```
プログラムを実行  
```bash
python main.py  
```
  
GUI操作：  
macro.txtを確認  


### 画像について
画像はモノクロビットマップのものをご用意ください．  


### 詳しい使用方法はこちら
あるごすにっき様より「【スプラトゥーン3】NX Macro controller Ver2.07 でイラスト自動ドット打ちをする」  
URL: http://blog.livedoor.jp/swanday/archives/89068767.html
