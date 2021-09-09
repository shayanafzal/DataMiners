=======
# Overview
## Introduction
This analysis is being done for business in the snack bar category. For confidentiality reasons the business would be referred to as ‘Snack Brands’ from here onwards. Snack Brands is involved in the manufacturing of chocolate bars. 
## Problem & Proposed Solution.
Snack Brands manufactures chocolate bars for which the procurement time is 8 weeks. Hence, we need to accurately forecast the sales 8 weeks into the future in order to procure the right amount of ingredients and manufacture the snack bars that we can sell after they 8 weeks procurement process. 
To further add value, the model will be used to predict sales 6 month into the future. This will allow Snack Brands to order the ingredients early and obtain better rates.
# Data
Please click here for the raw data set.
## Cleaning the Data Set
The original data set that has been obtained contains data in a number of columns, not all of which are relevant. From the original data set we will only be keeping the columns listed below. A description of the category has also been provided below:

* Year
* Month 
* InvDate - Dales Invoice Number
* InvNumbers – Invoice Numbe
* Market – The sales are broken down into three different regions	
CAN - Canada
US – United States
INTL – International
* InvCustomer – This the customer code
* CompanyName – This is the customer name
* ItemClass – Items are classified into two categories
ORG – manufactured using organic ingredients
CONV – manufactured using conventional ingredients
* SubCategory – The products are devided into the following subcategories
CHOC – Chocolate
F&N - Fruits and Nuts
GRAN - Granola 
LSUG – Low Sugar
PROT – Protein
* Flavours – This is product subcategory
* Product ID
* Product Description
* UOM – Unit of Measurement, that can either be a case or a carton ***********
* Pack ****************
* Real_QTY *******************
* CAD_value – Sales price on the order
# Description of Communication Protocols
The team will be using a private group on Slack as a primary communications protocol. We have set up multiple recurring meeting though out the week to meet up as a team and get the work done. Phone will be used to communicate in case there is an argent need.

## Creation of a database

A mockup database "DataMiners" was created in PG Admin as seen in the below image. The table "sales_data" was created manually using the SQL query saved in the file "Sales_Data_Schema". Since this is a mockup database to be created using a single dataset file, ERD was not prepared. Our project is to predict future sales based on the historical data from July 2013 - June 2021.

![Image](https://github.com/shayanafzal/DataMiners/blob/yashodhan/DataMiners_DB.png)

## Files used for creating database

We did not use pandas for deleting the unwanted columns for this segment deliverable. But we would be using pandas to delete the unwanted columns for the final project code.

1) ![Sales_Data - Only the columns we need](https://github.com/shayanafzal/DataMiners/blob/yashodhan/Sales_Data%20-%20Only%20the%20columns%20we%20need.csv)

