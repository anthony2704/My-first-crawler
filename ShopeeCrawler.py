from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
# chrome_options.add_argument("--headless")

chromedriver = '/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)
driver.get("https://shopee.vn/Laptop-cat.13030.13065")

all_links = driver.find_elements_by_class_name('_3eufr2')

for x in all_links:
    print(x.text)
    print('\n')

print('Complete')

driver.quit()
