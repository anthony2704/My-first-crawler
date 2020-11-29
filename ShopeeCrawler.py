import xlwt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chromedriver = '/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)
driver.get("https://shopee.vn/Laptop-cat.13030.13065")
all_links = driver.find_elements_by_class_name('_3eufr2')

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
sheet1.write(0, 0, "ITEM")
i = 1
for x in range(len(all_links)):
    sheet1.write(i, 0, all_links[x].text)
    i = i + 1
book.save("data.xlsx")

print('Complete')

driver.quit()
