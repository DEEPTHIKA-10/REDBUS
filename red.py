import streamlit as st
from sqlalchemy import create_engine
import pandas as pd


##SETTING UP STREAMLIT PAGE

st.set_page_config(layout="wide")
st.title("RED BUS ONLINE BOOKING APP")

st.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit ")
st.image(r"C:\Users\kumar\Desktop\scraped_data\redbusimage.jpg",width=1500)
st.subheader(":REDBUS: Project  by DEEPTHIKA BASKARAN")

engine = create_engine('mysql+pymysql://deepu:Ashokkumar1#@localhost:3306/redbus')
# Fetching data from the database
query = "SELECT * FROM bus_details"
data = pd.read_sql(query, engine)

# Filters
bustype_filter = st.multiselect('Select Bus Type:', options=data['Bus_type'].unique())
route_filter = st.multiselect('Select Route:', options=data['route'].unique())
price_filter = st.slider('Select Price Range:', min_value=int(data['Price'].min()), max_value=int(data['Price'].max()), value=(int(data['Price'].min()), int(data['Price'].max())))
star_filter = st.slider('Select Star Rating Range:', min_value=float(data['Ratings'].min()), max_value=float(data['Ratings'].max()), value=(float(data['Ratings'].min()), float(data['Ratings'].max())))
# Clean the 'Seats_Available' column to extract numeric values
data['Seats_Available'] = data['Seats_Available'].str.extract('(\d+)').astype(int)
availability_filter = st.slider(
    'Select Seat Availability Range:',
    min_value=int(data['Seats_Available'].min()),
    max_value=int(data['Seats_Available'].max()),
    value=(int(data['Seats_Available'].min()), int(data['Seats_Available'].max()))
)
# Filter data based on user inputs
filtered_data = data

if bustype_filter:
    filtered_data = filtered_data[filtered_data['Bus_type'].isin(bustype_filter)]

if route_filter:
    filtered_data = filtered_data[filtered_data['route'].isin(route_filter)]

filtered_data = filtered_data[(filtered_data['Price'] >= price_filter[0]) & (filtered_data['Price'] <= price_filter[1])]
filtered_data = filtered_data[(filtered_data['Ratings'] >= star_filter[0]) & (filtered_data['Ratings'] <= star_filter[1])]
filtered_data = filtered_data[(filtered_data['Seats_Available'] >= availability_filter[0]) & (filtered_data['Seats_Available'] <= availability_filter[1])]


# Display filtered data
st.write('Filtered Data:')
st.dataframe(filtered_data)

# Add a download button to export the filtered data
if not filtered_data.empty:
    st.download_button(
        label="Download Filtered Data",
        data=filtered_data.to_csv(index=False),
        file_name="filtered_data.csv",
        mime="text/csv"
    )
else:
    st.warning("No data available with the selected filters.")