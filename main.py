from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import command
from selenium.webdriver.support.ui import WebDriverWait  # added
from selenium.webdriver.support import expected_conditions as EC  # added
import time

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1,
    "profile.default_content_settings.geolocation": 1,
    "profile.default_content_settings.popups": 1
})
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1920, 1080")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')


client = webdriver.Chrome(options=chrome_options)

params = {
    "latitude": 35.66167,
    "longitude": 139.66683,
    "accuracy": 100
}
# client.execute_cdp_cmd("Page.setGeolocationOverride", params)
# client.get('https://www.infobyip.com/browsergeolocation.php')
client.execute_cdp_cmd("Emulation.setGeolocationOverride", params)
# client.get('https://browserleaks.com/geo')
client.get("https://google.com/search?q=1")
# width = client.execute_script("return document.documentElement.scrollWidth")
# height = client.execute_script("return document.documentElement.scrollHeight")
# client.set_window_size(width, height)
# print(width, height)
element = WebDriverWait(client, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "update-location")))  # added
element.click()  # added
time.sleep(4)
# client.find_element(By.TAG_NAME, 'update-location').click()
# client.find_element(By.ID, 'geo_update_button').click()

# 截图并关掉浏览器
client.save_screenshot("sc.png")
client.quit()
