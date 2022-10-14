# malaysiaCarlist
Scraping list of cars from paultan's carbase website and mycarinfo.my, useful for making requests to carbase to generate car market value and develop APIs for it.

JSON Format (list v1, from Carbase.my):
```
Brand
- Model
  - Year of Manufacturing
    - Engine CC
      - Transmission
        - Variant (Series)
 ```

JSON Format (list v2, from MyCarInfo.com.my):
```
Year of Manufacturing
- Brand
  - Model
    - Engine CC
      - Transmission
        - Variant (Series)
 ```

### carlist.py
- This is the source code of the scrapper. It takes around 2hours++ to grab the info. The interval (0.5s) can be reduced to get faster results, but idk.

### to-do
- more car info related scraping.
