# currency-converter

The project converts value from one currency to another currency. If output currency parameter is missing it converts the value to all currencies.
Project consists of CLI and web API application.

Rates for conversions are taken from website http://www.floatrates.com/daily/
These rates are updated on daily basis.  

#### Example run:
```
$ ./currency_converter.py --amount 10.5 --input_currency JP¥ --output_currency eur
{
    "input": 
    {
        "amount": 10.5, 
        "currency": "JPY"
    }, 
    
    "output": 0.0862339679034918
}

$ ./currency_converter.py --amount 10 --input_currency EUR
{
    "input": 
    {
        "amount": 10.0,
        "currency": "EUR"
    }, 
    
    "output": 
    {
        "USD": 11.24826691334, 
        "GBP": 8.9651198244998, 
        "AUD": 16.068702179681, 
        "CAD": 14.761792040783,
        ...
    }
}


GET /currency_converter?amount=0.9&input_currency=USD&output_currency=AUD
{
  "input": {
    "amount": 0.9,
    "currency": "USD"
  },
  "output": 1.28569423833297
}

GET /currency_converter?amount=0.9&input_currency=USD
{
  "input": {
    "amount": 0.9,
    "currency": "USD"
  },
  "output": {
    "AED": 3.30372729418338,
    "AFN": 73.4944670937675,
    "ALL": 98.018699654781,
    "AMD": 428.843452049199,
    ...
  }
}
```