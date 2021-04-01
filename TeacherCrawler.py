from selenium import webdriver

chrome_path = "D:\DownloadsInD\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

website = "https://pamplin.vt.edu/directory.html"

driver.get(website)
posts = driver.find_elements_by_class_name("h3")
for post in posts:
    print(post.text)

emails = driver.find_elements_by_partial_link_text("@vt.edu")
for email in emails:
    print(email.text)




import xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet("Sheet 1")


for iteration, post in enumerate(posts):
    sheet1.write(iteration, 0, "post.text")

for iteration, email in enumerate(emails):
    sheet1.write(iteration, 1, "email.text")

wb.save('VTprofessorsStaff')


print("Finished")



