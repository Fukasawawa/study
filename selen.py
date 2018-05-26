# coding: UTF-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import rm_emoji
import format
import sys
import numpy as np

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

'''
import sys
#import selenium

sys.path.append('C:/Users/user/Anaconda3/lib/site-packages/selenium/')
#print(selenium.__file__)
'''
def tweet_get(location):
    # ブラウザのオプションを格納する変数をもらってきます。
    options = Options()

    # Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
    options.set_headless(True)

    # ブラウザを起動する
    driver = webdriver.Chrome(chrome_options=options)

    # ブラウザでアクセスする
    driver.get("http://chizutwi.jp/twitter/")

    #位置情報入力
    driver.find_element_by_id('place').send_keys(location)

    #位置情報変更
    driver.find_element_by_id('move').click()

    #位置が変わるまで待つ
    driver.implicitly_wait(60)
    driver.set_script_timeout(60)
    WebDriverWait(driver, 30).until(lambda driver: driver.execute_script("return jQuery.active == 0"))

    #ツイートを格納する配列
    work = 'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ'
    tweet = [[work, 'ああ', 'う', 'え']]
    for i in range(4):
        if(i == 0):
            km = 0.1
        elif(i == 1):
            km = 0.5
        elif(i == 2):
            km = 1
        else:
            km = 5
        Select(driver.find_element_by_id('km')).select_by_value(str(km))
        driver.implicitly_wait(60)

        #検索ボタンをクリック
        driver.find_element_by_id('search').click()

        #結果が返ってくるまで待つ
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'text')))
        #driver.implicitly_wait(10)

        # HTMLを文字コードをUTF-8に変換してから取得
        html = driver.page_source.encode('utf-8')

        # BeautifulSoupで扱えるようにパース
        soup = BeautifulSoup(html, "html.parser")

        #htmlからタグ抽出
        text = soup.select('.text')
        timestamp = soup.select('.timestamp')


        #配列にデータ追加
        for j in range(len(text)):
            #テキスト
            add = [format.format_text(rm_emoji.remove_emoji(text[j].get_text().translate(non_bmp_map)))]
            #距離代入
            add.append(soup.select('option')[i].get_text())
            #時間代入
            time = timestamp[j].select('span')[0].get_text()

            #月を抽出
            month = int(time.split('年')[1].split('月')[0])
            if((month >= 12) or (month <= 2)):
                season = '冬'
            elif(month >= 9):
                season = '秋'
            elif(month >= 6):
                season = '夏'
            else:
                season = '春'
            #季節設定
            add.append(season)

            #時間を抽出
            hour = int(time.split(' ')[1].split(':')[0])
            if((hour >= 18) or (hour <= 3)):
                tzone = '夜'
            elif(hour >= 12):
                tzone = '昼'
            else:
                tzone = '朝'

            #時間帯設定
            add.append(tzone)
            #print(add[0])

            #同じデータがなければデータ追加
            #if((i == 0) and (j == 0)):
            #    tweet = [add]
            if(np.any(tweet==add[0])== False):
                #print(tweet)
                tweet = np.insert(tweet, 1, add, axis=0)


    #ドライバー切断
    driver.quit()
    tweet = np.delete(tweet, 0, 0)

    return tweet

'''
t = tweet_get("盛岡駅")
print(t)
'''
