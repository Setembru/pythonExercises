from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

driver.find_element_by_xpath('//*[@id="u_0_2"]').click()

driver.find_element_by_xpath('//*[@id="u_5_b"]').send_keys("Claus Albertinho")
driver.find_element_by_xpath('//*[@id="u_b_d"]').send_keys("Bienemann")  
driver.find_element_by_xpath('//*[@id="u_b_g"]').send_keys("niccolo.marlowe@auweek.net")  
driver.find_element_by_xpath('//*[@id="password_step_input"]').send_keys("Gunterzinho1234@a")

driver.find_element_by_xpath('//*[@id="day"]').send_keys("1")
driver.find_element_by_xpath('//*[@id="month"]').send_keys("out")
driver.find_element_by_xpath('//*[@id="year"]').send_keys("2001")

driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div[1]/div/div[1]/form/div[1]/div[7]/span/span[2]/label').click()

driver.find_element_by_xpath('//*[@id="u_b_s"]').click()