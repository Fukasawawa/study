from twitter import Twitter, OAuth

t = Twitter(auth=OAuth(
        <access token>,
        <access token secret>,
        <consumer key>,
        <consumer secret>
    ))

searchTweets = t.search.tweets(q = "Qiita")

friends = t.friends.ids()

remain = True
next_cursor = 0
while remain:
    friendsInfo = t.friends.list(cursor=next_cursor)
    for user in friendsInfo['users']:
        friendsNameList.append({
                'NumberID':user['id'],
                'userID':user['screen_name'],
                'userName':user['name']
            })
    next_cursor = friendsInfo['next_cursor']
    if(next_cursor == 0):
        remain = False
        print('Finish search')
