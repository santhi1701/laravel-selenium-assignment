from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://127.0.0.1:8000/login")

time.sleep(5)

email = f"user{random.randint(1000,9999)}@test.com"
password = f"pass{random.randint(1000,9999)}"

inputs = driver.find_elements(By.TAG_NAME, "input")

visible_inputs = []

for inp in inputs:
    if inp.is_displayed():
        visible_inputs.append(inp)

if len(visible_inputs) >= 2:
    visible_inputs[0].send_keys(email)
    visible_inputs[1].send_keys(password)

time.sleep(3)

driver.quit()