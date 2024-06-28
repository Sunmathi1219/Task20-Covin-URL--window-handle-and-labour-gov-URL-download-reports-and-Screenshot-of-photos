""""
Test menu bar Document link and download the monthly progress report
"""

from download_monthly_progress import Monthly_Progress_Report
import pytest

url = "https://labour.gov.in/"
monthly_report = Monthly_Progress_Report(url)

def test_get_url():
    assert monthly_report.get_url() == True
    print("Success : automation of web page has started")


def test_menubar_page():
    assert  monthly_report.menu_bar_page() == True
    print("Success : Hovering the document menu and submenu has been shown")

def test_click_monthly_report():
    assert  monthly_report.click_monthly_report() == True
    print("Success : monthly report link is clicked")

def test_download_page():
    assert monthly_report.download_page() == True
    print("Success : download link is clicked and popup message is handled using alerts")

def test_shutdown():
    assert  monthly_report.shutdown() == None
    print("Success : Close the automation")
