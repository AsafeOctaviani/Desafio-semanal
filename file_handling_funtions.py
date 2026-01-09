from menu_functions import menu,line



def file_exists(file_name):
    #print(f"Checking if the file {file_name} exists")
    try:
         file=open(file_name,"rt")
         file.close()

    except FileNotFoundError as fnf_error:
        return False
    
    else:
        return True
    


def create_a_file(file_name):
    #try:
        file=open(file_name,"wt+")
        file.close()
        #print(f"Creating a file named {file_name}")
    #except Exception as error:
        #print(f"An error occurred while creating the file: {error}")
    #else:
        #print(f"File {file_name} created successfully.")



def read_file(file_name):
    try:
        reading=open(file_name,"rt")
    except Exception as error:
        print(f"An error occurred while trying to read the file: {error}")
    else:
        #menu(file_name.upper())
        # print(reading.readlines())
        for c in reading:
            data=c.split(";")
            data[1]=data[1].replace("\n","")
            print(f"Name: {data[0]:<30} Age: {data[1]:>3} years")



def sign_up(file_name,name="unknown",second_name="unknown",age=0,passport=0,sex="unknown"):
    try:
        file=open(file_name,"at")
    except:
        print(f"An error occurred while trying to write to the file:")
    else:
        list_data=[name,second_name,age,passport,sex]
        list_str=["Name","Second Name","Age","Passport","Sex"]
        
        try:
            for c in range(len(list_data)):
                file.write(f"{list_str[c]:<15}: {list_data[c]}\n")
            # for c in list_data:
                
            #     file.write(f"{str(c)}\n")
            #file.write(f"{name};{second_name};{age};{passport};{sex}\n")
        except:
            print("An error occurred while trying to write the data.")
        else:
            print(f"User {name} {second_name} added successfully.")
            file.close()


