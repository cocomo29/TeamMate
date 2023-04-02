# edit these 5 variables:
DRIVER_PATH = r"C:\Program Files (x86)\chromedriver.exe"
EMAIL = "yourname@email.com"
PASSWORD = "supersecretpassword"
TEAM_NAME = "CS B Compiler Construction Spring 2023"
DATA = r"C:\Users\COCOMO\Desktop\teams automator\form.csv"  # csv file with column named 'RollNumber'

#optional variables:
SPEED = 3  #  5<= is recommended
REVIEW = True  # if set to False, the script will add members to the team without you having the chance to confirm the members 

# do not edit anything below this line
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored
from time import sleep
import csv
import os

if os.path.exists("notfound.txt"): #removing previous notfound.txt file to avoid duplicates
    os.remove("notfound.txt")

def reader(file):
    global rollNumbers
    rollNumbers = []
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                rollNumbers.append(row['RollNumber'])
            except KeyError:
                print(colored("Error: No column named 'RollNumber' found", "red"))
                print(colored("Tip: make sure the column name is 'RollNumber' and not 'Roll Number' or 'rollnumber' etc", "yellow"))
                exit()
    rollNumbers = list(map(lambda x: x + " ", rollNumbers))
    return rollNumbers
print(colored("attempting to add the following members:", "yellow"))
rn = reader(DATA)
[print(colored(i, "blue")) for i in rn]

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(DRIVER_PATH, options=options)
driver.get(r"https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=id_token&scope=openid%20profile&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=eyJpZCI6IjBlNjI3ZGNkLTI2NzAtNDJiNi1iZjk3LWU5NTE2ZDhjOWY4NCIsInRzIjoxNjc5MzQyNTMzLCJtZXRob2QiOiJyZWRpcmVjdEludGVyYWN0aW9uIn0%3D&nonce=78978161-6608-48a6-9162-066ea6583b67&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.3.4&client-request-id=07d1bf1c-9736-4d62-86bc-ad617a1147f0&response_mode=fragment&sso_reload=true")

wait = WebDriverWait(driver, 30)

try:
    email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#i0116")))
    email_input.send_keys(EMAIL)
    driver.find_element(By.CSS_SELECTOR, "#idSIButton9").click()
    password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#i0118")))
    password_input.send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "#idSIButton9").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#idBtn_Back"))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.table-cell.text-left.content:nth-child(2) > div:nth-child(2)"))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.join-team-button"))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.create-team-container button.ts-btn-fluent-primary"))).click()
    team_name_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#create-teamname")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'text') and text()='Dismiss']"))).click()
    team_name_input.send_keys(TEAM_NAME)
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[6]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/button[1]"))).click()
    name = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[6]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/recipient-line[1]/div[1]/div[1]/div[1]/div[1]/people-picker[1]/div[1]/input[1]")))
    
    for i in rollNumbers:
        name.send_keys(i)
        sleep(SPEED)
        result = wait.until(EC.visibility_of_element_located((By.XPATH,"//li[contains(@id, 'pp_')]")))
        if i.strip() in result.text.lower():
            result.click() # click on the result if it matches the search query
            print(colored(f"[+] added {i}", "green"))
        else:
            print(colored(f"[-] Couldn't add {i}", "red"))
            name.send_keys(Keys.BACKSPACE * len(i)) # remove the searched roll number
            with open("notfound.txt", "a") as f:
                f.write(f"{i}\n")

    sleep(SPEED)
    
    if not REVIEW:
        driver.find_element(By.CSS_SELECTOR, "body.exp-density-view.hide-messages.power-bar-visible.hybrid-layout-enabled.initialized.loadingscreendone.ngdialog-open:nth-child(2) div.ngdialog.ts-modal-dialog.custom-width.ts-create-team-dialog.dialog-hide-fullscreen.ts-add-members-common:nth-child(12) div.ngdialog-content div.container-fluid.ts-create-team div.ts-modal-dialog-container.vdi-occlusion div.analytics-panel div.ts-modal-dialog-content div.ts-modal-dialog-content-container div.step2 div.ts-add-members div.ts-add-members-header div.ts-select-people div.ts-add-btn-div > button.ts-btn.ts-btn-fluent.ts-btn-fluent-primary:nth-child(1)").click()

except Exception as e:
    print(colored(f"\nAn error occurred:\n{e} ", "red"))

finally:
    print(colored("Script finished executing", "yellow"))
