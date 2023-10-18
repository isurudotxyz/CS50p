import requests
import sys
import json

if len(sys.argv) == 2:
    try:
        if float(sys.argv[1]):
            price = sys.argv[1]
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        api = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = api.json()
        value = data["bpi"]["USD"]["rate_float"]
        result = float(value) * float(price)
        print(f"${result:,.4f}")
else:
    sys.exit("Missing command-line argument")
