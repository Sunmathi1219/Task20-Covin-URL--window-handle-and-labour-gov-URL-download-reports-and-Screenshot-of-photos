""""
Test the cowin page navigation of FAQ and PARTNER ancher tag
"""

from navigatio_faq_partners import Cowin_faq_patners
import pytest

url="https://www.cowin.gov.in/"
navigation=Cowin_faq_patners(url)

def test_homepage_navigation():
    assert navigation.homepage_navigation() == True
    print("Success : FAQ and PARTNER anchor tag page navigation has been done")

def test_shutdown():
    assert navigation.shutdown() == None
    print("Success : Cowin Homepage has been closed")
