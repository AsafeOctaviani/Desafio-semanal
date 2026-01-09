import file_handling_funtions
import menu_functions
import yes_no_fuctions
import nps_functions
import login_fuctions


user_data={}
while True:
    option01=menu_functions.choose_option(["Login","Quit"])
    if option01==2:
        yn=yes_no_fuctions.option_quit("Are you sure you want to quit? (Y/N):")
        if yn==True:
            break


    elif option01==1:
        login=login_fuctions.login(user_data)
        user_file0=file_handling_funtions.file_exists(f"User_{user_data['first name']}.txt")
        if user_file0 ==False:
            user_file=file_handling_funtions.create_a_file(f"User_{user_data['first name']}_{user_data['second name']}.txt")
        write=file_handling_funtions.sign_up(f"User_{user_data['first name']}_{user_data['second name']}.txt",user_data['first name'],
        user_data['second name'],user_data['Age'],user_data['Passport'],user_data['sex'])

nps1=nps_functions.nps()

