import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Webドライバーの設定
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://altema.jp/dotyusya/syoutaicode#commentstart')

element_to_click = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'dummy'))
)
element_to_click.click()

input_field = driver.find_element(By.NAME, 'comment_content_add1')
input_field.send_keys('2d79884b6845')

submit_button = driver.find_element(By.NAME, 'comment_submit')
#submit_button.click()
driver.execute_script("arguments[0].click();", submit_button)

# ブラウザを閉じる
driver.close()

