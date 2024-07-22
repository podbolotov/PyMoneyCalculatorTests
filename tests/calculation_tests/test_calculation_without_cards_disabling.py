import pytest
import allure
from lib.ui.screens.calc_screen import CalcScreenLocators, CalcScreenOperations
from lib.tools.element_finders import find_by_locator
from lib.tools.number_formatters import NumberFormatters as NumForm
from lib.tools.screenshotter import make_and_attach_screenshot


@allure.parent_suite("Тесты корректности вычислений")
@allure.suite("Вычисление суммы банкнот и монет")
@allure.sub_suite("Вычисления без отключения отдельных купюр и монет")
class TestCalculationWithoutNominalsDeactivation:
    @allure.title("Вычисление суммы одной случайной карточки")
    @allure.severity(severity_level="NORMAL")
    def test_one_random_card_calculation(self, appium_driver, reset_calculations_after_test):
        # Инициализируем операции экрана, пробрасываем драйвер.
        calc_screen = CalcScreenOperations(appium_driver)

        # Выбираем случайный локатор карточки банкноты или монеты
        random_card_locator = calc_screen.get_random_banknote_or_coin_locator()

        # Рассчитываем значения, которые мы будем вводить в карточку и ожидать в качестве её суммы.
        input_count = calc_screen.get_random_correct_card_count()

        # Вычисляем ожидаемую сумму по формуле (вводимое число * известная стоимость номинала банкноты/монеты)
        expected_amount = NumForm.format_amount(input_count * random_card_locator.data.cost)

        # Описываем тест
        allure.dynamic.description(f"Данный тест проверяет корректность рассчёта суммы одной отдельной карточки.\n"
                                   f"Карточка выбирается случайным образом.\n\n"
                                   f"Во время данной итерации выбрана карточка с локатором "
                                   f"{random_card_locator.__name__}.\n"
                                   f"Ценность выбранной банкноты/монеты: {random_card_locator.data.cost}.\n"
                                   f"Текстовое название выбранной банктноты/монеты: "
                                   f"\"{random_card_locator.data.text_name}\".\n\n"
                                   f"Ожидаемый результат: \n"
                                   f"- В карточку {random_card_locator.data.text_name} должно быть введено количество "
                                   f"{input_count}.\n"
                                   f"- Сумма карточки {random_card_locator.data.text_name} должна составляет "
                                   f"{expected_amount} ₽.\n"
                                   f"- Результирующее для экрана количество должно составлять {input_count}.\n"
                                   f"- Результирующая для экрана сумма вычислений должна составлять "
                                   f"{expected_amount} ₽.\n")

        with allure.step(f"Выбор случайной карточки, проверка имени выбранной карточки"):
            # Скроллим до выбранной случайной карточки
            calc_screen.scroll_to_card(random_card_locator)

            # После скролла - ищем данную карточку.
            random_card = find_by_locator(appium_driver, random_card_locator)

            # Кликаем по ней.
            random_card.click()

            found_card_name = calc_screen.find_card_inner_element(random_card_locator, "Name").text

            make_and_attach_screenshot(appium_driver)

            allure.attach(
                name='Результаты теста',
                body=f'Ожидаемое значение: "{random_card_locator.data.text_name}"\n'
                     f'Фактическое значение: "{found_card_name}"'
            )

            assert found_card_name == random_card_locator.data.text_name

        with allure.step(f"Ввод числа, проверка отображения карточкой введённого числа."):
            # Вводим число, рассчитанное в начале теста.
            calc_screen.enter_number_by_digit_buttons(input_count)

            actual_card_count = calc_screen.find_card_inner_element(random_card_locator, "Count").text

            expected_card_count = NumForm.format_count(input_count)

            make_and_attach_screenshot(appium_driver)

            allure.attach(
                name='Результаты теста',
                body=f'Ожидаемое значение: "{expected_card_count}"\n'
                     f'Фактическое значение: "{actual_card_count}"'
            )

            assert actual_card_count == expected_card_count

        with allure.step(f"Проверка отображения карточкой корректной суммы"):
            actual_card_amount = calc_screen.find_card_inner_element(random_card_locator, "Amount").text

            actual_card_amount_str = NumForm.format_amount(actual_card_amount)

            make_and_attach_screenshot(appium_driver)

            allure.attach(
                name='Результаты теста',
                body=f'Ожидаемое значение: "{expected_amount}"\n'
                     f'Фактическое значение: "{actual_card_amount_str}"'
            )

            assert actual_card_amount_str == expected_amount

        with allure.step(f"Проверка отображения корректного итогового количества"):
            actual_total_count = find_by_locator(appium_driver, CalcScreenLocators.TotalCalculationCount).text

            formatted_actual_total_count = NumForm.format_count(actual_total_count)

            expected_total_count = NumForm.format_count(input_count)

            make_and_attach_screenshot(appium_driver)

            allure.attach(
                name='Результаты теста',
                body=f'Ожидаемое значение: "{expected_total_count}"\n'
                     f'Фактическое значение: "{formatted_actual_total_count}"'
            )

            assert expected_total_count == formatted_actual_total_count

        with allure.step(f"Проверка отображения корректной итоговой суммы"):
            actual_total_amount = find_by_locator(appium_driver, CalcScreenLocators.TotalCalculationAmount).text

            actual_total_amount_str = NumForm.format_amount(actual_total_amount)

            make_and_attach_screenshot(appium_driver)

            allure.attach(
                name='Результаты теста',
                body=f'Ожидаемое значение: "{expected_amount}"\n'
                     f'Фактическое значение: "{actual_total_amount_str}"'
            )

            assert actual_total_amount_str == expected_amount

    @allure.title("Вычисление максимально возможной суммы")
    @allure.severity(severity_level="NORMAL")
    @pytest.mark.skip("Ожидается реализация фикстуры для сброса результатов вычислений")
    def test_maximal_amount_calculation(self, appium_driver, reset_calculations_after_test):
        pass
