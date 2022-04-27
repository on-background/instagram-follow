# instagram-follow

**READ ALL THIS FILE BEFORE USING THE CODE**

Get Instagram user, followers and following info and a list of followers not following or following not followers. Enjoy :)

**IMPORTANT**: This code only works with public Instagram accounts or with people who you are following (if you log into your account).

The default login uses ***datascrape_*** public account, so be respectful of your actions.

# dependencies
- [Instagrapi](https://adw0rd.github.io/instagrapi/):

  ```pip install instagrapi```

# usage

**instagram_follow.py [-h] (-u | -wrs | -wng | -a) -un USERNAME [-l LOGIN LOGIN] [-s]**

**arguments**:
<pre>
-   -h or --help                                 Print HELP
-   -u or --user                                 Get USER info
-   -wrs or --followers                          Get FOLLOWERS usernames and FOLLOWERS NOT FOLLOWING 
-   -wng or --following                          Get FOLLOWING usernames and FOLLOWING NOT FOLLOWERS
-   -a or --all                                  Get FOLLOWERS and FOLLOWING usernames
-   -un USERNAME or --username  USERNAME         Target USER that will be inspected
-   -l USER PASSWORD or --login USER PASSWORD    USER and PASSWORD for login
-   -s or --save                                 SAVE retrieved info to a file or files
</pre>

# examples

- If you want to retrieve *Cristiano Ronaldo* user info and save it to a file:</br>
  ```python3 instagram_follow.py -u -un cristiano -s```
  or
  ```python3 instagram_follow.py --user --username cristiano --save```

- If you want to get *Cristiano Ronaldo* followers and followers that his is not following: </br>
  ```python3 instagram_follow.py -wrs -un cristiano ```
  or
  ```python3 instagram_follow.py --followers --username cristiano ```
  

- If you want to get *Cristiano Ronaldo* following and followers that are not following him and store this info:</br>
  ```python3 instagram_follow.py -wng -un cristiano -s```
  or
  ```python3 instagram_follow.py --following --username cristiano --save```
  
- If you want to get *Cristiano Ronaldo* following, followers and user info besides not following and not follower:</br>
  ```python3 instagram_follow.py -a -un cristiano```
  or
  ```python3 instagram_follow.py --all --username cristiano```
  
- If you want to get *following private account* user info (you must log in):</br>
  ```python3 instagram_follow.py -u -un *account* -l YOUR_USER YOUR_PASSWORD```
  or
  ```python3 instagram_follow.py --user --username *account* --login YOUR_USER YOUR_PASSWORD```


# output
If *-s* (or *--save*) option is used the information will be written to the following files:
- User info --> **user.txt**
- Following users or following not follower --> **following.txt**
- Followers of follower not following --> **followers.txt**

# disclaimer
This code uses Instagrapi private API so I am not responsible for any illegal or unethical use of the data entered therein.




