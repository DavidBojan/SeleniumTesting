from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

""" By ID """
driver.get(url='http://automationpractice.com/index.php')
driver.find_element(By.ID, value='search_query_top')
sleep(3)

driver.get(url='https://www.phptravels.net/')
driver.find_element(By.ID, value='select2-hotels_city-container')
sleep(3)

driver.get(url='https://www.techlistic.com/p/selenium-practice-form.html')
driver.find_element(By.ID, value='profession-0')
sleep(3)

"""By link_text"""
driver.get(url='https://formy-project.herokuapp.com/')
driver.find_element(By.LINK_TEXT, 'Autocomplete').click()
sleep(3)

driver.get(url='https://formy-project.herokuapp.com/')
driver.find_element(By.LINK_TEXT, 'Buttons').click()
sleep(3)

driver.get(url='https://formy-project.herokuapp.com/')
driver.find_element(By.LINK_TEXT, 'Checkbox').click()
sleep(3)

"""Partial link text"""
driver.get(url='http://automationpractice.com/index.php')
driver.find_element(By.PARTIAL_LINK_TEXT, 'T-shirts').click()
sleep(3)

driver.get(url='http://automationpractice.com/index.php')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Chiffon').click()
sleep(3)

driver.get(url='http://automationpractice.com/index.php')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Summer Dress').click()
sleep(3)

""" Name / Tag """
driver.get(url='https://www.techlistic.com/p/selenium-practice-form.html')
name_element = driver.find_element(By.NAME, 'firstname')
name_element.send_keys('David')
lastname_element = driver.find_element(By.NAME, 'lastname')
lastname_element.send_keys('Bojan')
sleep(3)

driver.get(url='https://www.techlistic.com/p/selenium-practice-form.html')
input_list = driver.find_elements(By.TAG_NAME, 'input')
input_list[0].send_keys('David')
input_list[1].send_keys('Bojan')
sleep(3)

driver.get(url='http://automationpractice.com/index.php')
name_element = driver.find_element(By.NAME, 'search_query')
name_element.send_keys('dress')
sleep(3)

""" Class name """
driver.get(url='https://formy-project.herokuapp.com/form')
class_element = driver.find_elements(By.CLASS_NAME, 'form-control')
class_element[0].send_keys('David')
class_element[1].send_keys('Bojan')
class_element[2].send_keys('Technical specialist')
sleep(3)

""" CSS """
# selector by CSS - ID
driver.get(url='http://automationpractice.com/index.php')
selector_element = driver.find_element(By.CSS_SELECTOR, 'input#search_query_top')
selector_element.send_keys('dress')
sleep(3)

""" Selector by CSS - Class"""
driver.get(url='https://formy-project.herokuapp.com/form')
selector_class = driver.find_element(By.CSS_SELECTOR, 'input.form-control')
selector_class.send_keys('David')
sleep(3)

""" Selector by CSS - attribute = value"""
driver.get(url='https://formy-project.herokuapp.com/form')
selector_attribute = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter first name"]')
selector_attribute.send_keys('David')
sleep(3)


""" XPath """
""" selector by Xpath - attribute = value """

driver.get(url='https://www.techlistic.com/p/selenium-practice-form.html')
selector_value_one = driver.find_element(By.XPATH, '//input[@name="firstname"]')
selector_value_two = driver.find_element(By.XPATH, '//input[@name="lastname"]')
selector_value_three = driver.find_element(By.XPATH, '//input[@id="datepicker"]')
selector_value_one.send_keys('a')
selector_value_two.send_keys('b')
selector_value_three.send_keys('c')
sleep(5)

""" selector by XPATH - text element """
driver.get(url='https://the-internet.herokuapp.com/')
text_selector = driver.find_element(By.XPATH, "//a[text()='A/B Testing']")
sleep(3)
text_selector.click()
sleep(3)

driver.get(url='https://the-internet.herokuapp.com/')
text_selector = driver.find_element(By.XPATH, "//a[text()='Add/Remove Elements']")
sleep(3)
text_selector.click()
sleep(3)

driver.get(url='https://the-internet.herokuapp.com/')
text_selector = driver.find_element(By.XPATH, "//a[text()='Drag and Drop']")
sleep(3)
text_selector.click()
sleep(3)

""" Partial text """
driver.get(url='https://formy-project.herokuapp.com/form')
text_selector = driver.find_element(By.XPATH, "//*[contains(@id,'first')]")
sleep(3)
text_selector.send_keys('no name')
sleep(3)

"""Xpath using OR, pipe | """
driver.get(url='https://formy-project.herokuapp.com/form')
pipe_selector = driver.find_element(By.XPATH, '//input[@id="first-name"]|//input[@placeholder="Enter first name"]')
sleep(3)
pipe_selector.send_keys('no name')
sleep(3)

""" xpath using * """
driver.get(url='https://formy-project.herokuapp.com/form')
pipe_selector = driver.find_element(By.XPATH, '//input[@*="job-title"]')
sleep(3)
pipe_selector.send_keys('no job')
sleep(3)

""" xpath using (xpath)[1]"""
driver.get(url='https://formy-project.herokuapp.com/form')
list_selector = driver.find_elements(By.XPATH, '//input[@*="form-control"]')
list_selector[1].send_keys('second element')
sleep(3)

""" xpath element using parent """
driver.get(url='https://formy-project.herokuapp.com/form')
element_by_parent = driver.find_elements(By.XPATH, '//*[@type="text"]//parent::div')
print(f"The text inside the element is: {element_by_parent[1].text}")
sleep(3)

""" xpath following parent sibling"""
driver.get(url='https://formy-project.herokuapp.com/form')
element_by_sibling = driver.find_element(By.XPATH, '//*[@type="text"]//parent::div/following-sibling::div')
print(f"The text inside the element is: {element_by_sibling.text}")
sleep(3)

""" function that allows to choose the wanted element """

driver.get(url='https://formy-project.herokuapp.com/form')
element = input(f"Type the element: ")
# example that worked for id = first-name
element_by_sibling = driver.find_element(By.XPATH, f'//*[@id="{element}"]')
element_by_sibling.send_keys('test')
sleep(5)


def get_given_element():
    driver.get(url='https://formy-project.herokuapp.com/form')
    element = input(f"Type the element: ")
    # example that worked for id = first-name
    element_by_sibling = driver.find_element(By.ID, value=element)
    element_by_sibling.send_keys('test')
    sleep(5)
    driver.quit()


get_given_element()
