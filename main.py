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
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')


client = webdriver.Chrome(options=chrome_options)

params = {
    "latitude": 35.66167,
    "longitude": 139.66683,
    "accuracy": 100
}
# client.execute_cdp_cmd("Page.setGeolocationOverride", params)
# client.get("https://google.com/search?q=1")
# client.get('https://www.google.com/maps')
# client.get('https://www.infobyip.com/browsergeolocation.php')
client.execute_cdp_cmd("Emulation.setGeolocationOverride", params)
# client.get("https://maps.google.com")
client.get('https://browserleaks.com/geo')

width = client.execute_script("return document.documentElement.scrollWidth")
height = client.execute_script("return document.documentElement.scrollHeight")
client.set_window_size(width, height)
print(width, height)
# time.sleep(3)

element = WebDriverWait(client, 10).until(
    EC.presence_of_element_located((By.ID, "geo_update_button")))  # added
element.click()  # added


# client.find_element(By.TAG_NAME, 'update-location').click()
# client.find_element(By.ID, 'geo_update_button').click()

# 截图并关掉浏览器
client.save_screenshot("sc.png")
client.quit()
