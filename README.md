# Fred eXtreme

Performant package to interact with FRED API

- Request multiple series with a single line
- Fast
- Async
- All operations using a single http client

## Why Another FRED Package?

Existing packages only provide a method to extract a single series. I'm currently working on my Economics project and have found it cumbersome to extract multiple series.

## Installation

```bash
pip install fredx
# or
pip install "git+https://github.com/AhmedThahir/fredx"
```

## Import

```python
from fred import Fred
```

## Create Object

```python
API_KEY = ""
fred = Fred(API_KEY)
```

## Get list of series

```python
series_list_df = await (
    fred
    .get_series_list(
      tags = ["india", "monthly"],
      limit = 2
    )
)
```

## Get series data

```python
series_list = list(series_list_df["id"])
series_data = await fred.get_series(
    series_id_list = series_list,
    limit = 1
)
```
