import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

def download_and_extract_file(url, extract_base_path, downloaded_files_path):
    zip_filename = url.split('/')[-1]
    
    folder_name = os.path.splitext(zip_filename)[0]
    extract_path = os.path.join(extract_base_path, folder_name)
    
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)
    
    response = requests.get(url)
    with open(os.path.join(extract_path, zip_filename), 'wb') as out_file:
        out_file.write(response.content)
    
    with ZipFile(os.path.join(extract_path, zip_filename), 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def check_if_downloaded(file_name, downloaded_files_path):
    if not os.path.exists(downloaded_files_path):
        return False
    
    with open(downloaded_files_path, 'r') as file:
        downloaded_files = [line.strip() for line in file.readlines()]
    return file_name in downloaded_files

def download_data(url, extract_base_path):
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    
    zip_links = soup.find_all('a', href=True)
    zip_links = [link['href'] for link in zip_links if link['href'].endswith('.zip')]
    
    for zip_link in zip_links:
        if not check_if_downloaded(zip_link, 'codes/download/downloaded_files.txt'):
            print(f"Herunterladen von {zip_link}")
            download_and_extract_file(zip_link, extract_base_path, 'codes/download/downloaded_files.txt')
            
            with open('codes/download/downloaded_files.txt', 'a') as file:
                file.write(zip_link + '\n')