from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('./chromedriver.exe')


def canvasFileDownloader(url, ff):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(f'{url}/download')
    timeout = .1
    try:
        element_present = EC.presence_of_element_located((By.ID, 'main'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        ff += 1
        print("File Found! " + str(ff) + " files found so far!")
        return 1
    finally:
        return 0
        # print(f"Page Loaded: {url}")


if __name__ == "__main__":
    driver.get('https://canvas.iastate.edu/')
    filesFound = 0
    time.sleep(15)
    for x in range(19993700, 20597550):
        driver.switch_to.window(driver.window_handles[0])
        filesFound += canvasFileDownloader(f"https://canvas.iastate.edu/courses/97241/files/{x}", filesFound)
        driver.close()
