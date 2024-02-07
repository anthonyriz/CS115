def mostPopular(users):
    '''returns the most popular artist'''
    likes = {}
    for data in users.items():
        preferences = data.get('preferences', [])  
        if preferences and preferences[-1] != '':
            for artist in preferences:
                likes[artist] = likes.get(artist, 0) + 1
    popular_artists = sorted(likes, key=lambda x: (likes[x], x), reverse=True)[:3] 
    for artist in popular_artists:
        print(artist)