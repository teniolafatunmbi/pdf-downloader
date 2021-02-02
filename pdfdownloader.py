#A PDF downloader script in python.
#Written by Omoteniola-dev
'''Usage:
1. Copy the URL to the page you want to download from
2. Launch the script from directory you intend to save your pdfs(If you know some python, and intend to
use command line, run the script from the directory you want)
3. Wait until the download is finished(depending on your internet connection and the size of the files). It is
advisable to leave the window opened until the execution finishes.
'''

import requests, sys, pyperclip, os, bs4


def download(url):
    #Open the URL
    try:
        res = requests.get(url)
    #If request is not successful, end this script launch
    except:
        exit()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    link = soup.select('a[href$=".pdf"]') #selecting the <a> tags whose 'href' has the .pdf extension 
    num_link = len(link)
    try:
        download = os.makedirs("Pdf download")
        os.chdir("Pdf download")
    except FileExistsError:
        download = os.chdir("Pdf download")
    for i in range(num_link):
        pdfs = requests.get("https://ocw.mit.edu"+link[i].get('href'))
        name = link[i].getText() #Gets the element the selected anchor tags
        pdfs.raise_for_status() #raises and error if requests is not successful

        print("downloading {}".format(name))
        for i in range(num_link): 
            with open("{}.pdf".format(name), "wb") as save:
                save.write(pdfs.content) #write the content of the pdf to a pdf file
            save.close()
    
#The launch function to launch this script
def launch():  
    if len(sys.argv) > 1:
        url = sys.argv
        download(url)
    else: 
        url = pyperclip.paste()
        download(url)
launch()

#Thanks for viewing :)