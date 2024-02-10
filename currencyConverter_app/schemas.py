from pydantic import BaseModel

class GetCurrencyConversionRequest(BaseModel):
    from_currency: str
    to_currency: str
    amount: float

class CurrencyConversionResponse(GetCurrencyConversionRequest):
    converted_amount: float
    conversion_rate: float
    conversion_date: str

class CurrencyConversionErrorResponse(BaseModel):
    error: str
    error_description: str
    
