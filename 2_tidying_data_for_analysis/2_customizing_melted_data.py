""" Customizing melted data
When melting DataFrames, it would be better to have column names more meaningful than variable and value (the default names used by pd.melt()).

The default names may work in certain situations, but it's best to always have data that is self explanatory.

You can rename the variable column by specifying an argument to the var_name parameter, and the value column by specifying an argument to the value_name parameter. You will now practice doing exactly this. Pandas as pd and the DataFrame airquality has been pre-loaded for you. """

""" Instructions
    -   Print the head of airquality.
    -   Melt the columns of airquality with the defaultvariablecolumn renamed to'measurement'and the defaultvaluecolumn renamed to'reading'. You can do this by specifying, respectively, thevarnameandvaluename` parameters.
    -   Print the head of airquality_melt. 
"""

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt.head())
