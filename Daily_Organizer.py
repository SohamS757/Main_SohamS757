import os
import time
import pandas
import Daily_Organizer_Functions as dof

if os.path.exists(r'Daily_Organizer.xlsx') == False:
    with open(r"Daily_Organizer.xlsx",'a+') as age:
        df1 = pandas.DataFrame([['Wake_Up',7,7,0]],index=[5],columns=['Activity ','Start ','End ','Total_Time'])
        df1.to_excel("Daily_Organizer.xlsx",sheet_name='Daily ')
else:
    pass

Start = 7
n = 1
print('Wake Up Time = 7 ')

new_day = input('Do You Want To Start Organizing A New Day?(y/n): ')

if new_day == 'y':
    df1 = pandas.DataFrame([['Wake_Up',7,7,0]],index=[5],columns=['Activity ','Start ','End ','Total_Time'])
    df1.to_excel("Daily_Organizer.xlsx",sheet_name='Daily ')

while True:
    user_input = input('Continue Organizing? (y/n)')

    if user_input == 'y':
        # Collecting Data
        print()
        Activity = input(f'Enter Activity {n}: ')
        Total_Time = input('Enter Working Time (hours): ')
        Total_Time = dof.Checking_float(Total_Time)
        print()
        
        if Total_Time > 0:            
            End = Start + Total_Time

            main_dataframe = dof.exporting_Importing_values(Activity,Start,End,Total_Time)
            n += 1
            Start = End
        else:
            print('Checking Time Value ...')
            time.sleep(10)
            print('Invalid Value, Closing Program ..... \n')
            exit()
    else:
        print('''
        Thank You !! 
        For Using Daily Organizer.
        ''')
        break


access_data = input('Do You Want To Access Data?(y/n): ')
if access_data == 'y':
    print(main_dataframe)
else:
    pass