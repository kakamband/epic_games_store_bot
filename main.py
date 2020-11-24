from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from glist import Glist

CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google-chrome'

#GOOGLE_CHROME_BIN = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
#CHROMEDRIVER_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

gChromeOptions = webdriver.ChromeOptions()
gChromeOptions.binary_location = GOOGLE_CHROME_BIN
gChromeOptions.add_argument('--disable-gpu')
gChromeOptions.add_argument('--no-sandbox')


class Bot:
    def __init__(self):
        pass

    def check_if_element(self, browser, xpath):
        try:
            browser.find_element_by_xpath(xpath)
            return True
        except NoSuchElementException:
            return False

    def main(self):
        new_list = Glist().check()

        if new_list:

            for i in new_list:
                
                if i['state'] == 'available':
                
                    browser = webdriver.Chrome(chrome_options=gChromeOptions, executable_path=CHROMEDRIVER_PATH)
                
                    wait = WebDriverWait(browser, 10)
                    try:
                        browser.get(i['url'])
                    
                        browser.implicitly_wait(5)

                        try:
                            browser.find_element_by_xpath('//button[@class="css-19tmzba"]').click()
                    
                        except:
                            pass
                
                        getbtn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="purchase-cta-button"]')))
                        getbtn.click()
                
                        main_page = browser.current_window_handle 
                
                        wait.until(EC.element_to_be_clickable((By.ID, 'login-with-xbl'))).click()                       
                
                        browser.switch_to.window(browser.window_handles[1])                                             
                
                        username = wait.until(EC.presence_of_element_located((By.NAME, 'loginfmt')))                
                        username.send_keys('#your_email')                                                  
                        username.send_keys(Keys.ENTER)                                                  
                
                        password = wait.until(EC.presence_of_element_located((By.NAME, 'passwd')))      
                        password.send_keys('#your_password')                                              
                
                        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Sign in"]'))).click()
                    
                        try:
                            browser.implicitly_wait(5)
                            browser.find_element_by_xpath('//input[@value="No"]').click()
                    
                        except:
                            pass
                    
                        browser.switch_to.window(main_page)
                
                        browser.implicitly_wait(20)

                        if self.check_if_element(browser=browser, xpath='//button[@data-testid="purchase-cta-button"][@disabled]') \
                        and not self.check_if_element(browser=browser, xpath='//button[@class="btn btn-primary"]'):
                            Glist().owned(i['title'], i)
                    
                        else:
                            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary"]'))).click()
                            
                            browser,implicitly_wait(10)

                            wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), {}) and @data-component="Message"]'.format("Thank you for buying"))))
                            browser.implicitly_wait(5)
                        
                            Glist().owned(i['title'], i)
                            print('Purchased {}'.format(i['title']))
                            
                        browser.quit()

                    except Exception as e:
                        browser.quit()
                        print('error 111: ')
                        print(e)
                else:
                    print(str(i['title']) + ' - Coming_soon( {} )'.format(i['start_date']))
    
        else:
            print('all_caught_up!!!')

