
# Pinch Zoom 自动化脚本

这个脚本演示了如何使用 Appium Python 客户端自动化在 iPad 上执行捏合缩放手势。如果你需要在测试中模拟缩放手势，尤其是针对图片、地图或者支持手势的 UI 元素，这个脚本会非常有用。

## 前提条件

在运行脚本之前，确保你已经准备好了以下内容：

1. **安装 Appium Python 客户端**:
   ```bash
   pip install Appium-Python-Client
   ```

2. **Appium 服务器**:
   确保你的机器上已经安装并运行了 Appium 服务器。如果没有安装，可以使用：
   ```bash
   appium
   ```

3. **iOS 设备**:
   确保你的 iPad 已经连接并配置好，能够通过 Appium 进行测试。

4. **Xcode**:
   确保你已经安装了 Xcode，因为这个脚本使用的是 `XCUITest` 来进行自动化，Mac需要连接iOS设备，并运行WebDriverAgent项目。
   具体教程：https://cloud.tencent.com/developer/article/1864001
   拉取的代码：git clone https://github.com/appium/WebDriverAgent

6. **安装的 App**:
   需要在设备上安装测试的 App。默认情况下，脚本会用到 `com.onyx.galaxy.note` 这个 `bundleId`，你可以根据自己的需要更改。

## 脚本概述

这个脚本自动化了在 iPad 上执行捏合缩放手势。脚本会交替进行两种操作：

1. **放大（Zoom In）**: 使用 `ZOOM_SCALE` 缩放因子。
2. **缩小（Pinch Out）**: 使用 `PINCH_SCALE` 缩放因子。

脚本会循环执行 50 次（由 `LOOP_COUNT` 控制），每次交替进行放大和缩小操作。

## 配置

```python
CAPS = {
    "appium:deviceName": "onyx iPad2025",  # 设备名称
    "appium:udid": "00008120-000C20D8022A601E",  # 设备的 UDID
    "appium:automationName": "XCUITest",  # 使用 XCUITest 进行自动化
    "appium:platformVersion": "18.5",  # iOS 版本
    "platformName": "iOS",  # 平台为 iOS
    "appium:bundleId": "com.onyx.galaxy.note",  # 目标应用的 bundle ID
    "appium:noReset": True,  # 每次测试不重置应用
    "appium:includeSafariInWebviews": True,  # 对于混合应用包含 Safari WebView
    "appium:newCommandTimeout": 3600,  # 命令超时设置
    "appium:connectHardwareKeyboard": True,  # 连接硬件键盘（如果可用）
}
```

## 主要函数

### `get_screen_center(driver)`

这个函数会返回设备屏幕的中心坐标。它用来为缩放手势提供原点。

### `pinch_gesture(driver, scale, velocity)`

这个函数模拟捏合缩放手势：

- **scale**: 缩放因子。大于 1 表示放大，介于 0 和 1 之间表示缩小。
- **velocity**: 手势的速度，影响捏合动作的快慢。

### 循环执行

脚本会循环 50 次，交替进行缩放操作：

1. **放大**：通过调用 `pinch_gesture(driver, ZOOM_SCALE, 1.0)`。
2. **缩小**：通过调用 `pinch_gesture(driver, PINCH_SCALE, 0.1)`。

## 使用示例

```python
# 开始执行脚本
for i in range(LOOP_COUNT):
    logging.info("第 %d 次缩放", i + 1)
    pinch_gesture(driver, ZOOM_SCALE, 1.0)  # 放大
    pinch_gesture(driver, PINCH_SCALE, 0.1)  # 缩小
```

## 如何运行脚本

1. 确保 Appium 服务器已经启动。
2. 运行脚本：
   ```bash
   python pinch_zoom_script.py
   ```

## 可定制的参数

1. **ZOOM_SCALE**: 控制放大的缩放因子（大于 1 的值）。
2. **PINCH_SCALE**: 控制缩小的缩放因子（小于 1 的值）。
3. **LOOP_COUNT**: 控制缩放操作执行的次数。

## 常见问题

1. **设备未找到**:
   确保你的设备正确连接，并且 `UDID` 在 `CAPS` 配置中正确设置。

2. **Appium 超时**:
   如果脚本在等待命令时超时，可以尝试增加 `newCommandTimeout` 参数的值。

3. **手势无法执行**:
   确保目标应用支持捏合手势，并且应用元素可响应这些手势。


