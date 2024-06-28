"""""
Using the python selenium visit the URL https://labour.gov.in/ and do the following tasks given below-
1.)Goto the menu whose name is "Document" and download the monthly progress report
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Monthly_Progress_Report:
    Document_locator = "Documents"
    monthly_report_locator = "//a[@href='https://labour.gov.in/monthly-progress-report']"
    download_locator = "//table[@role='Presentation']//tbody//tr//td//a[@target='_BLANK' and text()='Download(139.61 KB)']"

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # open the URL
    def get_url(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(3)
        print("HOMEPAGE TITTLE",self.driver.title)
        homepage_window_handle = self.driver.current_window_handle
        print("Ministry Homepage window ID :", homepage_window_handle)
        return True

    #Hover the Document menu
    def menu_bar_page(self):
        #document element
        document_element = self.driver.find_element(by=By.LINK_TEXT, value=self.Document_locator)
        sleep(2)

        #action class-To Hover the Document menu
        actions = ActionChains(self.driver)
        actions.move_to_element(document_element).perform()
        sleep(2)
        return True

    #click the monthly report link
    def click_monthly_report(self):
        #click the monthly report
        monthly_report_element = self.driver.find_element(by=By.XPATH, value=self.monthly_report_locator)
        monthly_report_element.click()
        sleep(3)
        all_window_handle = self.driver.window_handles
        print("Dashboard Window ID :", all_window_handle)
        return True

    #click the download link and handle the Popup message and close the new window
    def download_page(self):
        #Click the monthly report download link
        download_element = self.driver.find_element(by=By.XPATH, value=self.download_locator)
        download_element.click()
        sleep(3)

        #click popup window using alert
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        # Accept the alert
        alert.accept()
        sleep(2)

        all_window_handle = self.driver.window_handles
        print("Dashboard Window ID :", all_window_handle)
        for windows in all_window_handle:
            if windows != self.driver.current_window_handle:
                self.driver.switch_to.window(windows)
                sleep(3)
                self.driver.close()
                sleep(2)
                break
            return True
    #close the web automation Homepage
    def shutdown(self):
        sleep(2)
        self.driver.quit()
        return None
    

"""
if __name__ == "__main__":
    monthly_report = Monthly_Progress_Report("https://labour.gov.in/")
    print(monthly_report.get_url())
    monthly_report.menu_bar_page()
    monthly_report.click_monthly_report()
    monthly_report.download_page()
    monthly_report.shutdown()
"""