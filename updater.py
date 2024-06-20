import os
import requests
import shutil
import subprocess

def download_file(url, dest_folder):
    print("Crimson Loader Updater")
    print("Wait 3-6 seconds for update")
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print("Making dir")
    
    local_filename = os.path.join(dest_folder, url.split('/')[-1])
    
    with requests.get(url, stream=True) as r:
        print("downloading...")
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    
    return local_filename

def open_file(filepath):
    if os.name == 'nt':
        os.startfile(filepath)
        print("opening...")

def main():
    url = "https://github.com/BrightCat14/crimson-loader/releases/download/Loader/crimson.loader.exe"
    appdata_folder = os.getenv('APPDATA')
    dest_folder = os.path.join(appdata_folder, 'crimson-loader')
    
    downloaded_file = download_file(url, dest_folder)
    open_file(downloaded_file)
    break

if __name__ == "__main__":
    main()
