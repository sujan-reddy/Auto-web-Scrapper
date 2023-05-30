import time, datetime, os, subprocess,sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from usnlists import usn_list
from threading import *
# from datelist import date_list_chunks

options= webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
# options.add_argument('--headless')
# options.add_argument('window-size=1920x1080')
# options.headless=True

# prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2, 
#                     'plugins': 2, 'popups': 2, 'geolocation': 2, 
#                     'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
#                     'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
#                     'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
#                     'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
#                     'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
#                     'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
#                     'durable_storage': 2}}
# options.add_experimental_option('prefs', prefs)

# options.add_argument("disable-infobars")
# options.add_argument("--disable-extensions")


# 1GA22AM032-T 18042004
driver=webdriver.Chrome(options=options)


driver.get('https://global.contineo.in/sims/')

# time.sleep(5)

usnbox=driver.find_element('xpath','//*[@id="myInput"]')
usnbox.send_keys('1GA22AM032-T')
time.sleep(0.1)


dob_box=driver.find_element('xpath','//*[@id="mypass"]')  
dob_box.send_keys('18042004')
time.sleep(0.1)

    
loginbutton=driver.find_element('xpath','//*[@id="form-login"]/div[3]/div[1]/span[3]/button')
loginbutton.click()

profilebutton=driver.find_element('xpath','//*[@id="page-header"]/table/tbody/tr/td[2]/ul/li[2]/a')
profilebutton.click()


with open("test.html", "w+") as f:
    f.write(driver.page_source)

            # subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

# threadlist=[]
# for usn_block in usn_list:
#     for usn in usn_block:    
#         if(continous_invalid>3):
#             print('end of this list')
#             break
#         path='Pthon scraper /TEXTFILES/'+usn[5:7]+'/21/'+str(usn)+'.txt'
#         Found=False
#         if(os.path.exists(path)):
#             continue
#         for small_chunks in date_list_chunks:
#             for dob in small_chunks:
#                 threads=Thread(target=run_test_on,args=(usn,dob))
#                 threads.start()
#                 threadlist.append(threads)
#             for thread in threadlist:
#                 thread.join()
        
#             print('thread list complete')
#             threadlist=[]
#         print('all combinations checked')
#         if(not os.path.exists(path)):
#             with open(path,'w+') as answer_file:
#                 answer_file.write(str(usn)+' '+'null')
#                 continous_invalid+=1
#                 file=open('notvalid.txt','a+')
#                 file.write(str(usn)+'\n')

# # os.system('poweroff')