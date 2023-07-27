"""
This script converts CSV data provided by Our World in Data 
into a JSON file that's more convenient to work with in javascript
"""


import pandas as pd
import typer
from pathlib import Path
from typing_extensions import Annotated


def main(
    csv_path: Path = typer.Option(help="Path to the CSV file", default='./electricity-prod-source-stacked.csv'),
    json_path: Path = typer.Option(help="Path to write json to", default='../src/country_data.json'),
):
    json_path.parent.mkdir(exist_ok=True, parents=True)

    df = pd.read_csv(csv_path)
    df = df.loc[(df['Year'] == 2022) & ~(df.Code.isna())]
    formatted = df.loc[(df['Year'] == 2022) & ~(df.Code.isna())]
    formatted.columns = [
                  "title",
                  "code",
                  "year",
                  "other_renewables_excluding_bioenergy_twh",
                  "electricity_from_bioenergy_twh",
                  "electricity_from_solar_twh",
                  "electricity_from_wind_twh",
                  "electricity_from_hydro_twh",
                  "electricity_from_nuclear_twh",
                  "electricity_from_oil_twh",
                  "electricity_from_gas_twh",
                  "electricity_from_coal_twh",
    ]
    formatted = formatted.fillna(0)
    formatted.to_json(json_path, orient='records')

if __name__ == "__main__":
    typer.run(main)
