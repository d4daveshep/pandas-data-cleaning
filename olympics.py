import pandas as pd


def read_data_file():
    df = pd.read_csv("data-sets/olympics.csv", header=1)  # use the second row (row 1) as the headers
    df = df.rename(columns={
        "Unnamed: 0": "country",
        "? Summer": "summer_olympics",
        "01 !": "summer_golds",
        "02 !": "summer_silvers",
        "03 !": "summer_bronzes",
        "? Winter": "winter_olympics",
        "01 !.1": "winter_golds",
        "02 !.1": "winter_silvers",
        "03 !.1": "winter_bronzes",
        "Total.1": "total_games",
        "01 !.2": "total_golds",
        "02 !.2": "total_silvers",
        "03 !.2": "total_bronzes",
        "Combined total": "combined_total"
    })
    return df


olympics = read_data_file()
print(olympics.head())
countries = olympics.loc[:,"country"]
print(countries.head())
