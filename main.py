
#Edit of code
#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

list = ["Yes", "yes", "YES"]

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
    KPopRankings_df.plot(
                    kind='bar',
                    x='Artist',
                    y='Number of times trending',
                    color='blue',
                    alpha=0.3,
                    title='Artist popularity')
    plt.show()

def ExtraVariables_DATAFRAME():
    answer = input("Would you like to choose a specific year? ")
    if answer in list:
        year1 = int(input("Name the year: "))
        remove_others = KPopRankings_df['year'] == year1
        df = KPopRankings_df[~remove_others]
        action = input("Would you like to to see the top artists and songs?")
        if action in list:
            top_number = int(input("Enter how many: "))

            print ("Output:")
            print(df)
            print(df.head(top_number))
        else:
            print(df)

    elif answer not in list:
        action = input("Would you like to to see the top artists and songs?")
        if action in list:
            top_number = int(input("Enter how many: "))
            print(KPopRankings_df.head(top_number))
        else:
            print ("Why did you type '4' if you're not going to add any extra variable then.")


def ExtraVariables_VISUALISED():
    answer = input("Would you like to choose a specific year? ")
    if answer in list:
        year1 = int(input("Name the year: "))
        remove_others = KPopRankings_df['year'] == year1
        df = KPopRankings_df[~remove_others]
        df_visualased = df.plot
        action = input("Would you like to to see the top artists and songs?")
        if action in list:
            top_number = int(input("Enter how many: "))

            print ("Output:")
            plt.show(df)
            print(df.head(top_number))
        else:
            plt.show(df)

    elif answer not in list:
        action = input("Would you like to to see the top artists and songs?")
        if action in list:
            top_number = int(input("Enter how many: "))
            print(KPopRankings_df.head(top_number))
        else:
            print ("Why did you type '5' if you're not going to add any extra variable then.")

def ExtraVariables():
    answer = input("Would you like to add a specific time period? ")
    if answer in list:
        year1 = int(input("Name the beginning year. "))
        year2 = int(input("Name the ending year. "))
        year_difference = year2 - year1
        if year_difference == 0:
            print("HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


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