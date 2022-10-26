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
#
# def create_firefox():
#     from selenium.webdriver.firefox.service import Service as FirefoxService
#     from webdriver_manager.firefox import GeckoDriverManager
#
#     driverFf = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     GeckoDriverManager(path = r".\\Drivers").install()
#     driverFf.quit()
#
#
# def create_brave ():
#
#     from selenium.webdriver.chrome.service import Service as BraveService
#     from webdriver_manager.chrome import ChromeDriverManager
#     from webdriver_manager.core.utils import ChromeType
#
#     ChromeDriverManager(path = r".\\Drivers").install()
#     driverBr = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
#     driverBr.get('https://google.com/')

class ChromeType(object):
    GOOGLE = "google-chrome"
    CHROMIUM = "chromium"
    BRAVE = "brave-browser"
    MSEDGE = "edge"


def get_browser_version_from_os(browser_type=None):
    """Return installed browser version."""
    cmd_mapping = {
        ChromeType.GOOGLE: {
            OSType.LINUX: linux_browser_apps_to_cmd(
                "google-chrome",
                "google-chrome-stable",
                "google-chrome-beta",
                "google-chrome-dev",
            ),
            OSType.MAC: r"/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version",
            OSType.WIN: windows_browser_apps_to_cmd(
                r'(Get-Item -Path "$env:PROGRAMFILES\Google\Chrome\Application\chrome.exe").VersionInfo.FileVersion',
                r'(Get-Item -Path "$env:PROGRAMFILES (x86)\Google\Chrome\Application\chrome.exe").VersionInfo.FileVersion',
                r'(Get-Item -Path "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe").VersionInfo.FileVersion',
                r'(Get-ItemProperty -Path Registry::"HKCU\SOFTWARE\Google\Chrome\BLBeacon").version',
                r'(Get-ItemProperty -Path Registry::"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Google Chrome").version',
            ),
        },
        ChromeType.CHROMIUM: {
            OSType.LINUX: linux_browser_apps_to_cmd("chromium", "chromium-browser"),
            OSType.MAC: r"/Applications/Chromium.app/Contents/MacOS/Chromium --version",
            OSType.WIN: windows_browser_apps_to_cmd(
                r'(Get-Item -Path "$env:PROGRAMFILES\Chromium\Application\chrome.exe").VersionInfo.FileVersion',
                r'(Get-Item -Path "$env:PROGRAMFILES (x86)\Chromium\Application\chrome.exe").VersionInfo.FileVersion',
                r'(Get-Item -Path "$env:LOCALAPPDATA\Chromium\Application\chrome.exe").VersionInfo.FileVersion',
                r'(Get-ItemProperty -Path Registry::"HKCU\SOFTWARE\Chromium\BLBeacon").version',
                r'(Get-ItemProperty -Path Registry::"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Chromium").version',
            ),
        },
        ChromeType.BRAVE: {
            OSType.LINUX: linux_browser_apps_to_cmd(
                "brave-browser", "brave-browser-beta", "brave-browser-nightly"
            ),
            OSType.MAC: r"/Applications/Brave\ Browser.app/Contents/MacOS/Brave\ Browser --version",
            OSType.WIN: windows_browser_apps_to_cmd(
                r'(Get-Item -Path "$env:PROGRAMFILES\BraveSoftware\Brave-Browser\Application\brave.exe").VersionInfo.FileVersion',
                r'(Get-Item -Path "$env:PROGRAMFILES (x86)\BraveSoftware\Brave-Browser\Application\brave.exe").VersionInfo.FileVersion',
                r'(Get-Item -Path "$env:LOCALAPPDATA\BraveSoftware\Brave-Browser\Application\brave.exe").VersionInfo.FileVersion',
                r'(Get-ItemProperty -Path Registry::"HKCU\SOFTWARE\BraveSoftware\Brave-Browser\BLBeacon").version',
                r'(Get-ItemProperty -Path Registry::"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\BraveSoftware Brave-Browser").version',
            ),
        },
        ChromeType.MSEDGE: {
            OSType.LINUX: linux_browser_apps_to_cmd(
                "microsoft-edge",
                "microsoft-edge-stable",
                "microsoft-edge-beta",
                "microsoft-edge-dev",
            ),
            OSType.MAC: r"/Applications/Microsoft\ Edge.app/Contents/MacOS/Microsoft\ Edge --version",
            OSType.WIN: windows_browser_apps_to_cmd(
                # stable edge
                r'(Get-Item -Path "$env:PROGRAMFILES\Microsoft\Edge\Application\msedge.exe").VersionInfo.FileVersion',
                r'(Get-Item -Path "$env:PROGRAMFILES (x86)\Microsoft\Edge\Application\msedge.exe").VersionInfo.FileVersion',
                r'(Get-ItemProperty -Path Registry::"HKCU\SOFTWARE\Microsoft\Edge\BLBeacon").version',
                r'(Get-ItemProperty -Path Registry::"HKLM\SOFTWARE\Microsoft\EdgeUpdate\Clients\{56EB18F8-8008-4CBD-B6D2-8C97FE7E9062}").pv',
                # beta edge
                r'(Get-Item -Path "$env:LOCALAPPDATA\Microsoft\Edge Beta\Application\msedge.exe").VersionInfo.FileVersion',
                r'(Get-Item -Path "$env:PROGRAMFILES\Microsoft\Edge Beta\Application\msedge.exe").VersionInfo.FileVersion',
                r'(Get-Item -Path "$env:PROGRAMFILES (x86)\Microsoft\Edge Beta\Application\msedge.exe").VersionInfo.FileVersion',
                r'(Get-ItemProperty -Path Registry::"HKCU\SOFTWARE\Microsoft\Edge Beta\BLBeacon").version',
                # dev edge
                r'(Get-Item -Path "$env:LOCALAPPDATA\Microsoft\Edge Dev\Application\msedge.exe").VersionInfo.FileVersion',
                r'(Get-Item -Path "$env:PROGRAMFILES\Microsoft\Edge Dev\Application\msedge.exe").VersionInfo.FileVersion',
                r'(Get-Item -Path "$env:PROGRAMFILES (x86)\Microsoft\Edge Dev\Application\msedge.exe").VersionInfo.FileVersion',
                r'(Get-ItemProperty -Path Registry::"HKCU\SOFTWARE\Microsoft\Edge Dev\BLBeacon").version',
                # canary edge
                r'(Get-Item -Path "$env:LOCALAPPDATA\Microsoft\Edge SxS\Application\msedge.exe").VersionInfo.FileVersion',
                r'(Get-ItemProperty -Path Registry::"HKCU\SOFTWARE\Microsoft\Edge SxS\BLBeacon").version',
                # highest edge
                r"(Get-Item (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\msedge.exe').'(Default)').VersionInfo.ProductVersion",
                r"[System.Diagnostics.FileVersionInfo]::GetVersionInfo((Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\msedge.exe').'(Default)').ProductVersion",
                r"Get-AppxPackage -Name *MicrosoftEdge.* | Foreach Version",
                r'(Get-ItemProperty -Path Registry::"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Microsoft Edge").version',
            ),
        },
        "firefox": {
            OSType.LINUX: linux_browser_apps_to_cmd("firefox"),
            OSType.MAC: r"/Applications/Firefox.app/Contents/MacOS/firefox --version",
            OSType.WIN: windows_browser_apps_to_cmd(
                r'(Get-Item -Path "$env:PROGRAMFILES\Mozilla Firefox\firefox.exe").VersionInfo.FileVersion',
                r'(Get-Item -Path "$env:PROGRAMFILES (x86)\Mozilla Firefox\firefox.exe").VersionInfo.FileVersion',
                r"(Get-Item (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\firefox.exe').'(Default)').VersionInfo.ProductVersion",
                r'(Get-ItemProperty -Path Registry::"HKLM\SOFTWARE\Mozilla\Mozilla Firefox").CurrentVersion',
            ),
        },
    }

    try:
        cmd_mapping = cmd_mapping[browser_type][os_name()]
        pattern = PATTERN[browser_type]
        version = read_version_from_cmd(cmd_mapping, pattern)
        return version
    except Exception:
        raise Exception(f"Can not find browser {browser_type} installed in your system!!!")

