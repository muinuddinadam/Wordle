import random

## List of words that cna be used for Wordle
word_list = ['ABOUT', 'ABOVE', 'ABUSE', 'ACTOR', 'ACUTE', 'ADMIT', 'ADOPT', 'ADULT', 'AFTER', 'AGAIN', 'AGENT', 'AGREE', 'AHEAD', 'ALARM', 'ALBUM', 'ALERT', 'ALIKE', 'ALIVE', 'ALLOW', 'ALONE', 'ALONG', 'ALTER', 'AMONG', 'ANGER', 'ANGLE', 'ANGRY', 'APART', 'APPLE', 'APPLY', 'ARENA', 'ARGUE', 'ARISE', 'ARRAY', 'ASIDE', 'ASSET', 'AUDIO', 'AUDIT', 'AVOID', 'AWARD', 'AWARE', 'BADLY', 'BAKER', 'BASES', 'BASIC', 'BASIS', 'BEACH', 'BEGAN', 'BEGIN', 'BEGUN', 'BEING', 'BELOW', 'BENCH', 'BILLY', 'BIRTH', 'BLACK', 'BLAME', 'BLIND', 'BLOCK', 'BLOOD', 'BOARD', 'BOOST', 'BOOTH', 'BOUND', 'BRAIN', 'BRAND', 'BREAD', 'BREAK', 'BREED', 'BRIEF', 'BRING', 'BROAD', 'BROKE', 'BROWN', 'BUILD', 'BUILT', 'BUYER', 'CABLE', 'CALIF', 'CARRY', 'CATCH', 'CAUSE', 'CHAIN', 'CHAIR', 'CHART', 'CHASE', 'CHEAP', 'CHECK', 'CHEST', 'CHIEF', 'CHILD', 'CHINA', 'CHOSE', 'CIVIL', 'CLAIM', 'CLASS', 'CLEAN', 'CLEAR', 'CLICK', 'CLOCK', 'CLOSE', 'COACH', 'COAST', 'COULD', 'COUNT', 'COURT', 'COVER', 'CRAFT', 'CRASH', 'CREAM', 'CRIME', 'CROSS', 'CROWD', 'CROWN', 'CURVE', 'CYCLE', 'DAILY', 'DANCE', 'DATED', 'DEALT', 'DEATH', 'DEBUT', 'DELAY', 'DEPTH', 'DOING', 'DOUBT', 'DOZEN', 'DRAFT', 'DRAMA', 'DRAWN', 'DREAM', 'DRESS', 'DRILL', 'DRINK', 'DRIVE', 'DROVE', 'DYING', 'EAGER', 'EARLY', 'EARTH', 'EIGHT', 'ELITE', 'EMPTY', 'ENEMY', 'ENJOY', 'ENTER', 'ENTRY', 'EQUAL', 'ERROR', 'EVENT', 'EVERY', 'EXACT', 'EXIST', 'EXTRA', 'FAITH', 'FALSE', 'FAULT', 'FIBER', 'FIELD', 'FIFTH', 'FIFTY', 'FIGHT', 'FINAL', 'FIRST', 'FIXED', 'FLASH', 'FLEET', 'FLOOR', 'FLUID', 'FOCUS', 'FORCE', 'FORTH', 'FORTY', 'FORUM', 'FOUND', 'FRAME', 'FRANK', 'FRAUD', 'FRESH', 'FRONT', 'FRUIT', 'FULLY', 'FUNNY', 'GIANT', 'GIVEN', 'GLASS', 'GLOBE', 'GOING', 'GRACE', 'GRADE', 'GRAND', 'GRANT', 'GRASS', 'GREAT', 'GREEN', 'GROSS', 'GROUP', 'GROWN', 'GUARD', 'GUESS', 'GUEST', 'GUIDE', 'HAPPY', 'HARRY', 'HEART', 'HEAVY', 'HENCE', 'HENRY', 'HORSE', 'HOTEL', 'HOUSE', 'HUMAN', 'IDEAL', 'IMAGE', 'INDEX', 'INNER', 'INPUT', 'ISSUE', 'JAPAN', 'JIMMY', 'JOINT', 'JONES', 'JUDGE', 'KNOWN', 'LABEL', 'LARGE', 'LASER', 'LATER', 'LAUGH', 'LAYER', 'LEARN', 'LEASE', 'LEAST', 'LEAVE', 'LEGAL', 'LEVEL', 'LEWIS', 'LIGHT', 'LIMIT', 'LINKS', 'LIVES', 'LOCAL', 'LOGIC', 'LOOSE', 'LOWER', 'LUCKY', 'LUNCH', 'LYING', 'MAGIC', 'MAJOR', 'MAKER', 'MARCH', 'MARIA', 'MATCH', 'MAYBE', 'MAYOR', 'MEANT', 'MEDIA', 'METAL', 'MIGHT', 'MINOR', 'MINUS', 'MIXED', 'MODEL', 'MONEY', 'MONTH', 'MORAL', 'MOTOR', 'MOUNT', 'MOUSE', 'MOUTH', 'MOVIE', 'MUSIC', 'NEEDS', 'NEVER', 'NEWLY', 'NIGHT', 'NOISE', 'NORTH', 'NOTED', 'NOVEL', 'NURSE', 'OCCUR', 'OCEAN', 'OFFER', 'OFTEN', 'ORDER', 'OTHER', 'OUGHT', 'PAINT', 'PANEL', 'PAPER', 'PARTY', 'PEACE', 'PETER', 'PHASE', 'PHONE', 'PHOTO', 'PIECE', 'PILOT', 'PITCH', 'PLACE', 'PLAIN', 'PLANE', 'PLANT', 'PLATE', 'POINT', 'POUND', 'POWER', 'PRESS', 'PRICE', 'PRIDE', 'PRIME', 'PRINT', 'PRIOR', 'PRIZE', 'PROOF', 'PROUD', 'PROVE', 'QUEEN', 'QUICK', 'QUIET', 'QUITE', 'RADIO', 'RAISE', 'RANGE', 'RAPID', 'RATIO', 'REACH', 'READY', 'REFER', 'RIGHT', 'RIVAL', 'RIVER', 'ROBIN', 'ROGER', 'ROMAN', 'ROUGH', 'ROUND', 'ROUTE', 'ROYAL', 'RURAL', 'SCALE', 'SCENE', 'SCOPE', 'SCORE', 'SENSE', 'SERVE', 'SEVEN', 'SHALL', 'SHAPE', 'SHARE', 'SHARP', 'SHEET', 'SHELF', 'SHELL', 'SHIFT', 'SHIRT', 'SHOCK', 'SHOOT', 'SHORT', 'SHOWN', 'SIGHT', 'SINCE', 'SIXTH', 'SIXTY', 'SIZED', 'SKILL', 'SLEEP', 'SLIDE', 'SMALL', 'SMART', 'SMILE', 'SMITH', 'SMOKE', 'SOLID', 'SOLVE', 'SORRY', 'SOUND', 'SOUTH', 'SPACE', 'SPARE', 'SPEAK', 'SPEED', 'SPEND', 'SPENT', 'SPLIT', 'SPOKE', 'SPORT', 'STAFF', 'STAGE', 'STAKE', 'STAND', 'START', 'STATE', 'STEAM', 'STEEL', 'STICK', 'STILL', 'STOCK', 'STONE', 'STOOD', 'STORE', 'STORM', 'STORY', 'STRIP', 'STUCK', 'STUDY', 'STUFF', 'STYLE', 'SUGAR', 'SUITE', 'SUPER', 'SWEET', 'TABLE', 'TAKEN', 'TASTE', 'TAXES', 'TEACH', 'TEETH', 'TERRY', 'TEXAS', 'THANK', 'THEFT', 'THEIR', 'THEME', 'THERE', 'THESE', 'THICK', 'THING', 'THINK', 'THIRD', 'THOSE', 'THREE', 'THREW', 'THROW', 'TIGHT', 'TIMES', 'TIRED', 'TITLE', 'TODAY', 'TOPIC', 'TOTAL', 'TOUCH', 'TOUGH', 'TOWER', 'TRACK', 'TRADE', 'TRAIN', 'TREAT', 'TREND', 'TRIAL', 'TRIED', 'TRIES', 'TRUCK', 'TRULY', 'TRUST', 'TRUTH', 'TWICE', 'UNDER', 'UNDUE', 'UNION', 'UNITY', 'UNTIL', 'UPPER', 'UPSET', 'URBAN', 'USAGE', 'USUAL', 'VALID', 'VALUE', 'VIDEO', 'VIRUS', 'VISIT', 'VITAL', 'VOICE', 'WASTE', 'WATCH', 'WATER', 'WHEEL', 'WHERE', 'WHICH', 'WHILE', 'WHITE', 'WHOLE', 'WHOSE', 'WOMAN', 'WOMEN', 'WORLD', 'WORRY', 'WORSE', 'WORST', 'WORTH', 'WOULD', 'WOUND', 'WRITE', 'WRONG', 'WROTE', 'YIELD', 'YOUNG', 'YOUTH']

## Selecting a random word
wordleword = random.choice(word_list)
print(wordleword)

## Coding the scoring algorithm
#userguess = input("Input a 5 letter word: ")
#wordleguess = userguess.upper()

# User gets 6 guesses
for z in range(6):
    # User guess automatically wrong
    firstletterexist = False
    secondletterexist = False
    thirdletterexist = False
    fourthletterexist = False
    fifthletterexist = False
    firstletterspot = False
    secondletterspot = False
    thirdletterspot = False
    fourthletterspot = False
    fifthletterspot = False

    # Taking the users word
    print("Guess number", z+1)
    userguess = input("Input a 5 letter word: ")
    wordleguess = userguess.upper()

    # Checking if the letters are correct
    for a in range(5):
        for b in range(5):
            if wordleguess[a] == wordleword[b] and a == 0:
                firstletterexist = True
            elif wordleguess[a] == wordleword[b] and a == 1:
                secondletterexist = True
            elif wordleguess[a] == wordleword[b] and a == 2:
                thirdletterexist = True
            elif wordleguess[a] == wordleword[b] and a == 3:
                fourthletterexist = True
            elif wordleguess[a] == wordleword[b] and a == 4:
                fifthletterexist = True

    # Checking if the letters are in the right spot
    for c in range(5):
        for d in range(5):
            if wordleguess[c] == wordleword[d] and c == d and 0 == c:
                firstletterspot = True
            if wordleguess[c] == wordleword[d] and c == d and 1 == c:
                secondletterspot = True
            if wordleguess[c] == wordleword[d] and c == d and 2 == c:
                thirdletterspot = True
            if wordleguess[c] == wordleword[d] and c == d and 3 == c:
                fourthletterspot = True
            if wordleguess[c] == wordleword[d] and c == d and 4 == c:
                fifthletterspot = True

    # Telling user the result of their guess
    correct = "exists and is in the correct position"
    partially = "exists but is not in the correct position"
    incorrect = "does not exist"
    if firstletterexist and firstletterspot == True:
        print(wordleguess[0], correct)
    elif firstletterexist == True:
        print(wordleguess[0], partially)
    else:
        print(wordleguess[0], incorrect)
    
    if secondletterexist and secondletterspot == True:
        print(wordleguess[1], correct)
    elif secondletterexist == True:
        print(wordleguess[1], partially)
    else:
        print(wordleguess[1], incorrect)
    
    if thirdletterexist and thirdletterspot == True:
        print(wordleguess[2], correct)
    elif thirdletterexist == True:
        print(wordleguess[2], partially)
    else:
        print(wordleguess[2], incorrect)

    if fourthletterexist and fourthletterspot == True:
        print(wordleguess[3], correct)
    elif fourthletterexist == True:
        print(wordleguess[3], partially)
    else:
        print(wordleguess[3], incorrect)

    if fifthletterexist and fifthletterspot == True:
        print(wordleguess[4], correct)
    elif fifthletterexist == True:
        print(wordleguess[4], partially)
    else:
        print(wordleguess[4], incorrect)

    # Checking if their guess is correct
    if firstletterexist and firstletterspot and secondletterexist and secondletterspot and thirdletterexist and thirdletterspot and fourthletterexist and fourthletterspot and fifthletterexist and fifthletterspot == True:
        print("Congratulations you win the game")
        break
    else:
        print("Try again")

"""
    for e in range(1):
        if firstletterexist == True:
            print(firstletterexist)
        else:
            print(False)
        if secondletterexist == True:
            print(secondletterexist)
        else:
            print(False)
        if thirdletterexist == True:
            print(thirdletterexist)
        else:
            print(False)
        if fourthletterexist == True:
            print(fourthletterexist)
        else:
            print(False)
        if fifthletterexist == True:
            print(fifthletterexist)
        else:
            print(False)
    for f in range(1):
        if firstletterspot == True:
            print(firstletterspot)
        else:
            print(False)
        if secondletterspot == True:
            print(secondletterspot)
        else:
            print(False)
        if thirdletterspot == True:
            print(thirdletterspot)
        else:
            print(False)
        if fourthletterspot == True:
            print(fourthletterspot)
        else:
            print(False)
        if fifthletterspot == True:
            print(fifthletterspot)
        else:
            print(False)
"""

#Take the user guess
#See if the first letter is right
#See if the first letter is in the right spot
#If the both are true then let the user know
#If it exists then let the user know
#If neither are true state that first letter is not a letter in the word