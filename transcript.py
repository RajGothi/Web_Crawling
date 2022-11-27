import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

chrome_driver_path="F:\\Code\\DAP Lab\\venv\\chromedriver.exe"
transcript_input_path='F:\\Code\\DAP Lab\\venv\\transcript_input.txt'
transcript_pdf_path = 'F:\Code\DAP Lab\Text'

file = open(transcript_input_path, 'r')
Lines = file.readlines()

for i in range(6):
    Lines[i]=Lines[i].strip()
    # print(Lines[i])    

def download(first_text,filename):

    first_text.send_keys("\n")
    # time.sleep(1)

def input_data():
        
    RNU_NSD_Type = wait.until(EC.element_to_be_clickable((By.ID,"ctl00_ContentPlaceHolder1_ddwtype")))
    dropdown=Select(RNU_NSD_Type)
    dropdown.select_by_visible_text(Lines[0])
    # RNU_NSD_Type.send_keys("Regional")
    print("set ",Lines[0])
    # time.sleep(5)

    RNU_NSD_Name = wait.until(EC.element_to_be_clickable((By.ID,"ctl00_ContentPlaceHolder1_ddwrnunsdname")))
    dropdown=Select(RNU_NSD_Name)
    dropdown.select_by_visible_text(Lines[1])
    # element.send_keys("RNU2")
    print("set ",Lines[1])

    RNU_NSD_Language_Name = wait.until(EC.element_to_be_clickable((By.ID,"ctl00_ContentPlaceHolder1_ddwlanguages")))
    dropdown=Select(RNU_NSD_Language_Name)
    dropdown.select_by_visible_text(Lines[2])
    print("set ",Lines[2])

    RNU_NSD_Bulletin_Name = wait.until(EC.element_to_be_clickable((By.ID,"ctl00_ContentPlaceHolder1_ddwrnunsd_bname")))
    dropdown=Select(RNU_NSD_Bulletin_Name)
    dropdown.select_by_visible_text(Lines[3])
    print("set ",Lines[3])

    Date_From = wait.until(EC.element_to_be_clickable((By.ID,"ctl00_ContentPlaceHolder1_from_Date_txt")))
    # dropdown=Select(element)
    Date_From.clear()
    Date_From.send_keys(Lines[4])
    print("set From ",Lines[4])

    Date_To = wait.until(EC.element_to_be_clickable((By.ID,"ctl00_ContentPlaceHolder1_to_Date_txt")))
    # dropdown=Select(element)
    Date_To.clear()
    Date_To.send_keys(Lines[5])
    print("set To ",Lines[5])

def all_text():
    
    wait = WebDriverWait(driver, 10)
    xpath="//*[@id='ctl00_ContentPlaceHolder1_GridView1']/tbody/tr[27]/td/table/tbody/tr"
    
    page=wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
    elementList = page.find_elements(By.TAG_NAME,"td")

    for j in range(len(elementList)):
        # print("in")

        for i in range(2,100000):
            bul_ID=f"ctl00_ContentPlaceHolder1_GridView1_ctl{i}_Label2"
            download_ID=f"ctl00_ContentPlaceHolder1_GridView1_ctl{i}_LinkButtonDownloadPdf"
            date_ID=f"ctl00_ContentPlaceHolder1_GridView1_ctl{i}_Label3"

            if i<10:
                bul_ID=f"ctl00_ContentPlaceHolder1_GridView1_ctl0{i}_Label2"
                download_ID=f"ctl00_ContentPlaceHolder1_GridView1_ctl0{i}_LinkButtonDownloadPdf"
                date_ID=f"ctl00_ContentPlaceHolder1_GridView1_ctl0{i}_Label3"

            print(i-2)
            
            try:
                
                bulletin=wait.until(EC.element_to_be_clickable((By.ID,bul_ID)))

                if not bulletin.text.startswith(Lines[3]):
                    continue

                current_text=wait.until(EC.element_to_be_clickable((By.ID,download_ID)))
                current_date=wait.until(EC.element_to_be_clickable((By.ID,date_ID)))
                download(current_text,current_date.text)
            except:
                break
            
        # next=wait.until(EC.element_to_be_clickable((By.ID,"ctl00_ContentPlaceHolder1_lbNext")))
        if j!=len(elementList)-1:
            page=wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
            elementList = page.find_elements(By.TAG_NAME,"td")
            elementList[j+1].find_elements(By.TAG_NAME,"a")[0].send_keys("\n")

def file_name_change():
    path=transcript_pdf_path
    os.chdir(path)

    filename = os.listdir()
    filename.sort()

    for i in range(len(filename)):
        ind=filename[i].index(Lines[3])
        new_name=filename[i][ind:]

        source=os.path.join(path,filename[i])
        dest=os.path.join(path,new_name)

        os.rename(source, dest)
  

if __name__ == "__main__":

    print("started")
    # chromeOptions=Options()
    # chromeOptions.add_experimental_option("pref",{"F:\\Code\\DAP Lab\\Text"})

    ser = Service(chrome_driver_path)
    op = webdriver.ChromeOptions()
    op.add_experimental_option("prefs",{"download.default_directory":transcript_pdf_path})
    driver = webdriver.Chrome(service=ser, options=op)

    # driver = webdriver.Chrome("chromedriver.exe")
    #driver=webdriver.firefox()
    #driver=webdriver.ie()
    #maximize the window size
    driver.maximize_window()

    #navigate to the url
    driver.get("https://newsonair.gov.in/RNU-NSD-Audio-Archive-Search.aspx")

    # audio=driver.find_element("id","ctl00_ContentPlaceHolder1_program_type_cbl_0")
    text=driver.find_element("id","ctl00_ContentPlaceHolder1_program_type_cbl_1")

    text.click()
    print("text button selected")

    wait = WebDriverWait(driver, 10)

    input_data()

    #click find button    
    find=wait.until(EC.element_to_be_clickable((By.ID,"ctl00_ContentPlaceHolder1_Button1")))
    find.click()

    
    all_text()

    file_name_change()

    #close the browser
    # driver.close()  #close the parrent window

    # driver.quit() #close all the window
    print("successfully completed")
