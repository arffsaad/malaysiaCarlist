from playwright.sync_api import sync_playwright
from time import sleep as sl

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.carbase.my/tool/car-market-value-guide")
    allCars = {}

    # Get all car brands
    brands = page.locator('xpath=//*[@id="brand"]').all_inner_texts()[0].split("\n")                                # STEP 1 : GET ALL VALUES
    for brand in brands:                                                                                            # STEP 2 : LOOP THRU THE VALUES
        if (brand == "-- Select Brand --"):
            pass
        else:
            allCars[brand] = {}                                                                                     # STEP 3 : INSERT INTO DICT
            page.select_option('xpath=//*[@id="brand"]', label=brand)                                               # STEP 4 : CHANGE THE VALUE
            sl(0.5)
            models = page.locator('xpath=//*[@id="family"]').all_inner_texts()[0].split("\n")                        # models step 1
            for model in models:                                                                                    # models step 2
                if (model == "-- Select Model --"):
                    pass
                else:
                    allCars[brand][model] = {}                                                                      # models step 3
                    page.select_option('xpath=//*[@id="family"]', label=model)                                       # models step 4
                    sl(0.5)
                    years = page.locator('xpath=//*[@id="year"]').all_inner_texts()[0].split("\n")                  # years step 1
                    for year in years:                                                                              # years step 2
                        if (year == "-- Select Year --"):
                            pass
                        else:
                            allCars[brand][model][year] = {}                                                        # years step 3
                            page.select_option('xpath=//*[@id="year"]', label=year)                                 # years step 4
                            sl(0.5)
                            ccs = page.locator('xpath=//*[@id="cc"]').all_inner_texts()[0].split("\n")              # ccs step 1
                            for cc in ccs:                                                                          # ccs step 2
                                if (cc == "-- Select Engine Capacity --"):                                         
                                    pass
                                else:
                                    allCars[brand][model][year][cc] = {}                                            # ccs step 3 
                                    page.select_option('xpath=//*[@id="cc"]', label=cc)                             # ccs step 4
                                    sl(0.5)
                                    transmissions = page.locator('xpath=//*[@id="transmission"]').all_inner_texts()[0].split("\n")          # transmissions step 1
                                    for transmission in transmissions:                                                                      # transmissions step 2
                                        if (transmission == "-- Select Transmission --"):
                                            pass
                                        else:
                                            allCars[brand][model][year][cc][transmission] = {}                                              # transmissions step 3
                                            page.select_option('xpath=//*[@id="transmission"]', label=transmission)                         # transmissions step 4
                                            sl(0.5)
                                            variant = page.locator('xpath=//*[@id="variant"]').all_inner_texts()[0].split("\n")          # variant step 1
                                            for var in variant:                                                                                     # variant step 2
                                                if (var == "-- Select Variant(Series) --"):
                                                    pass
                                                else:
                                                    allCars[brand][model][year][cc][transmission][var] = {}
                                                    page.select_option('xpath=//*[@id="variant"]', label=var)



    print(allCars)
    # write to cars.json as json
    import json
    with open('cars.json', 'w') as outfile:
        json.dump(allCars, outfile)
    browser.close()



    

# Get all car models
#print (page.locator('xpath=//*[@id="family"]').all_inner_texts()[0])

# Get all years
#print (page.locator('xpath=//*[@id="year"]').all_inner_texts()[0])

# Get all CC
#print (page.locator('xpath=//*[@id="cc"]').all_inner_texts()[0])

# Get all transmission
#print (page.locator('xpath=//*[@id="transmission"]').all_inner_texts()[0])

# Get all variants
#print (page.locator('xpath=//*[@id="variant"]').all_inner_texts()[0])
