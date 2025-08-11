import pyautogui
import time
import os

save_folder = "screenshots"
os.makedirs(save_folder,exist_ok=True)

num_shots = 12
interval = 3

print("Starting timelapse........")

for i in range(num_shots):
    filename = f"{save_folder}/screenshot_{i+1}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"Saved {filename}")
    time.sleep(interval)


print(f"All ss saved into {save_folder}")