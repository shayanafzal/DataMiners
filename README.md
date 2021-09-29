# Overview

[Presentation](https://docs.google.com/presentation/d/1LgEP1iabjOZd_n9z482B2Ra9EhcuanqxWKVCodDJ5jM/edit#slide=id.gebf57a60df_0_0)

[Dashboard](https://shayanafzal.github.io/DataMiners/index.html)


## Introduction
Accurate sales forcasting and procuring inputs to meet the sales demand, is not a new or unique problem within the business community. This project and the resulting analysis havs been conducted in response to a given business within the snack bar industry. For confidentiality purposes, the business will be referred to as ‘Snack Brands’ from here onwards. Snack Brands manufactures a varity of snack bars and has distribution throughout global makets. 

## Problem & Proposed Solution.
Snack Brands manufactures snack bars, and as a result the company needs to actively manage its supply chain networks. Specifically, procurement and production lead times, along with working capital levels need to be anticipated and planned for in order to optimize financial performance. Hence, we need to accurately forecast the sales in order to identify large cash outlays in response to sourcing inventory, managing inventory turnover as well as waste. To further add value, the project's model will be used to predict sales 24 months into the future, allowing Snack Brands to order the ingredients in a timely manner, source optimal ingredient pricing and manage inventory levels within the company's available financial resources.

# Description of Communication Protocols

The following communication tools were used when working on this project:

1. A private Slack group was used as the primary communications protocol. 
2. Recurring Zoom calls were setup to enable collaboration and communication between group members.
3. Phones will be utilized in case there is an urgent need to contact members.


# Data

## Raw Data Set

The raw data used for this analysis can be accessed [here](https://github.com/shayanafzal/DataMiners/blob/a17ea5362ba60a61753ce50b6ce491bb05168e33/Sales_Data_Raw.csv).

## Cleaning the Data Set
The original data set contained data in a number of columns, not all of which were relevant. From the original data set we only kept the columns listed below. A description of the category has also been provided.

#### Data Set Columns
* Year
* Month 
* InvDate - Dales Invoice Number
* InvNumbers – Invoice Numbe
* Market – The sales are broken down into three different regions	
	* CAN - Canada
	* US – United States
	* NTL – International
* InvCustomer – This is the customer code
* CompanyName – This is the customer name
* ItemClass – Items are classified into two categories
	* ORG – manufactured using organic ingredients
	* CONV – manufactured using conventional ingredients
* SubCategory – The products are devided into the following subcategories
	* CHOC – Chocolate
	* F&N - Fruits and Nuts
	* GRAN - Granola 
	* LSUG – Low Sugar
	* PROT – Protein
* Flavours – This is a product subcategory
* Product ID
* Product Description
* UOM – Unit of Measurement (either be pack or a carton as indicated in the column)
* Pack -
* Real_QTY - This indicates the total number of snack bars on the sales order regardless of wheather they were sold as a case or a carton
* CAD_value – Sales price of the order


# Coding 

The coding can be accessed [here](https://github.com/shayanafzal/DataMiners/blob/65c90f04cfc6d1c089585cc2a698855caca71611/Code.ipynb).

## Database

### Creation of a database

A mockup database "DataMiners" was created in PG Admin as seen in the image below. The table "sales_data" was created manually using the SQL query, and saved as the file, "Sales_Data_Schema". This mockup database was created using a single dataset file; therefore, an ERD was not prepared. Our project's goal is to predict future sales based on the historical data from July 2013 through June 2021.

![Image](https://github.com/shayanafzal/DataMiners/blob/main/Resources/Segment%201/DataMiners_DB.png)

### Files used for creating database

The final version of analysis will utilize pandas to deleting the unwanted columns. For segment 1 deliverable the unwanted columns have been deleted manually in excel. The final file containing only the columns necessary for this analysis can be accessed [here](https://github.com/shayanafzal/DataMiners/blob/bf6a8c03ea1d01bb2228b3789cd478d071deb9c4/Resources/Sales_Data_Raw.csv).

## Machine Learning Components

The following machine learning the models are being explored for this analysis. 

### Prophet

Prophet is a procedure that can be used to forecast time series data. This database works best with time series data that have seasonal affect and for dataset that contains several years of historical data. The raw data set being used for this analysis contains data from year 2013 to 2021, hence they stood out as a good choice. 

### Arima
Arima is another model that has been chosen to create a sales forecast. The results obtained will be analyzed to determine if this is a good model to use for the available data set. 

### Further Analysis
The aforementioned models are being used to forecast the sales. The results given by these methods would be further analyzed and the raw data may be further narrowed down to exclude sales data from the years 2020 and 2021. The current analysis shows that the sales were extremely low in the years 2020 and 2021 due to the effect of the Covid-19 Pandemic. Hence, it may better to exclude this data from the model. Further analysis will be done to see how the data from the pandemic time period affects the forecast.







# Technologies Used
## Data Cleaning and Analysis
Our project will use Pandas and Python for data cleaning, manipulation, integration and analysis. 

## Database Storage
After cleaning and analyzing our data, we will use PostgreSQL server. We will then use a Postgres query to join the data and further connect it to our Machine Learning Model.

## Machine Learning
We will be using the method of linear regression and Prophet for our Machine Learning Model. Also using the seaborn library and Arima

## Dashboard
We will use Javascript & HTML for the dashboard to view and analyze the difference in our snack bar results.







