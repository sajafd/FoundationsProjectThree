# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person
from math import *

my_name = "Fatma"
my_age = -1
my_bio = "Fun"
myself = Person(my_name, my_bio, my_age)
my_person_object = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!
    option_one = "1) Create a new club."
    option_two = "2) Browse and join clubs."
    option_three = "3) View existing clubs."
    option_four = "4) Display members of a club."
    option_neg_one = "-1) Close application."
    print ("\n Would you like to: \n\n %s \n or: \n %s \n or: \n %s \n or: \n %s \n or: \n %s \n \n " % (option_one , option_two , option_three, option_four , option_neg_one))
    option_picked = input ("Pick 1, 2, 3, 4, or -1: ")
    if option_picked == str(1):
        print()
        print ("You picked option %s" % option_picked) 
        create_club()
    elif option_picked == str(2):
        print()
        print ("You picked option %s" % option_picked)
        view_clubs()
        join_clubs()
    elif option_picked == str(3):
        print()
        print ("You picked option %s" % option_picked)
        view_clubs()
    elif option_picked == str(4):
        print()
        print ("You picked option %s" % option_picked)
        view_club_members()
    elif option_picked == "-1":
        print()
        print ("You picked option %s" % option_picked)
        print ("Exit")


def create_club():
    print()
    club_name = input("Type your club name: ")
    print()
    club_description = input("Type a brief description of your club: ")
    print()
    new_club = Club(club_name, club_description)
    clubs.append(new_club)
    print ("Enter the numbers of the people you would ()like to recruit to your new club (enter -1 to stop): ")
    print ("-----------------------------------------------------------------------------------------------")
    count = 1
    for member in population:
        print ("[%s] %s" % (count, member.name))
        count += 1
    print()
    picked_member = input("")
    while picked_member != "-1":
        new_club.recruit_member(population[int(picked_member) - 1])
        picked_member = input("")
    new_club.assign_president(my_name)
    print()
    print("Here are your club details: ")
    print (new_club.name)
    print (new_club.description)
    print ("Members:")
    print()
    age_sum = 0
    for member in new_club.members:
        print ("- %s ( %s years old ) %s" % (member.name, member.age, member.bio))
        print ()
        age_sum += member.age
    average_age = round((age_sum/len(new_club.members)),1)
    print ("The average age of members in this club is: %s" % average_age)
    print ("-----------------------------------------------------------------------------------------------")


def view_clubs():
    # your code goes here!
    for club in clubs: 
        name = club.name
        description = club.description
        members = len(club.members)
        print ("\n\tNAME: %s \n \tDESCRIPTION: %s \n \tMEMBERS: %s \n" % (name, description, members))
    

def view_club_members():
    # your code goes here!
    view_clubs()
    picked_for_details = input ("Enter the name of the club whose members you would like to see: ")

    for club in clubs: 
        if club.name == picked_for_details:
            for member in club.members:
                print ("- %s ( %s years old ) %s" % (member.name, member.age, member.bio))
                print ()
                
    print ("-----------------------------------------------------------------------------------------------")


def join_clubs():
    # your code goes here!
    picked_club = input ("Enter the name of the club you would like to join: ")
    for club in clubs:
        if picked_club == club.name:
            club.recruit_member(my_person_object)
            print ("%s just joined %s" % (my_name, picked_club))
            print ("-----------------------------------------------------------------------------------------------")


def application():
    introduction()
    options()
    # your code goes here!
