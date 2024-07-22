import allure
import time


def make_and_attach_screenshot(driver, timeout: int = 0):
    if timeout > 0:
        time.sleep(timeout)
    base64_screenshot = driver.get_screenshot_as_base64()
    allure.attach(
        f'''
        <head>
        <meta charset="utf-8">
        </head>
        <body>
        <img src='data:image/png;base64,{base64_screenshot}' style='width: 300px ; float: left;' />
        </body>''',
        name="Снимок экрана", attachment_type=allure.attachment_type.HTML)
