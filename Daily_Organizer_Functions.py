import pandas
import time
import os

def Checking_integer(numberr):    
    try:
        numberr = int(numberr)
        return numberr
    except ValueError:
        print('Checking Value ...\n')
        time.sleep(10)
        print('Invalid-Input ... Closing Program')
        exit()

def Checking_float(numberr):    
    try:
        numberr = float(numberr)
        return numberr
    except ValueError:
        print('Checking Value ...\n')
        time.sleep(10)
        print('Invalid-Input ... Closing Program')
        exit()

def exporting_Importing_values(Activity,Start,End,Total_Time):
    global main_df
    main_df = pandas.read_excel(r'Daily_Organizer.xlsx')
    
    main_df_t = main_df.T
    main_df_t[Activity] = [None,Activity,Start,End,Total_Time]
    main_df = main_df_t.T
    main_df = main_df.drop('Unnamed: 0',1)
        
    df_mean = main_df.mean(axis=0)
    main_df.to_excel("Daily_Organizer.xlsx",sheet_name='Daily ')
    return main_df