from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
import time
from selenium.webdriver.common.by import By

driver.get("https://practice.microdegree.work")