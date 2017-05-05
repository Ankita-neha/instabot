import requests          # Here importing the requests library which is installed by using pip.

APP_ACCESS_TOKEN = '1599633091.2fc0da1.63f5a1608a3e4414b4d96117bca38027'
BASE_URL = 'https://api.instagram.com/v1/'


def self_info():          # this is the function which fetches my instagram profile details by using api.

    request_url = (BASE_URL +'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'REQUESTING URL FOR DATA  : ' + request_url
    my_info = requests.get(request_url).json()
    print 'MY INFO IS: \n'
    print 'My Bio: ' + my_info['data']['bio']
    print 'My Website : ' + my_info['data']['website']
    print 'My Full Name : ' + my_info['data']['full_name']
    print 'My Username : ' + my_info['data']['username']
    print 'I am followed by : ' + str(my_info['data']['counts']['followed_by']) + ' Users'
    print 'I follow : ' + str(my_info['data']['counts']['follows']) + ' Users'

#self_info()


#this function is used to fetch another user's details by entering instagram username and also it will return the userID
def get_user_id_by_username(insta_username):

    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'REQUESTING URL FOR DATA  : ' + request_url

    search_results = requests.get(request_url).json()

    print search_results

    if search_results['meta']['code'] == 200:
        if len(search_results['data']) > 0:
            print 'User ID: ' + search_results['data'][0]['id']
            return search_results['data'][0]['id']
        else:
            print 'User does not found!'
    else:
        print 'Status code other than 200 was received'
    return None

#get_user_id_by_username('shubham.is.here')


def get_users_recent_posts(insta_username):              #This function fetches the recent uploaded posts by the user.

    user_id = get_user_id_by_username(insta_username)
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'REQUESTING URL FOR DATA  : ' + request_url

    recent_posts = requests.get(request_url).json()

    if recent_posts['meta']['code'] == 200:
        if len(recent_posts['data']):
            return recent_posts['data'][1]['id']
        else:
            print 'No recent post by this user!'
    else:
        print 'Status code other than 200'

#print get_users_recent_posts('shubham.is.here')


def like_users_post(insta_username):                        #Function to like the user post, it will like the post id that we fetched in the above funtion.
    post_id = get_users_recent_posts(insta_username)
    payload = {'access_token': APP_ACCESS_TOKEN}
    request_url = (BASE_URL + 'media/%s/likes') % (post_id)
    like_users_post = requests.post(request_url,payload).json()
    if like_users_post['meta']['code'] == 200:
        print "Like was successful"
    else:
        print "Like not successful"

#like_users_post('shubham.is.here')


def get_comment_id_for_a_post(insta_username):
    post_id = get_users_recent_posts(insta_username)
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (post_id, APP_ACCESS_TOKEN)
    print "REQUESTING COMMENTS FROM INSTAGRAM USING %s" % request_url
    comments = requests.get(request_url).json()
    print comments

    for comment in comments['data']:
        print "%s commented: %s" % (comment['from']['username'],comment['text'])
#get_comment_id_for_a_post('shubham.is.here')


def comment_on_users_post(insta_username):    #comment on the post of that user whose post id is fetched by above function.
    post_id = get_users_recent_posts(insta_username)
    request_url = (BASE_URL + 'media/%s/comments') % (post_id)
    request_data = {'access_token':APP_ACCESS_TOKEN, 'text':'instabot commented here'}
    comment_request = requests.post(request_url, request_data).json()
    if comment_request['meta']['code'] == 200:
        print "Comment successful"
    else:
        print "Comment unsuccessful"

#comment_on_users_post('shubham.is.here')


def get_the_comment_id(insta_username):                  #here we search the comment by word and return its commentid.
    post_id = get_users_recent_posts(insta_username)
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (post_id, APP_ACCESS_TOKEN)
    comment_id = requests.get(request_url).json()
    word_in_comment = raw_input("Enter a word that you want to find in the comment:")
    if comment_id['meta']['code'] == 200:
        for i in len(comment_id['data']):
            if word_in_comment in comment_id['data'][i]['text']:
                print "Comment found"
                return comment_id['data'][i]['id']
        else:
            print "Comment was not found"
    else:
        print "Status code other than 200 was received"

#get_the_comment_id('shubham.is.here')


def delete_comment_by_the_word(insta_username):              #Here we delete the comment whose id we fetched in above function.
    post_id  = get_users_recent_posts(insta_username)
    comment_id = get_the_comment_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/%s?access_token=%s') % (post_id, comment_id, APP_ACCESS_TOKEN)
    delete_comment = requests.delete(request_url).json()
    if delete_comment['meta']['code']==200:
        print "Comment deleted successfully"
    else:
        print "Comment was not successfully deleted"

#delete_comment_by_the_word('shubham.is.here')


condition = 'i'    #Here bot asks the user which action you want to perform

insta_username = raw_input("Enter the instagram username on which you want to perform any action: ")

if (condition=='i' ):

    print "The options of the actions that the bot can perform are given below:- \n\
    1. View the details of your instagram profile. \n\
    2. Fetch another user's instagram profile id. \n\
    3. Get user's recent uploaded post. \n\
    4. To like another user's post. \n\
    5. Comment on another user's post. \n\
    6. Search a word in your comments of the post and get the commentid. \n\
    7. Delete the searched comment. \n\
    8. Show the comments which are done on another user's post. \n"

    choose_the_option = int(raw_input("Enter your option: "))
    if choose_the_option==1:
        self_info()
    elif choose_the_option==2:
        get_user_id_by_username(insta_username)
    elif choose_the_option==3:
        get_users_recent_posts(insta_username)
    elif choose_the_option==4:
        like_users_post(insta_username)
    elif choose_the_option==5:
        comment_on_users_post(insta_username)
    elif choose_the_option==6:
        get_the_comment_id(insta_username)
    elif choose_the_option==7:
        delete_comment_by_the_word(insta_username)
    elif choose_the_option==8:
        get_comment_id_for_a_post(insta_username)
    else:
        print "Invalid selection"