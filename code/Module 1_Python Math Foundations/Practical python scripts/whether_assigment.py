############################################
# Leon Doungala - whether : Data Scientist Assigment 
# Date : 14 /02 / 2024
############################################
#Import libreries
import pandas as pd
import datetime
import warnings
warnings.filterwarnings('ignore')



########### Define functions ################

#To read CSV file from link
def read_csv_from_url(url):
    try:
        df = pd.read_csv(url)
        df = pd.DataFrame(df)
        return df
    except Exception as e:
        print(f"Error reading CSV from URL: {e}")
        return None

# URL of the CSV file
url = "http://www.fifeweather.co.uk/cowdenbeath/200606.csv"

#Read CSV file
df = read_csv_from_url(url)

#Hanle datetime
def preprocess_data(df):
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M').dt.time
    df["Date"] = pd.to_datetime(df['Date'], dayfirst=True)
    df["Year"] = df['Date'].dt.year
    df["Month"] = df['Date'].dt.month
    df["Day"] = df["Date"].dt.day
    return df

#Preprocess data
df = preprocess_data(df)


# Function to generate output file
def generate_output_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

########### Tak1 : ###########################


# 1. What is the average time of hottest daily temperature (over month);

def average_hottest_daily_temp_time(df):
    # Group by date and calculate hottest daily temperature
    hottest_daily_temperature = df.groupby(['Date', 'Time', 'Day', 'Month', 'Year'])['Hi Temperature'].max().reset_index()

    # Group by month (over month)
    grouped_months = hottest_daily_temperature.groupby(['Month'])

    # Average time
    avg_time_hottest_daily_temp = grouped_months['Time'].apply(
        lambda x: pd.to_datetime(x.apply(lambda y: str(y)), format='%H:%M:%S').mean().time()
    )

    # Reset index to make it a DataFrame
    avg_time_hottest_daily_temp = avg_time_hottest_daily_temp.reset_index()

    return avg_time_hottest_daily_temp




#2. What time of the day is the most commonly occurring hottest time;

def most_common_hottest_time(df):
    # Group by time and find the mode of the temperature for each time
    mode_temp_by_time = df.groupby('Time')['Hi Temperature'].agg(lambda x: x.mode().iloc[0]).reset_index()

    # Find the row with the maximum mode temperature
    most_common_time_row = mode_temp_by_time.loc[mode_temp_by_time['Hi Temperature'].idxmax()]
    return most_common_time_row['Time']
    



#3. Which are the Top Ten hottest times on distinct days, preferably sorted by date order.

def top_ten_hottest_times_on_distinct_days(df):
    # Sort DataFrame by 'Date' and 'Hi Temperature' in descending order
    sorted_df = df.sort_values(by=['Date', 'Hi Temperature'], ascending=[True, False])

    # Group by 'Date' and get the top ten hottest times for each date
    top_ten_by_date = sorted_df.groupby('Date').head(10)

    # Sort the result by 'Date' and 'Hi Temperature' in descending order
    top_ten_hottest_sorted = top_ten_by_date.sort_values(by=['Date', 'Hi Temperature'], ascending=[True, False])

    # Drop duplicates based on 'Date'
    top_ten_hottest_sorted = top_ten_hottest_sorted.drop_duplicates(subset='Date')

    return top_ten_hottest_sorted[['Date', 'Hi Temperature']].head(10)


########### Tak1 : ###########################


#Task 2. Using the ‘Hi Temperature’ values produce a “.txt” file containing all of the Dates and Times where
#        the “Hi Temperature” was within +/- 1 degree of 22.3 or the “Low Temperature” was within +/- 0.2 degree higher or lower of 10.3 over the first 9 days of June

# First 9 days of June
june_data = df[(df['Date'].dt.month == 6) & (df['Date'].dt.day <= 9)]

# Temperatures within the specified range
filtered_data = june_data[((june_data['Hi Temperature'] >= 21.3) & (june_data['Hi Temperature'] <= 23.3)) | 
                          ((june_data['Low Temperature'] >= 10.1) & (june_data['Low Temperature'] <= 10.5))]

# Extract Dates and Times
dates_times = filtered_data[['Date', 'Time']]





#Call implemented fonctions and generate output var 
output_1 = f"1. Average Time of Hottest Daily Temperature: {average_hottest_daily_temp_time(df)}\n\n"
output_2 = f"2. Most Common Hottest Time of the Day: {most_common_hottest_time(df)}\n\n"
output_3 = f"3. Top Ten hottest times on distinct days, preferably sorted by date order : {top_ten_hottest_times_on_distinct_days(df)}\n\n"

# Generate output file
generate_output_file("output.txt", output_1 + output_2 + output_3)

#Tak 2 : 

output_4 =f"Task 2 : Top Ten hottest times on distinct days, preferably sorted by date order : {dates_times}\n"
# Save to a .txt file
file_path = 'temperatures_within_range.txt'
with open(file_path, 'w') as file:
    file.write("Dates and Times where the temperature was within +/- 1 degree of 22.3 or +/- 0.2 degree of 10.3:\n")
    for index, row in dates_times.iterrows():
        file.write(f"{row['Date']} {row['Time']}\n")


print("Assignment completed and output files generated successfully.")




#Next potential step: Employ Machine Learning logistic regression from sklearn to forecast whether it will rain or not.