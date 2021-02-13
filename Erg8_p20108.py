import ast,requests


#Function crypto_to_euro:
#Params:diction(dictionary).
#Usage: A function that uses a dictionary of cryptocurrency and an api to calculate and print the value of the user's cryptocurrency.
#Return value: None.
def crypto_to_euro(diction):
    # Create the string of requested cryptocurrency to pass it as an argument.
    str_crypto = ''

    for key in diction:

        str_crypto += str(key)+','

    #Remove the last comma from the string
    str_crypto = str_crypto[0:len(str_crypto)-1]

    #Make the request to min-api
    req = requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms='+ str_crypto + '&tsyms=EUR')
    
    prices_dict = ast.literal_eval(req.text)

    #Compute the current values and display the on screen message.
    for key in diction:

        value = diction[key] * prices_dict[key]['EUR']
        print(str(key)+' value=',value)




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

crypto_to_euro(diction)