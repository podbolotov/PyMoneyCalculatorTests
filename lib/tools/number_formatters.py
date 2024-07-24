import decimal


class NumberFormatters:

    @staticmethod
    def format_amount(amount: str | int) -> str:
        """

        :param amount:
        :return:
        """

        number_to_string = str(amount)
        amount_without_rub_currency_symbol = number_to_string.replace('₽', '')
        amount_without_spaces = amount_without_rub_currency_symbol.replace(' ', '')

        ctx = decimal.Context()
        ctx.prec = 20

        d1 = ctx.create_decimal(repr(float(amount_without_spaces)))
        value_string = format(d1, 'f')

        splitted_string = value_string.split(".")

        if splitted_string[1] == '0' or splitted_string[1] == '00':
            result = splitted_string[0]
        else:
            result = "{:.2f}".format(float(value_string))

        return result

    @staticmethod
    def format_count(count: str | int):
        """

        :param count:
        :return:
        """

        count_to_string = str(count)
        count_without_label = count_to_string.replace('шт', '')
        count_without_spaces = count_without_label.replace(' ', '')

        try:
            int_count = int(count_without_spaces)
            if isinstance(int_count, int):
                result = count_without_spaces
                return result
        except ValueError:
            raise ValueError("Count should be Int!")
