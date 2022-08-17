# Scrape

# import pip3 install selenium/bs4/chromedriver/lsl/lxml parser


#https://www.pythonfixing.com/2021/11/fixed-beautifulsoupgettext-ignoring.html
#https://beautiful-soup-4.readthedocs.io/en/latest/
#https://www.bestproxyreviews.com/how-to-scrape-linkedin-using-proxies/
#https://phantombuster.com/blog/guides/linkedin-automation-rate-limits-2021-edition-5pFlkXZFjtku79DltwBF0M


from datetime import *
import time 
from threading import Thread 
import os,random,sys,time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class RandomThread(Thread): 
    """We'd like to keep track of the thread number, so the main 
       program passes it in when creating the thread, and thread 
       takes note of its number in self.num 
    """ 
    def __init__(self, num,lst,group,batchnum): 
        super().__init__() # Must call __init__() in the Thread class 
        self.num = num 
        self.lst = lst
        self.group=group
        self.batchnum=batchnum
        self.jobrun_list=[]
        # initiate variables
 
    def run(self): 
        jobrun_cnt=0
        next_Sleep_Step=3
        next_Sleep=jobrun_cnt+next_Sleep_Step
        browser=self.Login() 
        for profile in self.lst:

            #print("Running scrape for profile ",profile ,"on thread", self.num)  
            self.ScrapeProfile(profile+"/",browser) 
            #self.jobrun_list.append(self.lst)  
         
        if jobrun_cnt>next_Sleep:
            next_Sleep=next_Sleep+next_Sleep_Step
            time.sleep(5)
            #print(self.num," Slept for 3 sec")
           
        #print(self.num,"-->", jobrun_cnt)
    def Login(self):


        #print("Scrape started for ------"+profileURL)
        #print("-------- second login -------------")
        op = webdriver.ChromeOptions()
        op.add_argument("--incognito")
        #op.add_argument('headless')
        s = Service("C:\\Users\\ravip\\Downloads\\chromedriver_win32\\chromedriver.exe")
        #driver = webdriver.Chrome(service=s)
        browser=webdriver.Chrome(service=s,options=op)
        #browser.implicitly_wait(5)
        
        browser.get('https://www.linkedin.com/uas/login')
        username='testlink1729@gmail.com'
        password='T5stl!nk@1729!'

        elementID=browser.find_element(By.ID,'username')
        elementID.send_keys(username)
        elementID=browser.find_element(By.ID,'password')
        elementID.send_keys(password)
        elementID.submit()
        time.sleep(60)
        return browser

    def ScrapeProfile(self,profileURL,browser):

        """
        #print("Scrape started for ------"+profileURL)
        #print("-------- second login -------------")
        op = webdriver.ChromeOptions()
        op.add_argument("--incognito")
        #op.add_argument('headless')
        s = Service("C:\\Users\\ravip\\Downloads\\chromedriver_win32\\chromedriver.exe")
        #driver = webdriver.Chrome(service=s)
        browser=webdriver.Chrome(service=s,options=op)
        #browser.implicitly_wait(5)
    
         
        browser.get('https://www.linkedin.com/uas/login')
        username='testlink1729@gmail.com'
        password='T5stl!nk@1729!'

        elementID=browser.find_element(By.ID,'username')
        elementID.send_keys(username)
        elementID=browser.find_element(By.ID,'password')
        elementID.send_keys(password)
        elementID.submit()
        return bowser
        #WebDriverWait(browser,5)
        
        time.sleep(30)
        """
        #print("Success till submit")
        #ExpectedOutput of profile
        name=None
        title=None
        CurrentInfo_Company=None
        CurrentInfo_Education=None
        contact_info_output_list=[]
        Experience_output_list=[]
        Skills_output_list=[]


        #print("*************************** B A S E   P R O F I L E    D E T A I L S*******************************************")
        looplist=[profileURL]
        browser.maximize_window()
        for profile in looplist:
            fullLink=profile
            browser.get(fullLink)
            time.sleep(10)
            
            SCROLL_PAUSE_TIME = 3
            
            
            last_height=browser.execute_script("return document.body.scrollHeight")


            for i in range(3):
                browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(SCROLL_PAUSE_TIME)
                new_height=browser.execute_script("return document.body.scrollHeight")
                if(new_height==last_height):
                    break
                last_height=new_height

            src=browser.page_source
            soup=BeautifulSoup(src,'lxml')

            intro_div=soup.find('div',{'class':'mt2 relative'})
            if intro_div is not None:
                #print(intro_div)
                #intro_div_soup=BeautifulSoup(intro_div,'lxml')
                #intro_div=soup.find('div',{'class':'flex-1 mr5'})
                #name_loc=intro_div.find_all('ul')
                name=intro_div.find('h1',{'class':'text-heading-xlarge inline t-24 v-align-middle break-words'})
                if name is not None:
                    #print("------------------------name is not none")
                    name=name.get_text().strip()
                else:
                    print("name is none")

                
                title=intro_div.find('div',{'class':'text-body-medium break-words'})
                if title is not None:
                    title=title.get_text().strip()

                #CurrentInfo=intro_div.find('h2',{'class':"pv-text-details__right-panel-item-text hoverable-link-text break-words text-body-small inline"})
                CurrentInfo_Company=intro_div.find('div',{'aria-label':"Current company"})
                if CurrentInfo_Company is not None:
                    CurrentInfo_Company=CurrentInfo_Company.get_text().strip()
                
                CurrentInfo_Education=intro_div.find('div',{'aria-label':"Education"})
                if CurrentInfo_Education is not None:
                    CurrentInfo_Education=CurrentInfo_Education.get_text().strip()
                #print('{} *** {} *** {} *** {} ***  *** '.format(name,title,CurrentInfo_Company,CurrentInfo_Education))
        time.sleep(3)  
            
        #print("***************************C O N T A C T    D E T A I L S*******************************************")
        
        contact_info=profileURL+'overlay/contact-info/'
        browser.get(contact_info)

        last_height=browser.execute_script("return document.body.scrollHeight")


        for i in range(3):
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height=browser.execute_script("return document.body.scrollHeight")
            if(new_height==last_height):
                break
            last_height=new_height

        src=browser.page_source
        soup=BeautifulSoup(src,'lxml')
        #print(soup)
        contact_parent=soup.select("section[class*=pv-contact-info__contact-type]") #find_all("div", id=re.compile("^pv-contact-info__contact-type")) #soup.find_all('li',{'class':'pv-profile-section__section-info section-info'})
        #print(contact_parent)
        #print("**********************************************************************")
        #print(soup.find('section',{'class':'pv-profile-section pv-contact-info artdeco-container-card'}) )
        
        for x in contact_parent[0:]:
                
                

                alltext=x.get_text("**").split('\n')
                #print(alltext)
                contact_info_output = [item.split('**') for item in alltext] 
                contact_info_output = [item[1].strip() if len(item)>2 else item[0].strip() for item in contact_info_output] 
                contact_info_output = list(filter(None, contact_info_output))
                contact_info_output_list.append(contact_info_output) #print(contact_info_output)

        #print("***************************E X P E R I E N C E    D E T A I L S*******************************************")
        time.sleep(3)
        looplist=[profileURL+'details/experience/']
        for profile in looplist:
            fullLink=profile
            browser.get(fullLink)

            SCROLL_PAUSE_TIME = 3
            last_height=browser.execute_script("return document.body.scrollHeight")


            for i in range(3):
                browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(SCROLL_PAUSE_TIME)
                new_height=browser.execute_script("return document.body.scrollHeight")
                if(new_height==last_height):
                    break
                last_height=new_height

            src=browser.page_source
            soup=BeautifulSoup(src,'lxml')

            
            ###########
            Experience_parent=soup.find_all('li',{'class':'pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated'})
            for x in Experience_parent[0:]:
                
                

                alltext=x.get_text("**").split('\n')
                Experience_output = [item.split('**') for item in alltext] 
                Experience_output = [item[1].strip() if len(item)>2 else '' for item in Experience_output] 
                Experience_output = list(filter(None, Experience_output))
                Experience_output_list.append(Experience_output)
                #print(Experience_output)
                

        
        #print("***************************S K I L L S    D E T A I L S*******************************************")
        time.sleep(3)
        contact_info=profileURL+'details/skills/'
        browser.get(contact_info)
        last_height=browser.execute_script("return document.body.scrollHeight")


        for i in range(3):
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height=browser.execute_script("return document.body.scrollHeight")
            if(new_height==last_height):
                break
            last_height=new_height
        src=browser.page_source
        soup=BeautifulSoup(src,'lxml')
        #print(soup)
        skill_parent=soup.find_all('div',{'class':'display-flex flex-column full-width align-self-center'})
        #print(contact_parent)
        #print("**********************************************************************")
        #print(soup.find('section',{'class':'pv-profile-section pv-contact-info artdeco-container-card'}) )
        for x in skill_parent[0:]:
                
                #print("**********************************************************************")

                alltext=x.get_text("**").split('\n')
                Skills_output = [item.split('**') for item in alltext] 
                Skills_output = [item[1].strip() if len(item)>2 else '' for item in Skills_output] 
                Skills_output = list(filter(None, Skills_output))
                Skills_output_list.append(Skills_output)
                #print(Skills_output)
                #print("**********************************************************************")
        """
        print('({} , {} , {} , {})  '.format(name,title,CurrentInfo_Company,CurrentInfo_Education))
        print(contact_info_output) 
        print(Experience_output) 
        print(Skills_output)
        """
        tup=(profileURL,name,title,CurrentInfo_Company,CurrentInfo_Education,contact_info_output_list,Experience_output_list,Skills_output_list)    
        self.jobrun_list.append(tup)

def GetURLList(Searchargs):

        
    op = webdriver.ChromeOptions()
    
    op.add_argument('headless')
    s = Service("C:\\Users\\ravip\\Downloads\\chromedriver_win32\\chromedriver.exe")
        #driver = webdriver.Chrome(service=s)
    browser=webdriver.Chrome(service=s,options=op)
    #browser.implicitly_wait(5)

    browser.get('https://www.linkedin.com/uas/login')
    #username='testlink1729@gmail.com'
    #password='T5stl!nk@1729'
    username=''
    password=''
    elementID=browser.find_element(By.ID,'username')
    elementID.send_keys(username)
    elementID=browser.find_element(By.ID,'password')
    elementID.send_keys(password)
    elementID.submit()

    
    looplist=[]
    for pagenum in range(1,50):
        time_stamp = time.time()
        date_time = datetime.fromtimestamp(time_stamp)
        
        fullLink="https://www.linkedin.com/search/results/people/?keywords="+searchconcat+"&page="+str(pagenum)
        print(pagenum,date_time,fullLink)

        #ph0 pv2 artdeco-card mb2
        browser.get(fullLink)


        SCROLL_PAUSE_TIME = 3
        last_height=browser.execute_script("return document.body.scrollHeight")


        for i in range(3):
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height=browser.execute_script("return document.body.scrollHeight")
            if(new_height==last_height):
                break
            last_height=new_height

        src=browser.page_source
        soup=BeautifulSoup(src,'lxml')
        #print(soup)

        intro_div=soup.find('div',{'class':'ph0 pv2 artdeco-card mb2'})
        if intro_div is not None:
            name_list=intro_div.find_all('a',{'class':'app-aware-link'})
            #print(name_list)
            urllist=[]
            for name in name_list:
                #print("**********************************************************************")
                #print (name)
                urllist.append(name['href'])
            #print(urllist)
            looplist_in = (list(set(urllist)))
            #print("**********************************************************************")
            #print(looplist_in)
            #print("**********************************************************************")
            looplist_in = [item.split('?')[0] for item in looplist_in] 
            #print(looplist_in)
            #print("**********************************************************************")
            print("*************************** P R O F I L E S  T O  S C R A P E *******************************************",len(looplist_in))
            looplist.extend(looplist_in)
            with open(r'C:\\Users\\ravip\\Downloads\\Python\\URLList.txt', 'a') as fp:
                for url in looplist_in:
                    # write each item on a new line
                    fp.write("%s\n" % url)
            ##print('Done')

            
        else:
            #print("*************************** P R O F I L E S  T O  S C R A P E *******************************************")
            print("nothing found")
            #looplist=[]
        #print(fullLink,"<-------------------->")

    return looplist
            
    
    #print(Experience_parent)

searchwordslist=["singapore","reactjs"]
searchconcat=""
for word in searchwordslist:
    searchconcat+=word+"%20"
full_URL_list=[]
#full_URL_list=GetURLList(searchconcat)
#print(full_URL_list)

with open('C:\\Users\\ravip\\Downloads\\Python\\URLList.txt', 'r') as fp:
    Lines = fp.readlines()
  
    count = 0
    # Strips the newline character
    for line in Lines:
        full_URL_list.append(line.strip())
full_URL_list=full_URL_list[0:10]
#print(full_URL_list)
#full_URL_list=['https://www.linkedin.com/in/sudharsan-kesavanarayanan-75b2bbb', 'https://www.linkedin.com/in/imkarthekeyan']#, 'https://www.linkedin.com/in/ACoAAAVS9tEBYaiGGIwdi9Tc14Oe-3w6qukwQMA', 'https://www.linkedin.com/in/sardanalokesh', 'https://www.linkedin.com/in/ACoAAAU2-9sBIQB901M3UBW9CDf8yYXZyAAvAIk', 'https://www.linkedin.com/in/mary-ruth-diolas-8467bb164', 'https://www.linkedin.com/in/ACoAAAuSUD0BYbORbvsFtB31Jo-JyooB7cn4SFo', 'https://www.linkedin.com/in/ACoAAAPcdwkBFAheoZHB99T84NG-kgcRWs39AQo', 'https://www.linkedin.com/in/ACoAAADOzSABDamYZX4SDAzzawQoKY6mSKUFP9I', 'https://www.linkedin.com/in/manvita-syreddy', 'https://www.linkedin.com/in/teemingchew', 'https://www.linkedin.com/in/dickson-tan', 'https://www.linkedin.com/in/ritikbhatia', 'https://www.linkedin.com/in/ajeetbhatnagar', 'https://www.linkedin.com/in/abhishekpradeepmishra']
group="Random"
groupcnt=0
jobs_in_one_batch=100
number_of_threads=5
jobs_in_one_thread=int(jobs_in_one_batch/ number_of_threads  )
tnum=0
start = 0
end = len(full_URL_list)
ctr=0
time_stamp = time.time()
trunc_start_date_time = datetime.fromtimestamp(time_stamp)
#print("Started",trunc_start_date_time,"number of profiles in ",group," -->",end )
for i in range(start, end, jobs_in_one_batch):
    groupcnt+=1     
    trunc_list_start=i
    trunc_list_end=trunc_list_start+jobs_in_one_batch
    
    trunc_list=full_URL_list[trunc_list_start:trunc_list_start+jobs_in_one_batch]
    #print(trunc_list)
    
    
    threads=[]
    for j in range(trunc_list_start, trunc_list_end, jobs_in_one_thread):
        tnum=tnum+1
        sub_list_start = j
        #print("                ",trunc_list[sub_list_start-trunc_list_start:sub_list_start-trunc_list_start+jobs_in_one_thread],sub_list_start-trunc_list_start,sub_list_start-trunc_list_start+jobs_in_one_thread)
        sub_list=trunc_list[sub_list_start-trunc_list_start:sub_list_start-trunc_list_start+jobs_in_one_thread]
        threads.append(RandomThread(tnum,sub_list,group,trunc_list_start))
        
    time_stamp = time.time()
    start_date_time = datetime.fromtimestamp(time_stamp)
    
    # Start all the threads here 
    for thread in threads: 
        thread.start() 

    finallist=[]
    # The Thread.join() method will block unless the thread has completed 
    for thread in threads: 
        thread.join() 
        finallist.extend(thread.jobrun_list)
    #print(finallist)
    
    
    #print('All threads completed') 
    time_stamp = time.time()
    end_date_time = datetime.fromtimestamp(time_stamp)
    
    print("     Details --> ",group,number_of_threads,trunc_list_start,trunc_list_end,start_date_time, end_date_time)
    header=["profileURL","name","title","CurrentInfo_Company","CurrentInfo_Education","contact_info_output","Experience_output","Skills_output"]
    df = pd.DataFrame(finallist)
    if(groupcnt == 1):
        df.to_csv('C:\\Users\\ravip\\Downloads\\Python\\Fileoutput.csv', index=False, header=header, encoding="utf-8") 
    else:
        df.to_csv('C:\\Users\\ravip\\Downloads\\Python\\Fileoutput.csv', index=False, header=False,mode='a', encoding="utf-8") 


