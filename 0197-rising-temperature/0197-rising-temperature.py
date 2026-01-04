import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values('recordDate')
    temp_check = weather['temperature'] > weather['temperature'].shift(1)
    date_check = weather['recordDate'].diff().dt.days == 1
    return weather[temp_check & date_check][['id']]