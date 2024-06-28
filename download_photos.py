"""""
Using the python selenium visit the URL https://labour.gov.in/ and do the following tasks given below-
2.)Goto the menu whose name is "media" where you will find a submenu "photo gallery" .download photos and store them in
 a folder
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import os


class Photos_Download:
    #locators of web page
    media_locator="Media"
    photo_locator="//a[@href='/photo-gallery']"
    download_locator="//a[@href='/gallery/4th-ewg']"

    #folderpath and filename
    file_name="Screen_shot.png"
    folder_path="PhotoGallery_screenshot"

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    #open the url
    def get_url(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(2)
        print("Tittle of page : ", self.driver.title)
        return True

    #Hover the document menu
    def hover_media_menu(self):
        media_element=self.driver.find_element(by=By.LINK_TEXT, value=self.media_locator)
        sleep(2)

        actions=ActionChains(self.driver)
        actions.move_to_element(media_element).perform()
        sleep(2)
        return True

    # click the photo gallery link
    def click_Photo_gallery(self):
        photo_element=self.driver.find_element(by=By.XPATH, value=self.photo_locator)
        photo_element.click()
        sleep(2)
        print("Tittle of page : ", self.driver.title)
        return True

    #click the download link
    def download_photos(self):
        download_element=self.driver.find_element(by=By.XPATH, value=self.download_locator)
        download_element.click()
        sleep(2)
        print("Tittle of page : ", self.driver.title)
        return True

    #Take screenshot of particular link
    def take_screenshot(self):
        screenshot_path=os.path.join(self.folder_path,self.file_name)

        # Get total height of the webpage
        total_height = self.driver.execute_script("return document.body.scrollHeight")

        #set view port height to the total height of the webpage
        self.driver.set_window_size(1920, total_height)
        captured_height=0
        while captured_height<total_height:
            self.driver.save_screenshot(screenshot_path)
            self.driver.execute_script(f"window.scrollTo(0,{captured_height});")
            captured_height += 1200  #adjusting scrolling height
            sleep(2)

        print(f"ScreenShoot Saved to {screenshot_path}")
        return True

    #close the automation
    def shutdown(self):
        self.driver.quit()
        sleep(2)
        return None

"""
if __name__ == "__main__":
    photos_download=Photos_Download("https://labour.gov.in/")
    photos_download.get_url()
    photos_download.hover_media_menu()
    photos_download.click_Photo_gallery()
    photos_download.download_photos()
    photos_download.take_screenshot()
    photos_download.shutdown()
    
"""