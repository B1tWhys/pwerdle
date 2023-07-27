This script converts from the CSV format provided by [Our World in Data]("https://ourworldindata.org/explorers/energy?facet=none&country=USA~GBR~CHN~OWID_WRL~IND~BRA~ZAF&hideControls=false&Total+or+Breakdown=Total&Energy+or+Electricity=Primary+energy&Metric=Per+capita+consumption"):

|Entity       |Code|Year|Other renewables excluding bioenergy (TWh)|Electricity from bioenergy (TWh)|Electricity from solar (TWh)|Electricity from wind (TWh)|Electricity from hydro (TWh)|Electricity from nuclear (TWh)|Electricity from oil (TWh)|Electricity from gas (TWh)|Electricity from coal (TWh)|
|-------------|----|----|------------------------------------------|--------------------------------|----------------------------|---------------------------|----------------------------|------------------------------|--------------------------|--------------------------|---------------------------|
|Algeria      |DZA |2022|                                          |                                |0.68177                     |0.0105                     |0.07678                     |                              |                          |                          |                           |

into a nested JSON structure with more convenient field names:

```json
[
  {
    "title": "Algeria",
    "code": "DZA",
    "year": 2022,
    "other_renewables_excluding_bioenergy_twh": 0,
    "electricity_from_bioenergy_twh": 0,
    "electricity_from_solar_twh": 0.68177,
    "electricity_from_wind_twh": 0.0105,
    "electricity_from_hydro_twh": 0.07678,
    "electricity_from_nuclear_twh": 0,
    "electricity_from_oil_twh": 0,
    "electricity_from_gas_twh": 0,
    "electricity_from_coal_twh": 0
  }
]
```

### Installation
`pip3 install -r requirements.txt` (use a venv if you want :)

### Directions
```
> python3 ./owid_csv_to_json.py --help
  Usage: owid_csv_to_json.py [OPTIONS]

  Options:
    --csv-path PATH   Path to the CSV file  [default: ./electricity-prod-source-
                      stacked.csv]
    --json-path PATH  Path to write json to  [default: ../src/country_data.json]
    --help            Show this message and exit.
```