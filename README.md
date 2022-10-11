# malaysiaCarlist
Scraping list of cars from paultan's carbase website, useful for making requests to carbase to generate car market value and develop APIs for it.

JSON Format:
```
Brand
- Model
  - Year of Manufacturing
    - Engine CC
      - Transmission
        - Variant (Series)
 ```

### carlist.py
- This is the source code of the scrapper. It takes around 2hours++ to grab the info. The interval (0.5s) can be reduced to get faster results, but idk.

### to-do
- more car info related scraping.
