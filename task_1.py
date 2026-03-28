"""## Practical Exercise 1

### Title
**Automate Product Selection and Delivery Check on ShoppersStack**

### Description
Open the ShoppersStack website using Selenium WebDriver (https://www.shoppersstack.com/).

Automate the process of selecting a product category and verifying delivery availability using a pincode.

Perform the following steps:
- Launch the browser and open the ShoppersStack website
- Maximize the browser window
- Click on the **"APPLE"** product category
- Locate the delivery input field and enter the pincode
- Click on the **"Check"** button"""

from selenium.webdriver import Chrome,ChromeOptions
#ChromeOptions to customize browser settings

from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = ChromeOptions()
o.add_experimental_option("detach",True)
# Keep browser open even after script execution

driver = Chrome(options=o)
# Launch Chrome browser with given options


driver.get("https://www.shoppersstack.com/")
# Open the target website

driver.maximize_window()
# Maximize browser window

driver.implicitly_wait(100)
# Apply implicit wait (global wait for elements to load)

driver.find_element(By.XPATH,'//img[@src="https://m.media-amazon.com/images/I/71ZDY57yTQL._AC_UY327_FMwebp_QL65_.jpg"]').click()
# Located and clicked on product image using XPath

driver.find_element(By.XPATH,'//input[@id="Check Delivery"]').send_keys('123456')
# Located pincode input field and entered value

sleep(4)
wait = WebDriverWait(driver, 10)
ele = wait.until(EC.visibility_of_element_located((By.XPATH,'//button[@id="Check"]')))
# Explicit wait to pause execution until the element is visible and accessible
driver.find_element(By.XPATH,'//button[@id="Check"]').click()
sleep(4)
# Wait to observe result

driver.quit()

