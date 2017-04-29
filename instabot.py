import requests          # Here importing the requests library which is installed by using pip.

APP_ACCESS_TOKEN = '1599633091.2fc0da1.63f5a1608a3e4414b4d96117bca38027'
BASE_URL = 'https://api.instagram.com/v1/'

def self_info():         # this is the function which fetches my instagram details by using api.
    request_url = (BASE_URL +'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'REQUESTING URL FOR DATA : ' + request_url
    my_info = requests.get(request_url).json()
    print 'MY INFO IS: \n'
    print 'My Bio: ' + my_info['data']['bio']
    print 'My Website : ' + my_info['data']['website']
    print 'My Full Name : ' + my_info['data']['full_name']
    print 'My Username : ' + my_info['data']['username']
    print 'I am followed by : ' + str(my_info['data']['counts']['followed_by']) + ' Users'
    print 'I follow : ' + str(my_info['data']['counts']['follows']) + ' Users'

self_info()











#data = requests.get('https://api.github.com/events')

#print data.json()