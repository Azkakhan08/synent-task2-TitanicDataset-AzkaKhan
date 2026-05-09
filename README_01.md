# Task 1 - Data Cleaning and Preprocessing

## Problem Statement
Raw data is always messy. It contains missing values, duplicate rows and wrong data types. Before we can analyze any dataset we must clean it properly. In this task we clean the Titanic dataset and prepare it for analysis.

---

## Dataset Details

 Field        -> Details                      
---------------------------------------------
 Dataset Name --> Titanic Dataset              
 Total Rows   --> 20 passengers                
 Total Columns    --> | 9 columns                   
 Source       -->  Defined inside the code      

 Column Name  -->  Description                                      
--------------------------------------------------------------
 PassengerId  -->  Unique ID of passenger                           
 Survived     -->  0 = Did not survive  1 = Survived                
 Pclass       -->  Passenger class 1 2 or 3                         
 Name         -->   Name of passenger                                
 Sex          --> male or female                                   
 Age          --> Age of passenger  some values missing            
 Fare         --> Ticket price                                     
 Embarked     -->  Port of boarding  some values missing            
 Cabin        |--> Cabin number  mostly missing                     

---

## Approach

Step 1 - Define data as dictionary and create DataFrame

Step 2 - Show missing values before cleaning

Step 3 - Fill missing Age with median value

Step 4 - Fill missing Embarked with mode value

Step 5 - Drop Cabin column because 80 percent values are missing

Step 6 - Remove duplicate rows

Step 7 - Convert Survived to boolean and Pclass to string

Step 8 - Rename all columns to lowercase

Step 9 - Save cleaned data as titanic_clean.csv

Step 10 - Create bar charts for gender and passenger class

---

## Results

 Task                  |             Result                          
------------------------------------------------------
Missing values before | Age = 4  Embarked = 1  Cabin = many 
 Missing values after  | 0 missing values                
Duplicates removed    | 0                               
Final shape           | 20 rows x 8 columns             
Output file           | titanic_clean.csv               
Chart saved           | task1_output.png                
