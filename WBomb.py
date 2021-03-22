from selenium import webdriver  # pip install selenium
import time


def banner():
    print('''
		  ##              ##  =======     ####       ####    ####     =======
		  \ \    ####    / /  #      #  ##    ##    / /\ \  / /\ \    #      #
		   \ \  / /\ \  / /   #======   ##    ##   / /  \ \/ /  \ \   #====== 
		    \ \/ /  \ \/ /    #      #  ##    ##  / /    ####    \ \  #      #
		     ####    ####     =======     ####    ##              ##  =======
       
       +++WhatsApp Msg Bomb+++
       
       Edited by Elton Fungirai -- CryptoDog
       Email: xcryptocyber@gmail.com
       
		''')


def main(): 
    # First choose the browser you want to use and take note of its version so that
    # you can download the right version of the webdriver
    # Eg if you are using Chrome you must use webdriver.Chrome(path\to\chrome\webdriver.exe)        
    driver = webdriver.Edge(r"C:\Users\User\Downloads\edgedriver_win64\msedgedriver.exe")  # Change here
                                                                                           # Path to WebDriver located in Downloads which controls the browser 
                                                                                           # In this case Microsoft Edge is the browser
    driver.get('https://web.whatsapp.com/')

    name = input('Enter the Target name (Contact or Group): ')
    msg = input('Enter your message: ')
    count = int(input('Enter the Msg count: '))

    input('Enter any key after scanning QR code')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    # The classname of message box may vary.
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    for i in range(count):
        msg_box.send_keys(msg)
        # The classname of send button may vary.
        button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        button.click()
        time.sleep(1) # Increase or Decrease time delay, Zero means Instant bombing

    print('Bombing Complete!!')
    time.sleep(5)


banner()
main()
