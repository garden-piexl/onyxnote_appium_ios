import time
import logging
from pathlib import Path
from appium import webdriver
from appium.options.common.base import AppiumOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

logging.basicConfig(level=logging.INFO)

# —— 配置常量 ——
CAPS = {
    "appium:deviceName": "onyx iPad2025",
    "appium:udid": "00008120-000C20D8022A601E",
    "appium:automationName": "XCUITest",
    "appium:platformVersion": "18.5",
    "platformName": "iOS",
    "appium:bundleId": "com.onyx.galaxy.note",
    "appium:noReset": True,
    "appium:includeSafariInWebviews": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
}

LOOP_COUNT = 1000
SWIPE_START = (445, 187)
SWIPE_END = (445, 1025)
SWIPE_DURATION = 3.0  # 秒


# —— 1. 初始化 Appium 驱动 ——
options = AppiumOptions()
options.load_capabilities(CAPS)

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)


def swipe(driver, start_x: int, start_y: int, end_x: int, end_y: int, duration: float = 1.0):
    """在屏幕上从 (start_x, start_y) 滑动到 (end_x, end_y)。"""
    touch = PointerInput(interaction.POINTER_TOUCH, "touch")
    builder = ActionBuilder(driver, mouse=touch)

    builder.pointer_action.move_to_location(start_x, start_y)
    builder.pointer_action.pointer_down()
    builder.pointer_action.pause(duration)
    builder.pointer_action.move_to_location(end_x, end_y)
    builder.pointer_action.pointer_up()

    actions = ActionChains(driver)
    actions.w3c_actions = builder
    actions.perform()


def save_screenshot(driver, index: int, folder: str = "screenshots"):
    """保存当前屏幕截图到指定文件夹。"""
    Path(folder).mkdir(parents=True, exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}/screenshot_{index}_{timestamp}.png"
    driver.save_screenshot(filename)
    logging.info("截图已保存：%s", filename)


try:
    for i in range(LOOP_COUNT):
        logging.info("第 %d 次滚动", i + 1)
        swipe(driver, *SWIPE_START, *SWIPE_END, duration=SWIPE_DURATION)
        if i % 100 == 0:  # 每 100 次保存一次截图
            save_screenshot(driver, i + 1)
finally:
    driver.quit()
