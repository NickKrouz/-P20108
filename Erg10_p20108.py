import ast

#Function depth_count:
#Params:iterable(dictionary or list),checked(boolean),depth(integer).
#Usage: A recursive function that searches through every iterable object for nested iterables.
#Return value: The depth of the dictionary.
def depth_count(iterable,checked,depth):

    

    #If the iterable is not empty and there isn't another iterable already found in the parent iterable increase depth.
    if (len(iterable) !=0 ) and not checked:

        depth+=1
    #initialize the value of checked in case there are iterables inside this one.
    elif checked:

        checked=False
    
    #initialize a dep value to use in the recursive call of the function.
    dep = depth 

    for item in iterable:
        #Check if item is a list or a dictionary.
        if isinstance(iterable,list):

            if isinstance(item,(list,dict)):
                #recursive call the function giving it the newfound iterable.
                dep = depth_count(item,checked,dep)
                #set the value of checked true in case there is another iterable inside this list
                checked = True

        elif isinstance(iterable,dict):

            if isinstance(iterable[item],(list,dict)):
                #recursive call the function giving it the newfound iterable.
                dep = depth_count(iterable[item],checked,dep)
                #set the value of checked true in case there is another iterable inside this dictionary
                checked = True
    
    return dep


depth = 0
checked = False
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


depth = depth_count(diction,checked,depth)
print('Depth of dictionary '+str(diction)+':',depth)