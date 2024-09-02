import pyautogui
import os
import time

class DesktopAutomation:
    def open_app(self, app_path):
        os.startfile(app_path)
        time.sleep(5)

    def capture_screenshot(self, output_file):
        screenshot = pyautogui.screenshot()
        screenshot.save(output_file)
        print(f"Screenshot saved as {output_file}")
