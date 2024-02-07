''''
CS115 Group Project Pt.2

Pledge: I pledge my Honor that I have abided by the Stevens Honor System

Team Members: Brandon Gilman, Anthony Rizzuto, Chiara Plata Gomez
'''


def loadUsers(filename):
    """load user prefrences from a file into a dictionary    
    returns a dictionary containing user preferences
    
    Author: Brandon Gilman, Anthony Rizzuto, Chiara Plata Gomez
    """
    
    dic = {}
    try: 
        f = open(filename, "r")
    except FileNotFoundError:
        f = open(filename, "a")
    else: 
        for line in f:
            [username,singers]=line.strip().split(':')
            singerList = singers.strip().split(',')
            singerList.sort()
            dic[username] = {'preferences':singerList,'private mode': username.endswith('$')}
        f.close()
    return dic

def greeting(): 
    '''Greets user and collects username input
    
    Author: Brandon Gilman
    '''

    username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    return username
  
def enter_preferences(username, users, option):
    '''User enters their artist preferences. If user already exists, and wants to replace their preferenes, 
    if statement allows them to rewrite their preferences
    
    Author: Brandon Gilman, Anthony Rizzuto, Chiara Plata Gomez
    '''
    next_artist = ""
    status = True
    if username in users:
        if option == "e":
            preferences = []
            status = True
        else:
            preferences = users[username]['preferences']
            status = False
    else:
        preferences = []
        status = True
    while status == True:
        next_artist = input("Enter an artist that you like (Enter to finish):")
        if next_artist == "":
            break
        else: preferences.append(next_artist)
    preferences.sort()
    users[username] = {'preferences': preferences}
    return preferences

def getRecommendations(dic, currentUser):
    '''returns the recommendations for a user
    
    Author: Brandon Gilman, Anthony Rizzuto, Chiara Plata Gomez
    '''
    matches = {}
    recs = []
    user_preferences = set(dic[currentUser]["preferences"])
    for user, data in dic.items():
      if user != currentUser and not user.endswith('$'):  
          other_user_preferences = set(data["preferences"])
          common_preferences = user_preferences.intersection(other_user_preferences)
          if common_preferences:
            similarity_score = len(common_preferences) / len(user_preferences)
            matches[user] = similarity_score
    sorted_matches = sorted(matches.items(), key=lambda x: x[1], reverse=True)
    if sorted_matches:
      most_similar_user, _ = sorted_matches[0]
      for artist in dic[most_similar_user]["preferences"]:
        if artist not in user_preferences and artist not in common_preferences:
            recs.append(artist)
      recs = sorted(set(recs))
    #else: print ("No recommendations available.")
    

    if recs:
        for i in recs:
            print(i)
    else:
            print("No recommendations available.")
    
def mostPopular(users):
    '''returns the most popular artist
    
    Author: Chiara Plata Gomez
    '''
    likes = {}
    for user, data in users.items():
        preferences = data.get('preferences', [])  
        if preferences and preferences[-1] != '':
            for artist in preferences:
                likes[artist] = likes.get(artist, 0) + 1
    popular_artists = sorted(likes, key=lambda x: (likes[x], x), reverse=True)[:3] 
    for artist in popular_artists:
        print(artist)
  
def saveAndQuit(username, preferences, users, filename):
    ''' saves the data into the file. exits program afterwards. 
    
    Author: Anthony Rizzuto
    '''
    users[username] = {'preferences': preferences}
    with open(filename, "w") as f:
        for username, data in users.items():
            f.write(username +':'+','.join(data['preferences'])+'\n')
    exit()

def howPopular(users):
  '''Print the number of likes the most popular artist received.
  
  Author: Anthony Rizzuto, Chiara Plata Gomez
  '''
  popular = {}
  maxPopular = 0

  for user, data in users.items():
      if user.endswith('$'):
          continue
      if data['preferences'] and data['preferences'][-1] != '':
          preferences = data['preferences']
          for artist in preferences:
              if artist in popular:
                  popular[artist] += 1
              else:
                  popular[artist] = 1

              if popular[artist] > maxPopular:
                  maxPopular = popular[artist]
  if maxPopular == 0:
      print("Sorry, no artists found.")
  else: print(maxPopular) 

def mostLikes(users, filename):
  ''' Print the full name(s) of the user(s) who like(s) the most artists.
    Author: Brandon Gilman, Chiara Plata Gomez
  '''
  users = loadUsers(filename)
  x = 0
  y = ''
  for user in users:
      if not user.endswith('$'):
          if len(users[user]["preferences"])>x:
              x =len(users[user]["preferences"])
              y = user
          else: 
             y = "Sorry, no user found."
  print(y)

def main():
    ''' main function where all functions are called and user is prompted.
    
    Authors: Anthony Rizzuto, Chiara Plata Gomez
    '''
    filename = "musicrecplus.txt"
    users = loadUsers(filename)
    username = greeting()
    option = None
    preferences = enter_preferences(username, users, option)
    
    
    while True:
        option = input("""
        Enter a letter to choose an option:
            e - Enter preferences
            r - Get recommendations
            p - Show most popular artists
            h - How popular is the most popular
            m - Which user has the most likes 
            q - Save and quit
            """).lower()
      
        if option =='e':
            preferences = enter_preferences(username, users, option)
        if option =='r':
            getRecommendations(users, username)
        if option =='p':
            mostPopular(users)
        if option =='h':
            howPopular(users)
        if option == 'm':
            mostLikes(users, filename)
        if option =='q':
            saveAndQuit(username, preferences, users, filename)

if __name__ == "__main__":
  main()
