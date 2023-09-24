from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome("chromedriver.exe")

url = "https://aykome.mersin.bel.tr"

driver.get(url)
driver.maximize_window()

time.sleep(2)

user_name = driver.find_element(By.NAME,'paydas')
password = driver.find_element(By.NAME,'pswrd')




user_name.send_keys("18862")
password.send_keys("Aykome123*")

giris= driver.find_element(By.XPATH,"//*[@id='login-form']/input[3]")
giris.click()

time.sleep(3)

kurumOnylari= driver.find_element(By.XPATH,"//*[@id='heading_aykome_basvuru_onay']/h4")
kurumOnylari.click()
time.sleep(3)
onayBekliyenler= driver.find_element(By.XPATH,"//*[@id='kazi-onay-panel']/td[1]/input")
onayBekliyenler.click()
time.sleep(3)

onayTiki= driver.find_element(By.XPATH,"//*[@id='143205']/td[18]/i")
onayTiki.click()

time.sleep(5)
#window_after= driver.window_handles[0]
switch_to = driver.switch_to
iframe_element = driver.find_element(By.XPATH,"//*[@id='basvuru-frame']")
switch_to.frame(iframe_element)
onaylayanAdi= driver.find_element(By.XPATH,"//*[@id='view1:form1:onaylayanadi']")
onaylayanAdi.click()
onaylayanAdi.send_keys("Osman")
onaylayanSoyadi= driver.find_element(By.XPATH,"//*[@id='view1:form1:onaylayansoyadi']")
onaylayanSoyadi.click()
onaylayanSoyadi.send_keys("ŞEN")


time.sleep(10)


 


time.sleep(3)



