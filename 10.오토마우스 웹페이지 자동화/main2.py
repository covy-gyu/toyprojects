import pyautogui
import time
import pyperclip

pyautogui.moveTo(1727, 180, 0)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

start_x = 1361
start_y = 240

end_x = 2018
end_y = 646

pyautogui.screenshot(
    r"10.오토마우스 웹페이지 자동화\날씨.png",
    region=(start_x, start_y, end_x - start_x, end_y - start_y),
)
