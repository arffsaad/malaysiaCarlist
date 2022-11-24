# malaysiaCarlist
Scraping list of cars from paultan's carbase website and mycarinfo.my, useful for making requests to carbase to generate car market value and develop APIs for it.

JSON Format (list v1, from Carbase.my [16541 Unique Car Variants]):
```
Brand
- Model
  - Year of Manufacturing
    - Engine CC
      - Transmission
        - Variant (Series)
 ```

JSON Format (list v2, from MyCarInfo.com.my [16200 Unique Car Variants]):
```
Year of Manufacturing
- Brand
  - Model
    - Engine CC
      - Transmission
        - Variant (Series)
 ```

### carlist.py
- This is the source code of the scrapper. It takes around 2hours++ to grab the info. The interval (0.5s) can be reduced to get faster results, but the current interval is good enough.
Just run ``python3 carlist.py`` and it will scrape and save it to a json file.

### to-do
- more car info related scraping.
- crawl to find any exposed APIs to get directly get car valuation.
