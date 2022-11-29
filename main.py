from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configparser import ConfigParser
import requests
import os

configFilePath = r'F:\Code\DAP Lab\venv\config.ini'
configur = ConfigParser()
configur.read('config.ini')

chrome_driver_path=configur.get('path','chrome_driver_path')
input_path=configur.get('path','input_path')
main_directory_path=configur.get('path','main_directory_path')
file = open(input_path, 'r')
Lines = file.readlines()

# chrome_driver_path="F:\\Code\\DAP Lab\\venv\\chromedriver.exe"
# input_path='F:\\Code\\DAP Lab\\venv\\input.txt'
# main_directory_path="F:\\Code\\DAP Lab\\venv"

for i in range(6):
    Lines[i]=Lines[i].strip()

Smonth=Lines[4][:2]
Sdate=Lines[4][3:5]
Syear=Lines[4][6:10]

Emonth=Lines[5][:2]
Edate=Lines[5][3:5]
Eyear=Lines[5][6:10]

folder_name=Smonth+"_"+Sdate+"_"+Syear+"_to_"+Emonth+"_"+Edate+"_"+Eyear+"__"+Lines[2]
audio_stored_folder_path = os.path.join(main_directory_path, f"audio_{folder_name}")
print(audio_stored_folder_path)
transcript_pdf_path = os.path.join(main_directory_path, f"transcript_{folder_name}")

def make_folder(path,name):
    try:
        os.makedirs(path, exist_ok = True)
        print(f"{name} Directory created successfully")
    except OSError as error:
        print(f"{name} Directory can not be created")

#audio
def download_audio(first_audio,filename):
    # print("in")
    current_audio= first_audio.get_attribute('src')
    # print("out")
    # print(current_audio)
    doc = requests.get(current_audio)
    source=os.path.join(audio_stored_folder_path,filename)

    with open(source, 'wb') as f:
        f.write(doc.content)

#transcript
def download_text(first_text):

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
                download_audio(current_audio,current_date.text)
            except:
                break

        if j!=digit-1:
            next=wait.until(EC.element_to_be_clickable((By.ID,"ctl00_ContentPlaceHolder1_lbNext")))
            next.send_keys("\n")

def all_text():
    
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
                download_text(current_text)
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

    make_folder(audio_stored_folder_path,"audio")

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

    print("ALL audio file downloaded")

    print("Transcript crawler started")

    make_folder(transcript_pdf_path,"Transcript")

    op.add_experimental_option("prefs",{"download.default_directory":transcript_pdf_path})
    new_driver = webdriver.Chrome(service=ser, options=op)
    new_driver.maximize_window()
    new_driver.get("https://newsonair.gov.in/RNU-NSD-Audio-Archive-Search.aspx")

    text=new_driver.find_element("id","ctl00_ContentPlaceHolder1_program_type_cbl_1")

    text.click()
    print("text button selected")
    
    wait = WebDriverWait(new_driver, 10)

    input_data()

    #click find button    
    find=wait.until(EC.element_to_be_clickable((By.ID,"ctl00_ContentPlaceHolder1_Button1")))
    find.click()
    
    all_text()

    file_name_change()

    print("ALL Transcript downloaded")
    new_driver.close()  #close the parrent window
    driver.close()

    print("successfully completed")

