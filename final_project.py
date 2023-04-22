import json
import requests
import os
import sys
import webbrowser

def isAnswer(ans):
    '''indicate if the answer is true or false
    
    Parameters  
    -------------------
    ans: answer to the question
    
    Returns
    -------
    True if the ans is positive,
    or False if the answer is negative

    '''
    if ans.lower() in ['yes', 'y', 'yep', 'sure', 'yup']:
        return True
    return False

def isLeaf(tree):
    '''indicate if the node is leaf or not
    
    Parameters  
    -------------------
    tree: a set of tuples contain three things: questions, what to do on 'yes', what to do on 'no'
    
    Returns
    -------
    True if the node is leaf,
    or False if the node is not leaf

    '''
    
    root, left, right = tree
    if left == None and right == None:
        return True
    return False

def saveTree(tree, treeFile):
    '''save current tree into a file
    
    Parameters  
    -------------------
    tree: a set of tuples contain three things: questions, what to do on 'yes', what to do on 'no'
    treeFile: file handle

    Returns
    -------
    None

    '''
    root, left, right = tree

    if isLeaf(tree):
        print('Leaf', file = treeFile)
        print(root, file = treeFile)
    else:
        print('Internal Node', file = treeFile)
        print(root, file = treeFile)
        
        saveTree(left, treeFile)        
        saveTree(right, treeFile)


def loadTree(treeFile):
    '''load tree from a file
    
    Parameters  
    -------------------
    treeFile: file handle

    Returns
    -------
    tuple that contains a tree

    '''
    line = treeFile.readline()
    if line == '':
        return None
    
    elif line == 'Leaf\n':
        root = treeFile.readline()
        root = root.rstrip('\n')
        return (root, None, None)
    
    root = treeFile.readline()
    root = root.rstrip('\n')
    left = loadTree(treeFile)
    right = loadTree(treeFile)
    
    return (root, left, right)


def getNext(tree, input):
    input = int(input)
    nextTree = tree[input]
    return nextTree

def sortList(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if float(list[j]["imdbRating"]) < float(list[j+1]["imdbRating"]):
                list[j], list[j+1] = list[j+1], list[j]

def SearchMovie():
    '''main body of searching movies
    
    Parameters  
    -------------------
    None

    Returns
    -------
    None

    '''
    f = open("tree.json","r")
    tree = json.loads(f.read())
    f.close()

    print(tree[0])
    while True:
        userInput1 = input("Please enter 1, 2 or 'exit':(1)released before 2000 (2)released after 2000\n")
        if userInput1 == "exit":
            print("Bye!")
            quit()
        elif userInput1.isnumeric():
            if int(userInput1) != 1 and int(userInput1) != 2:
                print("Please enter a valid number.")
                continue
            else:
                Tree2 = getNext(tree, userInput1)
                print(Tree2[0])
                while True:
                    userInput2 = input("Please enter 1, 2, 3, back or exit:(1)less than 40 min (2)40~60 min (3)longer than 60 min\n")
                    if userInput2 == "exit":
                        print("Bye!")
                        quit()
                    elif userInput2 == "back":
                        print("Back to previous menu...")
                        print(tree[0])
                        break
                    elif userInput2.isnumeric():
                        if int(userInput2) not in [1,2,3]:
                            print("Please enter a valid number.")
                            continue
                        else:
                            Tree3 = getNext(Tree2, userInput2)
                            print(Tree3[0])
                            while True:
                                userInput3 = input("Please enter number between 1~10, back or exit:(1)Drama (2)Adult (3)Documentary (4)Adventure (5)Comedy (6)Crime (7)Mystery (8)Fantasy (9)Thriller (10)Other\n")
                                if  userInput3 == "exit":
                                    print("Bye!")
                                    quit()
                                elif userInput3 == "back":
                                    print("Back to previous menu...")
                                    print(Tree2[0])
                                    break
                                elif userInput3.isnumeric():
                                    if int(userInput3) not in [1,2,3,4,5,6,7,8,9,10]:
                                        print("Please enter a valid number.")
                                        continue
                                    else:
                                        movieList = getNext(Tree3, userInput3)
                                        sortList(movieList)
                                        i = 0
                                        if len(movieList) == 0:
                                            print("There is no movie of your choice in the library.")
                                            continue
                                        elif len(movieList) >= 10:
                                            print("Here are the top 10 movies of your choice: ")
                                            while i < 10:
                                                print(i+1, movieList[i]["Title"]," (imdbRating: ", movieList[i]["imdbRating"],")"," [", movieList[i]["Runtime"], "]")
                                                i += 1
                                        elif len(movieList) < 10:
                                            print("There are less than 10 movies, here are all the movies of your choice: ")
                                            while i < len(movieList):
                                                print(i+1, movieList[i]["Title"], " (imdbRating: ", movieList[i]["imdbRating"],")"," [", movieList[i]["Runtime"], "]")
                                                i += 1
                                        while True:
                                            print("Please select the movie you want to preview.")
                                            userInput4 = input("Enter the number before the movie title, back or exit: ")
                                            if userInput4 == "exit":
                                                print("Bye!")
                                                quit()
                                            elif userInput4 == "back":
                                                print("Back to previous menu...")
                                                print(Tree3[0])
                                                break
                                            elif userInput4.isnumeric():
                                                if int(userInput4) < 1 or int(userInput4) > min([len(movieList), 10]):
                                                    print("Please enter a valid input.")
                                                    continue
                                                else:
                                                    print()
                                                    print("Here is the info of the movie: ")
                                                    print("The plot of the movie: ")
                                                    print(movieList[int(userInput4)-1]["Plot"])
                                                    print()
                                                    print("The poster of the movie: ")
                                                    print(movieList[int(userInput4)-1]["Poster"])
                                                    

                                                    while True:
                                                        print("Do you want to save this movie's info into json file?")
                                                        userInput5 = input("Enter yes, back or exit: ")
                                                        if userInput5 == "exit":
                                                            print("Bye!")
                                                            quit()
                                                        elif userInput5 == "back":
                                                            print("Back to previous menu...")
                                                            break
                                                        elif isAnswer(userInput5):
                                                            with open("saved_movie.json", "w") as outfile:
                                                                json.dump(movieList[int(userInput4)-1], outfile)
                                                            print("This movie's info is saved.")
                                                            break
                                                        else:
                                                            print("Back to previous menu...")
                                                            break

                                                    continue
                                            else:
                                                print("Please input a valid input.")
                                                continue
                                else:
                                    print("Please input a valid input.")
                                    continue
                    else:
                        print("Please input a valid input.")
                        continue
        else:
            print("Please input a valid input.")
            continue

def main():
    while True:
        print("Welcome!")
        isload = input("Would you like to load the current movie?")
        if not isAnswer(isload):
            isexit = input("Do you want to quit?")
            if isAnswer(isexit):
                print("Bye!")
                quit()
            else:
                SearchMovie()
        else:
            f = open("saved_movie.json","r")
            load_movie = json.loads(f.read())
            f.close()
            print("Here is the info of saved movie: \n")
            print(load_movie["Title"]," (imdbRating: ", load_movie["imdbRating"],")"," [", load_movie["Runtime"], "]\n")
            print("The plot of the movie: ")
            print(load_movie["Plot"])
            print()
            print("The poster of the movie: ")
            print(load_movie["Poster"])
            print()

            isNew = input("Would you like to start a new searching? (yes or no)")
            if not isAnswer(isNew):
                print("Bye!")
                quit()
            else:
                SearchMovie()

                


if __name__ == '__main__':
    main()