from instagrapi import Client
from argparse import ArgumentParser

import datetime

FOLLOWERS_FILE = "followers.txt"
FOLLOWING_FILE = "following.txt"
USER_FILE = "user.txt"

#print user info
def _print_user_info(data):
    print("User info: {")
    for key, value in data.items():
        print("\t%s: %s" % (key, value))
    print("}")

# get user info
def get_user_info(client, user_id):
    user = client.user_info(user_id)
    return user

# get user id from username
def get_user_id_from_name(client, username):
    id = client.user_id_from_username(username)
    return id  

# get following usernames
def get_following_usernames(client, user_id, amount = 0):
    following = client.user_following(user_id, amount=amount)   #get following
    return [user.username for user in following.values()]

# get followers usernames
def get_followers_usernames(client, user_id, amount = 0):
    followers = client.user_followers(user_id, amount=amount)   #get followers
    return [user.username for user in followers.values()]

# filter users that don't follow you back
def following_not_follower(followers, following):
    return [fllwng for fllwng in following if fllwng not in followers]

# filter users that you don't follow back
def follower_not_following(followers, following):
    return [fllwr for fllwr in followers if fllwr not in following]

# save data to file
def save_to_file(data, file, title):
    with open(file, 'a') as f:  #open file on append mode
        f.write(f"[LOG]: {str(datetime.datetime.now())}")  #write date and time
        f.write("\n[---------------------------- %s ----------------------------]\n" % title)   #print title
        if isinstance(data, list):  #if data is a list
            for item in data:
                f.write("%s\n" % item)  #write each item
        elif isinstance(data, dict):   #if data is a dictionary
            f.write("{\n")
            for key, value in data.items():
                f.write("\t%s: %s\n" % (key, value))    #write each key and value
            f.write("}\n")
        else:
            f.write("%s\n" % data)  #write data
        
        f.write("-" * 100 + "\n\n") #write separator

# main function
if __name__ == '__main__':
    try:
        #define argument parser 
        parser = ArgumentParser(prog='instagram_follow.py') 

        #mutually exclusive group for options (following, followers or all)
        options = parser.add_mutually_exclusive_group(required = True)

        #user info (-u or --user)
        options.add_argument('-u', '--user', action='store_true', help="Get USER info")
        #followers  (-wrs or --followers)
        options.add_argument('-wrs', '--followers', action='store_true',  help='Get FOLLOWERS usernames and FOLLOWERS NOT FOLLOWING')
        #following  (-wng or --following)
        options.add_argument('-wng', '--following', action='store_true',  help="Get FOLLOWING usernames and FOLLOWING NOT FOLLOWERS")
        #followers and following (-a or --all)
        options.add_argument('-a', '--all', action='store_true', help="Get FOLLOWERS and FOLLOWING usernames")
        

        #target user (-u or --user)
        parser.add_argument('-un', '--username', nargs= 1, type = str, required=True, help='Target USER that will be inspected')
        
        #user and password 
        parser.add_argument('-l', '--login', nargs= 2, type = str, required=True, help='USER and PASSWORD for login')

        #save results to file (-s or --save)
        parser.add_argument('-s', '--save', action='store_true',  help='SAVE retrieved info to a file or files')

        #process parameters
        args = parser.parse_args()   

        print("Received arguments: ",args, "\n")    #print received arguments

        #login class
        cl = Client()

        cl.login(args.login[0], args.login[1])  #personal account

        #get user id
        user_id = get_user_id_from_name(cl, args.username[0]) 

        print("User ID: ", user_id) #print User ID

        user_info = get_user_info(cl, user_id).dict()  # get user info

        print("\nNumber of followers: ", user_info["follower_count"], " Number of following: ", user_info["following_count"]) #print number of followers

        if user_info["is_private"]: #if account is private
            raise Exception("Account is private. Try follow the account first.")    #raise exception
        
        
        followers = get_followers_usernames(cl, user_id)    #get a list of followers

        following = get_following_usernames(cl, user_id)    #get a list of following


        if args.user:   #user info option
            _print_user_info(user_info)    #print user info

            if args.save:
                save_to_file(user_info, USER_FILE, "USER INFO")  #save user info to "user.txt"

        if args.followers:  #followers option
            print("\nFollowers: ",followers)    #print followers    
            not_following = follower_not_following(followers, following)    #get users not following but followers
            print("\nFollower but not following: ", not_following)  #print not following

            if args.save:
                save_to_file(followers, FOLLOWERS_FILE, "FOLLOWERS")    #save followers to "followers.txt"
                save_to_file(not_following, FOLLOWERS_FILE, "FOLLOWERS NOT FOLLOWING")  #save not following to "followers.txt"

        if args.following:     #following option    
            print("\nFollowing: ",following)    #print following
            not_follower = following_not_follower(followers, following) #get users following but not followers
            print("\nFollowing but not follower: ", not_follower)   #print not follower

            if args.save:
                save_to_file(following, FOLLOWING_FILE, "FOLLOWING")    #save following to "following.txt"
                save_to_file(not_follower, FOLLOWING_FILE, "FOLLOWING NOT FOLLOWERS")   #save not follower to "following.txt"

        if args.all:    #user, followers and following option
            _print_user_info(user_info)    #print user info

            print("\nFollowers: ",followers)    #print followers    
            not_following = follower_not_following(followers, following)    #get users not following but followers
            print("\nFollower but not following: ", not_following)  #print not following
            
            print("\nFollowing: ",following)    #print following
            not_follower = following_not_follower(followers, following) #get users following but not followers
            print("\nFollowing but not follower: ", not_follower)   #print not follower

            if args.save:
                save_to_file(user_info, USER_FILE, "USER INFO")  #save user info to "user.txt"
                save_to_file(followers, FOLLOWERS_FILE, "FOLLOWERS")    #save followers to "followers.txt"
                save_to_file(not_following, FOLLOWERS_FILE, "FOLLOWERS NOT FOLLOWING")  #save not following to "followers.txt"
                save_to_file(following, FOLLOWING_FILE, "FOLLOWING")    #save following to "following.txt"
                save_to_file(not_follower, FOLLOWING_FILE, "FOLLOWING NOT FOLLOWERS")   #save not follower to "following.txt"

    
    except Exception as e:
        if hasattr(e, 'message'):
            print(f'\033[91m[ERROR]: {e.message}\033[00m')  #print exception message
        else:
            print(f'\033[91m[ERROR]: {e}\033[00m')  #print exception message
