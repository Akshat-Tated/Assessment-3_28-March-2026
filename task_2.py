"""## Practical Exercise 2

### Title
**Automate Myntra Product Selection**

### Description
Open the Myntra website using Selenium WebDriver (https://www.myntra.com/).

Automate the process of navigating categories, selecting a product, applying filters, sorting products and adding to bag.

Perform the following steps:
- Launch the browser and open the Myntra website
- Maximize the browser window
- Hover over the **Genz** category
- Click on **"Jackets Under ₹899"**
- Select any 2 filter under the product filters (e.g., brand, size, or color)
- Click on the **Sort By** 'Popularity'
- Click on the any one product
- Select size (if mentioned)
- Add to bag"""

from selenium.webdriver import Chrome,ChromeOptions
#ChromeOptions to customize browser settings

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = ChromeOptions()
o.add_experimental_option("detach",True)
# Keep browser open even after script execution

o.add_argument("--disable-notifications")
driver = Chrome(options=o)
#driver is holding the browser

driver.get("https://www.myntra.com/")
driver.maximize_window()
driver.implicitly_wait(100)

actions = ActionChains(driver)
ele = driver.find_element(By.XPATH,'//a[@href="/shop/fwd-women"][1]')
actions.move_to_element(ele).pause(2).perform()
#using actionchains to hover to the element

wait = WebDriverWait(driver, 10)
ele = wait.until(EC.visibility_of_element_located((By.XPATH,'//a[@data-reactid="837"]')))
# Explicit wait to pause execution until the element is visible and accessible
ele.click()

gender = driver.find_element(By.XPATH,'//input[@value="men,men women"]')
actions.click(gender).perform()
#click the radio button
sleep(3)

brand = driver.find_element(By.XPATH,'//input[@value="Rigo"]')
actions.click(brand).perform()
#slecting brand="rigo" checkbox
sleep(3)

sort_by = driver.find_element(By.XPATH,'//div[@class="sort-sortBy"]')
actions.move_to_element(sort_by).pause(2).release().perform()
#hover to the dropdown to select options

hover_ele = driver.find_element(By.XPATH,'//ul[@class="sort-list"]//li[3]//input')
actions.move_to_element(sort_by).click().perform()
# driver.find_element(By.XPATH,'//input[@value="popularity"]').click()
sleep(3)
# Wait to observe result

driver.find_element(By.XPATH,'//img[@title="Rigo Typography Printed Fleece Oversized Varsity Jacket"]').click()
sleep(3)
# Wait to observe result

driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH,'//div[@class="size-buttons-buttonContainer"][1]').click()
sleep(3)
# Wait to observe result

driver.find_element(By.XPATH,'//span[@class="myntraweb-sprite pdp-whiteBag sprites-whiteBag pdp-flex pdp-center"]').click()
sleep(3)
# Wait to observe result

driver.quit()

