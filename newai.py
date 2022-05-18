#import dependencies
import tensorflow as tf
import numpy as np
import pandas as pd
import time

t = 2.5
# load data from file

df = pd.read_csv('2015-08-07_2022-05-11_ethereumprice_org.csv')

# set undefined values to null
df = df.replace('undefined', np.nan)
#print(df.head())




# convert df to float types
df['timestamp'] = pd.to_numeric(df["timestamp"], downcast="float")
df['close'] = pd.to_numeric(df["close"], downcast="float")
df['high'] = pd.to_numeric(df["high"], downcast="float")
df['low'] = pd.to_numeric(df["low"], downcast="float")
df['open'] = pd.to_numeric(df["open"], downcast="float")


# put the close column into a separate dataframe
df_close = df[['close']]
df_main = df[['open', 'high', 'low']]

#print(df_close.dtypes)
#print(df_main.dtypes)
#print(df.dtypes)

# label 
# create a  keras model
model = tf.keras.Sequential()
# add layers
model.add(tf.keras.layers.Dense(units=1, input_shape=[3]))
# compile the model
model.compile(optimizer='adam', loss='mean_squared_error')
# fit the model
model.fit(df_main, df_close, epochs=10, verbose=1, batch_size=1)

