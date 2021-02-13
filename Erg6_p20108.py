import tweepy as tp
import re,string,copy

consumer_key = ''
consumer_secret  = ''

#Function get_tweets:
#Params:auth(OAuthHandler object),username(string).
#Usage: Uses authentication and username to retrieve the last 10 user's tweets.
#Return value: A list with 10 recent user's tweets.
def get_tweets(auth,username):
    
    api = tp.API(auth)

    new_tweets = api.user_timeline(screen_name = username,count=10 , tweet_mode = 'extended')

    #Initialize an empty list
    tweet_text = [] 

    for tweet in new_tweets:

        #Use a regex to remove user mentions and links inside the tweet.
        text = re.sub(r'((?:\@|https?\://)\S+)','', tweet.full_text) 
        #Append the user's tweet into the list that contains the tweets.
        tweet_text.append(text) 

    return tweet_text


#Function split_text:
#Params:tweet_text(string).
#Usage: Uses the users last 10 tweets to generate a list of words.
#Return value: A list with all the words from the user's last 10 tweets.
def split_text(tweet_text):

    #Initialize an empty list
    words = [] 

    for text in tweet_text: 

        #Remove all the punctuation marks from the text in order to acquire only words.
        pun_free_tex = text.translate(str.maketrans('', '', string.punctuation))
        #Add the list of the words formed by splitting the string text.
        words = words + pun_free_tex.split()

    return words

#Function print_max_words:
#Params:words(string).
#Usage: Uses the words from last 10 tweets to print the 5 maximum.
#Return value:None.
def print_max_words(words):

    #copy the words elements so that we don't change them.
    temp = copy.deepcopy(words)

    for i in range(0,5):

        #Find maximum defined by length.
        maximum = max(temp,key=len)
        print (maximum)
        #remove the element so that we can find the next one.
        temp.remove(maximum)

#Function print_min_words:
#Params:words(string).
#Usage: Uses the words from last 10 tweets to print the 5 minimum.
#Return value: None.
def print_min_words(words):

    #copy the words elements so that we don't change them.
    temp = copy.deepcopy(words)

    for i in range(0,5):
        #Find minimum defined by length.
        minimum = min(temp,key=len)
        print (minimum)
        #remove the element so that we can find the next one.
        temp.remove(minimum)
        


auth = tp.OAuthHandler(consumer_key = consumer_key,consumer_secret = consumer_secret)

username = input('Provide the username of the Twitter user:')
tweet_text = get_tweets(auth,username)
words = split_text(tweet_text)

print_max_words(words)
print_min_words(words)
