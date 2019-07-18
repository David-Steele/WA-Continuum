#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 06 19:14:19 2014
@author: David
"""
############################## import statements ##############################
import sys, getopt
import random
import minphrases2 as mp
import htmlElements as he
import bodyBuilder
import re
########################## end of import statements ###########################
myMax = 0
bb = bodyBuilder.BuildBody()
grid = None
sen = '''我 爱 你 ！ ||| i love you ! ||| 0-0 1-1 2-2 3-3'''
gridRange = 0;

def getRange(ranList):
    global gridRange;
    try:
        tList = gridRange.split(':')
        bot = int(tList[0]); top = int(tList[1])
        t = max(top,bot); b = min(top,bot)
        if t - b > 0 and t - b < len(ranList):
            ranList = ranList[b:t]
        else:
            print "\nRange out of scope - reverting back to default..."
    except:
        print "Your given range: **", gridRange,"** was in the wrong format.\n\nIt should be in the form of num1:num2."
        print "(Where num1 < num2)\n\nReverting back to the default range." 
        pass
    return ranList

def getExtStringList(corpus = "", wrd ='because', shuff = 'n'):
    if wrd == '<>':
        matcher = ".*?<.*>"
    else:
        matcher = ".*?\s{0}\s+".format(wrd)
    lineList = []
    corp = ["zh.en.al.oneSpace.txt","corpus.zh-en.copy.txt","insertThen.txt"]
    if corpus == "":
        lineList.append(sen)
    else:
        if corpus in [0,1,2]:
            inFile = open(corp[corpus],"r")
        else:
            try:
                inFile = open(corpus,"r")
            except IOError:
                print '''\nSORRY, I couldn't find the file named:\n ** {0} **.\n Please check and try again.'''.format(corpus)
                raise sys.exit()
        try:
             c = re.compile(matcher)
             for line in inFile:
                 if re.match(c, line):
                     lineList.append(line)
             inFile.close()
             if gridRange != 0:
                lineList = getRange(lineList)
        except IOError:
            print '''\nSORRY, I couldn't find the file named:\n ** {0} **.\n Please check and try again.'''.format(corpus)
            raise sys.exit()
        except:
            print "\nSorry there was a problem with the file"; raise sys.exit()
        if shuff != 'n': random.shuffle(lineList)
    return lineList
    
def createContents(strList, maxG):
    if maxG > 512: maxG = 2500
    strings = []
    allTables = 0
    
    for item in strList:
        if allTables < maxG:
            myItem = item[0]
            gr = item[1]
            #if item != strList[0]:
                #bb.changeBackCol = 'y'
            bb.longStr = myItem[0]
            bb.chAD = myItem[1]; bb.enAD = myItem[2]
            bb.createSplits()
            bb.grid = gr
            if len(bb.arrEN) <=100:
                allTables += 1
                bb.bodyBuilder()
                tup = bb.tableBuilder()
                bb.tID += 1
                strings.append(tup[0])
                bb.top = tup[1]
        
    contents = he.header + "".join(strings) + he.footer

    return contents

#def callBrowse(contents):
    #browseLocal(contents)
    
def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename, auto):
    '''Start browser with file containing the text with given filename.'''
    strToFile(webpageText, filename)
    if auto == 'y':    
        import webbrowser, os.path
        webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac
    else:
        print "Browser not started. Your file has been saved as\n", filename
        sys.exit(0)

def getMinPhrases(aStr):
    bb.longStr = aStr
    bb.createSplits()
    rangeCols = len(bb.arrZH); rangeRows = len(bb.arrEN)
    global grid
    grid = [[0 for i in xrange(rangeRows)] for j in xrange(rangeCols)]
    arrStr = bb.sAL;
    aligns = [map(int, link.split('-')) for link in arrStr.split()]
    y = mp.minimal_biphrases(bb.arrZH,bb.arrEN,aligns)
  
    sortedList = []
    for item in y:
        sortedList.append(item)
    '''
    sortedList.sort(key = lambda el: (len(el[0]) + len(el[1]), -(el[0][0])))
    sortedList = sortedList[::-1]
    '''
    return (sortedList, aligns)
    
def alterGrid(row, col):
    global grid
    if grid[row][col] == 0:
        grid[row][col] = 1
    elif grid[row][col] == 1:
        grid[row][col] = 2
    elif grid[row][col] == 2:
        grid[row][col] = 3
    elif grid[row][col] == 3:
        grid[row][col] = 4
    elif grid[row][col] == 4:
        grid[row][col] = 5
    else:
        grid[row][col] = 6
    
    
def createSentenceList(minTup):
    sList = [(bb.longStr,0,0)]
    for item in minTup[0]:
        chList = []; enList = [] #arrAL = [];
        topCH = max(item[0]); botCH = min(item[0])
        #print bb.arrZH
        for i in range(botCH,topCH+1):
            chList.append(bb.arrZH[i])
        topEN = max(item[1]); botEN = min(item[1])
        for i in range(botEN,topEN+1):
            enList.append(bb.arrEN[i])
        for c in range(botCH,topCH+1):
             for r in range(botEN,topEN+1):
                 alterGrid(c,r)
    top = 0
    global grid
    for item in grid:
        for el in item:
            if el > top:
                top = el
    global myMax
    if top > myMax:
        myMax = top
    return (sList[0],grid)

def err():
    print '''\nHmmm... did you provide arguments for the respective flags?'''
    print '''\nIf you use any of the following flags, then an argument is required:'''
    print '''\n-f -o -a -m -r -k \n    OR\n--keyWord, --fileIn, --fileOut, --aSentence, --maxGrids'''
    print '''\nFor further information run the file again using the\n-h  OR   --help switch.'''

def help():
    print "\n-a OR aSentence\nUse this switch if you want to input your own sentence.\n\
The sentence format should be: Source ||| Target ||| Alignments. \n(Don't Forget the quotes!)\n\
The default sentence (if you just run alignsView.py with no arguments) is:\n\
wo ai ni ! ||| i love you ! ||| 0-0 1-1 2-2 3-3\n"
    print "-b OR --biphraseOn\nUse this switch (with no args) to display the minimal biphrases.\n"
    print "-f yourInFileName OR --fileIn yourInFileName \nThe input file of your corpus... \n \
yourInFileName is required if you use this switch\n"
    print "-h OR --help\nThis prints out the help text....\n"
    print "-k OR --keyword\nThis switch needs the word you want to see grids for.\nThe default is 'love'\n"
    print "-l OR --lengthOnly\nThis only prints out the number of sentences for your keyword.\n\
    Useful for setting your range (see below).\n"
    print "-m OR --maxGrids\nThis requires an integer argument of 0 < m <= 512 (default = 256).\n\
The file will show upto 512 grids (hard max).\nIt has been tested working to over 10000,\n\
but 512 seems plenty and mainatains excellent performance.\n"
    print "-o yourOutFileName.html OR --fileOut yourOutFileName.html \nThe name of your output html file... \n \
yourOutFileName.html is required if you use this switch.\nMake sure the name has the extension .htm OR .html\n\
(or else it won't load in the browser)\n\
The default file name is 'alignmentGrids.html'\n"
    print "-r OR --range\nThis is probably the trickest switch to use.\n\
You should run the file with -l first\nto find out how many results there will be.\n\
You can then choose a sensible range within this amount.\n\
If your choice falls outside the range,\nthe program will revert to showing upto the default 256 grids.\n\
To choose a range the argument should be in this form:\n\
num1:num2 (no spaces), WHERE num1 < num2, AND num1 >= 0 AND num2 <= max.\n"
    print "-s OR --shuff\nUse this switch (with no args) to shuffle the order\nin which the grids will be displayed.\n"
    print "-x OR --autoLoad\nUse this switch (with no args) to stop the output file\n\
automatically loading into your browser. \ne.g. Saves the file only, so it can be viewed later.\n"
    sys.exit(0)
    
def startHere(fo, wrd='love', biOn = 'n', lengthOnly = 'n',shuff = 'n', maxGrids = 256, autoLoad = 'y',  corp = ""):
    if lengthOnly == 'y': 
        mainList = getExtStringList(corp,wrd)
        if corp == "":
            print "\nYou haven't loaded a corpus, so I'm only reading from one sentence..."
        else:
            print "\nThe number of sentences containing your word/phrase ('{0}') is: {1}".format(wrd,len(mainList))
    else:
        if biOn == 'n': bb.blueOnly = True
        mainList = getExtStringList(corp,wrd, shuff)
        contList = []
        cnt = 0
        try:
            for item in mainList:
                sl = getMinPhrases(item)
                #print cnt
                cnt+=1
                myList = createSentenceList(sl)
                contList.append(myList)
            cont = createContents(contList, maxGrids)
            browseLocal(cont, fo, autoLoad)
            if corp != "":
                print "\nThe number of sentences containing your word/phrase ('{0}') is: {1}".format(wrd, len(mainList))
                print "Max nest level for '{0}' is: {1}.".format(wrd, myMax)
            else:
                print "\nThe max nest level for your sentence is:", myMax
        except IndexError:
            print "\nSorry!!!\nIt appears a part of your input file or sentence could not be divided into the\n\
SOURCE ||| TARGET ||| ALIGNMENT format. Please check and try again."
        except ValueError:
            print "\nSorry!!!\nIt looks like your alignments did not have the correct number of values\n\
Please check that your alignments all come in pairs separeated by a '-'."
        except:
           print "\nSorry!!!\n\
There appeared to be a problem with your input file or sentence.\nPlease check and try again."
    
def main(argList):
    argList               
    try:                                
        opts, args = getopt.getopt(argList, "hlk:f:o:a:m:r:bsx", ["help", "lengthOnly", "keyWord=", "fileIn=","fileOut=",
        "aSentence=", "maxGrids=", "range", "biphraseOn","shuff","autoload"])
    except getopt.GetoptError:           
        err(); sys.exit(2) 
    global sen; global gridRange;
    wrd = 'love'; corp = ""; biOn = 'n'; lengthOnly = 'n'; shuff='n'; maxGrids = 256; fo = 'alignmentGrids.html';
    autoLoad = 'y';
    
        
    for opt, arg in opts:
        ################# no saved files here #################
        if opt in ("-h", "--help"): help()
        if opt in ("-l", "--lengthOnly"): lengthOnly = 'y'
        ################ save files start here ################
        if opt in ("-b", "--biphraseOn"): biOn = 'y'
        if opt in ("-s", "--shuff"): shuff = 'y'
        if opt in ("-o", "--fileOut"): fo = arg
        if opt in ("-k", "--keyWord"): wrd = arg
        if opt in ("-x", "--autoLoad"): autoLoad = 'n'
        if opt in ("-r", "--range"): gridRange = arg
        if opt in ("-m", "--maxGrids"): 
            try:
                maxGrids = int(arg)
                if maxGrids < 1: maxGrids = 1
            except:
                pass
        if opt in ("-a", "--aSentence"): 
            sen = arg
        elif opt in ("-f", "--fileIn"): corp = arg
    #wrd = 'if'; corp = 0; biOn = 'n'; 
   
    startHere(fo, wrd, biOn, lengthOnly, shuff, maxGrids, autoLoad, corp)  
            
if __name__ == "__main__":
    main(sys.argv[1:]) 

