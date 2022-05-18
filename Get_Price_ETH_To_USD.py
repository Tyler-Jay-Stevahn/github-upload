#import dependencies
from ast import Pass
import requests
import time
import pandas as pd


run = True
main = True
count = 0
count_max =  1200  
t = 0.25




# get price of Ethereum from Coinbase
def get_price():
    url = 'https://api.coinbase.com/v2/prices/ETH-USD/spot'
    response = requests.get(url)
    data = response.json()
    price = data['data']['amount']
    return price

# gets current price
curr_pricel = get_price()
curr_price = curr_pricel
#print(curr_price, time.ctime(), '0')
#starts dataframe
df = pd.DataFrame({'price': [curr_price], 'time': [time.ctime()]})

while main:
    while run:

        if get_price() != curr_price:
            #print(get_price(), time.ctime(), count)
            curr_price = get_price()
            #append to dataframe df
            df = df.append({'price': curr_price, 'time': time.ctime()}, ignore_index=True)

        else:
            count = 1 + count
            time.sleep(t)
            print(count)
            if count > count_max:
                run = False
            else:
                pass
    if run == False:
        print('Saved to csv')
        # append dataframe to csv


        df.to_csv('ETH_USD_price.csv', mode='a', header=False)
        count = 0
        run = True
    else:
        pass





