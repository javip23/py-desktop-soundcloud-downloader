from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import get_user_settings, get_configuration

class BaseDownloader():
    def __init__(self, track_url, base_download_url):
        opts = Options()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_options=opts, firefox_profile=self.get_firefox_profile())
        self.track_url = track_url
        self.base_download_url = base_download_url
    
    def get_url(self):
        self.driver.get(self.base_download_url)
    
    def set_url_to_download_in_main_textbox(self, element_id):
        main_textbox = self.driver.find_element_by_id(element_id)
        if main_textbox:
            main_textbox.clear()
            main_textbox.sendKeys(self.track_url)
    
    def click_download_button(self, element_id):
        download_button = self.driver.find_element_by_id(element_id)
        if download_button:
            download_button.click()
    
    def wait_until_element_appeared(self, element_id, poll_frequency=5):
        element = None
        try:
            element = WebDriverWait(self.driver, poll_frequency).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
        finally:
            self.driver.quit()
        return element
    
    def __del__(self):
        self.driver.close()
    
    def get_firefox_profile(self):
        profile = webdriver.FirefoxProfile()
        user_download_folder = get_user_settings(namespace="USERCONFIG",key="base_download_folder")
        handlers_config = get_configuration(namespace="BASECONFIG",key="save_to_disk_handlers")
        
        profile.set_preference("browser.download.folderList",1)
        if user_download_folder:
            profile.set_preference("browser.download.dir", user_download_folder)
            profile.set_preference("browser.download.downloadDir", user_download_folder)
            profile.set_preference("browser.download.defaultFolder", user_download_folder)  
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        profile.set_preference("browser.download.manager.showWhenStarting",False)
        profile.set_preference("pdfjs.disabled", True)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", handlers_config)
        profile.update_preferences()
        
        return profile