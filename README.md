# Web_Crawling

Requirements:

Python Library:
Selenium,
os,
requests,
time,

Before running the program,
In audio.py and transcript.py has path variable that need to change accordingly.

ex. of transcript.py
chrome_driver_path="F:\\Code\\DAP Lab\\venv\\chromedriver.exe"   (chrome driver I have attached above.)
transcript_input_path='F:\\Code\\DAP Lab\\venv\\transcript_input.txt' (Transcipt input text file)
transcript_pdf_path = 'F:\Code\DAP Lab\Text' (Folder location, Where we want to store the pdfs)

ex. of audio.py
chrome_driver_path="F:\\Code\\DAP Lab\\venv\\chromedriver.exe"  
audio_input_path='F:\\Code\\DAP Lab\\venv\\audio_input.txt' (audio input text file)
audio_stored_folder_path='F:\\Code\\DAP Lab\\audio' (Folder location, Where we want to store the audio files)

At the end of program, It will show successfully completed otherwise some error occurred.  
