
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

def ExtraVariables():
    answer = input("Would you like to add a specific time period? ")
    if answer in list:
        year1 = int(input("Name the beginning year. "))
        year2 = int(input("Name the ending year. "))
        year_difference = year2 - year1
        if year_difference == 0:


7




def userOptions():
    global quit

    print("""Welcome to the Kpop!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the most popular kpop songs
    4- Add extra variable [time period, most popular]
    5 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        elif choice == 2:
            showUpdatedData()
        elif choice == 3:
            showCharts()
        elif choice == 3:

        elif choice == 5:
            quit = True
        else:
            print('A number between 1 and 4, come on!')

    except:
        print('Enter a number, it is not that hard.')

   

#----Main program----#
while not quit:
    userOptions()