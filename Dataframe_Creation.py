import numpy as np
import pandas as pd

def main_data():

    """
    This function combines all the datasets into one unified dataset that we can use to compare any attacking player
    """


    passing = pd.read_csv('passing.txt', header = [0,1]).iloc[:,1:-2]
    dribbles = pd.read_csv('dribbles.txt', header=[0,1]).iloc[:,1:-2]
    shooting = pd.read_csv('shooting.txt', header=[0,1]).iloc[:,1:-2]
    xG = pd.read_csv('xG.txt', header=[0,1]).iloc[:,1:-2]
    xG[('Unnamed: 8_level_0',    '90s')] = xG[(      'Playing Time',    '90s')]
    defensive_work = pd.read_csv('defensive_work.txt', header=[0,1]).iloc[:,1:-2]

    df_list = [passing, dribbles, shooting, xG, defensive_work]


    joined = pd.merge(passing, dribbles, on = [('Unnamed: 1_level_0', 'Player'), ('Unnamed: 2_level_0', 'Nation'),
                                               ('Unnamed: 3_level_0',    'Pos'), ('Unnamed: 4_level_0',  'Squad'),
                                               ('Unnamed: 5_level_0',   'Comp'), ('Unnamed: 6_level_0',    'Age'),
                                               ('Unnamed: 7_level_0',   'Born'),
                                               ('Unnamed: 8_level_0',    '90s')]).merge(shooting, on = [('Unnamed: 1_level_0', 'Player'),
                                                                                                        ('Unnamed: 2_level_0', 'Nation'),
                                                                                                        ('Unnamed: 3_level_0',    'Pos'),
                                                                                                        ('Unnamed: 4_level_0',  'Squad'),
                                                                                                        ('Unnamed: 5_level_0',   'Comp'),
                                                                                                        ('Unnamed: 6_level_0',    'Age'),
                                                                                                        ('Unnamed: 7_level_0',   'Born'),
                                                                                                        ('Unnamed: 8_level_0',    '90s')]).merge(xG, on = [('Unnamed: 1_level_0', 'Player'), ('Unnamed: 2_level_0', 'Nation'), ('Unnamed: 3_level_0',    'Pos'), ('Unnamed: 4_level_0',  'Squad'), ('Unnamed: 5_level_0',   'Comp'), ('Unnamed: 6_level_0',    'Age'), ('Unnamed: 7_level_0',   'Born'), ('Unnamed: 8_level_0',    '90s')]).merge(defensive_work, on = [('Unnamed: 1_level_0', 'Player'), ('Unnamed: 2_level_0', 'Nation'), ('Unnamed: 3_level_0',    'Pos'), ('Unnamed: 4_level_0',  'Squad'), ('Unnamed: 5_level_0',   'Comp'), ('Unnamed: 6_level_0',    'Age'), ('Unnamed: 7_level_0',   'Born'), ('Unnamed: 8_level_0',    '90s')])

    return joined



