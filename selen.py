# coding: UTF-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import rm_emoji
import format
import sys

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

    #検索ボタンをクリック
    driver.find_element_by_id('search').click()

    #結果が返ってくるまで待つ
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'text')))
    #driver.implicitly_wait(10)

    # HTMLを文字コードをUTF-8に変換してから取得
    html = driver.page_source.encode('utf-8')

    #ドライバー切断
    driver.quit()

    # BeautifulSoupで扱えるようにパース
    soup = BeautifulSoup(html, "html.parser")

    #id=textを取り出し
    for t in soup.select('.text'):
        #絵文字やツイート特有の文字列を削除
        #yield format.format_text(rm_emoji.remove_emoji(t.get_text().translate(non_bmp_map)))
        yield rm_emoji.remove_emoji(t.get_text().translate(non_bmp_map))

'''
data = tweet_get("盛岡駅")
for i in data:
    print(i)
'''

