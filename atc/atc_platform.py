from selenium.webdriver.safari.options import Options
from selenium.webdriver.common.by import By
import time
from enum import Enum 
import selenium

class Level (Enum): 
    LEVEL1 = "classA"
    LEVEL2 = "classB"
    LEVEL3 = "classC"
    LEVEL4 = "classD"


#Time out base on internet connection
TIME_OUT = 3
class ATC_Platform:
    def __init__(self, web_driver) -> None:
        self.web_driver = web_driver
        self.web_driver.get("https://www.kegg.jp/brite/br08303")
        self.web_driver.maximize_window()
        time.sleep (TIME_OUT)


    def get_first_level_text (self):
        text = self.web_driver.find_elements(By.XPATH, "//tr[contains(@class, 'classA')]")
        return list (  filter ( lambda x : x != "", list(  map(lambda x: x.text, text))))

    
    def get_next_level_text( self,  list_of_text : list, level : Level):
        for item in list_of_text:
            self.web_driver.execute_script("window.scrollTo(0, 0);")        
            max_try = 3
            for x in range(0, max_try):
                try:
                    pointer = self.web_driver.find_element(By.XPATH, "//*[text()='" + item + "']/preceding-sibling::span[@class='handle']" )
                    time.sleep(0.5)
                    self.web_driver.execute_script("arguments[0].click();", pointer)
                    time.sleep(0.5)
                    break

                except selenium.common.exceptions.NoSuchElementException:
                    print ("%s not found ", item)
                    self.web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
                    continue
                except selenium.common.exceptions.StaleElementReferenceException: 
                    print ("%s StaleElementReferenceException ", item)
                    continue
            
        text = self.web_driver.find_elements(By.XPATH, "//tr[contains(@class, '"+ level.value + "')]")
        return list (  filter ( lambda x : x != "", list(  map(lambda x: x.text, text))))



    def close(self):
        self.web_driver.close()
        quit()