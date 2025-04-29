# Tariffs
https://dataweb.usitc.gov/tariff/annual

# How to start

1. Unzip the `data.zip` folder inside the root of the project
2. Run `python3 combine_datasets.py` to combine all the datasets
3. Run `python3 preprocess.py` to preprocess the datasets
4. Run the model setup and inference `python3 model.py`

# Flask server

The flask server features a dashboard where you can view all the classes and 
make test inference according to paramter

## Run flask server

```
python3 server.py

```

Go to `localhost:5000`
