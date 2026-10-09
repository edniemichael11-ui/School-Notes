# In pythin, a function can return multiple values using a single return statement
# When the interpreter encounters a return statement in a function, control is sent back
# to the calling code.

# returning multiple values:
def getPlayerStats(): #get_player_stats
    name = "Isaac"
    score = 95
    level = 3

    return name, score, level

#receiving multiple values:
playerName, playerScore, PlayerLevel = getPlayerStats()
#the variables above, receive the same values in the same order they were returned

print(PlayerLevel)
print(playerName)
print(playerScore)

#receive the values as a tuple:
player = getPlayerStats()
print(player)
print(player[0]) #prints the name

# you can ignore values you don't want
pname,_,plevel = getPlayerStats() #note: the _ is just a python convention
print(pname)
print(_)
print(plevel)
