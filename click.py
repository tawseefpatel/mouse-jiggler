import pyautogui


while (1):

    pyautogui.move(1, 0, duration=0.1)
    pyautogui.move(0, 1, duration=0.1)
    pyautogui.move(-1, 0, duration=0.1)
    pyautogui.move(0, -1, duration=0.1)

    pyautogui.click(1919, 1070)
    pyautogui.sleep(0.5)
    pyautogui.click(1919, 1070)

    for i in range(180, 0, -1):
        pyautogui.sleep(1)
        print(f"time remaining {i} ", end="\r", flush=True)
