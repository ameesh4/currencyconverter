import requests
from fastapi import FastAPI
import json

app = FastAPI()

import config, schemas

# # @app.get("/")
# # async def read_root():
# url = f"http://api.exchangeratesapi.io/v1/latest?access_key={config.get_settings().api_key}&words=10&paragraphs=4"
# response = requests.get(url)
# response = response.json()
# print(response['rates']['NPR'])

@app.post("/converter", response_model=schemas.CurrencyConversionResponse)
def currency_converter(request: schemas.GetCurrencyConversionRequest):
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={config.get_settings().api_key}"
    response = requests.post(url)
    response = response.json()
    conversion_rate = (response['rates'][request.to_currency] / response['rates'][request.from_currency])
    converted_amount = request.amount * conversion_rate
    converted = schemas.CurrencyConversionResponse(
        from_currency=request.from_currency,
        to_currency=request.to_currency,
        amount=request.amount,
        converted_amount=converted_amount,
        conversion_rate=conversion_rate,
        conversion_date=response['date']
    )
    return converted

