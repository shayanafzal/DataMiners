# Overview

[Presentation](https://docs.google.com/presentation/d/1LgEP1iabjOZd_n9z482B2Ra9EhcuanqxWKVCodDJ5jM/edit#slide=id.gebf57a60df_0_0)

[Dashboard Blueprint](https://docs.google.com/presentation/d/1nNB0tEEfZtC7Wzha4ysZ-Lvb9UOqLQpGOTRMRIGp7wk/edit#slide=id.gecfb9a4986_0_85)

## Introduction
This analysis is being done for business in the snack bar category. For confidentiality reasons the business would be referred to as ‘Snack Brands’ from here onwards. Snack Brands manufactures a varity of snack bars. 

## Problem & Proposed Solution.
Snack Brands manufactures chocolate bars for which we have to respect the procurement and production lead times and the working capital management aspect. Hence, we need to accurately forecast the sales into the future in order to identify the potential cash outflow based on the agreed payment terms with the vendors and also manage inventory with respect to the inventory turnover.To further add value, the model will be used to predict sales 24 months into the future. This will allow Snack Brands to order the ingredients early, obtain better ingredient prices and manage inventory levels.

# Description of Communication Protocols

The following communication tools will be used when working on this project

1. A private group on Slack will be used as a primary communications protocol. 
2. Recurring Zoom calls have been setup to collaborate and communicate
3. Phone will be used to communicate in case there is an urgent need.


# Data

## Raw Data Set

The raw data used for this analysis can be accessed [here](https://github.com/shayanafzal/DataMiners/blob/a17ea5362ba60a61753ce50b6ce491bb05168e33/Sales_Data_Raw.csv).

## Cleaning the Data Set
The original data set that has been obtained contains data in a number of columns, not all of which are relevant. From the original data set we will only be keeping the columns listed below. A description of the category has also been provided below:

* Year
* Month 
* InvDate - Sales Invoice Number
* InvNumber – Invoice Numbe
* Market – The sales are broken down into three different regions	
	* CAN - Canada
	* US – United States
	* NTL – International
* InvCustomer – This the customer code
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
* Flavours – This is product subcategory
* Product ID
* Product Description
* UOM – Unit of Measurement, that can either be pack or a carton as indicated in the column.
* Pack -
* Real_QTY - this indicates the total number of snack bars on the sales order regardless of wheather they were sold as a case or a caron
* CAD_value – Sales price on the order


# Coding 

The coding can be accessed [here](https://github.com/shayanafzal/DataMiners/blob/65c90f04cfc6d1c089585cc2a698855caca71611/Code.ipynb).

## Database

### Creation of a database

A mockup database "DataMiners" was created in PG Admin as seen in the below image. The table "sales_data" was created manually using the SQL query saved in the file "Sales_Data_Schema". A single flat file was created using SQL for the purposes of this project. To respect the confidentiality of the database, a mockup ERD is prepared to explain the rationale behind the tables in the database from which the flat file was created. Multiple SQL joins were used to create a flat file named "Sales_Data_Raw" Our project is to predict future sales based on the historical data from July 2013 - June 2021.

![Image](https://github.com/shayanafzal/DataMiners/blob/main/Resources/Segment%201/DataMiners_DB.png)

The ERD diagram is as follows :- 

![Image](https://github.com/shayanafzal/DataMiners/blob/main/Resources/Segment%201/ERD.png)

The flat file was created by joining the customers, product, sales_price_list and the invoice_lines tables.

### Files used for creating databaset

The final version of analysis will utilize pandas to deleting the unwanted columns. For segment 1 deliverable the unwanted columns have been deleted manually in excel. The final file containing only the columns necessary for this analysis can be accessed [here](https://github.com/shayanafzal/DataMiners/blob/bf6a8c03ea1d01bb2228b3789cd478d071deb9c4/Resources/Sales_Data_Raw.csv).

## Machine Learning Components

The following machine learning the models are being explored for this analysis. 

### Prophet

Prophet is a library that can be used to forecast time series data. This database works best with time series data that have seasonal affect and for dataset that contains several years of historical data. The raw data set being used for this analysis contains data from year 2013 to 2021, hence they stood out as a good choice. 

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







