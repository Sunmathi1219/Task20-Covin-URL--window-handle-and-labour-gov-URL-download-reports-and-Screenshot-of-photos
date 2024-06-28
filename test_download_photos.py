""""
Test the URL To take screenshot of full page
"""

from download_photos import Photos_Download
import pytest

url="https://labour.gov.in/"
photos_download=Photos_Download(url)

def test_get_url():
    assert photos_download.get_url() == True
    print("Success : Automation has begun")

def test_hover_media_menu():
    assert photos_download.hover_media_menu() == True
    print("Success:Hovered the media menu")

def test_click_photo_gallery():
    assert photos_download.click_Photo_gallery() == True
    print("Success : photo gallery link is clicked successfully")

def test_download_photos():
    assert photos_download.download_photos() == True
    print("Success : photo's link is clicked")

def test_take_screenshot():
    assert photos_download.take_screenshot() == True
    print("Success : screenshot of particular link is saved in the folder")

def test_shutdown():
    assert  photos_download.shutdown() ==None
    print("Success : Automation closed")

