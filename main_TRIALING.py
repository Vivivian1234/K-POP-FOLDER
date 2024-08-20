
original_df = pd.read_csv('C:/Users/echo2/Documents/kpop_rankings.csv')


#Edit of code
#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

affirmative_responses = ["Yes", "yes", "YES"]

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
original_df = pd.read_csv('kpop_rankings.csv')


KPopRankings_df = pd.read_csv('kpop_rankings.csv')

#----Define Functions Below----#
def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(KPopRankings_df)

def showCharts():
    popularity_df = KPopRankings_df.groupby(['song_title', 'artist']).size().reset_index(name='counts')
    popularity_df = popularity_df.sort_values(by='counts', ascending=False).head(10)
    popularity_df['label'] = popularity_df['song_title'] + ' by ' + popularity_df['artist']
    
    popularity_df.plot(
        kind='bar',
        x='label',
        y='counts',
        color='blue',
        alpha=0.7,
        title='Top 10 Most Popular K-pop Songs',
        legend=False
    )
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Song Title and Artist')
    plt.ylabel('Counts')
    plt.tight_layout()
    plt.show()



def ExtraVariables_DATAFRAME():
    year1 = int(input("Name the year: "))
    remove_others = KPopRankings_df['year'] == year1
    df = KPopRankings_df[remove_others]
    
    print("\nFull Year DataFrame:")
    print(df)
    
    action = input("Would you like to see the top artists and songs? (Yes/No) ")
    if action in affirmative_responses:
        top_number = int(input("Enter how many: "))
        top_songs_df = df.groupby(['song_title', 'artist']).size().reset_index(name='counts')
        top_songs_df = top_songs_df.sort_values(by='counts', ascending=False).head(top_number)
        
        print("\nTop Songs DataFrame:")
        print(top_songs_df)
    else:
        print("No top songs data to display.")



def ExtraVariables_VISUALISED():
    year1 = int(input("Name the year: "))
    filtered_df = KPopRankings_df[KPopRankings_df['year'] == year1]
    action = input("Would you like to see the top artists and songs? (Yes/No) ")
    
    if action in affirmative_responses:
        top_number = int(input("Enter how many: "))
        
        top_artists_df = filtered_df.groupby('artist').size().reset_index(name='counts')
        top_artists_df = top_artists_df.sort_values(by='counts', ascending=False).head(top_number)
        
        top_artists_df.plot(
            kind='bar',
            x='artist',
            y='counts',
            color='blue',
            alpha=0.7,
            title=f'Top {top_number} Artists of {year1}',
            legend=False
        )
        plt.xticks(rotation=45, ha='right')
        plt.xlabel('Artist')
        plt.ylabel('Counts')
        plt.tight_layout()
        plt.show()
        
        print("\nTop Artists DataFrame:")
        print(top_artists_df)
    else:
        filtered_df = filtered_df.groupby('artist').size().reset_index(name='counts')
        filtered_df.plot(
            kind='bar',
            x='artist',
            y='counts',
            color='blue',
            alpha=0.7,
            title=f'Artists of {year1}',
            legend=False
        )
        plt.xticks(rotation=45, ha='right')
        plt.xlabel('Artist')
        plt.ylabel('Counts')
        plt.tight_layout()
        plt.show()



def userOptions():
    global quit

    print("""Welcome to the Top Kpop Rankings from 2011 to 2022!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the most popular kpop songs
    4- Add extra variable [year, top #] (dataframe)
    5- Add extra variable [year, top #] (visualised)
    6 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        elif choice == 2:
            showUpdatedData()
        elif choice == 3:
            showCharts()
        elif choice == 4:
            ExtraVariables_DATAFRAME()
        elif choice == 5:
            ExtraVariables_VISUALISED()
        elif choice == 6:
            quit = True
        else:
            print('A number between 1 and 4, come on!')

    except:
        print('Enter a number, it is not that hard.')

   

#----Main program----#
while not quit:
    userOptions()