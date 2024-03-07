# Fred API

```python
import Fred
```

## Create Object

```python
fred = Fred(API_KEY)
```

## Filter Series

```python
series_list_df = await (
    fred
    .get_series_list(
      tags = ["india", "monthly"],
      limit = 2
    )
)
series_list_df
```

## Get series data

```python
series_list = list(series_list_df["id"])
series_data = await fred.get_series(
    series_id_list = series_list,
    limit = 1
)

series_data
```