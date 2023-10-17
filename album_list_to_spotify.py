from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "D:/Documents/Google Drive/Development/Study@DaysPython@-days-Repo/Day48_Selenium/chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("PATH=" + chrome_driver_path)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://open.spotify.com/search")

# click login
click_login_page = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]')
click_login_page.click()

time.sleep(2)

# enter email
enter_email = driver.find_element(By.XPATH, '//*[@id="login-username"]')
enter_email.send_keys("1114961163")

# enter password
enter_pw = driver.find_element(By.XPATH, '//*[@id="login-password"]')
enter_pw.send_keys("*********")

# click login
click_login = driver.find_element(By.XPATH, '//*[@id="login-button"]/span[1]/span')
click_login.click()

time.sleep(3)


def like_album(album):
    try:
        # enter search
        driver.get("https://open.spotify.com/search")
        time.sleep(3)

        search = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input')
        search.send_keys(album)

        time.sleep(3)

        # click album
        found_album = driver.find_element(By.CSS_SELECTOR, '[data-testid="herocard-click-handler"]')
        found_album.click()

        time.sleep(3)

        # like album
        buttons = driver.find_elements(By.CLASS_NAME, 'RbsCNNM9a0WkFCM2UzBA')
        if len(buttons) > 1:
            like = buttons[1]  # Assuming the second button is the one you want
            like.click()
            time.sleep(3)
            print(f"Liking album: {album}")
        else:
            print(f"No suitable button found for search term: {album}")

    except ElementClickInterceptedException as e:
        print(f"No album found for search term: {album}")
        print("Continuing with the next album...\n")

    except NoSuchElementException:
        print(f"No album found for search term: {album}")
        print("Continuing with the next album...\n")

    except IndexError:
        print(f"No suitable button found for search term: {album}")
        print("Continuing with the next album...\n")


with open('album_list.txt', 'r', encoding='utf-8') as file:

    lines = file.readlines()

    for line in lines:
        search_term = line.strip()
        like_album(search_term)



