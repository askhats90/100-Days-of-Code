from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\Study\Development\chromedriver.exe"
link = "https://orteil.dashnet.org/experiments/cookie/"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get(link)
driver.maximize_window()


def buy_upgrade():
    items = store.find_elements(By.TAG_NAME, "b")
    grayed_items = store.find_elements(By.CLASS_NAME, "grayed")

    grayed_items_texts = [x.text.split("\n")[0] for x in grayed_items]
    available_items = {}

    # Filling in available items' dictionary {Upgrade: Price}
    for item in items[:-1]:
        if item.text not in grayed_items_texts:
            item_price = int(item.text.split(" - ")[1].replace(",", ""))
            item_name = item.text.split(" - ")[0]
            available_items[item_name] = item_price

    print(available_items)

    # Buy upgrades algorithm
    if num_of_cookies >= max(available_items.values()):
        name = max(available_items, key=available_items.get)
        upgrade = store.find_element(By.ID, f"buy{name}")
        upgrade.click()

    print(int(money.text.replace(",", "")))


timeout = 60
start_time = time.time()
loops = 1

cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")
store = driver.find_element(By.ID, "store")
cookies_per_second = driver.find_element(By.ID, "cps")

while time.time() < start_time + timeout:
    cookie.click()

    num_of_cookies = int(money.text.replace(",", ""))

    if time.time() >= start_time + 5 * loops:
        print(f"Start time: {time.ctime(start_time)}", f"Loop time: {time.ctime(start_time + 5 * loops)}")
        print(f"Number of cookies: {num_of_cookies}")
        buy_upgrade()
        print(cookies_per_second.text)

        loops += 1
