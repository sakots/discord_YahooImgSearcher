from dotenv import load_dotenv

import argparse
import json
import os
import urllib

import requests

from urllib import request as req
from urllib import error
from urllib import parse
import bs4
import pathlib

from mimetypes import guess_extension
from urllib.request import urlopen, Request
from urllib.parse import quote
from bs4 import BeautifulSoup
import discord

import sys
import re
import shutil
import random

# discord_YahooImgSearcher v0.1.0 by sakots

load_dotenv()

token = os.environ['ACCESS_TOKEN']

client = discord.Client()
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print('------')
    # 起動時に動作する処理
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

def _request(url):
    # requestを処理しHTMLとcontent-typeを返す
    req = Request(url)
    try:
        with urlopen(req, timeout=5) as p:
             b_content = p.read()
             mime = p.getheader('Content-Type')
    except:
        return None, None
    return b_content, mime

def _yahoo_img_search(word):
    # ディレクトリ作成
    if not os.path.exists('img'):
        os.mkdir('img')
    # yahoo!画像検索の結果から画像を返す
    url = 'https://search.yahoo.co.jp/image/search?p={}&fr=top_ga1_sa&ei=UTF-8&vd=y'.format(quote(word))
    response = requests.get(url)
    img_src_list = []
    pattern = 'original":{"url":"' + '(.*?)' + '"'
    tmp_extracted_text_array = re.findall(pattern, response.text)
    img_src_list.extend(tmp_extracted_text_array)
    # 画像ダウンロード
    imgnum = 0
    for imageURL in img_src_list:
        pal = '.jpg'
        if '.jpg' in imageURL:
            pal = '.jpg'
        elif '.JPG' in imageURL:
            pal = '.jpg'
        elif '.png' in imageURL:
            pal = '.png'
        elif '.gif' in imageURL:
            pal = '.gif'
        elif '.jpeg' in imageURL:
            pal = '.jpeg'
        else:
            pal = '.png'
        
        try:
            img = urllib.request.urlopen(imageURL)
            localfile = open('./img/' + str(imgnum)+pal, 'wb')
            localfile.write(img.read())
            img.close()
            localfile.close()
            imgnum += 1
        except UnicodeEncodeError:
            continue
        except error.HTTPError:
            continue
        except error.URLError:
            continue
        break

@client.event
async def on_message(message):
    # 「!i」で始まるか調べる
    if message.content.startswith("!i"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            command = message.content[len("!i"):].lower().strip()

            _yahoo_img_search(command)

            # ランダムに1枚選ぶ    
            random_file = random.choice(os.listdir("./img"))
            imgpath = "./img/" + random_file

            await message.channel.send(command)
            if os.path.isfile(imgpath) == False:
                await message.channel.send('＞＜')
            await message.channel.send(file=discord.File(imgpath))
            shutil.rmtree("img")

# Botの起動とDiscordサーバーへの接続
client.run(token)
