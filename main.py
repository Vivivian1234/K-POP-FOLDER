

#Edit of code
#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

affirmative_responses = ["Yes", "yes", "YES", "yeas", "yeah", "yea", "yep", "YEAS", "YEAH", "YEA", "YEP", "yuppers"]

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
original_df = pd.read_csv('kpop_ranking.csv')


KPopRankings_df = pd.read_csv('kpop_ranking.csv')

#----Define Functions Below----#
def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(KPopRankings_df)

def showCharts():
    popularity_df = KPopRankings_df.groupby(['Song Title', 'Artist(s)']).size().reset_index(name='counts')
    popularity_df = popularity_df.sort_values(by='counts', ascending=False).head(10)
    popularity_df['label'] = popularity_df['Song Title'] + ' by ' + popularity_df['Artist(s)']
    
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
    SECONDfiltered_df = KPopRankings_df[KPopRankings_df['Year'] == year1]
    action = input("Would you like to see the top artists and songs? (Yes/No) ")
    
    if action in affirmative_responses:
        top_number = int(input("Enter how many: "))
        top_songs_df = SECONDfiltered_df.groupby(['Song Title', 'Artist(s)']).size().reset_index(name='counts')
        top_songs_df = top_songs_df.sort_values(by='counts', ascending=False).head(top_number)

        print("\nFull Year DataFrame:")
        print(SECONDfiltered_df)  
        print("\nTop Songs DataFrame:")
        print(top_songs_df)
    else:
        print("\nFull Year DataFrame:")
        print(SECONDfiltered_df)



def ExtraVariables_VISUALISED():
    year1 = int(input("Name the year: "))
    filtered_df = KPopRankings_df[KPopRankings_df['Year'] == year1]
    action = input("Would you like to see the top artists and songs? (Yes/No) ")
    
    if action in affirmative_responses:
        top_number = int(input("Enter how many: "))
        top_artists_df = filtered_df.groupby('Artist(s)').size().reset_index(name='counts')
        top_artists_df = top_artists_df.sort_values(by='counts', ascending=False).head(top_number)

        print("\nTop Artists DataFrame:")
        print(top_artists_df)

        top_artists_df.plot(
            kind='bar',
            x='Artist(s)',
            y='counts',
            color='blue',
            alpha=0.7,
            title=f'Top {top_number} Artists of {year1}',
            legend=False
        )
        plt.xticks(rotation=45, ha='right')
        plt.xlabel('Artist(s)')
        plt.ylabel('Counts')
        plt.tight_layout()
        plt.show()
        

    else:
        filtered_df = filtered_df.groupby('Artist(s)').size().reset_index(name='counts')
        filtered_df.plot(
            kind='bar',
            x='Artist(s)',
            y='counts',
            color='blue',
            alpha=0.7,
            title=f'Artists of {year1}',
            legend=False
        )
        plt.xticks(rotation=45, ha='right')
        plt.xlabel('Artist(s)')
        plt.ylabel('Counts')
        plt.tight_layout()
        plt.show()



def userOptions():
    global quit

    print("""\nWelcome to the Top Kpop Rankings from 2011 to 2023!
          
    Please select an option:
    1 - Show the original dataset
    2 - Visualise the most popular kpop songs
    3- Add extra variable [year, top #] (dataframe)
    4- Add extra variable [year, top #] (visualised)
    5 - Quit Program
        """)
    
    choice = int(input('Enter Selection: '))
    
    if choice == 1:
        showOriginalData()
    elif choice == 2:
        showCharts()
    elif choice == 3:
        ExtraVariables_DATAFRAME()
    elif choice == 4:
        ExtraVariables_VISUALISED()
    elif choice == 5:
        quit = True
    else:
        print('A number between 1 and 6, come on!')

   

#----Main program----#
while not quit:
    userOptions()