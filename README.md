# Web_Crawling

What does code do?

It crawl the website https://newsonair.gov.in/RNU-NSD-Audio-Archive-Search.aspx, To download the audio and transcript corresponding to given field value.

------------------------------------

Requirements:
Python Library: Selenium,
os,
requests,
time,
ConfigParser,
Google chrome

Chrome driver Extension file:
https://chromedriver.chromium.org/downloads
Based on the version of Chrome that is installed in the system, download corresponding driver and unzip in same directory as code with name 'chromedriver.exe'


-----------------------------------------------
->First user need to clone the repo
->Open config.ini file

chrome_driver_path= (here paste the path of chromedriver.exe that is attached with repo) 

input_path= (Paste the path of input.txt file from which code will read the 6 field value)

main_directory_path= (Paste the path, where above repo is cloned)

ex.

chrome_driver_path=F:\Code\DAP Lab\venv\chromedriver.exe

input_path=F:\Code\DAP Lab\venv\input.txt

main_directory_path=F:\Code\DAP Lab\venv

---------------------------------------------------

Input.txt File:
You can see that there are 6 field value that user need to enter to get audio and Transcript in the website.

1)RNU-NSD Type,2)RNU-NSD Name,3)RNU-NSD Language Name,4)RNU-NSD  Bulletin Name,5)Date from,6) Date to 
That 6 field value user need to write in input.txt file, line by line(not in same line).. (Repo contains the example of input.txt file)

Make sure that whatever value you written in input.txt file is valid(same to same as show in website).
(You can copy-paste the 6 field value in txt file.)

ex. Input.txt

Regional

Ahmedabad

Gujarati

1910

10/26/2022 8:10:15 PM

11/26/2022 8:10:15 PM

-------------------------------------------------
Now Run the Main.py file

Output of code:

Code will make 2 folder corresponding to audio and transcript

Audio folder contain the all downloaded audio and

Transcript folder contain the all downloaded transcript corresponding to input.txt file value.

-------------------------------------------
At the end of program, It will show successfully completed otherwise some error occurred.  

