# selenium 4
from selenium import webdriver

''''''
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

ChromeDriverManager(path = r".\\Drivers").install()
driverCr = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driverCr.quit()

''''''
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driverFf = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
GeckoDriverManager(path = r".\\Drivers").install()
driverFf.quit()

''''''
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

ChromeDriverManager(path = r".\\Drivers").install()
driverBr = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
driverBr.get('https://google.com/')
driverBr.quit()