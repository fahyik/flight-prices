# Flight Prices

## Installation

On Mac:

``pip install selenium``

``brew install phantomjs``

## Examples:

#### selenium_swiss.py

```python
swiss = SwissAirfareCrawler(
	orig='ZRH',  # Zurich
	dest='CDG',  # Paris
	out_date='2017-12-15',
	in_date='2017-12-18'
)

swiss.get_prices()

swiss.print_results()
```

output
```
{
    "OUTBOUND": [
        {
            "arr_flight": "CDG 09:00",
            "dep_flight": "ZRH 07:30",
            "price_bus": "220",
            "price_eco": "69"
        },
        {
            "arr_flight": "CDG 14:10",
            "dep_flight": "ZRH 12:45",
            "price_bus": "220",
            "price_eco": "69"
        },
        {
            "arr_flight": "CDG 18:05",
            "dep_flight": "ZRH 16:50",
            "price_bus": "364",
            "price_eco": "174"
        },
        {
            "arr_flight": "CDG 20:10",
            "dep_flight": "ZRH 18:55",
            "price_bus": "220",
            "price_eco": "69"
        }
    ],
    "INBOUND": [
        {
            "arr_flight": "ZRH 08:20",
            "dep_flight": "CDG 07:00",
            "price_bus": "247",
            "price_eco": "69"
        },
        {
            "arr_flight": "ZRH 11:15",
            "dep_flight": "CDG 09:55",
            "price_bus": "247",
            "price_eco": "69"
        },
        {
            "arr_flight": "ZRH 16:20",
            "dep_flight": "CDG 15:00",
            "price_bus": "247",
            "price_eco": "124"
        },
        {
            "arr_flight": "ZRH 20:00",
            "dep_flight": "CDG 18:45",
            "price_bus": "247",
            "price_eco": "69"
        },
        {
            "arr_flight": "ZRH 22:00",
            "dep_flight": "CDG 20:50",
            "price_bus": "247",
            "price_eco": "69"
        }
    ]
}
```
