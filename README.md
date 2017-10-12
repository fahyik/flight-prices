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

swiss = get_prices()

swiss.print_results()
```


