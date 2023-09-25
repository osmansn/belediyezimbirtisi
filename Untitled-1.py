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

giris= driver.find_element(By.XPATH,"//*[contains(text(),'AYKOME Başvuru')]")
giris.click()
time.sleep(10)

kurumOnylari= driver.find_element(By.XPATH,"//*[@id='aykome_basvuru_onay_label']")
kurumOnylari.click()
time.sleep(3)
onayBekliyenler= driver.find_element(By.XPATH,"//*[@id='kazi-onay-panel']/td[1]/input")
onayBekliyenler.click()
time.sleep(3)

onayTiki= driver.find_element(By.XPATH,"(//i[@title='Onay'])[1]")
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


time.sleep(3)

tarih_icon= driver.find_element(By.XPATH,"//*[@id='view1:form1:tarih_onaytarihi']")
tarih_icon.click()
 
time.sleep(3)
tarih_icon2= driver.find_element(By.XPATH,"//*[@class='dpDayHighlightTD']")
tarih_icon2.click()
 

time.sleep(3)
soruisareti= driver.find_element(By.XPATH,"//*[@title='Listeden seçmek için tıklayınız...']")
soruisareti.click()


ana_pencere_kolu = driver.current_window_handle  # Ana pencerenin kolu
tum_pencereler = driver.window_handles         # Tüm pencerelerin listesi
yeni_pencere_kolu = None

# Ana pencerenin dışındaki pencerelerin kollarını bul
for pencere in tum_pencereler:
    if pencere != ana_pencere_kolu:
        yeni_pencere_kolu = pencere

# Yeni pencereye geçiş yap
driver.switch_to.window(yeni_pencere_kolu)


time.sleep(3)
onaylandi= driver.find_element(By.XPATH,"(//*[@name='selectOne'])[1]")
onaylandi.click()
time.sleep(3)
sec= driver.find_element(By.XPATH,"//*[@id='submitBTN']")
sec.click()
time.sleep(8)

driver.switch_to.window(ana_pencere_kolu)
time.sleep(3)

switch_to = driver.switch_to
iframe_element = driver.find_element(By.XPATH,"//*[@id='basvuru-frame']")
switch_to.frame(iframe_element)
time.sleep(3)
def doesElemntExist(xpath):
    try:
        print("arıyor")
        driver.find_element(By.XPATH,xpath)
        print("buldu")

        return True
    except:
        print("bulamadı")

        return False
basexpath_lokasyon="(//*[@class='dataTable']//*[@class='inputCompInactive' and (contains(@name,'lokasyon'))])[number]"
oburu="(//*[@class='selectOneMenuD'])[number]"
for i in range(1,50):
    lokasyonxpath=basexpath_lokasyon.replace("number",str(i))
    print(lokasyonxpath)
    if not doesElemntExist(lokasyonxpath):
        break
    lokasyon_text=driver.find_element(By.XPATH,lokasyonxpath).get_attribute("value")
    print(lokasyon_text)

    if lokasyonkayırlı:
        tıkla vars
    else:
        tıla yok

    break

