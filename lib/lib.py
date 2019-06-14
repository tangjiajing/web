from selenium import webdriver
import time

class Common(object):
    def __init__(self,brower):
        if brower == 'Firefox':
            self.driver = webdriver.Firefox()
        elif brower == 'Chrome':
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def delay(self):
        self.driver.implicitly_wait(5)

    def openurl(self,url):
        self.driver.get(url)
        self.delay()
    def locateelement(self,locatetype,value):
        el = None
        if locatetype == 'id':
            el = self.driver.find_element_by_id(value)
        elif locatetype == 'class_name':
            el = self.driver.find_element_by_class_name(value)
        elif locatetype == 'tag_name':
            el = self.driver.find_element_by_tag_name(value)
        elif locatetype == 'link_text':
            el = self.driver.find_element_by_link_text(value)
        elif locatetype == 'partial_link_text':
            el = self.driver.find_element_by_partial_link_text(value)
        elif locatetype == 'xpath':
            el = self.driver.find_element_by_xpath(value)
        elif locatetype == 'css':
            el = self.driver.find_element_by_css_selector(value)
        elif locatetype == 'name':
            el = self.driver.find_element_by_name(value)

        if el is not None:
            return el

    def click(self,locatetype,value):
            self.locateelement(locatetype,value).click()
    def input(self,locatetype,value,data):
            self.locateelement(locatetype,value).send_keys(data)
    def __del__(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    com = Common('Chrome')
    com.openurl('http://www.baidu.com')
    com.input('id','kw','selenium')


