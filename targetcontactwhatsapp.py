#C:\Users\ritsingh0\Downloads\chromedriver_win32

####this code is for sending messages to the targete group in a whatsapp 
####web automation


from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
  
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome(r'C:/Users/ritsingh0/Downloads/chromedriver_win32/chromedriver.exe') 
  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600)
print ("i m ok")
  
# Replace 'Friend's Name' with the name of your friend  
# or the name of a group  
target = '"Twilio"'
print ("i m ok")
# Replace the below string with your own message 
string = "I am Jarvis"
time.sleep(18);
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located(( 
    By.XPATH, x_arg)))
print(x_arg)

group_title.click()
print(group_title)
print ("i m ok")
#inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'
message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]


message.send_keys(string)

sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
sendbutton.click()
print ("i m ok")
##input_box = wait.until(EC.presence_of_element_located(( 
##    By.XPATH, inp_xpath)))
##print ("i love you")
##for i in range(2): 
##    input_box.send_keys("bgjk" + Keys.ENTER) 
##    time.sleep(1) 
