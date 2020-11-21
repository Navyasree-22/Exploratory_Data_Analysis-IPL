#importing librariesand load the data
import pandas as pd
ipldf = pd.read_csv("D:/datasets/Indian Premier League/matches.csv")
ipldf.head()
ipldf.info()
#to see summary statistics
ipldf.describe()
#to know number of rows and columns
ipldf.shape
#to find if any null value is present
ipldf.isnull().sum()
#Matches we have got in the dataset.
ipldf['id'].max()
#Seasons we have got in the dataset
ipldf['season'].unique()
len(ipldf['season'].unique())
#Team won by Maximum Runs
ipldf.iloc[ipldf['win_by_runs'].idxmax()]
ipldf.iloc[ipldf['win_by_runs'].idxmax()]['winner']
#Team won by Maximum Wickets
ipldf.iloc[ipldf['win_by_wickets'].idxmax()]['winner']
#Team won by minimum runs
ipldf.iloc[ipldf[ipldf['win_by_runs'].ge(1)].win_by_runs.idxmin()]['winner']
#Team won by Minimum Wickets
ipldf.iloc[ipldf[ipldf['win_by_wickets'].ge(1)].win_by_wickets.idxmin()]
ipldf.iloc[ipldf[ipldf['win_by_wickets'].ge(1)].win_by_wickets.idxmin()]['winner']

#Season Which had most number of matches.
sns.countplot(x='season', data=ipldf)
plt.show()
#Exploratory Analysis and Visualization
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
sns.color_palette("Paired")
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (12, 8)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
#The team with the most number of wins per season
teams_per_season = ipldf.groupby('season')['winner'].value_counts()
teams_per_season
"""
for i, v in win_per_season.iteritems():
    print(i, v)
    
for items in win_per_season.iteritems():
    print(items)    
"""
year = 2008
win_per_season_df = pd.DataFrame(columns=['year', 'team', 'wins'])
for items in teams_per_season.iteritems():    
    if items[0][0]==year:
        print(items)
        win_series = pd.DataFrame({
            'year': [items[0][0]],
            'team': [items[0][1]],
            'wins': [items[1]]
        })
        win_per_season_df = win_per_season_df.append(win_series)
        year += 1
win_per_season_df
sns.barplot('wins', 'team', hue='year', data=win_per_season_df, palette='Paired')
#The most successful IPL team
team_wins_ser = ipldf['winner'].value_counts()

team_wins_df = pd.DataFrame(columns=["team", "wins"])
for items in team_wins_ser.iteritems():
    temp_df1 = pd.DataFrame({
        'team':[items[0]],
        'wins':[items[1]]
    })
    team_wins_df = team_wins_df.append(temp_df1, ignore_index=True)
team_wins_df
import matplotlib.pyplot as plt
import seaborn as sns
plt.title("Total Victories of IPL Teams")
sns.barplot(x='wins', y='team', data=team_wins_df, palette='Paired');
#Most Valuable Player
mvp_ser = ipldf['player_of_match'].value_counts()

mvp_ten_df = pd.DataFrame(columns=["player", "wins"])
count = 0
for items in mvp_ser.iteritems():
    if count>9:
        break
    else:
        temp_df2 = pd.DataFrame({
            'player':[items[0]],
            'wins':[items[1]]
        })
        mvp_ten_df = mvp_ten_df.append(temp_df2, ignore_index=True)
        count += 1
mvp_ten_df
plt.title("Top Ten IPL Players")
sns.barplot(x='wins', y='player', data=mvp_ten_df, palette='Paired');

        
