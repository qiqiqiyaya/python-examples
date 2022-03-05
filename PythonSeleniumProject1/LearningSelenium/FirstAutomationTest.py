from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import winreg

def get_chrome_version():
    """Reads current Chrome version from registry."""
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Google\Chrome\BLBeacon')
    version, _ = winreg.QueryValueEx(reg_key, 'version')
    winreg.CloseKey(reg_key)
    print(version)
    return version

driver = webdriver.Chrome(service=Service(ChromeDriverManager(version=get_chrome_version()).install()))
driver.get("http://www.baidu.com")
print(driver.title)
driver.close()
