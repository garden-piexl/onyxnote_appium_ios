# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import logging
from appium import webdriver
from appium.options.common.base import AppiumOptions

logging.basicConfig(level=logging.INFO)

# iPad 配置
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

LOOP_COUNT = 50
ZOOM_SCALE = 2.0
PINCH_SCALE = 0.5

# iPad
options = AppiumOptions()
options.load_capabilities(CAPS)

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)


# 获取屏幕中心点
def get_screen_center(driver):
    size = driver.get_window_size()
    return size['width'] / 2, size['height'] / 2


def pinch_gesture(driver, scale, velocity):
    """执行缩放手势，scale>1 放大，scale<1 缩小"""
    cx, cy = get_screen_center(driver)
    args = {
        "scale": scale,
        "velocity": velocity if scale > 1 else -abs(velocity),
        "origin": {"x": cx, "y": cy},
    }
    driver.execute_script("mobile: pinch", args)


try:
    for i in range(LOOP_COUNT):
        logging.info("第 %d 次缩放", i + 1)
        pinch_gesture(driver, ZOOM_SCALE, 1.0)
        pinch_gesture(driver, PINCH_SCALE, 0.1)
finally:
    driver.quit()

