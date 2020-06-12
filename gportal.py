from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform 
from os import path
import sys

is_frozen = getattr(sys, 'frozen', False)
bundle_dir = path.join(path.dirname(__file__))

if is_frozen:
    bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))

def restart_server():
    plt = platform.system()
   
    if plt == 'Windows':
        path_to_driver = bundle_dir + '/chromedriver_83_win.exe'
        
    if plt == 'Darwin':
        path_to_driver = bundle_dir + '/chromedriver_83'
    
    driver = webdriver.Chrome(path_to_driver)
    
    driver.get("https://id2.g-portal.com/login")
    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.current_url != "https://id2.g-portal.com/login")
    username = driver.find_element_by_id("login")
    password = driver.find_element_by_id("password")

    username.send_keys("Tkyser")
    password.send_keys("Scooby25")

    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[4]/input').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/div[2]/a/span').click()

    driver.switch_to.window(driver.window_handles[1])

    #driver.implicitly_wait(10)
    #element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.content:nth-child(2) > a:nth-child(3)')))

    actualTitle = driver.title
    print(actualTitle)

    driver.find_element(By.XPATH, '/html/body/section/div[3]/div[3]/div[2]/div/div[1]/div[2]/ul/li[4]/a').click()
    driver.quit()
