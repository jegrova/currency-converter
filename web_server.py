"""
Web application module
"""

from converter import Converter, ConverterError
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/currency_converter')
def currency_converter():
    try:
        amount = float(request.args['amount'])
        input_currency = request.args['input_currency']
        output_currency = request.args.get('output_currency')
    except KeyError:
        return jsonify({'reason': 'missing input parameter'})
    except ValueError:
        return jsonify({'reason': 'amount has to be float'})

    try:
        if output_currency:
            conv = Converter(amount, input_currency, output_currency)
            res = conv.convert(output=True)
        else:
            conv = Converter(amount, input_currency)
            res = conv.convert()

        return jsonify(conv.create_dict(res))
    except ConverterError as e:
        return jsonify({'reason': e.text()})
