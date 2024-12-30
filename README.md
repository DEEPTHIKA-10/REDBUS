# Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

## Project Overview
This project demonstrates how to scrape Redbus data using Selenium and create an interactive web application with Streamlit for dynamic filtering of the scraped data. The goal is to efficiently gather bus travel information, store it in a structured format, and enable users to explore and analyze the data through a user-friendly interface.

## Skills Takeaway
By completing this project, you will gain hands-on experience in the following:

1. **Web Scraping**
   - Extracting data from dynamic web pages using Selenium.
   - Handling web page elements such as buttons, dropdowns, and scrollable content.

2. **Python Programming**
   - Writing efficient Python scripts for data extraction and manipulation.
   - Utilizing Python libraries for data processing and analysis.

3. **Streamlit**
   - Building an interactive web app for data filtering and visualization.
   - Implementing user-friendly controls such as sliders, dropdowns, and search bars.

4. **SQL**
   - Storing and retrieving scraped data in/from a database.
   - Performing queries to filter and analyze the data.

## Features
- **Data Scraping**: Extract detailed bus travel information such as route, price, travel duration, and bus type from the Redbus website.
- **Data Storage**: Store scraped data in an SQL database for easy access and management.
- **Dynamic Filtering**: Allow users to filter data by various criteria like price range, travel time, and bus type using a Streamlit app.
- **User-Friendly Interface**: Provide an interactive and visually appealing way to explore bus travel options.

## Technologies Used
- **Programming Language**: Python
- **Web Scraping**: Selenium
- **Web Application Framework**: Streamlit
- **Database**: SQL (e.g., SQLite or MySQL)

## Project Structure
```
Redbus-Scraping-Streamlit/
├── data/              # Folder for storing scraped data
├── scripts/           # Python scripts for scraping and data processing
├── app/               # Streamlit application files
├── database/          # SQL database and schema
├── README.md          # Project overview and documentation
└── requirements.txt   # Dependencies for the project
```

## How to Run the Project
1. **Setup Environment**:
   - Install Python 3.8 or higher.
   - Clone the repository.
   - Install required dependencies using:
     ```bash
     pip install -r requirements.txt
     ```

2. **Scrape Data**:
   - Run the Selenium script to scrape data from Redbus:
     ```bash
     python scripts/scrape_redbus.py
     ```

3. **Store Data**:
   - Load the scraped data into the SQL database.

4. **Run Streamlit App**:
   - Start the Streamlit app:
     ```bash
     streamlit run app/app.py
     ```
   - Open the provided URL in your browser to access the app.

## Future Enhancements
- Implement advanced visualizations using libraries like Matplotlib or Plotly.
- Enable exporting filtered results as CSV or Excel files.
- Add support for additional filtering criteria like bus operator ratings.

## Conclusion
This project serves as a comprehensive introduction to web scraping, data storage, and building interactive data applications. It showcases how these technologies can be combined to create practical solutions for real-world problems.

