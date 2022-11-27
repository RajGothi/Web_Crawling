from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os

chrome_driver_path="F:\\Code\\DAP Lab\\venv\\chromedriver.exe"
audio_input_path='F:\\Code\\DAP Lab\\venv\\audio_input.txt'
audio_stored_folder_path='F:\\Code\\DAP Lab\\audio'

def download(first_audio,filename):
    # print("in")
    current_audio= first_audio.get_attribute('src')
    # print("out")
    # print(current_audio)
    doc = requests.get(current_audio)
    source=os.path.join(audio_stored_folder_path,filename)

    with open(source, 'wb') as f:
        f.write(doc.content)

def input_data():

    file = open(audio_input_path, 'r')
    Lines = file.readlines()
    
    # Strips the newline character
    for i in range(6):
        Lines[i]=Lines[i].strip()
        # print(Lines[i])
        
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

def all_audio():
    
    wait = WebDriverWait(driver, 10)
    no_of_page=wait.until(EC.element_to_be_clickable((By.ID,'ctl00_ContentPlaceHolder1_lblpage')))
    print(no_of_page.text)
    string=no_of_page.text
    ind=string.rindex(' ')
    digit=int(string[ind+1:])
    # print(int(digit))

    for j in range(digit):
        # print("in")

        for i in range(0,100000):
            audio_ID=f"ctl00_ContentPlaceHolder1_RepterDetails_ctl{i}_audio_player"
            date_ID=f"ctl00_ContentPlaceHolder1_RepterDetails_ctl{i}_HyperLink2"
            if i<10:
                audio_ID=f"ctl00_ContentPlaceHolder1_RepterDetails_ctl0{i}_audio_player"   
                date_ID=f"ctl00_ContentPlaceHolder1_RepterDetails_ctl0{i}_HyperLink2" 

            print(i)
            try:
                current_audio=wait.until(EC.element_to_be_clickable((By.ID,audio_ID)))
                current_date=wait.until(EC.element_to_be_clickable((By.ID,date_ID)))
            except:
                break
            else:
                download(current_audio,current_date.text)

        if j!=digit-1:
            next=wait.until(EC.element_to_be_clickable((By.ID,"ctl00_ContentPlaceHolder1_lbNext")))
            next.send_keys("\n")

if __name__ == "__main__":

    print("started")

    ser = Service(chrome_driver_path)
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)

    # driver = webdriver.Chrome("chromedriver.exe")
    #driver=webdriver.firefox()
    #driver=webdriver.ie()
    #maximize the window size
    driver.maximize_window()

    #navigate to the url
    driver.get("https://newsonair.gov.in/RNU-NSD-Audio-Archive-Search.aspx")

    audio=driver.find_element("id","ctl00_ContentPlaceHolder1_program_type_cbl_0")
    # text=driver.find_element("id","ctl00_ContentPlaceHolder1_program_type_cbl_1")

    audio.click()
    print("audio button selected")

    wait = WebDriverWait(driver, 10)

    input_data()

    #click find button    
    find=wait.until(EC.element_to_be_clickable((By.ID,"ctl00_ContentPlaceHolder1_Button1")))
    find.click()

    all_audio()

    #close the browser
    # driver.close()  #close the parrent window

    # driver.quit() #close all the window
    print("successfully completed")
