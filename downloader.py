import os
import requests
import shutil
import zipfile

# Function to create directories if they don't exist
def create_directories(directories):
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        else:
            print(f"Directory already exists: {directory}")

# Function to download a file
def download_file(url, dest):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        zip_path = os.path.join(dest, os.path.basename(url))
        with open(zip_path, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
        print(f"Downloaded: {zip_path}")
        return zip_path
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return None

# Function to unzip a file
def unzip_file(src, dest):
    try:
        with zipfile.ZipFile(src, 'r') as zip_ref:
            zip_ref.extractall(dest)
        print(f"Extracted {src} to {dest}")
    except zipfile.BadZipFile:
        print(f"Error unzipping {src}")

# Function to delete files or directories
def delete_directory(path):
    try:
        shutil.rmtree(path)
        print(f"Deleted: {path}")
    except FileNotFoundError:
        print(f"Directory not found: {path}")
    except Exception as e:
        print(f"Error deleting {path}: {e}")

# Chrome and Firefox configuration
chrome_versions = range(90, 100)  # Example versions for Chrome
firefox_versions = range(90, 100)  # Example versions for Firefox

# Directories for Chrome
chrome_folder = "G:\\chrome\\"
new_chrome_folder = "G:\\New_chrome_browser\\"
chrome_drivers_folder = "G:\\drivers\\Chrome\\"

# Directories for Firefox
firefox_folder = "G:\\firefox\\"
new_firefox_folder = "G:\\New_browser_firefox\\"
firefox_drivers_folder = "G:\\drivers\\Firefox\\"

# 1. Create directories for Chrome and Firefox
create_directories([chrome_folder, new_chrome_folder, firefox_folder, new_firefox_folder])

# 2. Download Chrome browser
for version in chrome_versions:
    url = f"https://ltbrowserdeploy.lambdatest.com/windows/chrome/Google+Chrome+{version}.0.zip"
    download_file(url, new_chrome_folder)

# 3. Download Chrome drivers
for version in chrome_versions:
    url = f"https://ltbrowserdeploy.lambdatest.com/windows/drivers/Chrome/{version}.0.zip"
    download_file(url, new_chrome_folder)

# 4. Unzip Chrome drivers
for version in chrome_versions:
    zip_path = os.path.join(new_chrome_folder, f"{version}.0.zip")
    unzip_file(zip_path, chrome_drivers_folder)

# 5. Unzip Chrome browser
for version in chrome_versions:
    zip_path = os.path.join(new_chrome_folder, f"Google+Chrome+{version}.0.zip")
    unzip_file(zip_path, chrome_folder)

# 6. Download Firefox browser
for version in firefox_versions:
    url = f"https://ltbrowserdeploy.lambdatest.com/windows/firefox/{version}.0.zip"
    download_file(url, new_firefox_folder)

# 7. Download Firefox drivers
for version in firefox_versions:
    url = f"https://ltbrowserdeploy.lambdatest.com/windows/drivers/Firefox/{version}.0.zip"
    download_file(url, new_firefox_folder)

# 8. Unzip Firefox drivers
for version in firefox_versions:
    zip_path = os.path.join(new_firefox_folder, f"{version}.0.zip")
    unzip_file(zip_path, firefox_drivers_folder)

# 9. Unzip Firefox browser
for version in firefox_versions:
    zip_path = os.path.join(new_firefox_folder, f"{version}.0.zip")
    unzip_file(zip_path, firefox_folder)

# 10. Delete temporary Chrome and Firefox browser and driver zip folders
delete_directory(new_chrome_folder)
delete_directory(new_firefox_folder)
