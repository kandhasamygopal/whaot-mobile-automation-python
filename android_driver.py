from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Define desired capabilities using UiAutomator2Options
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "ZD222C9DR6"  # Replace with the device name from adb devices
# options.app = "/storage/emulated/0/Download/whaot-57-1.3.7-dev-debug-build-202409041222.apk"  # Path to your APK
options.app_package = "ai.whaot.snt.qa"  # Replace with your app's package name
options.app_activity = "com.illuminz.application.ui.splash.SplashActivity"  # Main activity
options.automation_name = "UiAutomator2"
options.no_reset = True
options.full_reset = False


# Initialize the Appium driver
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Perform any driver actions
print("App launched successfully!")
time.sleep(2)
click_Signin = driver.find_element(AppiumBy.ID,'ai.whaot.snt.qa:id/btnSignIn')
click_Signin.click()
time.sleep(3)
enter_number = driver.find_element(AppiumBy.ID,'ai.whaot.snt.qa:id/etPhone')
enter_number.send_keys("1257486458")
time.sleep(2)
Click_Proceed = driver.find_element(AppiumBy.ID,'ai.whaot.snt.qa:id/btnProceed')
Click_Proceed.click() 
time.sleep(2)
Enter_OTP=driver.find_element(AppiumBy.ID,'ai.whaot.snt.qa:id/otpPinView')
Enter_OTP.send_keys('123456')
time.sleep(2)
Otp_Contiune=driver.find_element(AppiumBy.ID,'ai.whaot.snt.qa:id/btnProceed')
Otp_Contiune.click()
time.sleep(2)
enter_username=driver.find_element(AppiumBy.ID,'ai.whaot.snt.qa:id/etFullName')
enter_username.send_keys("SAMASK")
time.sleep(2)
save_user=driver.find_element(AppiumBy.ID,"ai.whaot.snt.qa:id/btnProceed")
save_user.click()
