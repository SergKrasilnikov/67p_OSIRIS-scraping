import requests
from bs4 import BeautifulSoup
import os

# create the output folder
def make_dir():
    try:
        os.mkdir('output')
    except:
        print(f'Folder "output" already exist.')

# get the file list from the website
def files_list():
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        new_list = []
        for link in soup.find_all("a"):
            href = link.get("href")
            if href.endswith("/") or href.startswith("?"):
                continue
            new_list.append(href)
        print("List of files:")
        for file in new_list:
            print(file)
    else:
        print("Failed to fetch the file list.")

    return new_list

# download the data
def download_data(file_list):
    for filename in file_list:
        response = requests.get(url + filename)
        if response.status_code == 200:
            with open(os.path.join(os.getcwd(), 'output/') + filename, "wb") as file:
                file.write(response.content)
            print(rf"{filename} file downloaded successfully.")
        else:
            print(rf"Failed to download the file - {filename}.")


# change this link if you want to download the files from the different folders
url = "https://archives.esac.esa.int/psa/ftp/INTERNATIONAL-ROSETTA-MISSION/OSINAC/RO-C-OSINAC-4-PRL-67PCHURYUMOV-M05-V1.0/BROWSE/"

make_dir()
file_list = files_list()
download_data(file_list)
