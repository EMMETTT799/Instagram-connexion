from selenium import webdriver
import pyautogui, time
from selenium.webdriver.common.keys import Keys
#############################################################
pseudo = input("Entrez votre adresse mail de connexion (ou pseudo):")
time.sleep(10)
####################################################################
mdp = input("Entrez votre mots de passe de connexion:")
time.sleep(20)
##############################################
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.instagram.com/accounts/login/")
print(driver.current_url, 'et voila le travail')
time.sleep(6)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').click()
pyautogui.write(pseudo, interval=0.25)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').click()
pyautogui.write(mdp, interval=0.25)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
