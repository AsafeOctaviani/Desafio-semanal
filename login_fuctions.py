import time
import menu_functions


def login_sex():
    """
    Docstring for login
    :return: "Female" or "Male"
    This function prompts the user to choose their sex
    param sex: The sex input by the user
    param stripped: trimmed input
    param formatted_sex: formatted input to uppercase first letter
    """
    while True:
        try:
            sex = input("Sex: (F/M): ")
            stripped = sex.strip()
            if not stripped:
                raise ValueError
            formatted_sex = stripped.upper()[0]
            if formatted_sex not in ("F", "M"):
                raise ValueError
        except ValueError:
            menu_functions.line()
            print("\033[31mInput ERROR! Please enter F or M.\033[m")
            continue

        if formatted_sex == 'F':
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("...")
            time.sleep(1)
            return "Female"
        else:
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("...")
            time.sleep(1)
            return "Male"
        


def login(library):
    
    while True:
        try:
            library['first name'] = input("First name:")
        except (ValueError,TypeError,KeyboardInterrupt,IndexError):
            print("\033[31mInput ERROR! Please enter the data correctly.\033[m")

        try:
            library['second name']= input("Second name:")
        except (ValueError,TypeError,KeyboardInterrupt,IndexError):
            print("\033[31mInput ERROR! Please enter the data correctly.\033[m")

            


        
        while True:
            try:
                library['Age']=int(input("Age:"))
                if library['Age']<0:
                    raise ValueError("error! negative age")
                if library['Age']>130:
                    raise ValueError("error! age too high")
            except (ValueError,TypeError,KeyboardInterrupt,IndexError):
                menu_functions.line()
                print("\033[31mInput ERROR! Please enter the data correctly.\033[m")
            else:
                break
        while True:
        
            try:
                    
                library['Passport']=int(input("Passport:"))
            except (ValueError,TypeError,KeyboardInterrupt,IndexError):
                menu_functions.line()
                print("\033[31mInput ERROR! Please enter the data correctly.\033[m")
                continue

            try:
                library["sex"]=login_sex()
            except (ValueError,TypeError,KeyboardInterrupt,IndexError):
                menu_functions.line()
                print("\033[31mInput ERROR! Please enter the data correctly.\033[m")
            else:
                break
        #else:
        
        return library
        



#option01=option()
#print(f"Option chosen: {option01}")
#if option01==False:
#    break