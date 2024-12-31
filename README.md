Mobile Automation Project with Appium
📋 Project Overview
This project is designed to automate the Whaot mobile application using Appium and Python. The automation script includes functionalities such as signing in, entering OTP, and saving user profile details.

 Prerequisites
1. Software Requirements
Python: Version 3.8 or later.
Appium Server: Installed and running.
Android SDK and ADB Tools: Installed and configured.
2. Device Requirements
Android Device: USB Debugging enabled.
APK File: Installed or path specified in the script.
Device Name: Retrieved using adb devices.

📦 Setup Instructions
Step 1: Clone the Repository
git clone https://github.com/<your-username>/mobile-automation-appium.git
cd mobile-automation-appium

Step 2: Install Dependencies
pip install Appium-Python-Client

Step 3: Configure the Script
options.device_name: Replace with your Android device's ID.
options.app_package: Replace with the app's package name.
options.app_activity: Replace with the app's main activity.


Here is the README.md content specifically for your Appium mobile automation project:

Mobile Automation Project with Appium
📋 Project Overview
This project is designed to automate the Whaot mobile application using Appium and Python. The automation script includes functionalities such as signing in, entering OTP, and saving user profile details.

⚙️ Prerequisites
1. Software Requirements
Python: Version 3.8 or later.
Appium Server: Installed and running.
Android SDK and ADB Tools: Installed and configured.
2. Device Requirements
Android Device: USB Debugging enabled.
APK File: Installed or path specified in the script.
Device Name: Retrieved using adb devices.
📦 Setup Instructions
Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/<your-username>/mobile-automation-appium.git
cd mobile-automation-appium
Step 2: Install Dependencies
Install the required Python packages:

bash
Copy code
pip install Appium-Python-Client
Step 3: Configure the Script
Update the following details in the script:

options.device_name: Replace with your Android device's ID.
options.app_package: Replace with the app's package name.
options.app_activity: Replace with the app's main activity.



🚀 How to Run the Script
1. Start Appium Server Ensure the Appium server is running:
appium

2.Run the Python Script Execute the automation script:
python automation_script.py


🧾 Script Features
Capabilities Configuration
The script uses UiAutomator2Options to specify:

Platform: Android
Device name: Retrieved from adb devices
App package and activity: Identified from the app.
Automated Actions
Launches the app.
Clicks the "Sign In" button.
Enters a phone number and proceeds.
Inputs an OTP and confirms.
Fills in the username and saves the user profile.


🔧 Customization
Update the phone number, OTP, and username in the script as required.
Adjust the element locators (IDs) if the app UI changes.


🐞 Troubleshooting
Device Not Found:
Ensure the device is connected and adb devices detects it.

Appium Server Issues:
Verify the server is running on http://127.0.0.1:4723.

Element Not Found:
Confirm the element IDs in the app using a tool like UIAutomatorViewer.

📜 License
This project is licensed under the MIT License. Feel free to use and modify as needed.





