<h1 align="center">

  Address-Grouping
</h1>

<p align="center">This repository contains the code of the <strong>Address-Grouping</strong>. It is a Python application that groups people living at identical addresses. It is built using Python and leverages various third-party dependencies for enhanced functionality.</p>

<p align="center">
    <a href="https://www.python.org/"><img src="https://www.python.org/static/img/python-logo.png" width="150" align="center" alt="Python Reference"></a>
    <a href="https://flask.palletsprojects.com/en/3.0.x/"><img src="https://miro.medium.com/v2/resize:fit:640/1*XzIRJGujfqAiOV2EIQgR_Q.png" width="150" align="center" alt="Python Reference"></a>
</p>

---

## Dependencies

This project relies on the following Python packages:

- [Flask](https://github.com/pallets/flask) v3.0.0
  - A lightweight WSGI web application framework in Python, used for building APIs and web applications.

- [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/) v0.18.0
  - Fuzzy string matching. It uses Levenshtein Distance to calculate the differences between sequences in a simple-to-use package.

___
# Requirements
For development, you will need Python. 

# Python

Python is a popular programming language used for a wide range of applications, including web development, data analysis, machine learning, and more. Installing Python on your computer is the first step towards starting your Python journey. In this guide, we'll cover how to install Python on different operating systems.

## Installing Python on Windows

To install Python on Windows, follow these steps:

1. Visit the [Python downloads page](https://www.python.org/downloads/) and click on the latest stable release of Python for Windows.
2. Scroll down to the Files section and click on the executable installer for your version of Windows (32-bit or 64-bit).
3. Once the download is complete, run the installer and follow the prompts to install Python.
4. Make sure to select the "Add Python X.X to PATH" option during the installation process to ensure that Python is added to your system path.

## Installing Python on macOS

To install Python on macOS, follow these steps:

1. Open a web browser and visit the [Python downloads page](https://www.python.org/downloads/) for macOS.
2. Click on the latest stable release of Python for macOS.
3. Once the download is complete, open the downloaded package file.
4. Follow the prompts to install Python on your system.
5. You may need to open a new terminal window for the changes to take effect.

## Installing Python on Linux

Python comes pre-installed on many Linux distributions. To check if Python is installed on your system, open a terminal window and type:
````bash
python3 --version
````
If Python is not installed, follow these steps to install it:

1. Open a terminal window.
2. Type the following command to update the package list:
````bash
sudo apt-get update
````
3. Type the following command to install Python:
````bash
sudo apt-get install python3
````
4. Once the installation is complete, you can verify that Python is installed by typing:
````bash
python3 --version
````

---

## Usage

- Type in or insert a .csv file containing Names and Addresses in the following format:
```
Name,Address
Ivan Draganov,”ul. Shipka 34, 1000 Sofia, Bulgaria”
Leon Wu,”1 Guanghua Road, Beijing, China 100020”
Ilona Ilieva,”ул. Шипка 34, София, България”
Dragan Doichinov,”Shipka Street 34, Sofia, Bulgaria”
Li Deng,”1 Guanghua Road, Chaoyang District, Beijing, P.R.C 100020”
Frieda Müller,”Konrad-Adenauer-Straße 7, 60313 Frankfurt am Main, Germany”
````
- Click submit or upload based on the provided type of input.
- See results in UI and also download .txt file.

--- 
## BUILD
To run the web application locally, follow these steps:
1. **Clone the repository:**
   ```bash
   git clone git@github.com:AKumanov/address_group.git
   cd group-people-by-address
2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the application:**
    ```bash
    python main.py
    ```
