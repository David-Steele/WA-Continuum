# -*- coding: utf-8 -*-
"""
Created on Fri Nov 07 20:04:27 2014

@author: David
"""
class BuildBody(object):
    def __init__(self, chAD = 0, enAD = 0):
        self.cols = ["#bbb", "#8f8","#F3F781","#FFA500", "#FE2E2E", "#5E5A80", "#0000FF"]
        self.top = 0
        self.left = 20
        self.initialDrop = 84
        self.spacer = 20
        self.leftMargin = 30
        self.leftMiniMargin = 20
        self.longStr = "" #"太冷 不 开 花 ? ||| too cold for flowers ? ||| 0-0 1-0 0-1 2-1 0-2 3-3 4-4"
        self.sEN = ""
        self.sZH = ""
        self.sAL = ""
        self.arrEN = []
        self.arrZH = []
        self.aligns = []
        self.intAligns = []
        self.bList = []
        self.cnt = 0
        self.enAD = enAD
        self.chAD = chAD
        self.changeBackCol = 'n'
        self.grid = None
        self.tID = 0
        self.call = 'onmouseover="c(this)" onmouseout="d(this)"'
        self.blueOnly = False

    def createSplits(self):
        lStr = self.longStr.split("|||")
        self.sEN = lStr[1].strip()
        self.arrEN = self.sEN.split()
        self.sZH = lStr[0].strip()
        if '<' in self.sZH and '>' in self.sZH:
            self.sZH = self.sZH.replace('<', '&lt;').replace('<', '&gt;')
        self.arrZH = self.sZH.split()
        self.sAL = lStr[2].strip()
        self.aligns = self.sAL.split()
    
    def bodyBuilder(self):
        sCnt = '<div style="position: absolute;top:{0}px; left:4px;"><h5>{1}<h5></div>'.format(self.top + 100,self.tID,self.cnt)
        self.bList.append(sCnt)
        self.top +=self.spacer
        self.bList.append('<table class="table table-header-rotated" style="position: absolute;top:{0}px; left: 30px;">\n<thead>\n<tr>'.format(self.top))
        #for item in self.arrEN:
            #self.bList.append('<th class="rotate"><div><span>{0}</span></div></th>'.format(item))
        for i in range(len(self.arrEN)):
                temp = "{0}:{1}".format(self.tID,i + self.enAD)
                self.bList.append('<th class="rotate"><div><span id="{0}">{1}) {2}</span></div></th>'.format(temp,i + self.enAD, self.arrEN[i]))   
        self.bList.append('</tr>\n</thead>\n<tbody>')
        self.top += self.initialDrop; self.left = self.leftMargin
        self.cnt +=1
    
    def tableBuilder(self):
        border = 1
        xMark = "#"
        elID = ""
        tempStr = []; 
        mCols = len(self.arrEN); mRows = len(self.arrZH)
        for r in range(mRows):
            tempStr.append('<tr>')
            for c in range(mCols):
                myColour = self.cols[(self.grid[r][c])]
                elID = "{0}-{1}:{2}".format(r,self.tID, c + self.enAD)
                #print elID
                if str(r+self.chAD)+'-'+str(c+self.enAD) in self.aligns:
                    if self.blueOnly == True:
                        myColour = '#00F'
                        xMark = ""; border = 0
                    if self.changeBackCol == 'n':
                        #tempStr.append('<td style="background-color:#0ff; border: 1px solid black;">#</td>') 
                        tempStr.append('<td id="{0}" {1} style="background-color:{2}; border: {3}px solid black;">{4}</td>'.format(elID, self.call, myColour, border, xMark)) #
                    else:
                         tempStr.append('<td id="{0}" {1} style="background-color:#8f8;">x</td>'.format(elID, self.call)) 
                else:
                    if self.blueOnly == True:
                        myColour = '#bbb'
                    if self.changeBackCol == 'n':
                        #tempStr.append('<td style="background-color:#bbb"></td>')
                        tempStr.append('<td style="background-color:{0}"></td>'.format(myColour))
                    else:
                        tempStr.append('<td style="background-color:#8f8"></td>') 
            zh = '<td style="white-space: nowrap;">{0}) {1}</td></tr>'.format(r+self.chAD, self.arrZH[r])
            tempStr.append(zh)
            self.top += self.spacer
        tempStr.append('''<tr><td colspan="100%">{0}</td></tr>
                            <tr><td colspan="100%">{1}</td></tr>
                            <tr><td colspan="100%">{2}</td></tr>
                            '''.format(self.sZH,self.sEN,self.sAL))
        tempStr.append('</table>')
        self.top += self.initialDrop + self.spacer
        self.bList.append("".join(tempStr))    
        self.top += (self.spacer)
     
        self.bList.append("")
        self.left = self.leftMiniMargin
        finStr = "\n".join(self.bList)
        self.bList = []
        return (finStr, self.top)

