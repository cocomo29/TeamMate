<h1 align="center"> TeamMate </h1>


<div align="center"></div>

<p align="center">Save time and effort by automating the process of manually adding members to a Microsoft Teams.</p>
<p align="center" > 
    <a href="" target="_blank"> <img src="https://i.imgur.com/IFuls1z.gif"/> </a>
<p/>

</div>
</br>

# Prerequisites
To run this script, you need to have the following installed on your computer.

- Python. You can download it from [here](https://www.python.org/downloads/).
- Chrome browser. You can download it from [here](https://www.google.com/chrome/).
- Chrome driver. You can download it from [here](https://chromedriver.chromium.org/downloads).

**Note:** you'll need to download the version of the Chrome driver that matches your Chrome browser version. You can check your Chrome browser's version by typing `chrome://version/` in the address bar. ⚠️ 

# Installation
Follow the steps below to install the script.

1. Clone the repository: `https://github.com/cocomo29/TeamMate.git`
1. Navigate to the cloned repo: `cd TeamMate`
2.  Install the required packages: `pip install selenium termcolor`
3. Edit the following variables in the `driver.py` file:
    - **DRIVER_PATH** : The path to the Chrome driver (usually `C:\Users\name\Downloads\chromedriver_win32\chromedriver.exe`).
    - **EMAIL** : Your Microsoft Teams email address.
    - **PASSWORD** : Your Microsoft Teams password.
    - **TEAM_NAME** : The name of the team you want to create and add members to.
    - **DATA** : The path to the csv file containing the members you want to add to the team. e.g: `C:\Users\name\Downloads\members.csv`
4. Run the script. `python driver.py`

he script will launch the Chrome browser and log in to your Microsoft Teams account. It will then create a new team with the name you specified and add the members from the CSV file to the team.

If the script is unable to find a roll number that is in the CSV file, it will print the roll number in the console and create a file called notfound.txt in the same directory as the script. You can then manually add those members to the team.

<div align="center">

| **notfound.txt** | **terminal** |
|:---:|:---:|
| <img src="https://i.imgur.com/e9NZcZ5.png"> | <img src="https://i.imgur.com/H9IhfmW.png"> |

</div>


## CSV file format 

⚠️ It is important that your CSV file has a `RollNumber` column. The script will use this column to add members to the team. The other columns are optional; you can add as many columns as you want. The script will only use the `RollNumber` column.

Note that the `RollNumber` column is case-sensitive and must not contain spaces. It should be ✅`RollNumber`, not ❌`rollnumber` or ❌`rollNumber` or ❌`Roll Numbers`, etc.

If you don't have a CSV file, you can create a Google Form, share it with the members you want in the team, and export the responses as a CSV file.

# Trouble shooting and Tips

1. Other than the variables you edited above, you can also edit the following variables in the `driver.py` file.
    - **SPEED** : The speed at which the script will run. 1 is the fastest, but it might cause the script to skip more roll numbers. You should set it to `3` or higher, especially if you are running the script for the first time.
    - **REVIEW** : By default, its value is `True`. This will stop the script after entering all the roll numbers and will not press the add button. This is to give you a chance to review the roll numbers before adding them to the team. If you have tried the script before and are sure that it will work, you can set it to `False`, and the script will automatically add the members to the team.

2. With multiple tests, I have found that the script works best when your internet connection is fast and stable. If the script fails without any error, wait for a few minutes and try again when your internet connection is stable (maybe try a different network).

3. Do not change other variables in the `driver.py` file. If you do, the script might not work. Also, don't remove r before the strings of `DRIVER_PATH` and `DATA` variables.

# Contribution and Support
If you find any bugs or have any suggestions, feel free to open an issue or create a pull request. If you have any questions, feel free to contact me on [Discord](https://discordapp.com/users/558261366776004648/) or [Twitter](https://twitter.com/hahaha_haroon).
