import os
from appium.options.android import UiAutomator2Options


class ApplicationCapabilities:
    @staticmethod
    def get():
        application_path = '/home/maxim/Projects/PyMoneyCalculatorTests/app-debug.apk'
        application_capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName=os.environ.get("DEVICE_NAME") or 'Android 11',
            appPackage='kaczmarek.moneycalculator',
            appActivity='MainActivity',
            app=application_path,
            fullReset='true'
        )
        capabilities = UiAutomator2Options().load_capabilities(application_capabilities)
        return capabilities
