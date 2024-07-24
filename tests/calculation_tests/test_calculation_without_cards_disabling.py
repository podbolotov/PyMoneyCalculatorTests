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

        # Рассчитываем значения, которые мы будем вводить в карточку и ожидать в качестве её значения.
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
    def test_maximal_amount_calculation(self, appium_driver, reset_calculations_after_test):
        # Инициализируем операции экрана, пробрасываем драйвер.
        calc_screen = CalcScreenOperations(appium_driver)

        # Получаем имена всех классов-локаторов карточек с банкнотами и монетами.
        all_cards_locators_names = calc_screen.get_all_banknotes_and_coins_locator_classes_names()

        # Устанавливаем значение, которое мы будем вводить в каждую карточку и ожидать в качестве её значения.
        input_count = 99999  # TODO: Вынести максимальные и минимальные значения в отдельный класс.

        # Производим предварительное вычисление ожидаемого итогового количества купюр и банкнот.
        final_expected_count = len(all_cards_locators_names) * input_count

        # Производим предварительное вычисление ожидаемой итоговой суммы.
        final_expected_amount = 0
        for card in all_cards_locators_names:
            # Ищем локатор карточки по имени класса-локатора.
            card_locator = CalcScreenOperations.get_banknote_or_coin_locator_by_name(card)
            # Вычисляем сумму карточки путём умножения её стоимости на ожидаемое вводимое значение.
            expected_card_cost = card_locator.data.cost * input_count
            # Прибавляем ожидаемую стоимость карточки к общей ожидаемой сумме.
            final_expected_amount = final_expected_amount + expected_card_cost

        # Устанавливаем значение общего рассчитываемого счётчика купюр и банкнот
        screen_total_count = NumForm.format_count(0)

        # Устанавливаем значение счётчика общей рассчитываемой суммы
        screen_total_amount = NumForm.format_amount(0)

        # Описываем тест
        allure.dynamic.description(f"Данный тест проверяет корректность рассчёта максимально возможной суммы.\n"
                                   f"В каждую карточку вводится максимальное допустимое значение ({input_count}).\n\n"
                                   f"В ходе тестирования проверяется имя каждой карточки, значение каждой отдельной"
                                   f" карточки после ввода, а также рассчитанная сумма каждой отдельной карточки.\n\n"
                                   f"Дополнительно проверяется соответствие прироста общего количества введённых "
                                   f" купюр и банкнот ожидаемому значению.\n\n"
                                   f"Последней проверкой в тесте, после заполнения всех карточек, проверяется "
                                   f"соответствие итоговых значений общего количества банкнот и купюр и общей суммы "
                                   f"значениям, вычисленным предварительно ({final_expected_count} шт., "
                                   f"{final_expected_amount} ₽).")

        for card in all_cards_locators_names:

            # Ищем локатор карточки по имени класса-локатора.
            card_locator = calc_screen.get_banknote_or_coin_locator_by_name(card)

            with (allure.step(f'Ввод значения {input_count} в карточку "{card_locator.data.text_name}"')):

                # Фиксируем текущее значение общего счётчика купюр и банкнот
                screen_total_count_before_input = screen_total_count

                # Фиксируем текущее значение счётчика общей суммы
                screen_total_amount_before_input = screen_total_amount

                # Скроллим до нужной карточки.
                calc_screen.scroll_to_card(card_locator)

                # После скролла - ищем данную карточку.
                card = find_by_locator(appium_driver, card_locator)

                # Кликаем по ней.
                card.click()

                # Вводим значение в карточку.
                calc_screen.enter_number_by_digit_buttons(input_count)

                # После ввода - делаем скриншот экрана.
                make_and_attach_screenshot(appium_driver, title="Снимок экрана после ввода значения")

                with allure.step(f'Проверяем, что имя карточки соответствует значению {card_locator.data.text_name}'):
                    # Извлекаем имя карточки.
                    found_card_name = calc_screen.find_card_inner_element(card_locator, "Name").text

                    allure.attach(
                        name='Результаты теста',
                        body=f'Ожидаемое значение: "{card_locator.data.text_name}"\n'
                             f'Фактическое значение: "{found_card_name}"'
                    )

                    # Сравниваем извлечённое имя карточки с ожидаемым.
                    assert found_card_name == card_locator.data.text_name

                # Приводим ожидаемое значение карточки к установленному формату.
                expected_card_count_str = NumForm.format_count(input_count)
                with allure.step(f'Проверяем, что значение карточки соответствует значению {expected_card_count_str}'):
                    # Извлекаем сумму карточки.
                    actual_card_count = calc_screen.find_card_inner_element(card_locator, "Count").text

                    # Приводим формат значения к установленному.
                    actual_card_count_str = NumForm.format_count(actual_card_count)

                    allure.attach(
                        name='Результаты теста',
                        body=f'Ожидаемое значение: "{expected_card_count_str}"\n'
                             f'Фактическое значение: "{actual_card_count_str}"'
                    )

                    # Сравниваем извлечённое значение карточки с ожидаемым.
                    assert actual_card_count_str == expected_card_count_str

                # Рассчитываем ожидаемую сумму карточки.
                expected_card_amount_str = NumForm.format_amount(input_count * card_locator.data.cost)
                with allure.step(f'Проверяем, что сумма карточки соответствует значению {expected_card_amount_str}'):
                    # Извлекаем сумму карточки.
                    actual_card_amount = calc_screen.find_card_inner_element(card_locator, "Amount").text

                    # Приводим формат суммы к установленному.
                    actual_card_amount_str = NumForm.format_amount(actual_card_amount)

                    allure.attach(
                        name='Результаты теста',
                        body=f'Ожидаемое значение: "{expected_card_amount_str}"\n'
                             f'Фактическое значение: "{actual_card_amount_str}"'
                    )

                    # Сравниваем извлечённую сумму карточки с ожидаемой.
                    assert actual_card_amount_str == expected_card_amount_str

                # Вычисляем ожидаемое значение общего счётчика купюр и банкнот после ввода значения в карточку.
                expected_total_count = NumForm.format_count(input_count + int(screen_total_count_before_input))
                with allure.step(
                        f'Проверяем, что значение общего счётчика увеличилось с {screen_total_count_before_input} '
                        f'до {expected_total_count}'):

                    # Извлекаем значение общего счётчика купюр и банкнот
                    actual_total_count = find_by_locator(appium_driver, CalcScreenLocators.TotalCalculationCount).text

                    formatted_actual_total_count = NumForm.format_count(actual_total_count)

                    allure.attach(
                        name='Результаты теста',
                        body=f'Ожидаемое значение: "{expected_total_count}"\n'
                             f'Фактическое значение: "{formatted_actual_total_count}"'
                    )

                    # Сравниваем извлечённое значение карточки с ожидаемым.
                    assert formatted_actual_total_count == expected_total_count

                    # Если значение увеличилось на ожидаемое
                    if input_count + int(screen_total_count_before_input) == int(expected_total_count):
                        screen_total_count = expected_total_count
                    else:
                        raise AssertionError("Прирост счётчика общего количества купюр"
                                             " и банкнот отличается от ожидаемого")

                # Вычисляем ожидаемое значение общей суммы после ввода в карточку,
                # складывая сумму, имевшуюся в поле общей суммы до ввода значения в карточку с
                # вычисленной ранее суммой самой карточки.
                expected_total_amount = NumForm.format_amount(
                    str(
                        float(expected_card_amount_str) + float(screen_total_amount_before_input)
                    )
                )
                with allure.step(f'Проверяем, что значение общей суммы увеличилось с '
                                 f'{screen_total_amount_before_input} до {expected_total_amount}'):

                    # Извлекаем значение общей суммы
                    actual_total_amount = find_by_locator(appium_driver, CalcScreenLocators.TotalCalculationAmount).text

                    formatted_actual_total_amount = NumForm.format_amount(actual_total_amount)

                    allure.attach(
                        name='Результаты теста',
                        body=f'Ожидаемое значение: "{expected_total_amount}"\n'
                             f'Фактическое значение: "{formatted_actual_total_amount}"'
                    )

                    # Сравниваем извлечённое значение карточки с ожидаемым.
                    assert formatted_actual_total_amount == expected_total_amount

                    # Если значение увеличилось на ожидаемое
                    if float(screen_total_amount_before_input) + \
                            float(expected_card_amount_str) == float(expected_total_amount):
                        screen_total_amount = expected_total_amount
                    else:
                        raise AssertionError("Прирост общей суммы отличается от ожидаемого")

        with ((allure.step(f'Проверка соответствия итоговых данных значениям, рассчитанным предварительно'))):

            formatted_final_expected_count = NumForm.format_count(final_expected_count)
            with (allure.step(f'Итоговое количество банкнот и купюр ({screen_total_count}) '
                              f'соответствует рассчитанным предварительно ({formatted_final_expected_count})')):
                actual_screen_total_count = find_by_locator(appium_driver,
                                                            CalcScreenLocators.TotalCalculationCount).text
                formatted_actual_screen_total_count = NumForm.format_count(actual_screen_total_count)
                allure.attach(
                    name='Результаты теста',
                    body=f'Ожидаемое значение (предварительное): "{formatted_final_expected_count}"\n'
                         f'Фактическое значение (рассчитанное): "{screen_total_count}"\n'
                         f'Фактическое значение (полученное): "{formatted_actual_screen_total_count}"\n'
                )

                assert formatted_final_expected_count == screen_total_count and \
                       formatted_final_expected_count == formatted_actual_screen_total_count

            formatted_final_expected_amount = NumForm.format_amount(final_expected_amount)
            with (allure.step(f'Итоговая сумма ({screen_total_amount}) соответствует рассчитанной'
                              f' предварительно ({formatted_final_expected_amount})')):
                actual_screen_total_amount = find_by_locator(appium_driver,
                                                             CalcScreenLocators.TotalCalculationAmount).text
                formatted_actual_screen_total_amount = NumForm.format_amount(actual_screen_total_amount)
                allure.attach(
                    name='Результаты теста',
                    body=f'Ожидаемое значение (предварительное): "{formatted_final_expected_amount}"\n'
                         f'Фактическое значение (рассчитанное): "{screen_total_amount}\n"'
                         f'Фактическое значение (полученное): "{formatted_actual_screen_total_amount}\n"'
                )

                assert formatted_final_expected_amount == screen_total_amount and \
                       formatted_final_expected_amount == formatted_actual_screen_total_amount
