#!/usr/bin/env python3
"""
Day One Project the code village
"""

storyFormat = """
My favorite animal is {animal}.  This {animal}
likes to eat a lot {food}, I have to get {food} from {city}.
"""

def outputStory():
    userPicks = dict()
    addSelection('animal', userPicks)
    addSelection('food', userPicks)
    addSelection('city', userPicks)
    story = storyFormat.format(**userPicks)
    print(story)

def addSelection(cue, dictionary):
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    prompt = 'Enter a name for ' + cue + ': '
    response = input(prompt).strip()
    dictionary[cue] = response                                                             
outputStory()
input("Press Enter to end the program.")
