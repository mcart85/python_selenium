
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element_by_id("book").click()

    # browser.find_element_by_css_selector("[type='submit']").click()
    # time.sleep(1)
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)
    #
    x = browser.find_element_by_id("input_value").text
    answer = calc(x)
    browser.find_element_by_id("answer").send_keys(answer)
    #
    # # browser.find_element_by_name("firstname").send_keys("Artyom")
    # # browser.find_element_by_name("lastname").send_keys("Makarov")
    # # browser.find_element_by_name("email").send_keys("mcart85@gmail.com")
    # # current_dir = os.path.abspath(os.path.dirname(__file__))
    # # file_path = os.path.join(current_dir, 'file.txt')
    # # inputFile = browser.find_element_by_id("file")
    # # inputFile.send_keys(file_path)
    submit = browser.find_element_by_xpath("//button[text()='Submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()
    time.sleep(30)



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
