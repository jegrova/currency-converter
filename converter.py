"""
Currency conversion module
"""

import requests
import iso4217parse


class ConverterError(Exception):
    def text(self):
        return self.__str__()


class Converter:

    def __init__(self, amount, input_cur, output_cur=None):
        self.amount = amount
        self.input_cur = input_cur.upper()
        list_of_currencies = iso4217parse.parse(input_cur)
        if list_of_currencies is None:
            raise ConverterError("Unknown currency")
        elif len(list_of_currencies) == 1:
            self.input_cur = list_of_currencies[0].alpha3
            if self.input_cur == 'XXX':
                # library iso4217parse returns object Currency with name No currency
                raise ConverterError("Unknown currency")
        elif len(list_of_currencies) > 1:
            list_symbols = list()
            for i in range(len(list_of_currencies)):
                symbol = list_of_currencies[i].symbols[0]
                if symbol == self.input_cur:
                    continue
                list_symbols.append(symbol)
            raise ConverterError("Input currency is ambiguous, did you mean: " + str(list_symbols)[1:-1])
        if output_cur:
            self.output_cur = output_cur.upper()
        self.list_currencies = self.initialize_list_currencies()

    def initialize_list_currencies(self):
        """
        Method for getting a currency list
        """
        rates = self.get_currency_rates()
        list_currencies = list()
        for key in rates.keys():
            list_currencies.append(key)
        return list_currencies

    def get_currency_rates(self):
        """
        Method for gathering current data of currencies
        """
        url = 'http://www.floatrates.com/daily/' + self.input_cur.lower() + '.json'
        rates_for_currency = requests.get(url).json()
        return rates_for_currency

    def convert(self, output=None):
        """
        Method that converts a given currency value to a value of another currency
        """
        rates_for_currency = self.get_currency_rates()
        if output:
            rate = rates_for_currency[self.output_cur.lower()]['rate']
            converted_value = self.amount * rate
            return converted_value
        else:
            converted_values = dict()
            for currency in self.list_currencies:
                converted_values[currency.upper()] = self.amount * rates_for_currency[currency]['rate']
            return converted_values

    def create_dict(self, value, output=None):
        """
        Creates dictionary for the output data
        """
        if output:
            output_value = {self.output_cur: value}
        else:
            output_value = value

        result = {
            'input': {
                'amount': self.amount,
                'currency': self.input_cur,
            },
            'output': output_value
        }

        return result
