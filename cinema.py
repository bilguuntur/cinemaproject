global f
f = 0
 
#this t_movie function is used to select movie name
def t_movie():
    global f
    f = f+1
    print("which movie do you want to watch?")
    print("1,Batman ")
    print("2,Morbius ")
    print("3,Spider-man")
    print("4,back")
    movie = int(input("choose your movie: "))
    if movie == 4:
      # it goes back to the previous question
      center()
      theater()
      return 0
    if f == 1:
      theater()
 
# this theater function used to select screen
def theater():
    print("which screen do you want to watch movie: ")
    print("1,SCREEN 1")
    print("2,SCREEN 2")
    print("3,SCREEN 3")
    a = int(input("choose your screen: "))
    ticket = int(input("number of ticket do you want?: "))
    sit()
 
# this timing function used to select timing for movie
def timing(a):
    time1 = {
        "1": "10.00-1.00",
        "2": "1.10-4.10",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
    }
    time2 = {
        "1": "10.15-1.15",
        "2": "1.25-4.25",
        "3": "4.35-7.35",
        "4": "7.45-10.45"
    }
    time3 = {
        "1": "10.30-1.30",
        "2": "1.40-4.40",
        "3": "4.50-7.50",
        "4": "8.00-10.45"
    }
    if a == 1:
        print("choose your time:")
        print(time1)
        t = input("select your time:")
        x = time1[t]
        print("successful!, enjoy movie at "+x)
    elif a == 2:
        print("choose your time:")
        print(time2)
        t = input("select your time:")
        x = time2[t]
        print("successful!, enjoy movie at "+x)
    elif a == 3:
        print("choose your time:")
        print(time3)
        t = input("select your time:")
        x = time3[t]
        print("successful!, enjoy movie at "+x)
    return 0
 

def sit():
    print("where do you want to sit: ")
    print("1,In the top part")
    print("2,In the middle")
    print("3,In the bottom part")
    a = int(input("choose your sit: "))
    timing(a)
    
    
def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("wrong choice")
 
 
def center():
    print("which theater do you wish to see movie? ")
    print("1,Urgoo")
    print("2,Imax")
    print("3,Gegeenten")
    print("4,back")
    a = int(input("choose your option: "))
    movie(a)
    return 0
 
# this function is used to select city
def city():
    print("Hi welcome to movie ticket booking: ")
    print("where you want to watch movie?:")
    print("1,Darkhan")
    print("2,Ulaanbaatar ")
    print("3,Erdenet ")
    place = int(input("choose your option: "))
    if place == 1:
      center()
    elif place == 2:
      center()
    elif place == 3:
      center()
    else:
      print("wrong choice")
 
 
city() # it calls the function city
