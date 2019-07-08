"""
Main function
"""

import argparse
from converter import Converter, ConverterError
import json


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--amount', type=float, required=True)  # TODO help='...'
    parser.add_argument('--input_currency', type=str, required=True)
    parser.add_argument('--output_currency', type=str)
    args = parser.parse_args()

    return args


if __name__ == '__main__':

    args = get_arguments()
    amount = args.amount
    input_cur = args.input_currency

    try:
        if args.output_currency:
            output_cur = args.output_currency
            conv = Converter(amount, input_cur, output_cur)
            res = conv.convert(output=True)
        else:
            conv = Converter(amount, input_cur)
            res = conv.convert()

        print(json.dumps(conv.create_dict(res)))
    except ConverterError as e:
        print(e.text())
