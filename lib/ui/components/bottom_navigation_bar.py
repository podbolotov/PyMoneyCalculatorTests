from appium.webdriver.common.appiumby import AppiumBy


class BottomNavbarLocators:
    """ Данный класс содержит локаторы компонентов нижней навигационной панели. """
    BOTTOM_NAVBAR_BUTTON_CALC = {
        'type': AppiumBy.XPATH,
        'value': '//android.view.View[@resource-id="tt_bnavbar_button_calc"]',
    }
    BOTTOM_NAVBAR_BUTTON_HISTORY = {
        'type': AppiumBy.XPATH,
        'value': '//android.view.View[@resource-id="tt_bnavbar_button_history"]',
    }
    BOTTOM_NAVBAR_BUTTON_SETTINGS = {
        'type': AppiumBy.XPATH,
        'value': '//android.view.View[@resource-id="tt_bnavbar_button_settings"]',
    }


class BottomNavbarOperations:
    """ Данный класс содержит методы взаимодействия с нижней навигационной панелью.
    При инициализации требует передачи активного драйвера.
    :param driver: Драйвер, предоставляемый фикстурой appium_driver.
    """

    def __init__(self, driver):
        self.driver = driver

    def find_bottom_navbar_button_calc(self):
        """ Метод поиска кнопки "Калькулятор" на нижней навигационной панели.
        :return: Класс кнопки "Калькулятор" нижней навигационной панели.
        :raises RuntimeError: Ошибка, возвращаемая в случае, если кнопку найти не удалось.
        """
        try:

            locator_type = BottomNavbarLocators.BOTTOM_NAVBAR_BUTTON_CALC['type']
            locator_value = BottomNavbarLocators.BOTTOM_NAVBAR_BUTTON_CALC['value']

            bottom_navbar_button_calc = self.driver.find_element(
                by=locator_type,
                value=locator_value
            )

            return bottom_navbar_button_calc

        except Exception as e:
            raise RuntimeError(e)

    def find_bottom_navbar_button_history(self):
        """ Метод поиска кнопки "История" на нижней навигационной панели.
        :return: Класс кнопки "История" нижней навигационной панели.
        :raises RuntimeError: Ошибка, возвращаемая в случае, если кнопку найти не удалось.
        """
        try:

            locator_type = BottomNavbarLocators.BOTTOM_NAVBAR_BUTTON_HISTORY['type']
            locator_value = BottomNavbarLocators.BOTTOM_NAVBAR_BUTTON_HISTORY['value']

            bottom_navbar_button_history = self.driver.find_element(
                by=locator_type,
                value=locator_value
            )

            return bottom_navbar_button_history

        except Exception as e:
            raise RuntimeError(e)

    def find_bottom_navbar_button_settings(self):
        """ Метод поиска кнопки "Настройки" на нижней навигационной панели.
        :return: Класс кнопки "Настройки" нижней навигационной панели.
        :raises RuntimeError: Ошибка, возвращаемая в случае, если кнопку найти не удалось.
        """
        try:

            locator_type = BottomNavbarLocators.BOTTOM_NAVBAR_BUTTON_SETTINGS['type']
            locator_value = BottomNavbarLocators.BOTTOM_NAVBAR_BUTTON_SETTINGS['value']

            bottom_navbar_button_settings = self.driver.find_element(
                by=locator_type,
                value=locator_value
            )

            return bottom_navbar_button_settings

        except Exception as e:
            raise RuntimeError(e)
