import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def run():
    # Loading in the data    
    df = pd.read_csv('GrowLocations.csv')

    # https://sparkbyexamples.com/pandas/get-first-row-of-pandas-dataframe/
    # this tutorial helped with accessing the first row, which was then used to compare
    # the column names with the data in the columns. It is likely that Type is a subtype of 
    # the flower power sensor that lists what the sensor is sensing, 
    # but it should be renamed so as to avoid confusion
    # print(df.columns.tolist())
    # print(df.iloc[0].tolist())
    #['Serial', 'Latitude', 'Longitude', 'Type', 'SensorType', 'Code', 'BeginTime', 'EndTime']
    #['PI040298AD5I214048', 54.443, -1.934, 'Thingful.Connectors.GROWSensors.AirTemperature', 'Flower Power', 'Grow.Thingful.Sensors_98b4dscx', '2019-05-23T16:11:17.000Z', '2019-10-23T17:18:06.000Z']

    # Renaming the Type column to Functionality
    df = df.rename(columns = {'Type':'Functionality'})

    # Removing rows with invalid longitude/latitude, if there are any

    # Assuming the longitude and latitude are not swapped, the resulting data frame has 120 rows
    # Assuming that they are swapped, the resulting data frame has 6438 rows
    # Assuming that more sensors are reporting correct data than not, the longitude and latitude columns should be swapped in the data
    df = df.rename(columns = {'Longitude':'Latitude','Latitude':'Longitude'})


    # https://stackoverflow.com/questions/36921951/truth-value-of-a-series-is-ambiguous-use-a-empty-a-bool-a-item-a-any-o
    # Answer by MSeifert was used to drop rows with invalid longitude and latitude
    df = df.drop(df[(df.Longitude < -10.592) | (df.Longitude > 1.6848)].index)
    df = df.drop(df[(df.Latitude < 50.681) | (df.Latitude > 57.985)].index)

    # Also removing rows where the endtime is before the begin time, if there are any
    df = df.drop(df[df.EndTime < df.BeginTime].index)

    # plotting the image
    # https://matplotlib.org/stable/tutorials/intermediate/imshow_extent.html
    # this tutorial showed how to use extent to scale the image, so as to avoid having to map the lon/lat to image coordinates
    img = mpimg.imread('map7.png')
    imgplot = plt.imshow(img, extent = (-10.592,1.6848,50.681,57.985))
    imgplot

    plt.scatter(x = df['Longitude'], y = df['Latitude'])
    plt.show()
    plt

    # The points seem to be all on land as opposed to in the middle of water, so swapping longitude and latitude was likely correct
if __name__ == "__main__":
    run()
