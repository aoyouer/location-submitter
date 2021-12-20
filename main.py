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
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
client = webdriver.Chrome(options=chrome_options)
# fake geo location
params = {
    "latitude": 35.66167,
    "longitude": 139.66683,
    "accuracy": 100
}
# client.execute_cdp_cmd("Page.setGeolocationOverride", params)
client.execute_cdp_cmd("Emulation.setGeolocationOverride", params)
# 无头模式需要下面的命令才有权限获取位置信息
client.execute_cdp_cmd(
    "Browser.grantPermissions",
    {
        "origin": "https://www.google.com/",
        "permissions": ["geolocation"]
    },
)
# client.get('https://browserleaks.com/geo')
client.get("https://google.com/search?q=1")
# 截图相关
width = client.execute_script("return document.documentElement.scrollWidth")
height = client.execute_script("return document.documentElement.scrollHeight")
client.set_window_size(width, height)
element = WebDriverWait(client, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "update-location")))  # added
element.click()  # added
print('更新位置')
time.sleep(4)
# 截图并关掉浏览器
client.save_screenshot("sc.png")
client.quit()
