import copy
import ArrayListOfLatinSquares4by4
FullSquaresWithRows=ArrayListOfLatinSquares4by4.M

''' This document takes in a list of full latin squares 4by4 and systematically
deletes entries to make partial latin squares.'''

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += str(ele) 
    
    # return string   
    return str1

FullSquares=[]

'''Converts latin square to long list of entries for easier iteration later'''
for a in FullSquaresWithRows:
    currentsquare=[a[0][0],a[0][1],a[0][2],a[0][3],a[1][0],a[1][1],a[1][2],a[1][3],a[2][0],a[2][1],a[2][2],a[2][3],a[3][0],a[3][1],a[3][2],a[3][3]]
    FullSquares.append(currentsquare)

def textSquare(M): #takes in square as list of lists and converts it to a string
        answer="["
        for i in (M[0],M[1],M[2],M[3]):
            for j in range(0,4):
                if j==0:
                    if i==M[0]:
                        answer=answer+"["+str(i[j])+","
                    else:
                        answer=answer+",["+str(i[j])+","
                if j==3:
                    answer = answer+str(i[j])+"]"
                if j!=0 and j!=3:
                    answer = answer+str(i[j])+","
        answer=answer+"]"              
        return answer


    

def ListToSquare(L):
    ans=[]
    row=[]
    for i in range(len(L)):
        row.append(L[i])
        if i%4== 3:
            ans.append(row)
            row=[]
    return ans    

'''Lists of partial squares'''

#OneLessSquares=[]
#TwoLessSquares=[]
#ThreeLessSquares=[]
#FourLessSquares=[]
#FiveLessSquares=[]
#SixLessSquares=[]
#SevenLessSquares=[]
#EightLessSquares=[]

'''deleting entries from different latin squares can create the same partial squares.
These libraries are to remove any duplicates'''
OneLessSquaresDict={}
TwoLessSquaresDict={}
ThreeLessSquaresDict={}
FourLessSquaresDict={}
FiveLessSquaresDict={}
SixLessSquaresDict={}
SevenLessSquaresDict={}
EightLessSquaresDict={}

'''creating lists and dictionaries of up to 8 cancelled entries'''
for a in FullSquares:
    for b in range(0,16):
        M=copy.deepcopy(a)
        M[b]=7
        #OneLessSquares.append(M)
        OneLessSquaresDict[listToString(M)]=ListToSquare(M)

        for c in range(b+1,16):
            N=copy.deepcopy(M)
            N[c]=7
            #TwoLessSquares.append(N)
            TwoLessSquaresDict[listToString(N)]=ListToSquare(N)
            
            for d in range(c+1,16):
                L=copy.deepcopy(N)
                L[d]=7
                #ThreeLessSquares.append(L)
                ThreeLessSquaresDict[listToString(L)]=ListToSquare(L)

                for e in range(d+1,16):
                    O=copy.deepcopy(L)
                    O[e]=7
                    #FourLessSquares.append(O)
                    FourLessSquaresDict[listToString(O)]=ListToSquare(O)

                    for f in range(e+1,16):
                        P=copy.deepcopy(O)
                        P[f]=7
                        #FiveLessSquares.append(P)
                        FiveLessSquaresDict[listToString(P)]=ListToSquare(P)

                        for g in range(f+1,16):
                            Q=copy.deepcopy(P)
                            Q[g]=7
                            #SixLessSquares.append(Q)
                            SixLessSquaresDict[listToString(Q)]=ListToSquare(Q)

                            for h in range(g+1,16):
                                R=copy.deepcopy(Q)
                                R[h]=7
                                #SevenLessSquares.append(R)
                                SevenLessSquaresDict[listToString(R)]=ListToSquare(R)

                                for r in range(h+1,16):
                                    S=copy.deepcopy(R)
                                    S[r]=7
                                    #EightLessSquares.append(S)
                                    EightLessSquaresDict[listToString(S)]=ListToSquare(S)


''' The purpose of json is to encode the data in the dictionary in a text file that when it is read
again later it will be interpreted as a list, and not just a really long string'''
        
import json

with open('DictionariesOfPartialLatinCubes/OnePartials.txt','w') as filehandle:
    json.dump(list(OneLessSquaresDict.values()),filehandle)

'''
Here is how you read in this information for the other document that needs the partial squares
newdict={}
with open('listfile.txt','r') as filehandle:
    newdict=json.load(filehandle)'''


with open('DictionariesOfPartialLatinCubes/TwoPartials.txt','w') as filehandle:
    json.dump(list(TwoLessSquaresDict.values()),filehandle)

with open('DictionariesOfPartialLatinCubes/ThreePartials.txt','w') as filehandle:
    json.dump(list(ThreeLessSquaresDict.values()),filehandle)

with open('DictionariesOfPartialLatinCubes/FourPartials.txt','w') as filehandle:
    json.dump(list(FourLessSquaresDict.values()),filehandle)

with open('DictionariesOfPartialLatinCubes/FivePartials.txt','w') as filehandle:
    json.dump(list(FiveLessSquaresDict.values()),filehandle)

with open('DictionariesOfPartialLatinCubes/SixPartials.txt','w') as filehandle:
    json.dump(list(SixLessSquaresDict.values()),filehandle)

with open('DictionariesOfPartialLatinCubes/SevenPartials.txt','w') as filehandle:
    json.dump(list(SevenLessSquaresDict.values()),filehandle)

with open('DictionariesOfPartialLatinCubes/EightPartials.txt','w') as filehandle:
    json.dump(list(EightLessSquaresDict.values()),filehandle)

print(newdict)

