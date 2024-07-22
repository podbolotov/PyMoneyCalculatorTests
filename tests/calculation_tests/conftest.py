import time
import pytest
from selenium.webdriver import ActionChains
from lib.ui.screens.calc_screen import CalcScreenLocators
from lib.tools.element_finders import find_by_locator


@pytest.fixture(scope="function")
def reset_calculations_after_test(appium_driver):
    """
    Данная фикстура сбрасывает результаты рассчётов на экране "Калькулятор" после выполнения теста
    """
    yield

    print("\nСброс вычислений, возвращение к первой активной карточке...")

    # Ищем кнопку "backspace"
    backspace_button = find_by_locator(appium_driver, CalcScreenLocators.BackspaceButton)

    # Инициализируем ActionChains, пробрасываем драйвер.
    actions = ActionChains(appium_driver)

    # Начинаем действие "нажать на кнопку и держать".
    actions.click_and_hold(backspace_button)
    actions.perform()

    # Ожидаем одну секунду, удерживая кнопку "backspace".
    time.sleep(1)

    # Отпускаем удерживаемую кнопку "backspace".
    actions.release(backspace_button)
    actions.perform()

    time.sleep(5)
