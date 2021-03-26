from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class to_Do_App_Page():
    ## START Functions used for general purpose
    def __init__(self,app):
        '''Contructor'''
        self.driver = app.driver;

    def end_session(self):
        '''Stop Driver'''
        self.driver.quit()

    def reload_page(self):
        '''Reload Page'''
        self.driver.refresh()

    def find_by_css(self,css):
            try:
                i = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_css_selector(css))
            except (NoSuchElementException, TimeoutException):

                return False
            return i

    def find_by_xpath(self,xpath):
            try:
                i = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(xpath))
            except (NoSuchElementException, TimeoutException):

                return False
            return i

    def find_by_xpath_contains(self,xpathc):
            xpath = "//*[contains(text(),'"+xpathc+"')]"
            try:
                i = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(xpath))
            except (NoSuchElementException, TimeoutException):

                return False
            return i

    def find_by_id(self,id):
            try:
                i = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_id(id))
            except (NoSuchElementException, TimeoutException):

                return False
            return i
    #END  Functions used for general purpose


    ## START get elemets
    def look_for_title(self):
        self.ITEM_TITLE = self.driver.title
        return self.ITEM_TITLE

    def look_for_page_title(self):
        self.ITEM_TITLE_PAGE = self.find_by_xpath("//h1[normalize-space()='Agenda']")
        return self.ITEM_TITLE_PAGE

    def look_for_calendar(self):
        self.ITEM_CALENDAR = self.find_by_xpath("//input[@id='datetime-local']")
        return self.ITEM_CALENDAR

    def look_for_name(self):
        self.ITEM_NAME = self.find_by_xpath("//div[@class='complete']//div[1]//input[1]")
        return self.ITEM_NAME

    def look_for_obs(self):
        self.ITEM_OBS = self.find_by_xpath("//div[@class='complete']//div[2]//input[1]")
        return self.ITEM_OBS


    def look_for_text_box(self):
        #self.ITEM_TEXT_BOX = self.find_by_id('new_record')
        self.ITEM_TEXT_BOX = self.find_by_xpath("//input[@id='new_record']")
        return self.ITEM_TEXT_BOX

    def look_for_button_add(self):
        self.ITEM_BUTTON_ADD = self.find_by_xpath("//span[@class='MuiButton-label']")
        return self.ITEM_BUTTON_ADD

    def look_for_added_item(self,value):
        try:
            i = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath("//b[normalize-space()='"+value+"']"))
        except (NoSuchElementException, TimeoutException):

            return False
        return i
        # if msj in i.text:
        #     return i
        # return False
        # self.ITEM_ADDED = self.find_by_xpath_contains()
        # return self.ITEM_ADDED

    def look_for_remove_button(self):
        self.ITEM_BUTTON_REMOVE = self.find_by_xpath("//span[contains(text(),'❌')]")
        return self.ITEM_BUTTON_REMOVE
    # END get elements


    ## START Functions used for specific steps

    def go_to_web_site(self):
        '''Go to Agenda app WebApp'''
        self.driver.maximize_window();
        self.driver.get("https://agenda-153b4.web.app/")
        return self.look_for_title()

    def send_msj(self,dataT,dataH,dataM,name,obs):
        if not self.look_for_calendar(): return False

        self.ITEM_CALENDAR.send_keys(str(dataT))
        self.ITEM_CALENDAR.send_keys(Keys.TAB)
        self.ITEM_CALENDAR.send_keys(str(dataH))
        self.ITEM_CALENDAR.send_keys(str(dataM))

        if not self.look_for_name(): return False
        self.ITEM_NAME \
            .send_keys(str(name)) \

            # .send_keys(Keys.RETURN)

        if not self.look_for_obs(): return False
        self.ITEM_OBS\
            .send_keys(str(obs))

        return True

    def click_add_button(self):
        if not self.look_for_button_add(): return False
        self.find_by_xpath("//span[@class='MuiButton-label']").click()
        #self.ITEM_BUTTON_ADD.click()
        return True

    def click_remove(self):
        if not self.look_for_remove_button(): return False
        self.ITEM_BUTTON_REMOVE.click()
        return True
    # END Functions used for specific steps