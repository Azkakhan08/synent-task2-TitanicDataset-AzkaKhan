# Task 1 - Data Cleaning and Preprocessing
# Dataset  - Titanic Dataset
# Language - Python
# Run      - python task1_titanic_cleaning.py

import pandas as pd
import matplotlib.pyplot as plt

# define data
data = {
    "PassengerId" : [1,  2,  3,  4,  5,  6,  7,  8,  9,  10,
                     11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "Survived"    : [0,  1,  1,  1,  0,  0,  0,  0,  1,  1,
                     1,  1,  0,  0,  0,  1,  0,  1,  0,  1],
    "Pclass"      : [3,  1,  3,  1,  3,  3,  1,  3,  3,  2,
                     3,  1,  3,  3,  3,  2,  3,  2,  3,  3],
    "Name"        : ["Mr. Owen", "Mrs. John", "Miss. Laina", "Mrs. Jacques",
                     "Mr. William", "Mr. James", "Mr. Timothy", "Master. Gosta",
                     "Mrs. Oscar", "Mrs. Nicholas", "Miss. Marguerite", "Miss. Florence",
                     "Mr. Anders", "Mr. Harry", "Miss. Ida", "Mrs. Ernest",
                     "Master. Eugene", "Mr. Francis", "Mrs. Henry", "Mrs. Lily"],
    "Sex"         : ["male", "female", "female", "female", "male",
                     "male", "male", "male", "female", "female",
                     "female", "female", "male", "male", "female",
                     "female", "male", "male", "female", "female"],
    "Age"         : [22, 38, 26, 35, None, None, 54, 2, 27, 14,
                     4,  58, 20, 39, 14,   55,   2, None, 31, None],
    "Fare"        : [7.25, 71.28, 7.92, 53.10, 8.05, 8.46, 51.86, 21.07,
                     11.13, 30.07, 16.70, 26.55, 8.05, 31.27, 7.85, 16.00,
                     29.12, 13.00, 18.00, 7.22],
    "Embarked"    : ["S", "C", "S", "S", "S", "Q", "S", "S",
                     "S", "C", "S", "S", "S", "S", "S", "S",
                     "Q", "S", "S", None],
    "Cabin"       : [None, "C85", None, "C123", None, None, "E46", None,
                     None, None, "G6", "C103", None, None, None, None,
                     None, None, None, None]
}

# create dataframe
df = pd.DataFrame(data)

# show original data
print("==============================")
print("      ORIGINAL DATASET")
print("==============================")
print(df)
print()
print("Shape :", df.shape)
print()

# show missing values before cleaning
print("==============================")
print("   MISSING VALUES BEFORE")
print("==============================")
print(df.isnull().sum())
print()

# handle missing values
# fill Age with median value
df["Age"] = df["Age"].fillna(df["Age"].median())

# fill Embarked with mode value
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# drop Cabin column - too many missing values
df = df.drop(columns=["Cabin"])

# remove duplicate rows
df = df.drop_duplicates()

# convert data types
df["Survived"] = df["Survived"].astype(bool)
df["Pclass"]   = df["Pclass"].astype(str)

# rename columns to lowercase
df = df.rename(columns={
    "PassengerId" : "passenger_id",
    "Survived"    : "survived",
    "Pclass"      : "pclass",
    "Name"        : "name",
    "Sex"         : "sex",
    "Age"         : "age",
    "Fare"        : "fare",
    "Embarked"    : "embarked"
})

# show cleaned data
print("==============================")
print("      CLEANED DATASET")
print("==============================")
print(df)
print()

# show missing values after cleaning
print("==============================")
print("   MISSING VALUES AFTER")
print("==============================")
print(df.isnull().sum())
print()

# save clean dataset
df.to_csv("titanic_clean.csv", index=False)
print("Saved : titanic_clean.csv")
print()

# setup figure and subplots
plt.figure(figsize=(12, 5))

# bar chart - gender distribution
plt.subplot(1, 2, 1)
sex_count = df["sex"].value_counts()
plt.bar(sex_count.index, sex_count.values, color="lightblue", edgecolor="black")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Gender Distribution")

# bar chart - passenger class
plt.subplot(1, 2, 2)
class_count = df["pclass"].value_counts().sort_index()
plt.bar(class_count.index, class_count.values, color="lightgreen", edgecolor="black")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.title("Passenger Class Distribution")

# display
plt.tight_layout()
plt.savefig("task1_output.png")
plt.show()
print("Saved : task1_output.png")
