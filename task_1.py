from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://www.shoppersstack.com/")
driver.maximize_window()
driver.implicitly_wait(100)

driver.find_element(By.XPATH,'//img[@src="https://m.media-amazon.com/images/I/71ZDY57yTQL._AC_UY327_FMwebp_QL65_.jpg"]').click()

driver.find_element(By.XPATH,'//input[@id="Check Delivery"]').send_keys('123456')
sleep(4)
wait = WebDriverWait(driver, 10)
ele = wait.until(EC.visibility_of_element_located((By.XPATH,'//button[@id="Check"]')))
driver.find_element(By.XPATH,'//button[@id="Check"]').click()
sleep(4)

driver.quit()
