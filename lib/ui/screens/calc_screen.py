import re
import time
import random


from appium.webdriver.common.appiumby import AppiumBy
from lib.tools.element_finders import find_by_locator
from lib.data.banknotes_data import BanknotesData


class CalcScreenLocators:
    """ Данный класс содержит локаторы компонентов экрана "Калькулятор". """

    # Containers
    class BanknotesCardContainer:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId(\"CalculatorUiBanknoteCardsContainer\"'

    # Total Fields
    class TotalCalculationAmount:
        type = AppiumBy.XPATH
        value = '//android.widget.TextView[@resource-id="CalculatorUiTotalBoardTotalAmount"]'

    class TotalCalculationCount:
        type = AppiumBy.XPATH
        value = '//android.widget.TextView[@resource-id="CalculatorUiTotalBoardTotalCount"]'

    # Cards
    class Card5000Rub:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiBanknoteCard1"]'
        data = BanknotesData.Rub5000

    class Card2000Rub:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiBanknoteCard2"]'
        data = BanknotesData.Rub2000

    class Card1000Rub:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiBanknoteCard3"]'
        data = BanknotesData.Rub1000

    class Card500Rub:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiBanknoteCard4"]'
        data = BanknotesData.Rub500

    class Card200Rub:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiBanknoteCard5"]'
        data = BanknotesData.Rub200

    class Card100Rub:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiBanknoteCard6"]'
        data = BanknotesData.Rub100

    class Card50Rub:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiBanknoteCard7"]'
        data = BanknotesData.Rub50

    class Card10Rub:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiBanknoteCard8"]'
        data = BanknotesData.Rub10

    class Card5Rub:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiBanknoteCard9"]'
        data = BanknotesData.Rub5

    class Card2Rub:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiBanknoteCard10"]'
        data = BanknotesData.Rub2

    class Card1Rub:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiBanknoteCard11"]'
        data = BanknotesData.Rub1

    class Card50Kop:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiBanknoteCard12"]'
        data = BanknotesData.Kop50

    class Card10Kop:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiBanknoteCard13"]'
        data = BanknotesData.Kop10

    class Card5Kop:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiBanknoteCard14"]'
        data = BanknotesData.Kop5

    class Card1Kop:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiBanknoteCard15"]'
        data = BanknotesData.Kop1

    # Digit buttons
    class DigitButton1():
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiCalculatorKeyboardDigitButton1"]'
        
    class DigitButton2:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiCalculatorKeyboardDigitButton2"]'
        
    class DigitButton3:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiCalculatorKeyboardDigitButton3"]'
        
    class DigitButton4:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiCalculatorKeyboardDigitButton4"]'

    class DigitButton5:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiCalculatorKeyboardDigitButton5"]'

    class DigitButton6:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiCalculatorKeyboardDigitButton6"]'

    class DigitButton7:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiCalculatorKeyboardDigitButton7"]'

    class DigitButton8:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiCalculatorKeyboardDigitButton8"]'

    class DigitButton9:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiCalculatorKeyboardDigitButton9"]'

    class DigitButton0:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculatorUiCalculatorKeyboardDigitButton0"]'

    class BackspaceButton:
        type = AppiumBy.XPATH
        value = '//android.widget.Button[@resource-id="CalculatorUiCalculatorKeyboardBackspaceIconButton"]'


class CalcScreenOperations:
    """ Данный класс содержит методы взаимодействия с экраном "Калькулятор".
    При инициализации требует передачи активного драйвера.
    :param driver: Драйвер, предоставляемый фикстурой appium_driver.
    """

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_card(self, looked_object_id):
        """

        :param looked_object_id:
        :return:
        """
        self.driver.implicitly_wait(1)

        scroll_container_locator = CalcScreenLocators.BanknotesCardContainer

        scroll_forward = (f"new UiScrollable({scroll_container_locator.value}).scrollable(true)).setAsHorizontalList("
                          f").scrollForward()")
        scroll_backward = (f"new UiScrollable({scroll_container_locator.value}).scrollable(true)).setAsHorizontalList("
                           f").scrollBackward()")

        print(f"\nНачинаем поиск элемента с id {looked_object_id.value}.")

        def is_element_displayed(looked_object):
            state = False
            try:
                # print(str(looked_object.type)+" "+str(looked_object.value) )
                state = (self.driver.find_element(looked_object.type, looked_object.value).is_displayed())
                return state
            except Exception as e:
                ex = e
                print("Элемент не обнаружен. ")
                return state

        scroll_locator = scroll_forward

        tries = 1
        while not is_element_displayed(looked_object_id):
            print(f"Делаем свайп (попытка {tries})...")
            self.driver.find_element(
                by=AppiumBy.ANDROID_UIAUTOMATOR,
                value=scroll_locator
            )
            tries = tries + 1
            if tries == 10:
                scroll_locator = scroll_backward
                print(f"Пробуем поменять направление на обратное...")
            if tries == 20:
                break

        if not is_element_displayed(looked_object_id):
            self.driver.implicitly_wait(60)
            raise RuntimeError(f"Элемент с id {looked_object_id} найти не удалось.")
        else:
            self.driver.implicitly_wait(60)
            print(f"Элемент с id {looked_object_id} найден.")

    def enter_number_by_digit_buttons(self, number: int):
        string_number = str(number)
        for symbol in string_number:

            locator_class = getattr(CalcScreenLocators, "DigitButton" + symbol)

            digit_button = self.driver.find_element(
                by=locator_class.type,
                value=locator_class.value
            )

            digit_button.click()

            time.sleep(0.5)

    def find_card_inner_element(self, locator, element_type: str = "Name"):
        """

        :param locator:
        :param element_type:
        :return:
        """
        match element_type:

            case "Name":
                xpath_string = locator.value + '/android.widget.TextView[@resource-id="CalculatorUiBanknoteCardName"]'
            case "Count":
                xpath_string = locator.value + '/android.widget.TextView[@resource-id="CalculatorUiBanknoteCardCount"]'
            case "Amount":
                xpath_string = locator.value + '/android.widget.TextView[@resource-id="CalculatorUiBanknoteCardAmount"]'
            case _:
                raise RuntimeError(f"Inner element \"{element_type}\" not avalaible for found.")

        inner_element = self.driver.find_element(
            by=AppiumBy.XPATH,
            value=xpath_string
        )

        return inner_element

    @staticmethod
    def get_all_banknotes_and_coins_locators():
        all_locators = dir(CalcScreenLocators)
        print(f"All attributes ({len(all_locators)}): {all_locators}")

        cards_locators = []

        for locator in all_locators:
            if re.match(r'^(Card)\d{1,4}((Kop)|(Rub))$', locator):
                # print(print(f" + Аттрибут {locator} соответствует паттерну."))
                cards_locators.append(locator)

        print(f"Card locators attributes ({len(cards_locators)}): {cards_locators}")

        return cards_locators

    @staticmethod
    def get_random_banknote_or_coin_locator():
        """
        Метод возвращает локатор случайной банкноты или монеты.
        :return:
        """

        cards_locators = CalcScreenOperations.get_all_banknotes_and_coins_locators()
        random_card_name = random.choice(cards_locators)

        card = getattr(CalcScreenLocators, random_card_name)
        print(f"\nRandom card name: {random_card_name}\n"
              f"Card locator type: {card.type}\n"
              f"Card locator value: {card.value}")

        return card

    @staticmethod
    def get_random_correct_card_count() -> int:
        """
        Метод возвращает случайное количество банкнот или монет, которые можно ввести в одну карточку.
        :return: Возможное для ввода в карточку случайное число.
        """
        count = random.randint(1, 99999)
        return count

