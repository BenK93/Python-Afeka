"""
Created on Dec 2021
HW assignment 4: pandas and functions
@author: Hadas Lapid
"""
"""
import data structure library
import plotting library
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
create a global empty dataframe named 'db'
create a global list named 'group_names'
create a global list 'side_effects'
create a global pandas Series 'group_means'
create a global dataframe 'side_effect_freqs'
"""
db = pd.DataFrame()
group_names = []
side_effects = []
group_means = pd.Series([])
side_effect_freqs = pd.DataFrame()

""" Q1 """
def init_db(file_name: str) -> pd.DataFrame:  # fill input
    """
    read input csv file ('filename') into global db
    return global dataframe
    """
    global db
    db = pd.read_csv(file_name, index_col=[0])
    return db


""" Q2 """
def find_uniques(vector) -> list:  # fill input
    """
    return unique entries in an input vector, v as list
    hint: use function 'set'
    """
    return list(set(vector))


""" Q3 """
def calc_group_means(feature_col, group_col):  # fill input
    """"
    the function 'calc_group_means' gets a feature column name ('feature_col'),
    and a group column name ('group_col').
    the function updates 'group_names' global
    by calling 'find_uniques' with 'group_col' column from db global as input.
    the function loops over all groups, calculates their respective means
    and updates their mean values in 'group_means' Series
    the function returns 'group_means' global Series.
    """
    group_names.extend(find_uniques(db[group_col]))
    mean_list = []
    for name in group_names:
        data = db.loc[db[group_col] == name]
        mean = data[feature_col].mean()
        mean_list.append(mean)
    global group_means
    group_means = pd.Series(mean_list)
    # means = db.groupby(group_col)[feature_col].mean()
    # group_means = means
    return group_means

""" Q4 """
def calc_side_effects_frequencies():
    """
    'calc_side_effects_frequencies' calculates number of appearances
    of each side effect level in each treatment group
    and stores the appearances in 'side_effect_freqs' global dataframe.
    the function has no inputs and uses global variables for its operations
    for this,
    * the function updates the list of side effect levels, 'side_effects',
    using the function 'find_uniques' on "side effects" column
    * the function updates the list of group names, 'group_names',
    using the function 'find_uniques' on "treatment group" column
    * the function initiates 'side_effect_freqs' dataframe
    with 'group_names' rows and 'side_effects' columns
    * then, the function loops over all groups, and over all side_effect levels
    and counts the number of appearances of each side_effect level in each group,
    the function stores the counts in the right row/column in 'side_effect_freqs' dataframe.
    the function returns 'side_effect_freqs' dataframe
    Hint: sum(boolean vector) gives the sum of all True inserts in the vector
    """
    global side_effect_freqs
    unique_effects = find_uniques(db['side effects'])
    side_effect_freqs = pd.DataFrame(columns=unique_effects, index=group_names)
    for i, group in enumerate(group_names):
        for j, effect_level in enumerate(unique_effects):
            total = db.loc[(db['treatment group'] == group) & (db['side effects'] == effect_level)]
            side_effect_freqs.at[group, effect_level] = len(total)
    return side_effect_freqs

""" Q5 """
def save_side_effect_freqs(filename:str):  # fill input
    """
    the function gets a csv file name ('filename')
    and saves 'side_effect_freqs' global to a csv file including its indexes
    """
    global side_effect_freqs
    side_effect_freqs.to_csv(filename, index=True)


""" Q6 """


def plot_side_effect_freqs():
    """
    the function plots the side-effect frequencies of
    each group in a different color ('a' in black, 'b' in red).
    the function saves the plot under the name "side_effect_freqs.tiff"
    hint: you can assume that there are only two groups, 'a' and 'b'
    hint2: you can use the side-effect level as x-axis and the frequency as y-axis in the pplot
    the function does not require inputs and does not return any value
    """
    range_val = np.arange(1,4)
    plt.bar(range_val - 0.1, side_effect_freqs.loc['a'], 0.2, color='cyan')
    plt.bar(range_val + 0.1,  side_effect_freqs.loc['b'], 0.2, color='green')
    plt.xticks(range_val, ['1', '2', '3'])
    plt.legend(['Team A', 'Team B'])
    plt.show()


""" Q7 Bonus """


def validate_side_effect_freqs():
    """
    frequencies checkup
    validate that the numbers you calculated in 'side_effect_freqs' global
    add up to the total numbers of appearances in all categories for each group
    and in all groups in each category
    (two loops proof required)
    the function does not require any return value,
    just prints out the counts per category/per group
    the function does not require any input
    """
    pass
