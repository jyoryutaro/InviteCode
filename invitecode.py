import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.binary_location = "/usr/bin/google-chrome"
chrome_service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

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

