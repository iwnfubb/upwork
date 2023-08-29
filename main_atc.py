from selenium.webdriver import Safari
from selenium.webdriver.safari.options import Options
from selenium.webdriver.common.by import By
from atc.atc_platform import ATC_Platform
from atc.atc_platform import Level


opts = Options()
opts.add_argument("--headless")
browser = Safari(options=opts)
atc = ATC_Platform(browser)
first_level = atc.get_first_level_text()
print (first_level)
second_level= atc.get_next_level_text (first_level, Level.LEVEL2)
print (second_level)
third_level= atc.get_next_level_text (second_level, Level.LEVEL3)
print (third_level)
forth_level= atc.get_next_level_text (third_level, Level.LEVEL4)
print (forth_level)