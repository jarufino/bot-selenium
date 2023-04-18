from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Chrome()
browser.get("https://www.linkedin.com/login")
input_email=browser.find_element(By.ID,"username")
input_email.send_keys("jarufino@bol.com.br")
input_senha=browser.find_element(By.ID,"password")
input_senha.send_keys("689812aa")
btn_login= browser.find_element(By.XPATH, "//button[@type='submit']")
btn_login.click()
icons_vagas=browser.find_element(By.XPATH, "//span[@title='Vagas']")
icons_vagas.click()
search_box = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Pesquisar cargo, competência ou empresa']")))
search_box.send_keys("Python")
search_box.send_keys(Keys.RETURN)
input('')
