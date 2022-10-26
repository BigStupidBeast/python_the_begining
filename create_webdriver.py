# selenium 4
from selenium import webdriver



from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

ChromeDriverManager(path = r".").install()
my_bro_chr = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
my_bro_chr.quit()

my_bro_chr = webdriver.Chrome(".\\.wdm\\drivers\\chromedriver\\win32\\106.0.5249\\chromedriver.exe")
my_bro_chr.get('https://google.com/')

# def check_my_bro():
#     my_bro_chr = webdriver.Chrome()
#     my_bro_chr.get('https://google.com/')
#
#
# check_my_bro()

def create_firefox():
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from webdriver_manager.firefox import GeckoDriverManager

    driverFf = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    GeckoDriverManager(path = r".\\Drivers").install()
    driverFf.quit()


def create_brave ():

    from selenium.webdriver.chrome.service import Service as BraveService
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.core.utils import ChromeType

    ChromeDriverManager(path = r".\\Drivers").install()
    driverBr = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
    driverBr.get('https://google.com/')

#