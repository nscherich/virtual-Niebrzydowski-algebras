import ListofLatinCubes
ListOfCubes=ListofLatinCubes.N

import ArrayListOfLatinSquares4by4
ListOfSquares=ArrayListOfLatinSquares4by4.M

import json
'''
with open('DictionariesOfPartialLatinCubes/OnePartials.txt','r') as filehandle:
    ListOfPartialsOne=json.load(filehandle)

with open('DictionariesOfPartialLatinCubes/TwoPartials.txt','r') as filehandle:
    ListOfPartialsTwo=json.load(filehandle)

with open('DictionariesOfPartialLatinCubes/ThreePartials.txt','r') as filehandle:
    ListOfPartialsThree=json.load(filehandle)

with open('DictionariesOfPartialLatinCubes/FourPartials.txt','r') as filehandle:
    ListOfPartialsFour=json.load(filehandle)

with open('DictionariesOfPartialLatinCubes/FivePartials.txt','r') as filehandle:
    ListOfPartialsFive=json.load(filehandle)
'''
with open('DictionariesOfPartialLatinCubes/SixPartials.txt','r') as filehandle:
    ListOfPartialsSix=json.load(filehandle)
'''
with open('DictionariesOfPartialLatinCubes/SevenPartials.txt','r') as filehandle:
    ListOfPartialsSeven=json.load(filehandle)

with open('DictionariesOfPartialLatinCubes/EightPartials.txt','r') as filehandle:
    ListOfPartialsEight=json.load(filehandle)
'''
''' This document imports the list of latin cubes and latin squares. It creates
 a tuple of two cubes and a square and checks if it satisfies all the N algebra
 axioms'''

#Need to create a list of of pairs of latin cubes and one latin square to
# send to the NalgTest program.

#print(len(ListOfCubes))
#print(len(ListOfSquares))

#n=ListOfCubes[0]

#for a in ListOfCubes:
#    currentTuple=[n]
#    currentTuple.append(a)
#    for b in ListOfSquares:
#         currentTuple.append(b)
         


def sBracketTest(N):
    '''takes in a single Latin cube and checks to see if it satisfies the
        [,]-only relations
    '''
    answer=False
    
    #checking the N tribracket
    #%%[a,b,[b,c,d]] = [a,[a,b,c],[[a,b,c],c,d]]
    size=len(N)
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                for d in range(0,size):
                    if N[a][b][N[b][c][d]] != N[a][N[a][b][c]][N[N[a][b][c]][c][d]]:
                        #print("ax1")
                        return answer
                    
    #%%[[a,b,c],c,d] = [[a,b,[b,c,d]],[b,c,d],d]   
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                for d in range(0,size):
                    if N[N[a][b][c]][c][d] != N[N[a][b][N[b][c][d]]][N[b][c][d]][d]:
                        #print("ax2")
                        return answer                   

    answer=True
    return answer


sBracketList=[]

from time import gmtime, strftime
print (strftime( "%H:%M:%S", gmtime()))

for a in ListOfCubes:
    if sBracketTest(a)==True:
        sBracketList.append(a)
        #print("got one!")
                 
print (strftime( "%H:%M:%S", gmtime()))        
print(len(sBracketList))


def aBracketTest(N):
    '''takes in a single Latin cube and checks to see if it satisfies the
        <,>-only relations
    '''
    answer=False
    
    size=len(N)
    
    #%%< a, < a,b,c >, c > =b  - I don't like that is says b here
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                if N[a][N[a][b][c]][c] != b: ##
                    #print("ax3")
                    return answer
                
    #%%< a,b, < b,c,d >> = < a, < a,b,c, >, < < a,b,c >, c,d > > 
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                for d in range(0,size):
                    if N[a][b][N[b][c][d]] != N[a][N[a][b][c]][N[N[a][b][c]][c][d]]:
                        #print("Ax4")
                        return answer
                
    #%%< < a,b,c >, c,d > = < < a,b, < b,c,d > >, < b,c,d >, d > 
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                for d in range(0,size):
                    if N[N[a][b][c]][c][d] != N[N[a][b][N[b][c][d]]][N[b][c][d]][d]:
                        #print("ax5")
                        return answer
                    
    answer=True
    return answer

aBracketList=[]
for a in ListOfCubes:
    if aBracketTest(a)==True:
        aBracketList.append(a)
        #print("got one!")

print(len(aBracketList))

def BracketCompatTest(N):
    ''' Takes in two brackets and checks if they are compatible'''
    answer=False
    
    size=len(N)
    #%%[a,b < b,c,d >]= < a, < a,b,c >, [ < a,b,c >, c,d] > 
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                for d in range(0,size):
                    if N[0][a][b][N[1][b][c][d]] != N[1][a][N[1][a][b][c]][N[0][N[1][a][b][c]][c][d]]:
                        #print("ax6")
                        return answer
                    
    #%%[ < a,b,c >, c,d ] = < [a,b, < b,c,d >], < b,c,d>, d> 
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                for d in range(0,size):
                    if N[0][N[1][a][b][c]][c][d] != N[1][N[0][a][b][N[1][b][c][d]]][N[1][b][c][d]][d]:
                        #print("ax7")
                        return answer
    answer=True
    return answer

CompatList=[]
for a in sBracketList:
    for b in aBracketList:
        currenttuple=[a,b]
        if BracketCompatTest(currenttuple)== True:
            CompatList.append(currenttuple)

print("Length of compatible brackets")
print(len(CompatList))


def NAlgTest(N):
    ''' takes in a tuple of latin Cube, latin cube, latin square and checks if they are compatible
    '''

    answer=False
    
    size=3 #len(N)

                    
    #%%< a,b,c > c = < ab, b,c > 
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                if N[2][a][b] != 7 and N[2][N[1][a][b][c]][c] != 7and N[2][N[1][a][b][c]][c] != N[1][N[2][a][b]][b][c]:
                    #print("ax8")
                    return answer
                
    #%%< a, ab, < ab, b,c > > = < a,b,c > 
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                if N[2][a][b] != 7 and N[1][a][N[2][a][b]][N[1][N[2][a][b]][b][c]] != N[1][a][b][c]:
                    #print("ax9")
                    return answer
                
    #%%a < a,b,c > = < a,b,bc > 
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                if N[2][b][c] != 7 and N[2][a][N[1][a][b][c]] != N[1][a][b][N[2][b][c]]:
                    #print("ax10")
                    return answer
                
    #%%< < a,b,bc >, bc,c > = < a,b,c > 
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                if N[2][b][c] != 7 and N[1][N[1][a][b][N[2][b][c]]][N[2][b][c]][c] != N[1][a][b][c]:
                    #print("ax11")
                    return answer

    #[a,ab,b]=ab
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                if N[2][a][b] != 7 and N[0][a][N[2][a][b]][b] !=N[2][a][b]:
                    #print("ax12")
                    return answer

    #a[a,b,c]=[a,b,bc]
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                if N[2][b][c] != 7 and N[2][a][N[0][a][b][c]] != N[0][a][b][N[2][b][c]]:
                    #print("ax13")
                    return answer

    #[a,b,c]c=[ab,b,c]
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                if N[2][a][b] != 7 and N[2][N[0][a][b][c]][c] !=7 and N[2][N[0][a][b][c]][c] != N[0][N[2][a][b]][b][c]:
                    #print("ax14")
                    return answer

    #[a,b,c]=[[a,b,bc],bc,c]
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                if N[2][b][c] != 7 and N[0][a][b][c] != N[0][N[0][a][b][N[2][b][c]]][N[2][b][c]][c]:
                    #print("ax15")
                    return answer

    #[a,b,c]=[a,ab,[ab,b,c]]
    for a in range(0,size):
        for b in range(0,size):
            for c in range(0,size):
                if N[2][a][b] != 7 and N[0][a][b][c] != N[0][a][N[2][a][b]][N[0][N[2][a][b]][b][c]]:
                    #print("ax16")
                    #print(a)
                    #print(b)
                    #print(c)
                    #print(N[0][a][b][c])
                    #print(N[0][N[2][a][b]][N[0][N[2][a][b]][b][c]])
                    return answer

    answer=True
    return answer

#K=[sBracketList[0],aBracketList[0],ListOfSquares[0]]
#print(NAlgTest(K))

NAlgList=[]
currenttuple=[]
print (strftime( "%H:%M:%S", gmtime()))
#import PartialLatinSquares
#Partial5List=PartialLatinSquares.FiveList
#Partial4Dict=PartialLatinSquares.FourLessSquaresDict
#print (strftime( "%H:%M:%S", gmtime()))

#count=0

for a in CompatList:
    for c in ListOfPartialsSix: 
         currenttuple=[a[0],a[1],c]
         if NAlgTest(currenttuple)==True:
            NAlgList.append(currenttuple)




print (strftime( "%H:%M:%S", gmtime()))
print(len(NAlgList))

with open('DictionariesOfPartialLatinCubes/NAlgList.txt','w') as filehandle:
    json.dump(NAlgList,filehandle)


#   ''' for c in ListOfPartialsOne: 
#         currenttuple=[a[0],a[1],c]
 #        if NAlgTest(currenttuple)==True:
 #           NALgList.append(currenttuple)
 #   for c in ListOfPartialsTwo: 
 #        currenttuple=[a[0],a[1],c]
 #        if NAlgTest(currenttuple)==True:
 #           NALgList.append(currenttuple)
 #   for c in ListOfPartialsThree: 
 #        currenttuple=[a[0],a[1],c]
 #        if NAlgTest(currenttuple)==True:
 #           NALgList.append(currenttuple)
 #   for c in ListOfPartialsFour: 
 #        currenttuple=[a[0],a[1],c]
  #       if NAlgTest(currenttuple)==True:
  #          NALgList.append(currenttuple)
  #  for c in ListOfPartialsFive: 
  #       currenttuple=[a[0],a[1],c]
  #       if NAlgTest(currenttuple)==True:
  #          NAlgList.append(currenttuple)

 #for c in ListOfPartialsSeven: 
 #        currenttuple=[a[0],a[1],c]
 #        if NAlgTest(currenttuple)==True:
 #           NAlgList.append(currenttuple)
 #   for c in ListOfPartialsEight: 
  #       currenttuple=[a[0],a[1],c]
   #      if NAlgTest(currenttuple)==True:
   #         NAlgList.append(currenttuple)'''
