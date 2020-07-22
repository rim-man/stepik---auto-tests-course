from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
       element.send_keys("Мой ответ")

    button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла
