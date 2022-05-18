#import dependencies
import tensorflow as tf
import numpy as np
import pandas as pd
import time

t = 2.5
# load data from ETH_USD_price.csv
df = pd.read_csv('ETH_USD_price.csv')

# set the learning rate
learning_rate = 0.001

# define the model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

# add hidden layers
model.add(tf.keras.layers.Dense(units=500, activation='relu'))
model.add(tf.keras.layers.Dense(units=500, activation='relu'))
model.add(tf.keras.layers.Dense(units=500, activation='relu'))
model.add(tf.keras.layers.Dense(units=500, activation='relu'))
model.add(tf.keras.layers.Dense(units=500, activation='relu'))
model.add(tf.keras.layers.Dense(units=500, activation='relu'))

# add output layer for prediction
model.add(tf.keras.layers.Dense(units=1))
opt = tf.keras.optimizers.Adam(learning_rate=1e-4)
model.compile(optimizer=opt, loss='mean_squared_error', metrics=['mean_absolute_error'])




# load the model
#model.load_weights('model.h5')
#print('model loaded')

run = True

while run:
    # train the model
    model.fit(df['price'].values, df['price'].values, epochs=10)
    # get the latest price
    latest_price = df['price'].values[-2]
    # predict the next price
    predicted_price = model.predict([latest_price])
    # print the predicted price
    actual_price = df['price'].values[-1]
    print(predicted_price, actual_price, abs(predicted_price - actual_price), 'Past price :', latest_price)
    # check if the predicted price is the same as the latest price
    if predicted_price == df['price'].values[-1]:
        print('The predicted price is the same as the latest price')
        run = False
    else:
        #print the accuracy and loss of the model
        #print('The accuracy and loss of the model are', model.evaluate(df['price'].values, df['price'].values, verbose=0))
        #print('The predicted price is not the same as the latest price')
        pass
    run = False
    time.sleep(t)
# save the model
model.save('model.h5')
print('Model saved')