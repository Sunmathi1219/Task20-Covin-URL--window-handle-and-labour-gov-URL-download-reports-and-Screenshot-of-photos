""""
Using Python selenium and the URL https://www.cowin.gov.in/ you have to
1.) click on the "create FAQ" and "Partners" anchor tags present on the homepage and open two new windows
2.) Now you have to fetch the opened windows/frame ID and display the same on the console
3.) Kindly close the two new windows and come back to the home page also
"""


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

class Cowin_faq_patners:

       faq_locator="//div[@class='noMobile ml-auto']//div//ul//li//a[@href='/faq']"
       partner_locator="//div[@class='noMobile ml-auto']//div//ul//li//a[@href='/our-partner']"

       def __init__(self,url):
         self.url= url
         self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
         sleep(3)

       #fetch the url
       def homepage_navigation(self):
         self.driver.maximize_window()
         self.driver.get(self.url)
         sleep(2)

         #Window ID of the cowin homepage
         homepage_window_handle=self.driver.current_window_handle
         print("Cowin HomePage Window ID :", homepage_window_handle)

         # Click the "faq" and "partner" anchor tag
         self.driver.find_element(by=By.XPATH, value=self.faq_locator).click()
         self.driver.find_element(by=By.XPATH, value=self.partner_locator).click()
         sleep(2)

         # 2.)Window ID of FAQ anchor tag Page
         all_window_handle = self.driver.window_handles
         print("Dashboard Window ID : ", all_window_handle)
         # Close the faq anchor tag Page and goto the cowin homepage
         for windows in all_window_handle:
             if windows != homepage_window_handle:
                 self.driver.switch_to.window(windows)
                 print("FAQ Window ID :",windows)
                 sleep(2)
                 self.driver.close()
                 break


         # 2.)Window ID of Partner anchor tag Page
         all_window_handle = self.driver.window_handles
         print("Dashboard Window ID : ", all_window_handle)
         # Close the partner anchor tag Page and goto the cowin homepage
         for windows in all_window_handle:
             if windows != homepage_window_handle:
                self.driver.switch_to.window(windows)
                print("Partner Window ID :", windows)
                sleep(2)
                self.driver.close()
                break

         return True

       #close the cowin web automation page
       def shutdown(self):
           self.driver.quit()
           return None

"""
if __name__ == "__main__":
    faq_partner_navigation = Cowin_faq_patners("https://www.cowin.gov.in/")
    faq_partner_navigation.homepage_navigation()
    faq_partner_navigation.shutdown()
"""