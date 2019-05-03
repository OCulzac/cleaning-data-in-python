""" Custom functions to clean data
You'll now practice writing functions to clean data.

The tips dataset has been pre-loaded into a DataFrame called tips. It has a 'sex' column that contains the values 'Male' or 'Female'. Your job is to write a function that will recode 'Female' to 0, 'Male' to 1, and return np.nan for all entries of 'sex' that are neither 'Female' nor 'Male'.

Recoding variables like this is a common data cleaning task. Functions provide a mechanism for you to abstract away complex bits of code as well as reuse code. This makes your code more readable and less error prone.

As Dan showed you in the videos, you can use the .apply() method to apply a function across entire rows or columns of DataFrames. However, note that each column of a DataFrame is a pandas Series. Functions can also be applied across Series. Here, you will apply your function over the 'sex' column.

Instructions
100 XP
Instructions
100 XP
Define a function named recode_gender() that has one parameter: gender.
If gender equals 'Male', return 1.
Else, if gender equals 'Female', return 0.
If gender does not equal 'Male' or 'Female', return np.nan. NumPy has been pre-imported for you.
Apply your recode_gender() function over tips.sex using the .apply() method to create a new column: 'recode'. Note that when passing in a function inside the .apply() method, you don't need to specify the parentheses after the function name.
Hit 'Submit Answer' and take note of the new 'gender_recode' column in the tips DataFrame! """


# Define recode_gender()
def recode_gender(gender):

    # Return 0 if gender is 'Female'
    if gender == 'Female':
        return 0
    
    # Return 1 if gender is 'Male'    
    elif gender == 'Male':
        return 1
    
    # Return np.nan    
    else:
        return np.nan

# Apply the function to the sex column
tips['recode'] = tips.sex.apply(recode_gender)

# Print the first five rows of tips
print(tips.head())
