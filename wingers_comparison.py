import Dataframe_Creation

df=main_data()

def wingers_dataframe():
    """defining a dataset containing only stats helpful to gauge the best wingers"""
    df = main_data()
    df = df[[( 'Unnamed: 1_level_0',  'Player'), ( 'Unnamed: 3_level_0',     'Pos'),
             ( 'Unnamed: 4_level_0',   'Squad'), ( 'Unnamed: 5_level_0',    'Comp'),
             ( 'Unnamed: 6_level_0',     'Age'), ( 'Unnamed: 8_level_0',     '90s'),
             (              'Total',    'Cmp%'), (              'Total', 'PrgDist'),
             ('Unnamed: 23_level_0',     'Ast'), ('Unnamed: 24_level_0',      'xA'),
             ('Unnamed: 26_level_0',      'KP'), ('Unnamed: 27_level_0',     '1/3'),
             ('Unnamed: 28_level_0',     'PPA'), ('Unnamed: 29_level_0',   'CrsPA'),
             ('Unnamed: 30_level_0',    'Prog'), ( 'Touches', 'Att 3rd'),
             ( 'Touches', 'Att Pen'), ('Dribbles',     'Att'), ('Dribbles',   'Succ%'),
             ('Dribbles',     '#Pl'), ( 'Carries', 'Carries'), ( 'Carries', 'TotDist'),
             ( 'Carries', 'PrgDist'), ( 'Carries',    'Prog'), (  'Carries',     '1/3'),
             (  'Carries',     'CPA'), (  'Carries',     'Mis'), (  'Carries',     'Dis'),
             ('Receiving',    'Targ'), ('Receiving',     'Rec'), ('Receiving',    'Rec%'),
             ('Receiving',    'Prog'), (  'Standard',     'Gls'), (  'Standard',   'Sh/90'),
             (  'Standard',    'SoT%'), (  'Standard',    'G/Sh'), (  'Standard',   'G/SoT'),
             ('Performance', 'Gls'), ('Performance', 'Ast'), (  'Expected_x',      'xG'),
             (  'Expected_x',    'npxG'), (  'Expected_x', 'npxG/Sh'), ('Per 90 Minutes',     'Gls'),
             ('Per 90 Minutes',     'Ast'), ('Per 90 Minutes',     'G+A'), ('Per 90 Minutes',    'G-PK'),
             ('Per 90 Minutes',  'G+A-PK'), (    'Expected_y',      'xG'), (    'Expected_y',    'npxG'),
             (    'Expected_y',      'xA'), (    'Expected_y', 'npxG+xA'), ('Per 90 Minutes',      'xG'),
             ('Per 90 Minutes',      'xA'), ('Per 90 Minutes',   'xG+xA'), (            'Tackles',     'Tkl'),
             ('Vs Dribbles', 'Tkl%'), (          'Pressures',   'Press'), (          'Pressures',       '%'),
             ('Unnamed: 28_level_0', 'Int')
             ]]
    df = df[(df[('Unnamed: 3_level_0',    'Pos')] == 'MFFW')|(df[('Unnamed: 3_level_0',    'Pos')] == 'FW')]
    return df




df_wingers = main_data()
df_wingers.columns[0:5]
df_messi = df_wingers[df_wingers[('Unnamed: 1_level_0', 'Player')] == 'Lionel Messi']