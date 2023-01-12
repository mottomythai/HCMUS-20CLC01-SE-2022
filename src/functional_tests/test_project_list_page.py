from django.test import TestCase, SimpleTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from hi5.models import product
from django.urls import reverse
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# Create your tests here.
# class SimpleTest(SimpleTestCase):
#     databases = '_all_'
#     def test_home_page_status(self):
#         response = self.client.get('/')
#         self.assertEquals(response.status_code, 200)

class TestSearchPage(StaticLiveServerTestCase):
    #
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe', chrome_options=chrome_options)
    
    def tearDown(self):
        self.browser.quit()

    def test_search_with_unexisted_input(self,input="?query=shirt"):
        #database="_all_"
        self.browser.get(self.live_server_url+reverse('search')+input)
        #time.sleep(200)
        notfound = self.browser.find_element(By.CLASS_NAME,"content grid").find_element(By.CLASS_NAME,"container")
        self.assertEquals(
            (notfound.find_element(By.TAG_NAME,'q')).text,
            'No Product Found'
        )


    # def test_search_normal(self):
    #     self.browser.get(self.live_server_url)
    #     search_bar = self.find_element_by_name("q")
    #     self.clear()
    #     self.send_keys("shirt")
    #     self.send_keys(Keys.RETURN)
    #     print(self.current_url)
    #     self.close()


    # def test_search_with_unexisted_input(self):
    #     #database="_all_"
    #     self.browser.get(self.live_server_url)
    #     add_url=self.live_server_url+reverse('search/')
    #     notfound = self.browser.find_element(By.CLASS_NAME,"container")
    #     self.assertEquals(
    #         notfound.find_element(By.TAG_NAME,'p').text,"No Product Found"
    #     )
    #     #self.assertEquals(response.status_code, 200)
    #     # response = self.client.get('/')
    #     #self.assertEquals(response.status_code, 200)
    #     #self.assertEquals(0,1)