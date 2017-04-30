import requests          # Here importing the requests library which is installed by using pip.

APP_ACCESS_TOKEN = '1599633091.2fc0da1.63f5a1608a3e4414b4d96117bca38027'
BASE_URL = 'https://api.instagram.com/v1/'


def self_info():         # this is the function which fetches my instagram profile details by using api.

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

self_info()


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

get_user_id_by_username('shubham.is.here')


def get_users_recent_posts(insta_username):              #This function fetches the recent uploaded posts by the user.

    user_id = get_user_id_by_username(insta_username)
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'REQUESTING URL FOR DATA  : ' + request_url

    recent_posts = requests.get(request_url).json()

    if recent_posts['meta']['code'] == 200:
        if len(recent_posts['data']):
            return recent_posts['data'][0]['id']
        else:
            print 'No recent post by this user!'
    else:
        print 'Status code other than 200'

print get_users_recent_posts('shubham.is.here')

