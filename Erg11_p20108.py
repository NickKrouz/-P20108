import ast


#Function key_count:
#Params:iterable(dictionary or list),key_dict(dictionary).
#Usage: A recursive function that searches through every iterable object for all the keys and constructs a dictionary of key frequency.
#Return value: None.
def key_count(iterable,key_dict):

    

    for item in iterable:
        #Check if item is a list or a dictionary.
        if isinstance(iterable,list):

            if isinstance(item,(list,dict)):
                #recursive call the function giving it the newfound iterable.
                key_count(item,key_dict)
                

        elif isinstance(iterable,dict):
            #If the key is already found increase its frequency by one,else initialize it to 1.
            if (item not in key_dict):
                key_dict[item] = 1
            else:
                key_dict[item] += 1

            if isinstance(iterable[item],(list,dict)):
                #recursive call the function giving it the newfound iterable.
                key_count(iterable[item],key_dict)



#Function most_used_key:
#Params:key_dict(dictionary)
#Usage: It uses a dictionary of keys and how often the appear to determine the max frequency that a key appears
#Return value: None
def most_used_key(key_dict):

    #Find the max frequency 
    max_freq = max(key_dict.values(),key=int)

    #Find the key with max frequency and print it.
    for item in key_dict:
        if max_freq == key_dict[item]:
            print('The most frequent key is:\t'+ item)





#create an error check for correct data.
error_check = True

while error_check:

    try:

        filepath = input('Provide a file path:')

        with open(filepath,"r") as f:
        
            try:
                #read and convert data to dictionary.
                diction = ast.literal_eval(f.readline())
        
                if isinstance(diction,dict):
                    #If the data is correct set the flag to exit the loop.
                    error_check = False
                else:
        
                    print('The file you provided does not contain a dictionary. Please try again.')
        
            except ValueError as e:
        
                print('The file you provided does not contain a dictionary. Please try again.')
        
    except IOError as e:
        
        print(e.strerror+'.',"Try again.")



key_dict = {}

key_count(diction,key_dict)

most_used_key(key_dict)