import wget
import zipfile
import os
import platform
import subprocess
import asyncio
import psutil
import shutil
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

def mkdiraimstar():
    documents_path = os.path.expanduser('~\\Documents')
    onedrive_path = os.path.expanduser('~\\OneDrive')
    aimstar_path_od = os.path.join(onedrive_path, 'Documents', 'AimStar', 'Offsets')
    aimstar_path = os.path.join(documents_path, 'AimStar', 'Offsets')
    try:
        os.makedirs(aimstar_path_od, exist_ok=True)
        os.makedirs(aimstar_path, exist_ok=True)
    except Exception as e:
        print(Fore.RED + f"Error with creating offsets directories: {e}")


def check_process(process_name):
    """
    Функция для проверки существования процесса по его имени.
    
    Args:
    - process_name (str): Имя процесса для проверки.
    
    Returns:
    - bool: True, если процесс существует, False в противном случае.
    """
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            return True
    return False

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def colored_print(text, color=Fore.WHITE):
    print(color + text + Style.RESET_ALL)

def main_menu():
    clear_screen()
    colored_print("     Crimson Loader", Fore.RED)
    colored_print("     1 - Show cheats for CS:2", Fore.YELLOW)
    colored_print("     2 - Show cheats for Roblox", Fore.LIGHTBLACK_EX)
    colored_print("     3 - Settings", Fore.RED)
    colored_print("     0 - Exit", Fore.RED)

    choice = int(input(Fore.CYAN +"\n Choice: "))
    return choice

def cs2_menu():
    clear_screen()
    colored_print("1 - aimstar (Use this at your own risk.)", Fore.YELLOW)
    colored_print("2 - luno (Use this at your own risk.)", Fore.YELLOW)
    colored_print("3 - xone", Fore.GREEN)
    colored_print("4 - tkazer (Use this at your own risk.)", Fore.YELLOW)
    colored_print("0 - Return to main menu", Fore.RED)
    choice = int(input("Choice: "))
    return choice


def roblox_menu():
    clear_screen()
    colored_print("1 - solara (Use this at your own risk.)", Fore.YELLOW)
    colored_print("2 - incognito", Fore.RED)
    colored_print("0 - Return to main menu", Fore.RED)
    choice = int(input("Choice: "))
    return choice

async def sleep_for_seconds(seconds):
    await asyncio.sleep(seconds)

def download_and_extract_zip(url, extract_folder):
    try:
        file_name = url.split('/')[-1]
        extract_folderc = os.path.join(os.getcwd(), extract_folder)
        file = os.path.join(os.getcwd(), file_name)
        # Check if the extraction folder already exists
        if os.path.exists(extract_folder):
            # Delete the folder and its contents
            shutil.rmtree(extract_folderc)
            print("Deleted ", extract_folderc, " directory")
        else:
            print(f"{extract_folderc} not found")
        asyncio.run(sleep_for_seconds(1))
        if os.path.exists(file):
    # Удаляем файл
            os.remove(file)
            print(f"File {file} deleted.")
        else:
            print(f"File {file} not found.")

        asyncio.run(sleep_for_seconds(1))

        # Download and extract the zip file
        file_path = wget.download(url)
        if os.path.exists(file_path):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_folder)
            return True, extract_folder
        else:
            print(Fore.RED + "Download failed.")
            asyncio.run(sleep_for_seconds(3))
            return False, None
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        asyncio.run(sleep_for_seconds(3))
        return False, None

def download_and_execute(url, new_window=False):
    try:
        file_name = url.split('/')[-1]  # Extract filename from URL
        file_path = os.path.join(os.getcwd(), file_name)  # Current directory + filename
        
        # Check if the file already exists
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File {file_path} deleted")
        else:
            print(f"File {file_path} not found")

        # Download the file
        file_path = wget.download(url)

        asyncio.run(sleep_for_seconds(1.5))

        # Execute the downloaded file
        if os.path.exists(file_path):
            if new_window:
                subprocess.Popen(f'"{file_path}"', creationflags=subprocess.CREATE_NEW_CONSOLE)
            else:
                os.system(f'"{file_path}"')
            return True
        else:
            print(Fore.RED + "Download failed.")
            asyncio.run(sleep_for_seconds(3))
            return False
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        asyncio.run(sleep_for_seconds(3))
        return False

while True:
    choice1 = main_menu()

    if choice1 == 1:
        choice2 = cs2_menu()
        
        if choice2 == 1:
            if check_process("cs2.exe"):
                mkdiraimstar()
                success, extract_path = download_and_extract_zip("https://github.com/CowNowK/AimStar/releases/download/v4.5.0/AimStar_4.5.0.zip", 'unpacked_files_aimstar', "AimStar_4.5.0.zip")
                if success:
                    exe_path = os.path.join(extract_path, 'AimStar.exe')
                    if os.path.exists(exe_path):
                        os.system(f'"{exe_path}"')
                    else:
                        print(Fore.RED + "Executable not found.")
                        asyncio.run(sleep_for_seconds(3))
            else:
                print(Fore.RED + "CS:2 is not running.")
                print(Fore.GREEN + "Starting CS:2...")
                print(Fore.GREEN + "Just wait 15+ seconds")
                os.system('start "cmd" steam://rungameid/730')
                asyncio.run(sleep_for_seconds(15))
                success, extract_path = download_and_extract_zip("https://github.com/CowNowK/AimStar/releases/download/v4.5.0/AimStar_4.5.0.zip", 'unpacked_files_aimstar')
                if success:
                    exe_path = os.path.join(extract_path, 'AimStar.exe')
                    if os.path.exists(exe_path):
                        subprocess.Popen(f'"{exe_path}"', creationflags=subprocess.CREATE_NEW_CONSOLE)
                    else:
                        print(Fore.RED + "Executable not found.")
                        asyncio.run(sleep_for_seconds(3))
        
        elif choice2 == 2:
            if check_process("cs2.exe"):
                download_and_execute("https://github.com/BrightCat14/crimson-loader/releases/download/fordownload/Loader.exe", new_window=False)
            else:
                print(Fore.RED + "CS:2 is not running.")
                print(Fore.GREEN + "Starting CS:2...")
                print(Fore.GREEN + "Just wait 5+ seconds")
                asyncio.run(sleep_for_seconds(5))
                os.system('start "cmd" steam://rungameid/730')
                download_and_execute("https://github.com/BrightCat14/crimson-loader/releases/download/fordownload/Loader.exe", new_window=False)
        
        elif choice2 == 3:
            if check_process("cs2.exe"):
                download_and_execute("https://github.com/BrightCat14/crimson-loader/releases/download/fordownloadx/Ext._XONE_Free_1716538814.exe", new_window=False)
                wget.download("https://github.com/BrightCat14/crimson-loader/releases/download/fordownloadx/Ext._XONE_Free_1716538814.dat", new_window=False)
            else:
                print(Fore.RED + "CS:2 is not running.")
                print(Fore.GREEN + "Starting CS:2...")
                print(Fore.GREEN + "Just wait 15+ seconds")
                os.system('start "cmd" steam://rungameid/730')
                asyncio.run(sleep_for_seconds(15))
                wget.download("https://github.com/BrightCat14/crimson-loader/releases/download/fordownloadx/Ext._XONE_Free_1716538814.dat")
                download_and_execute("https://github.com/BrightCat14/crimson-loader/releases/download/fordownloadx/Ext._XONE_Free_1716538814.exe", new_window=False)
                continue

        elif choice2 == 4:
            if check_process("cs2.exe"):
                download_and_execute("https://github.com/BrightCat14/crimson-loader/releases/download/fordownloadtkazer/TKazerAimStar_TKazer.exe", new_window=True)
            else:
                print(Fore.RED + "CS:2 is not running.")
                print(Fore.GREEN + "Starting CS:2...")
                print(Fore.GREEN + "Just wait 15+ seconds")
                os.system('start "cmd" steam://rungameid/730')
                asyncio.run(sleep_for_seconds(15))
                download_and_execute("https://github.com/BrightCat14/crimson-loader/releases/download/fordownloadtkazer/TKazerAimStar_TKazer.exe", new_window=True)
                continue

        elif choice2 == 0:
            continue  # Возвращаемся в основное меню

        else:
            print(Fore.RED + "Invalid choice.")
            asyncio.run(sleep_for_seconds(3))

    elif choice1 == 2:
        choice2 = roblox_menu()
        
        if choice2 == 1:
                download_and_execute("https://github.com/BrightCat14/crimson-loader/releases/download/fordownloadrs/SolaraBootstrapper.exe", new_window=True)
        
        elif choice2 == 2:
            colored_print("Incognito are not implemented yet.", Fore.RED)
            asyncio.run(sleep_for_seconds(3))

        elif choice2 == 0:
            main_menu()  # Return to main menu
        
        else:
            print(Fore.RED + "Invalid choice.")
            asyncio.run(sleep_for_seconds(3))

    elif choice1 == 3:
        clear_screen()
        print(Fore.RED + "Settings are not implemented yet.")
        asyncio.run(sleep_for_seconds(3))
    
    elif choice1 == 0:
        clear_screen()
        print(Fore.RED + "Exiting...")
        break
    
    else:
        print(Fore.RED + "Invalid choice.")
        asyncio.run(sleep_for_seconds(3))
