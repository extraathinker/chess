# importing libraries
import pygame

# initializing pygame
pygame.init()

# making the screen
board = pygame.display.set_mode((600,600))
pygame.display.set_caption('chess')

# constants

boardStatus = {}
playStatus = False
moveStatus = True
possible = []
inMotionStatus = False
inHand = ''
cutPiece = []
player = 'white'
check = False
playerPos = 0
newPos = 0
pieceDict = {'whiteKing':0,'whiteQueen':0,'whiteWazir1':0, 'whiteWazir2':0,
             'whiteHathi1': 0,'whiteHathi2': 0,'whiteGhora1': 0,'whiteGhora2': 0,
            'whiteSanik1': 0,'whiteSanik2': 0,'whiteSanik3': 0,'whiteSanik4': 0,
            'whiteSanik5': 0,'whiteSanik6': 0,'whiteSanik7': 0,'whiteSanik8': 0,
            'blackKing': 0,'blackQueen':0,'blackWazir1':0, 'blackWazir2':0,
            'blackHathi1': 0,'blackHathi2': 0,'blackGhora1': 0,'blackGhora2': 0,
            'blackSanik1': 0,'blackSanik2': 0,'blackSanik3': 0,'blackSanik4': 0,
            'blackSanik5': 0,'blackSanik6': 0,'blackSanik7': 0,'blackSanik8': 0}
# defining locations for blitting image
location= []
locX = 20
locY = 20
for m in range(8):
    for n in range(8):
        location.append([locX,locY])
        locX += 75
    locX = 20 
    locY += 75

# defining boxes
box = []
for k in range(8):
    for l in range(8):
        box.append(pygame.Rect(l*75,k*75,75,75))

# storing pieces information in dictionary
assign = {}
for ab in range(64):
    assign[ab] = ''

# assigning boardstatus value
for pl in range(64):
    boardStatus[pl] = False

# importing images
whiteKing = pygame.image.load('chess/whiteking.png')
whiteQueen = pygame.image.load('chess/whiteQueen.png')
whiteSanik = pygame.image.load('chess/whitesanik.png')
whiteHathi = pygame.image.load('chess/whitehathi.png')
whiteWazir = pygame.image.load('chess/whitewazir.png')
whiteGhora = pygame.image.load('chess/whiteghora.png')
blackKing = pygame.image.load('chess/blackking.png')
blackQueen = pygame.image.load('chess/blackQueen.png')
blackSanik = pygame.image.load('chess/blacksanik.png')
blackHathi = pygame.image.load('chess/blackhathi.png')
blackWazir = pygame.image.load('chess/blackwazir.png')
blackGhora = pygame.image.load('chess/blackghora.png')

# defining the location of images
wkX = location[4][0]
wkY = location[4][1]
wqX = location[3][0]
wqY = location[3][1]
ws1X = location[8][0]
ws1Y = location[8][1]
ws2X = location[9][0]
ws2Y = location[9][1]
ws3X = location[10][0]
ws3Y = location[10][1]
ws4X = location[11][0]
ws4Y = location[11][1]
ws5X = location[12][0]
ws5Y = location[12][1]
ws6X = location[13][0]
ws6Y = location[13][1]
ws7X = location[14][0]
ws7Y = location[14][1]
ws8X = location[15][0]
ws8Y = location[15][1]
wh1X = location[0][0]
wh1Y = location[0][1]
wh2X = location[7][0]
wh2Y = location[7][1]
ww1X = location[2][0]
ww1Y = location[2][1]
ww2X = location[5][0]
ww2Y = location[5][1]
wg1X = location[1][0]
wg1Y = location[1][1]
wg2X = location[6][0]
wg2Y = location[6][1]
bkX = location[59][0]
bkY = location[59][1]
bqX = location[60][0]
bqY = location[60][1]
bs1X = location[48][0]
bs1Y = location[48][1]
bs2X = location[49][0]
bs2Y = location[49][1]
bs3X = location[50][0]
bs3Y = location[50][1]
bs4X = location[51][0]
bs4Y = location[51][1]
bs5X = location[52][0]
bs5Y = location[52][1]
bs6X = location[53][0]
bs6Y = location[53][1]
bs7X = location[54][0]
bs7Y = location[54][1]
bs8X = location[55][0]
bs8Y = location[55][1]
bh1X = location[56][0]
bh1Y = location[56][1]
bh2X = location[63][0]
bh2Y = location[63][1]
bw1X = location[58][0]
bw1Y = location[58][1]
bw2X = location[61][0]
bw2Y = location[61][1]
bg1X = location[57][0]
bg1Y = location[57][1]
bg2X = location[62][0]
bg2Y = location[62][1]

# filled value
filled = [location[0],location[1],location[2],location[3],location[4],location[5],location[6],location[7],
          location[8],location[9],location[10],location[11],location[12],location[13],location[14],location[15],
          location[48],location[49],location[50],location[51],location[52],location[53],location[54],location[55],
          location[56],location[57],location[58],location[59],location[60],location[61],location[62],location[63]]

# color function for making chessboard
def fillColor(x,y):
    for j in range(8):
        if j % 2 == 0:
            board.fill((255,255,255),(x,y,75,75))
            x += 75
        else:
            x += 75


locationList = []
# defining movement of the king
def whiteKingMovement(abcd):
    locationList = []
    if abcd in [0]:
        plist = [0]
        for i in plist:
            if i == abcd:
                locationList.append(i+1)
                locationList.append(i+8)
                locationList.append(i+9)
                break
        for j in locationList:
            if 'black' in assign[j]:
                continue
            else:
                locationList.remove(j)
    elif abcd in [1,2,3,4,5,6]:
        plist = [1,2,3,4,5,6]
        for i in plist:
            if i == abcd:
                locationList.append(i-1)
                locationList.append(i+1)
                locationList.append(i+7)
                locationList.append(i+8)
                locationList.append(i+9)
                break
        for j in locationList:
            if 'black' in assign[j]:
                continue
            elif 'white' in assign[j]:
                locationList.remove(j)
    elif abcd in [7]:
        plist = [7]
        for i in plist:
            if i == abcd:
                locationList.append(i-1)
                locationList.append(i+7)
                locationList.append(i+8)
                break
        for j in locationList:
            if 'black' in assign[j]:
                continue
            else:
                locationList.remove(j)
    elif abcd in [8,16,24,32,40,48]:
        plist = [8,16,24,32,40,48]
        for i in plist:
            if i == abcd:
                locationList.append(i-8)
                locationList.append(i-7)
                locationList.append(i+1)
                locationList.append(i+8)
                locationList.append(i+9)
                break
        for j in locationList:
            if 'black' in assign[j]:
                continue
            else:
                locationList.remove(j)
    elif abcd in [9,10,11,12,13,14,17,18,19,20,21,22,25,26,27,28,29,30,33,34,35,36,37,38,41,42,43,44,45,46,49,50,51,52,53,54]:
        plist = [9,10,11,12,13,14,17,18,19,20,21,22,25,26,27,28,29,30,33,34,35,36,37,38,41,42,43,44,45,46,49,50,51,52,53,54]
        for i in plist:
            if i == abcd:
                locationList.append(i-9)
                locationList.append(i-8)
                locationList.append(i-1)
                locationList.append(i+1)
                locationList.append(i+7)
                locationList.append(i+8)
                locationList.append(i+9)
                break
        for j in locationList:
            if 'black' in assign[j]:
                continue
            else:
                locationList.remove(j)
    elif abcd in [15,23,31,39,47,55]:
        plist = [15,23,31,39,47,55]
        for i in plist:
            if i == abcd:
                locationList.append(i-9)
                locationList.append(i-8)
                locationList.append(i-1)
                locationList.append(i+7)
                locationList.append(i+8)
                break
        for j in locationList:
            if 'black' in assign[j]:
                continue
            else:
                locationList.remove(j)
    elif abcd in [56]:
        plist = [56]
        for i in plist:
            if i == abcd:
                locationList.append(i-8)
                locationList.append(i-7)
                locationList.append(i+1)
                break
        for j in locationList:
            if 'black' in assign[j]:
                continue
            else:
                locationList.remove(j)
    elif abcd in [57,58,59,60,61,62]:
        plist = [57,58,59,60,61,62]
        for i in plist:
            if i == abcd:
                locationList.append(i-9)
                locationList.append(i-8)
                locationList.append(i-7)
                locationList.append(i-1)
                locationList.append(i+1)
                break
        for j in locationList:
            if 'black' in assign[j]:
                continue
            else:
                locationList.remove(j)
    elif abcd in [63]:
        plist = [63]
        for i in plist:
            if i == abcd:
                locationList.append(i-9)
                locationList.append(i-8)
                locationList.append(i-1)
                break
        for j in locationList:
            if 'black' in assign[j]:
                continue
            else:
                locationList.remove(j)
    return locationList
def blackKingMovement(abcd):
    locationList = []
    if abcd in [0]:
        plist = [0]
        for i in plist:
            if i == abcd:
                locationList.append(i+1)
                locationList.append(i+8)
                locationList.append(i+9)
        for j in locationList:
            if 'white' in assign[j]:
                continue
            else:
                locationList.remove(j)
    elif abcd in [1,2,3,4,5,6]:
        plist = [1,2,3,4,5,6]
        for i in plist:
            if i == abcd:
                locationList.append(i-1)
                locationList.append(i+2)
                locationList.append(i+7)
                locationList.append(i+8)
                locationList.append(i+9)
        for j in locationList:
            if 'white' in assign[j]:
                continue
            else:
                locationList.remove(j)
    elif abcd in [7]:
        plist = [7]
        for i in plist:
            if i == abcd:
                locationList.append(i-1)
                locationList.append(i+7)
                locationList.append(i+8)
        for j in locationList:
            if 'white' in assign[j]:
                continue
            else:
                locationList.remove(j)
    elif abcd in [8,16,24,32,40,48]:
        plist = [8,16,24,32,40,48]
        for i in plist:
            if i == abcd:
                locationList.append(i-8)
                locationList.append(i-7)
                locationList.append(i+1)
                locationList.append(i+8)
                locationList.append(i+9)
        for j in locationList:
            if 'white' in assign[j]:
                continue
            else:
                locationList.remove(j)
    elif abcd in [9,10,11,12,13,14,17,18,19,20,21,22,25,26,27,28,29,30,33,34,35,36,37,38,41,42,43,44,45,46,49,50,51,52,53,54]:
        plist = [9,10,11,12,13,14,17,18,19,20,21,22,25,26,27,28,29,30,33,34,35,36,37,38,41,42,43,44,45,46,49,50,51,52,53,54]
        for i in plist:
            if i == abcd:
                locationList.append(i-9)
                locationList.append(i-8)
                locationList.append(i-1)
                locationList.append(i+1)
                locationList.append(i+7)
                locationList.append(i+8)
                locationList.append(i+9)
        for j in locationList:
            if 'white' in assign[j]:
                continue
            else:
                locationList.remove(j)
    elif abcd in [15,23,31,39,47,55]:
        plist = [15,23,31,39,47,55]
        for i in plist:
            if i == abcd:
                locationList.append(i-9)
                locationList.append(i-8)
                locationList.append(i-1)
                locationList.append(i+7)
                locationList.append(i+8)
        for j in locationList:
            if 'white' in assign[j]:
                continue
            else:
                locationList.remove(j)
    elif abcd in [56]:
        plist = [56]
        for i in plist:
            if i == abcd:
                locationList.append(i-8)
                locationList.append(i-7)
                locationList.append(i+1)
        for j in locationList:
            if 'white' in assign[j]:
                continue
            else:
                locationList.remove(j)
    elif abcd in [57,58,59,60,61,62]:
        plist = [57,58,59,60,61,62]
        for i in plist:
            if i == abcd:
                locationList.append(i-9)
                locationList.append(i-8)
                locationList.append(i-7)
                locationList.append(i-1)
                locationList.append(i+1)
        for j in locationList:
            if 'white' in assign[j]:
                continue
            else:
                locationList.remove(j)
    elif abcd in [63]:
        plist = [63]
        for i in plist:
            if i == abcd:
                locationList.append(i-9)
                locationList.append(i-8)
                locationList.append(i-1)
        for j in locationList:
            if 'white' in assign[j]:
                continue
            else:
                locationList.remove(j)  
    return locationList
    
def blackQueenMovement(abcd):
    locationList = []
    if abcd in [0]:
        plist = [0]
        myList1 = []
        myList2 = []
        myList3 = []
        mList1 = []
        mList2 = []
        mList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8):  
                    myList1.append(i + j)  # right 
                    myList2.append(i + j*8)  # down
                for j in range(1,8):  #right down
                    myList1.append(j*9)
                break
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    elif abcd in [1,2,3,4,5,6]:
        plist = [1,2,3,4,5,6]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        myList4 = []
        myList5 = []
        mList1 = []
        mList2 = []
        mList3 = []
        mList4 = []
        mlist5 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):  #left 
                    myList1.append(i - j)
                inc += 1
                for jj in range(1,9-inc):  #right
                    myList2.append(i + jj)
                inc += 1
                for jjj in range(1,8):  #down
                    myList2.append(i + jjj*8)
                inc += 1
                for jjjj in range(1,inc):  #left down
                    myList4.append(i + jjjj*7)
                inc += 1
                for jjjjj in range(1,9-inc):  #right down
                    myList5.append(i + jjjjj*9)
                inc += 1
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
        for llll in myList4:
            if 'white' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)+ 1]
                break
            elif 'black' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)]
                break
        for mmmm in mList4:
            locationList.append(mmmm)
        for lllll in myList5:
            if 'white' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)+ 1]
                break
            elif 'black' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)]
                break
        for mmmmm in mList5:
            locationList.append(mmmmm)
    elif abcd in [7]:
        plist = [7]
        mList1 = []
        mList2 = []
        mList3 = []
        myList1 = []
        myList2 = []
        myList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8):  #left
                    myList1.append(i - j)
                for jj in range(1,8):  #down
                    myList1.append(i + jj*8)
                for jjj in range(1,8):  #left down
                    myList3.append(i + jjj*7)
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    elif abcd in [8,16,24,32,40,48]:
        plist = [8,16,24,32,40,48]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        myList4 = []
        myList5 = []
        mList1 = []
        mList2 = []
        mList3 = []
        mList4 = []
        mList5 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc): # up
                    myList1.append(i - j*8)
                inc += 1
                for jj in range(1,8): #right
                    myList2.append(i + jj)
                inc += 1
                for jjj in range(1,9-inc): #down
                    myList3.append(i + jjj*8)
                inc += 1
                for jjjj in range(1,inc): # right up
                    myList4.append(i - jjjj*7)
                inc += 1
                for jjjjj in range(1,9-inc): #right down
                    myList5.append(i + jjjjj*9)
                inc += 1
                break
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
        for llll in myList4:
            if 'white' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)+ 1]
                break
            elif 'black' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)]
                break
        for mmmm in mList4:
            locationList.append(mmmm)
        for lllll in myList5:
            if 'white' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)+ 1]
                break
            elif 'black' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)]
                break
        for mmmmm in mList5:
            locationList.append(mmmmm)
    elif abcd in [9,10,11,12,13,14,17,18,19,20,21,22,25,26,27,28,29,30,33,34,35,36,37,38,41,42,43,44,45,46,49,50,51,52,53,54]:
        plist1 = [9,10,11,12,13,14]
        plist2 = [17,18,19,20,21,22]
        plist3 = [25,26,27,28,29,30]
        plist4 = [33,34,35,36,37,38]
        plist5 = [41,42,43,44,45,46]
        plist6 = [49,50,51,52,53,54]
        inc1 = 2
        myList1 = []
        myList2 = []
        myList3 = []
        myList4 = []
        myList5 = []
        myList6 = []
        myList7 = []
        myList8 = []
        mList1 = []
        mList2 = []
        mList3 = []
        mList4 = []
        mList5 = []
        mList6 = []
        mList7 = []
        mList8 = []
        pl = [plist1,plist2,plist3,plist4,plist5,plist6]
        for pp in pl:
            for i in pp:
                if i == abcd:
                    for j in range(1,inc1):  #left
                        myList1.append(i - j)
                    inc1 += pl.index(pp)
                    for jj in range(1,inc1):  #up
                        myList2.append(i - jj*8)
                    inc1 += pp.index(i+1)
                    for jjj in range(1,9-inc1): #right
                        myList3.append(i + jjj)
                    inc1 += pl.index(pp)
                    for jjjj in range(1,9-inc1):  #down
                        myList4.append(i + jjjj*8)
                    inc1 += pp.index(i+1)
                    for jjjjj in range(1,inc1):  #left up
                        myList5.append(i - jjjjj*9)
                    inc1 += pl.index(pp)
                    for jjjjjj in range(1,inc1):  #left down
                        myList6.append(i + jjjjjj*7)
                    inc1 += pp.index(i+1)
                    for jjjjjjj in range(1,inc1): #right up
                        myList7.append(i - jjjjjjj*7)
                    inc1 += pl.index(pp)
                    for jjjjjjjj in range(1,9-inc1):  #right down
                        myList8.append(i + jjjjjjjj*9)
                    inc1 += pp.index(i+1)
                    break
            break
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
        for llll in myList4:
            if 'white' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)+ 1]
                break
            elif 'black' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)]
                break
        for mmmm in mList4:
            locationList.append(mmmm)
        for lllll in myList5:
            if 'white' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)+ 1]
                break
            elif 'black' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)]
                break
        for mmmmm in mList5:
            locationList.append(mmmmm)
        for llllll in myList6:
            if 'white' in assign[llllll]:
                mList6 = myList6[:myList6.index(llllll)+ 1]
                break
            elif 'black' in assign[llllll]:
                mList6 = myList6[:myList6.index(llllll)]
                break
        for mmmmmm in mList6:
            locationList.append(mmmmmm)
        for lllllll in myList7:
            if 'white' in assign[lllllll]:
                mList7 = myList7[:myList7.index(lllllll)+ 1]
                break
            elif 'black' in assign[lllllll]:
                mList7 = myList7[:myList7.index(lllllll)]
                break
        for mmmmmmm in mList7:
            locationList.append(mmmmmmm)
        for llllllll in myList8:
            if 'white' in assign[llllllll]:
                mList8 = myList8[:myList8.index(llllllll)+ 1]
                break
            elif 'black' in assign[llllllll]:
                mList8 = myList8[:myList8.index(llllllll)]
                break
        for mmmmmmmm in mList8:
            locationList.append(mmmmmmmm)
    elif abcd in [15,23,31,39,47,55]:
        plist = [15,23,31,39,47,55]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        myList4 = []
        myList5 = []
        mList1 = []
        mList2 = []
        mList3 = []
        mList4 = []
        mList5 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):  #up
                    myList1.append(i - j*8)
                inc += 1
                for jj in range(1,9-inc):  #left
                    myList2.append(i - jj)
                inc += 1
                for jjj in range(1,9-inc):  #down
                    myList3.append(i + jjj*8)
                inc += 1
                for jjjj in range(1,inc):  #left up
                    myList4.append(i - jjjj*9)
                inc += 1
                for jjjjj in range(1,9-inc):  #left down
                    myList5.append(i + jjjjj*7)
                inc += 1
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
        for llll in myList4:
            if 'white' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)+ 1]
                break
            elif 'black' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)]
                break
        for mmmm in mList4:
            locationList.append(mmmm)
        for lllll in myList5:
            if 'white' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)+ 1]
                break
            elif 'black' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)]
                break
        for mmmmm in mList5:
            locationList.append(mmmmm)
    elif abcd in [56]:
        plist = [56]
        mList1 = []
        mList2 = []
        mList3 = []
        myList1 = []
        myList2 = []
        myList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8): #up
                    myList1.append(i - j*8)
                for jj in range(1,8): #right
                    myList2.append(i + jj)
                for jjj in range(1,8): #right up
                    myList3.append(i - jjj*7)
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    elif abcd in [57,58,59,60,61,62]:
        plist = [57,58,59,60,61,62]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        myList4 = []
        myList5 = []
        mList1 = []
        mList2 = []
        mList3 = []
        mList4 = []
        mList5 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):  # left
                    myList1.append(i - j)
                inc += 1
                for jj in range(1,8): # up
                    myList2.append(i - jj*8)
                inc += 1
                for jjj in range(1,9-inc): # right
                    myList3.append(i + jjj)
                inc += 1
                for jjjj in range(1,inc):  # left up
                    myList4.append(i - jjjj*9)
                inc += 1
                for jjjjj in range(1,9-inc): #right up
                    myList5.append(i - jjjjj*7)
                inc += 1
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
        for llll in myList4:
            if 'white' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)+ 1]
                break
            elif 'black' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)]
                break
        for mmmm in mList4:
            locationList.append(mmmm)
        for lllll in myList5:
            if 'white' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)+ 1]
                break
            elif 'black' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)]
                break
        for mmmmm in mList5:
            locationList.append(mmmmm)
    elif abcd in [63]:
        plist = [63]
        mList1 = []
        mList2 = []
        mList3 = []
        myList1 = []
        myList2 = []
        myList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8): # left
                    myList1.append(i - j)
                for jj in range(1,8): # up
                    myList2.append(i - jj*8)
                for jjj in range(1,8): # left up
                    myList3.append(i - jjj*9)
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    return locationList
def whiteQueenMovement(abcd):
    locationList = []
    if abcd in [0]:
        plist = [0]
        myList1 = []
        myList2 = []
        myList3 = []
        mList1 = []
        mList2 = []
        mList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8):  
                    myList1.append(i + j)  # right 
                    myList2.append(i + j*8)  # down
                for jj in range(1,8):  #right down
                    myList3.append(jj*9)
                break
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    elif abcd in [1,2,3,4,5,6]:
        plist = [1,2,3,4,5,6]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        myList4 = []
        myList5 = []
        mList1 = []
        mList2 = []
        mList3 = []
        mList4 = []
        mList5 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):  #left 
                    myList1.append(i - j)
                inc += 1
                for jj in range(1,9-inc):  #right
                    myList2.append(i + jj)
                inc += 1
                for jjj in range(1,8):  #down
                    myList3.append(i + jjj*8)
                inc += 1
                for jjjj in range(1,inc):
                    myList4.append(i + jjjj*7)
                inc += 1
                for jjjjj in range(1,9-inc):
                    myList5.append(i + jjjjj*9)
                inc += 1
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
        for llll in myList4:
            if 'black' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)+ 1]
                break
            elif 'white' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)]
                break
        for mmmm in mList4:
            locationList.append(mmmm)
        for lllll in myList5:
            if 'black' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)+ 1]
                break
            elif 'white' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)]
                break
        for mmmmm in mList5:
            locationList.append(mmmmm)
    elif abcd in [7]:
        plist = [7]
        mList1 = []
        mList2 = []
        mList3 = []
        myList1 = []
        myList2 = []
        myList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8):  #left
                    myList1.append(i - j)
                for jj in range(1,8):  #down
                    myList1.append(i + jj*8)
                for jjj in range(1,8):
                    myList3.append(i + jjj*7)
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    elif abcd in [8,16,24,32,40,48]:
        plist = [8,16,24,32,40,48]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        myList4 = []
        myList5 = []
        mList1 = []
        mList2 = []
        mList3 = []
        mList4 = []
        mList5 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc): # up
                    myList1.append(i - j*8)
                inc += 1
                for jj in range(1,8): #right
                    myList2.append(i + jj)
                inc += 1
                for jjj in range(1,9-inc): #down
                    myList3.append(i + jjj*8)
                inc += 1
                for jjjj in range(1,inc):
                    myList4.append(i - jjjj*7)
                inc += 1
                for jjjjj in range(1,9-inc):
                    myList5.append(i + jjjjj*9)
                inc += 1
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
        for llll in myList4:
            if 'black' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)+ 1]
                break
            elif 'white' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)]
                break
        for mmmm in mList4:
            locationList.append(mmmm)
        for lllll in myList5:
            if 'black' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)+ 1]
                break
            elif 'white' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)]
                break
        for mmmmm in mList5:
            locationList.append(mmmmm)
    elif abcd in [9,10,11,12,13,14,17,18,19,20,21,22,25,26,27,28,29,30,33,34,35,36,37,38,41,42,43,44,45,46,49,50,51,52,53,54]:
        plist1 = [9,10,11,12,13,14]
        plist2 = [17,18,19,20,21,22]
        plist3 = [25,26,27,28,29,30]
        plist4 = [33,34,35,36,37,38]
        plist5 = [41,42,43,44,45,46]
        plist6 = [49,50,51,52,53,54]
        inc1 = 2
        myList1 = []
        myList2 = []
        myList3 = []
        myList4 = []
        myList5 = []
        myList6 = []
        myList7 = []
        myList8 = []
        mList1 = []
        mList2 = []
        mList3 = []
        mList4 = []
        mList5 = []
        mList6 = []
        mList7 = []
        mList8 = []
        pl = [plist1,plist2,plist3,plist4,plist5,plist6]
        for pp in pl:
            for i in pp:
                if i == abcd:
                    for j in range(1,inc1):  #left
                        myList1.append(i - j)
                    inc1 += pl.index(pp)
                    for jj in range(1,inc1):  #up
                        myList2.append(i - jj*8)
                    inc1 += pp.index(i+1)
                    for jjj in range(1,9-inc1): #right
                        myList3.append(i + jjj)
                    inc1 += pl.index(pp)
                    for jjjj in range(1,9-inc1):  #down
                        myList4.append(i + jjjj*8)
                    inc1 += pp.index(i+1)
                    for jjjjj in range(1,inc1):  #left up
                        myList5.append(i - jjjjj*9)
                    inc1 += pl.index(pp)
                    for jjjjjj in range(1,inc1):  #left down
                        myList6.append(i + jjjjjj*7)
                    inc1 += pp.index(i+1)
                    for jjjjjjj in range(1,inc1): #right up
                        myList7.append(i - jjjjjjj*7)
                    inc1 += pl.index(pp)
                    for jjjjjjjj in range(1,9-inc1):  #right down
                        myList8.append(i + jjjjjjjj*9)
                    inc1 += pp.index(i+1)
                    break
            break
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
        for llll in myList4:
            if 'black' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)+ 1]
                break
            elif 'white' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)]
                break
        for mmmm in mList4:
            locationList.append(mmmm)
        for lllll in myList5:
            if 'black' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)+ 1]
                break
            elif 'white' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)]
                break
        for mmmmm in mList5:
            locationList.append(mmmmm)
        for llllll in myList6:
            if 'black' in assign[llllll]:
                mList6 = myList6[:myList6.index(llllll)+ 1]
                break
            elif 'white' in assign[llllll]:
                mList6 = myList6[:myList6.index(llllll)]
                break
        for mmmmmm in mList6:
            locationList.append(mmmmmm)
        for lllllll in myList7:
            if 'black' in assign[lllllll]:
                mList7 = myList7[:myList7.index(lllllll)+ 1]
                break
            elif 'white' in assign[lllllll]:
                mList7 = myList7[:myList7.index(lllllll)]
                break
        for mmmmmmm in mList7:
            locationList.append(mmmmmmm)
        for llllllll in myList8:
            if 'black' in assign[llllllll]:
                mList8 = myList8[:myList8.index(llllllll)+ 1]
                break
            elif 'white' in assign[llllllll]:
                mList8 = myList8[:myList8.index(llllllll)]
                break
        for mmmmmmmm in mList8:
            locationList.append(mmmmmmmm)
    elif abcd in [15,23,31,39,47,55]:
        plist = [15,23,31,39,47,55]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        myList4 = []
        myList5 = []
        mList1 = []
        mList2 = []
        mList3 = []
        mList4 = []
        mList5 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):  #up
                    myList1.append(i - j*8)
                inc += 1
                for jj in range(1,9-inc):  #left
                    myList2.append(i - jj)
                inc += 1
                for jjj in range(1,9-inc):  #down
                    myList2.append(i + jjj*8)
                inc += 1
                for jjjj in range(1,inc):
                    myList4.append(i - jjjj*9)
                inc += 1
                for jjjjj in range(1,9-inc):
                    myList5.append(i + jjjjj*7)
                inc += 1
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
        for llll in myList4:
            if 'black' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)+ 1]
                break
            elif 'white' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)]
                break
        for mmmm in mList4:
            locationList.append(mmmm)
        for lllll in myList5:
            if 'black' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)+ 1]
                break
            elif 'white' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)]
                break
        for mmmmm in mList5:
            locationList.append(mmmmm)
    elif abcd in [56]:
        plist = [56]
        mList1 = []
        mList2 = []
        mList3 = []
        myList1 = []
        myList2 = []
        myList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8): #up
                    myList1.append(i - j*8)
                for jj in range(1,8): #right
                    myList2.append(i + jj)
                for jjj in range(1,8):
                    myList1.append(i - jjj*7)
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    elif abcd in [57,58,59,60,61,62]:
        plist = [57,58,59,60,61,62]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        myList4 = []
        myList5 = []
        mList1 = []
        mList2 = []
        mList3 = []
        mList4 = []
        mList5 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):  # left
                    myList1.append(i - j)
                inc += 1
                for jj in range(1,8): # up
                    myList2.append(i - jj*8)
                inc += 1
                for jjj in range(1,9-inc): # right
                    myList3.append(i + jjj)
                inc += 1
                for jjjj in range(1,inc):
                    myList4.append(i - jjjj*9)
                inc += 1
                for jjjjj in range(1,9-inc):
                    myList5.append(i - jjjjj*7)
                inc += 1
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
        for llll in myList4:
            if 'black' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)+ 1]
                break
            elif 'white' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)]
                break
        for mmmm in mList4:
            locationList.append(mmmm)
        for lllll in myList5:
            if 'black' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)+ 1]
                break
            elif 'white' in assign[lllll]:
                mList5 = myList5[:myList5.index(lllll)]
                break
        for mmmmm in mList5:
            locationList.append(mmmmm)
    elif abcd in [63]:
        plist = [63]
        mList1 = []
        mList2 = []
        mList3 = []
        myList1 = []
        myList2 = []
        myList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8): # left
                    myList1.append(i - j)
                for jj in range(1,8): # up
                    myList2.append(i - jj*8)
                for jjj in range(1,8):
                    myList3.append(i - jjj*9)
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    return locationList

def blackWazirMovement(abcd):
    locationList = []
    if abcd in [0]:
        plist = [0]
        myList1 = []
        myList = []
        for i in plist:
            if i == abcd:
                for j in range(1,8):  #right down
                    myList1.append(j*9)
                break
        for k in myList1:
            if 'white' in assign[k]:
                myList = myList1[:myList1.index(k)+ 1]
                break
            elif 'black' in assign[k]:
                myList = myList1[:myList1.index(k)]
                break
        for l in myList:
            locationList.append(l)
    elif abcd in [1,2,3,4,5,6]:
        plist = [1,2,3,4,5,6]
        inc = 2
        myList1 = []
        myList2 = []
        mList1 = []
        mList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):  #left down
                    myList1.append(i + j*7)
                inc += 1
                for k in range(1,9-inc):  #right down
                    myList2.append(i + k*9)
                inc += 1
                break
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
    elif abcd in [7]:
        plist = [7]
        mList = []
        for i in plist:
            if i == abcd:
                for j in range(1,8):  #left down
                    locationList.append(i + j*7)
        for l in locationList:
            if 'white' in assign[l]:
                mList = locationList[:locationList.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList = locationList[:locationList.index(l)]
                break
        for m in mList:
            locationList.append(m)
    elif abcd in [8,16,24,32,40,48]:
        plist = [8,16,24,32,40,48]
        inc = 2
        myList1 = []
        myList2 = []
        mList1 = []
        mList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc): # right up
                    myList1.append(i - j*7)
                inc += 1
                for jj in range(1,9-inc): #right down
                    myList2.append(i + jj*9)
                inc += 1
                break
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
    elif abcd in [9,10,11,12,13,14,17,18,19,20,21,22,25,26,27,28,29,30,33,34,35,36,37,38,41,42,43,44,45,46,49,50,51,52,53,54]:
        plist1 = [9,10,11,12,13,14]
        plist2 = [17,18,19,20,21,22]
        plist3 = [25,26,27,28,29,30]
        plist4 = [33,34,35,36,37,38]
        plist5 = [41,42,43,44,45,46]
        plist6 = [49,50,51,52,53,54]
        inc1 = 2
        myList1 = []
        myList2 = []
        myList3 = []
        myList4 = []
        mList1 = []
        mList2 = []
        mList3 = []
        mList4 = []
        pl = [plist1,plist2,plist3,plist4,plist5,plist6]
        for pp in pl:
            for i in pp:
                if i == abcd:
                    for j in range(1,inc1):  #left up
                        myList1.append(i - j*9)
                    inc1 += pl.index(pp)
                    for k in range(1,inc1):  #left down
                        myList2.append(i + k*7)
                    inc1 += pp.index(i+1)
                    for l in range(1,inc1): #right up
                        myList3.append(i - l*7)
                    inc1 += pl.index(pp)
                    for m in range(1,9-inc1):  #right down
                        myList4.append(i + m*9)
                    inc1 += pp.index(i+1)
                    break
            break
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
        for llll in myList4:
            if 'white' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)+ 1]
                break
            elif 'black' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)]
                break
        for mmmm in mList4:
            locationList.append(mmmm)
    elif abcd in [15,23,31,39,47,55]:
        plist = [15,23,31,39,47,55]
        inc = 2
        myList1 = []
        myList2 = []
        mList1 = []
        mList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):  #left up
                    myList1.append(i - j*9)
                inc += 1
                for jj in range(1,9-inc):  #left down
                    myList2.append(i + jj*7)
                inc += 1
                break
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(m)
    elif abcd in [56]:
        plist = [56]
        mList1 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8): #right up
                    myList1.append(i - j*7)
                break
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
    elif abcd in [57,58,59,60,61,62]:
        plist = [57,58,59,60,61,62]
        inc = 2
        myList1 = []
        myList2 = []
        mList1 = []
        mList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):  # left up
                    myList1.append(i - j*9)
                inc += 1
                for k in range(1,9-inc): #right up
                    myList2.append(i - k*7)
                inc += 1
                break
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
    elif abcd in [63]:
        plist = [63]
        mList1 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8): # left up
                    myList1.append(i - j*9)
                break
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
    return locationList
def whiteWazirMovement(abcd):
    locationList = []
    if abcd in [0]:
        plist = [0]
        myList1 = []
        myList = []
        for i in plist:
            if i == abcd:
                for j in range(1,8):  #right down
                    myList1.append(j*9)
                break
        for k in myList1:
            if 'black' in assign[k]:
                myList = myList1[:myList1.index(k)+ 1]
                break
            elif 'white' in assign[k]:
                myList = myList1[:myList1.index(k)]
                break
        for l in myList:
            locationList.append(m)
    elif abcd in [1,2,3,4,5,6]:
        plist = [1,2,3,4,5,6]
        inc = 2
        myList1 = []
        myList2 = []
        mList1 = []
        mList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):
                    myList1.append(i + j*7)
                inc += 1
                for k in range(1,9-inc):
                    myList2.append(i + k*9)
                inc += 1
                break
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
        for mm in mList2:
            locationList.append(mm)
    elif abcd in [7]:
        plist = [7]
        mlist = []
        for i in plist:
            if i == abcd:
                for j in range(1,8):
                    locationList.append(i + j*7)
                break
        for l in locationList:
            if 'black' in assign[l]:
                mList = locationList[:locationList.index(l)+ 1]
            elif 'white' in assign[l]:
                mList = locationList[:locationList.index(l)]
                break
        for m in mList:
            locationList.append(m)
    elif abcd in [8,16,24,32,40,48]:
        plist = [8,16,24,32,40,48]
        inc = 2
        myList1 = []
        myList2 = []
        mList1 = []
        mList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):
                    myList1.append(i - j*7)
                inc += 1
                for jj in range(1,9-inc):
                    myList2.append(i + jj*9)
                inc += 1
            break
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
    elif abcd in [9,10,11,12,13,14,17,18,19,20,21,22,25,26,27,28,29,30,33,34,35,36,37,38,41,42,43,44,45,46,49,50,51,52,53,54]:
        plist1 = [9,10,11,12,13,14]
        plist2 = [17,18,19,20,21,22]
        plist3 = [25,26,27,28,29,30]
        plist4 = [33,34,35,36,37,38]
        plist5 = [41,42,43,44,45,46]
        plist6 = [49,50,51,52,53,54]
        inc1 = 2
        myList1 = []
        myList2 = []
        myList3 = []
        myList4 = []
        mList1 = []
        mList2 = []
        mList3 = []
        mList4 = []
        pl = [plist1,plist2,plist3,plist4,plist5,plist6]
        for pp in pl:
            for i in pp:
                if i == abcd:
                    for j in range(1,inc1):  #left up
                        myList1.append(i - j*9)
                    inc1 += pl.index(pp)
                    for k in range(1,inc1):  #left down
                        myList2.append(i + k*7)
                    inc1 += pp.index(i+1)
                    for l in range(1,inc1): #right up
                        myList3.append(i - l*7)
                    inc1 += pl.index(pp)
                    for m in range(1,9-inc1):  #right down
                        myList4.append(i + m*9)
                    inc1 += pp.index(i+1)
                    break
            break
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
        for llll in myList4:
            if 'black' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)+ 1]
                break
            elif 'white' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)]
                break
        for mmmm in mList4:
            locationList.append(mmmm)
    elif abcd in [15,23,31,39,47,55]:
        plist = [15,23,31,39,47,55]
        inc = 2
        myList1 = []
        myList2 = []
        mList1 = []
        mList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):
                    myList1.append(i - j*9)
                inc += 1
                for k in range(1,9-inc):
                    myList2.append(i + j*7)
                inc += 1
            break
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList1 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList1 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
    elif abcd in [56]:
        plist = [56]
        mList1  = []
        for i in plist:
            if i == abcd:
                for j in range(1,8):
                    myList1.append(i - j*7)
                break
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
    elif abcd in [57,58,59,60,61,62]:
        plist = [57,58,59,60,61,62]
        inc = 2
        myList1 = []
        myList2 = []
        mList1 = []
        mList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):
                    myList1.append(i - j*9)
                inc += 1
                for k in range(1,9-inc):
                    myList2.append(i - k*7)
                inc += 1
                break
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
    elif abcd in [63]:
        plist = [63]
        mlist = []
        for i in plist:
            if i == abcd:
                for j in range(1,8):
                    myList1.append(i - j*9)
                break
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m) 
    return locationList 

def blackGhoraMovement(abcd):
    locationList = []
    if abcd in [0]:
        plist = [0]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd + 10)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [1]:
        plist = [1]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd + 10)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [6]:
        plist = [6]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd + 6)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [7]:
        plist = [7]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd + 6)
                myList1.append(abcd + 15)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [8]:
        plist = [8]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 2)
                myList1.append(abcd + 10)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [15]:
        plist = [15]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd + 6)
                myList1.append(abcd + 15)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [2,3,4,5]:
        plist = [2,3,4,5]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd + 6)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
                myList1.append(abcd + 10)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [9]:
        plist = [9]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 6)
                myList1.append(abcd + 10)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [14]:
        plist = [14]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd + 6)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [10,11,12,13]:
        plist = [10,11,12,13]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd + 6)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
                myList1.append(abcd + 10)
                myList1.append(abcd - 6)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [16,24,32,40]:
        plist = [16,24,32,40]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 15)
                myList1.append(abcd + 17)
                myList1.append(abcd - 6)
                myList1.append(abcd + 10)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [17,25,33,41]:
        plist = [17,25,33,41]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
                myList1.append(abcd + 10)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [18,19,20,21,26,27,28,29,34,35,36,37,42,43,44,45]:
        plist = [18,19,20,21,26,27,28,29,34,35,36,37,42,43,44,45]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd + 6)
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
                myList1.append(abcd + 10)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [22,30,38,46]:
        plist = [22,30,38,46]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
                myList1.append(abcd + 6)
                myList1.append(abcd - 10)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [23,31,39,47]:
        plist = [23,31,39,47]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd + 6)
                myList1.append(abcd - 17)
                myList1.append(abcd + 15)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [50,51,52,53]:
        plist = [50,51,52,53]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd + 6)
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
                myList1.append(abcd + 10)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [58,59,60,61]:
        plist = [58,59,60,61]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [48]:
        plist = [48]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
                myList1.append(abcd + 10)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [49]:
        plist = [49]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
                myList1.append(abcd + 10)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [56]:
        plist = [56]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [57]:
        plist = [57]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [54]:
        plist = [54]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd + 6)
                myList1.append(abcd - 10)
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [55]:
        plist = [55]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd + 6)
                myList1.append(abcd - 17)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [62]:
        plist = [62]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [63]:
        plist = [63]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd - 17)
        for j in myList1:
            if 'black' in assign[j]:
                myList1.remove(j)
            elif 'white' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    return locationList
def whiteGhoraMovement(abcd):
    locationList = []
    if abcd in [0]:
        plist = [0]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd + 10)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [1]:
        plist = [1]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd + 10)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [6]:
        plist = [6]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd + 6)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [7]:
        plist = [7]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd + 6)
                myList1.append(abcd + 15)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [8]:
        plist = [8]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 2)
                myList1.append(abcd + 10)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [15]:
        plist = [15]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd + 6)
                myList1.append(abcd + 15)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [2,3,4,5]:
        plist = [2,3,4,5]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd + 6)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
                myList1.append(abcd + 10)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [9]:
        plist = [9]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 6)
                myList1.append(abcd + 10)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [14]:
        plist = [14]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd + 6)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [10,11,12,13]:
        plist = [10,11,12,13]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd + 6)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
                myList1.append(abcd + 10)
                myList1.append(abcd - 6)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [16,24,32,40]:
        plist = [16,24,32,40]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 15)
                myList1.append(abcd + 17)
                myList1.append(abcd - 6)
                myList1.append(abcd + 10)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [17,25,33,41]:
        plist = [17,25,33,41]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
                myList1.append(abcd + 10)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [18,19,20,21,26,27,28,29,34,35,36,37,42,43,44,45]:
        plist = [18,19,20,21,26,27,28,29,34,35,36,37,42,43,44,45]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd + 6)
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
                myList1.append(abcd + 10)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [22,30,38,46]:
        plist = [22,30,38,46]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
                myList1.append(abcd + 6)
                myList1.append(abcd - 10)
                myList1.append(abcd + 15)
                myList1.append(abcd + 17)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [23,31,39,47]:
        plist = [23,31,39,47]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd + 6)
                myList1.append(abcd - 17)
                myList1.append(abcd + 15)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [50,51,52,53]:
        plist = [50,51,52,53]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd + 6)
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
                myList1.append(abcd + 10)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [58,59,60,61]:
        plist = [58,59,60,61]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [48]:
        plist = [48]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
                myList1.append(abcd + 10)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [49]:
        plist = [49]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
                myList1.append(abcd + 10)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [56]:
        plist = [56]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [57]:
        plist = [57]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
                myList1.append(abcd - 6)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [54]:
        plist = [54]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd + 6)
                myList1.append(abcd - 10)
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [55]:
        plist = [55]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd + 6)
                myList1.append(abcd - 17)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [62]:
        plist = [62]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd - 17)
                myList1.append(abcd - 15)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k)
    elif abcd in [63]:
        plist = [63]
        myList1 = []
        for i in plist:
            if i == abcd:
                myList1.append(abcd - 10)
                myList1.append(abcd - 17)
        for j in myList1:
            if 'white' in assign[j]:
                myList1.remove(j)
            elif 'black' in assign[j]:
                continue
        for k in myList1:
            locationList.append(k) 
    return locationList

def blackHathiMovement(abcd):
    locationList = []
    if abcd in [0]:
        plist = [0]
        myList1 = []
        myList2 = []
        mList1 = []
        mList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8):  
                    myList1.append(i + j)  # right 
                    myList2.append(i + j*8)  # down
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
    elif abcd in [1,2,3,4,5,6]:
        plist = [1,2,3,4,5,6]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        mList1 = []
        mList2 = []
        mList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):  #left 
                    myList1.append(i - j)
                inc += 1
                for jj in range(1,9-inc):  #right
                    myList2.append(i + jj)
                inc += 1
                for jjj in range(1,8):  #down
                    myList3.append(i + jjj*8)
                inc += 1
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    elif abcd in [7]:
        plist = [7]
        mList1 = []
        mList2 = []
        myList1 = []
        myList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8):  #left
                    myList1.append(i - j)
                for jj in range(1,8):  #down
                    myList1.append(i + jj*8)
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
    elif abcd in [8,16,24,32,40,48]:
        plist = [8,16,24,32,40,48]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        mList1 = []
        mList2 = []
        mList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc): # up
                    myList1.append(i - j*8)
                inc += 1
                for jj in range(1,8): #right
                    myList2.append(i + jj)
                inc += 1
                for jjj in range(1,9-inc): #down
                    myList3.append(i + jjj*8)
                inc += 1
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    elif abcd in [9,10,11,12,13,14,17,18,19,20,21,22,25,26,27,28,29,30,33,34,35,36,37,38,41,42,43,44,45,46,49,50,51,52,53,54]:
        plist1 = [9,10,11,12,13,14]
        plist2 = [17,18,19,20,21,22]
        plist3 = [25,26,27,28,29,30]
        plist4 = [33,34,35,36,37,38]
        plist5 = [41,42,43,44,45,46]
        plist6 = [49,50,51,52,53,54]
        inc1 = 2
        myList1 = []
        myList2 = []
        myList3 = []
        myList4 = []
        mList1 = []
        mList2 = []
        mList3 = []
        mList4 = []
        pl = [plist1,plist2,plist3,plist4,plist5,plist6]
        for pp in pl:
            for i in pp:
                if i == abcd:
                    for j in range(1,inc1):  #left
                        myList1.append(i - j)
                    inc1 += pl.index(pp)
                    for jj in range(1,inc1):  #up
                        myList2.append(i - jj*8)
                    inc1 += pp.index(i+1)
                    for jjj in range(1,9-inc1): #right
                        myList3.append(i + jjj)
                    inc1 += pl.index(pp)
                    for jjjj in range(1,9-inc1):  #down
                        myList4.append(i + jjjj*8)
                    inc1 += pp.index(i+1)
                    break
            break
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
        for llll in myList4:
            if 'white' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)+ 1]
                break
            elif 'black' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)]
                break
        for mmmm in mList4:
            locationList.append(mmmm)
    elif abcd in [15,23,31,39,47,55]:
        plist = [15,23,31,39,47,55]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        mList1 = []
        mList2 = []
        mList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):  #up
                    myList1.append(i - j*8)
                inc += 1
                for jj in range(1,9-inc):  #left
                    myList2.append(i - jj)
                inc += 1
                for jjj in range(1,9-inc):  #down
                    myList2.append(i + jjj*8)
                inc += 1
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    elif abcd in [56]:
        plist = [56]
        mList1 = []
        mList2 = []
        myList1 = []
        myList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8): #up
                    myList1.append(i - j*8)
                for jj in range(1,8): #right
                    myList2.append(i + jj)
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
    elif abcd in [57,58,59,60,61,62]:
        plist = [57,58,59,60,61,62]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        mList1 = []
        mList2 = []
        mList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):  # left
                    myList1.append(i - j)
                inc += 1
                for jj in range(1,8): # up
                    myList2.append(i - jj*8)
                inc += 1
                for jjj in range(1,9-inc): # right
                    myList3.append(i + jjj)
                inc += 1
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    elif abcd in [63]:
        plist = [63]
        mList1 = []
        mList2 = []
        myList1 = []
        myList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8): # left
                    myList1.append(i - j)
                for jj in range(1,8): # up
                    myList2.append(i - jj*8)
        for l in myList1:
            if 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
    return locationList
def whiteHathiMovement(abcd):
    locationList = []
    if abcd in [0]:
        plist = [0]
        myList1 = []
        myList2 = []
        mList1 = []
        mList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8):  
                    myList1.append(i + j)  # right 
                    myList2.append(i + j*8)  # down
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
    elif abcd in [1,2,3,4,5,6]:
        plist = [1,2,3,4,5,6]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        mList1 = []
        mList2 = []
        mList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):  #left 
                    myList1.append(i - j)
                inc += 1
                for jj in range(1,9-inc):  #right
                    myList2.append(i + jj)
                inc += 1
                for jjj in range(1,8):  #down
                    myList3.append(i + jjj*8)
                inc += 1
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    elif abcd in [7]:
        plist = [7]
        mList1 = []
        mList2 = []
        myList1 = []
        myList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8):  #left
                    myList1.append(i - j)
                for jj in range(1,8):  #down
                    myList1.append(i + jj*8)
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
    elif abcd in [8,16,24,32,40,48]:
        plist = [8,16,24,32,40,48]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        mList1 = []
        mList2 = []
        mList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc): # up
                    myList1.append(i - j*8)
                inc += 1
                for jj in range(1,8): #right
                    myList2.append(i + jj)
                inc += 1
                for jjj in range(1,9-inc): #down
                    myList3.append(i + jjj*8)
                inc += 1
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    elif abcd in [9,10,11,12,13,14,17,18,19,20,21,22,25,26,27,28,29,30,33,34,35,36,37,38,41,42,43,44,45,46,49,50,51,52,53,54]:
        plist1 = [9,10,11,12,13,14]
        plist2 = [17,18,19,20,21,22]
        plist3 = [25,26,27,28,29,30]
        plist4 = [33,34,35,36,37,38]
        plist5 = [41,42,43,44,45,46]
        plist6 = [49,50,51,52,53,54]
        inc1 = 2
        myList1 = []
        myList2 = []
        myList3 = []
        myList4 = []
        mList1 = []
        mList2 = []
        mList3 = []
        mList4 = []
        pl = [plist1,plist2,plist3,plist4,plist5,plist6]
        for pp in pl:
            for i in pp:
                if i == abcd:
                    for j in range(1,inc1):  #left
                        myList1.append(i - j)
                    inc1 += pl.index(pp)
                    for jj in range(1,inc1):  #up
                        myList2.append(i - jj*8)
                    inc1 += pp.index(i+1)
                    for jjj in range(1,9-inc1): #right
                        myList3.append(i + jjj)
                    inc1 += pl.index(pp)
                    for jjjj in range(1,9-inc1):  #down
                        myList4.append(i + jjjj*8)
                    inc1 += pp.index(i+1)
                    break
            break
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
        for llll in myList4:
            if 'black' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)+ 1]
                break
            elif 'white' in assign[llll]:
                mList4 = myList4[:myList4.index(llll)]
                break
        for mmmm in mList4:
            locationList.append(mmmm)
    elif abcd in [15,23,31,39,47,55]:
        plist = [15,23,31,39,47,55]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        mList1 = []
        mList2 = []
        mList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):  #up
                    myList1.append(i - j*8)
                inc += 1
                for jj in range(1,9-inc):  #left
                    myList2.append(i - jj)
                inc += 1
                for jjj in range(1,9-inc):  #down
                    myList3.append(i + jjj*8)
                inc += 1
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    elif abcd in [56]:
        plist = [56]
        mList1 = []
        mList2 = []
        myList1 = []
        myList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8): #up
                    myList1.append(i - j*8)
                for jj in range(1,8): #right
                    myList2.append(i + jj)
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
    elif abcd in [57,58,59,60,61,62]:
        plist = [57,58,59,60,61,62]
        inc = 2
        myList1 = []
        myList2 = []
        myList3 = []
        mList1 = []
        mList2 = []
        mList3 = []
        for i in plist:
            if i == abcd:
                for j in range(1,inc):  # left
                    myList1.append(i - j)
                inc += 1
                for jj in range(1,8): # up
                    myList2.append(i - jj*8)
                inc += 1
                for jjj in range(1,9-inc): # right
                    myList3.append(i + jjj)
                inc += 1
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)
        for lll in myList3:
            if 'black' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)+ 1]
                break
            elif 'white' in assign[lll]:
                mList3 = myList3[:myList3.index(lll)]
                break
        for mmm in mList3:
            locationList.append(mmm)
    elif abcd in [63]:
        plist = [63]
        mList1 = []
        mList2 = []
        myList1 = []
        myList2 = []
        for i in plist:
            if i == abcd:
                for j in range(1,8): # left
                    myList1.append(i - j)
                for jj in range(1,8): # up
                    myList2.append(i - jj*8)
        for l in myList1:
            if 'black' in assign[l]:
                mList1 = myList1[:myList1.index(l)+ 1]
                break
            elif 'white' in assign[l]:
                mList1 = myList1[:myList1.index(l)]
                break
        for m in mList1:
            locationList.append(m)
        for ll in myList2:
            if 'black' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)+ 1]
                break
            elif 'white' in assign[ll]:
                mList2 = myList2[:myList2.index(ll)]
                break
        for mm in mList2:
            locationList.append(mm)  
    return locationList  

def whiteSanikMovement(abcd):
    myList1 = []
    if abcd in [8]:
        myList1.append(abcd + 8)
        myList1.append(abcd + 16)
        if 'white' in assign[abcd + 8] or 'black' in assign[abcd + 8]:
            myList1.remove(abcd + 8)
        elif 'white' in assign[abcd + 16] or 'black' in assign[abcd + 16]:
            myList1.remove(abcd + 16)
        elif 'black' in assign[abcd + 9]:
            myList1.append(abcd + 9)
    elif abcd in [15]:
        myList1.append(abcd + 8)
        myList1.append(abcd + 16)
        if 'white' in assign[abcd + 8] or 'black' in assign[abcd + 8]:
            myList1.remove(abcd + 8)
        elif 'white' in assign[abcd + 16] or 'black' in assign[abcd + 16]:
            myList1.remove(abcd + 16)
        elif 'black' in assign[abcd + 7]:
            myList1.append(abcd + 7)
    elif abcd in [16,24,32,40,48]:
        myList1.append(abcd + 8)
        if 'white' in assign[abcd + 8] or 'black' in assign[abcd + 8]:
            myList1.remove(abcd + 8)
        elif 'black' in assign[abcd + 9]:
            myList1.append(abcd + 9)
    elif abcd in [23,31,39,47,55]:
        myList1.append(abcd + 8)
        if 'white' in assign[abcd + 8] or 'black' in assign[abcd + 8]:
            myList1.remove(abcd + 8)
        elif 'black' in assign[abcd + 7]:
            myList1.append(abcd + 7)
    elif abcd in [9,10,11,12,13,14]:
        myList1.append(abcd + 8)
        myList1.append(abcd + 16)
        if 'white' in assign[abcd + 8] or 'black' in assign[abcd + 8]:
            myList1.remove(abcd + 8)
        elif 'white' in assign[abcd + 16] or 'black' in assign[abcd + 16]:
            myList1.remove(abcd + 16)
        elif 'black' in assign[abcd + 9]:
            myList1.append(abcd + 9)
        elif 'black' in assign[abcd + 7]:
            myList1.append(abcd + 7)
    elif abcd in [17,18,19,20,21,22,25,26,27,28,29,30,33,34,35,36,37,38,41,42,43,44,45,46,49,50,51,52,53,54]:
        myList1.append(abcd + 8)
        if 'white' in assign[abcd + 8] or 'black' in assign[abcd + 8]:
            myList1.remove(abcd + 8)
        elif 'black' in assign[abcd + 9]:
            myList1.append(abcd + 9)
        elif 'black' in assign[abcd + 7]:
            myList1.append(abcd + 7)
    elif abcd in [56,57,58,59,60,61,62,63]:
        pass 
    return myList1
def blackSanikMovement(abcd):
    myList1 = []
    if abcd in [48]:
        myList1.append(abcd - 8)
        myList1.append(abcd - 16)
        if 'white' in assign[abcd - 8] or 'black' in assign[abcd - 8]:
            myList1.remove(abcd - 8)
        elif 'white' in assign[abcd - 16] or 'black' in assign[abcd - 16]:
            myList1.remove(abcd - 16)
        elif 'white' in assign[abcd - 7]:
            myList1.append(abcd - 7)
    elif abcd in [63]:
        myList1.append(abcd - 8)
        myList1.append(abcd - 16)
        if 'white' in assign[abcd - 8] or 'black' in assign[abcd - 8]:
            myList1.remove(abcd - 8)
        elif 'white' in assign[abcd - 16] or 'black' in assign[abcd - 16]:
            myList1.remove(abcd - 16)
        elif 'white' in assign[abcd - 9]:
            myList1.append(abcd - 9)
    elif abcd in [40,32,24,16,8]:
        myList1.append(abcd - 8)
        if 'white' in assign[abcd - 8] or 'black' in assign[abcd - 8]:
            myList1.remove(abcd - 8)
        elif 'white' in assign[abcd - 7]:
            myList1.append(abcd - 7)
    elif abcd in [23,31,39,47,55]:
        myList1.append(abcd - 8)
        if 'white' in assign[abcd - 8] or 'black' in assign[abcd - 8]:
            myList1.remove(abcd - 8)
        elif 'white' in assign[abcd - 9]:
            myList1.append(abcd - 9)
    elif abcd in [49,50,51,52,53,54]:
        myList1.append(abcd - 8)
        myList1.append(abcd - 16)
        if 'white' in assign[abcd - 8] or 'black' in assign[abcd - 8]:
            myList1.remove(abcd - 8)
        elif 'white' in assign[abcd - 16] or 'black' in assign[abcd - 16]:
            myList1.remove(abcd - 16)
        elif 'white' in assign[abcd - 9]:
            myList1.append(abcd - 9)
        elif 'white' in assign[abcd - 7]:
            myList1.append(abcd - 7)
    elif abcd in [9,10,11,12,13,14,17,18,19,20,21,22,25,26,27,28,29,30,33,34,35,36,37,38,41,42,43,44,45,46]:
        myList1.append(abcd - 8)
        if 'white' in assign[abcd - 8] or 'black' in assign[abcd - 8]:
            myList1.remove(abcd - 8)
        elif 'white' in assign[abcd - 9]:
            myList1.append(abcd - 9)
        elif 'white' in assign[abcd - 7]:
            myList1.append(abcd - 7)
    elif abcd in [56,57,58,59,60,61,62,63]:
        pass
    return myList1

# making the chessboard
def makeBoard():
    pygame.draw.line(board,(255,255,255),(75,0),(75,600))
    pygame.draw.line(board,(255,255,255),(75*2,0),(75*2,600))
    pygame.draw.line(board,(255,255,255),(75*3,0),(75*3,600))
    pygame.draw.line(board,(255,255,255),(75*4,0),(75*4,600))
    pygame.draw.line(board,(255,255,255),(75*5,0),(75*5,600))
    pygame.draw.line(board,(255,255,255),(75*6,0),(75*6,600))
    pygame.draw.line(board,(255,255,255),(75*7,0),(75*7,600))

    pygame.draw.line(board,(255,255,255),(0,75),(600,75))
    pygame.draw.line(board,(255,255,255),(0,75*2),(600,75*2))
    pygame.draw.line(board,(255,255,255),(0,75*3),(600,75*3))
    pygame.draw.line(board,(255,255,255),(0,75*4),(600,75*4))
    pygame.draw.line(board,(255,255,255),(0,75*5),(600,75*5))
    pygame.draw.line(board,(255,255,255),(0,75*6),(600,75*6))
    pygame.draw.line(board,(255,255,255),(0,75*7),(600,75*7))
    
    fillColor(0,0)
    fillColor(75,75)
    fillColor(0,150)
    fillColor(75,75*3)
    fillColor(0,75*4)
    fillColor(75,75*5)
    fillColor(0,75*6)
    fillColor(75,75*7)

# assigning the value at position
assign[4] = 'whiteKing'  
assign[3] = 'whiteQueen'
assign[2] = 'whiteWazir1'
assign[5] = 'whiteWazir2'
assign[1] = 'whiteGhora1'
assign[6] = 'whiteGhora2'
assign[0] = 'whiteHathi1'
assign[7] = 'whiteHathi2'
assign[8] = 'whiteSanik1'
assign[9] = 'whiteSanik2'
assign[10] = 'whiteSanik3'
assign[11] = 'whiteSanik4'
assign[12] = 'whiteSanik5'
assign[13] = 'whiteSanik6'
assign[14] = 'whiteSanik7'
assign[15] = 'whiteSanik8'
assign[59] = 'blackKing'
assign[60] = 'blackQueen'
assign[58] = 'blackWazir1'
assign[61] = 'blackWazir2'
assign[57] = 'blackGhora1'
assign[62] = 'blackGhora2'
assign[56] = 'blackHathi1'
assign[63] = 'blackHathi2'
assign[48] = 'blackSanik1'
assign[49] = 'blackSanik2'
assign[50] = 'blackSanik3'
assign[51] = 'blackSanik4'
assign[52] = 'blackSanik5'
assign[53] = 'blackSanik6'
assign[54] = 'blackSanik7'
assign[55] = 'blackSanik8'

# blitting the image on screen
def originalPlace():
    board.blit(whiteKing,(wkX,wkY))
    board.blit(whiteQueen,(wqX,wqY))
    board.blit(whiteWazir,(ww1X,ww1Y))
    board.blit(whiteWazir,(ww2X,ww2Y))
    board.blit(whiteGhora,(wg1X,wg1Y))
    board.blit(whiteGhora,(wg2X,wg2Y))
    board.blit(whiteHathi,(wh1X,wh1Y))
    board.blit(whiteHathi,(wh2X,wh2Y))
    board.blit(whiteSanik,(ws1X,ws1Y))
    board.blit(whiteSanik,(ws2X,ws2Y))
    board.blit(whiteSanik,(ws3X,ws3Y))
    board.blit(whiteSanik,(ws4X,ws4Y))
    board.blit(whiteSanik,(ws5X,ws5Y))
    board.blit(whiteSanik,(ws6X,ws6Y))
    board.blit(whiteSanik,(ws7X,ws7Y))
    board.blit(whiteSanik,(ws8X,ws8Y))
    board.blit(blackKing,(bkX,bkY))
    board.blit(blackQueen,(bqX,bqY))
    board.blit(blackWazir,(bw1X,bw1Y))
    board.blit(blackWazir,(bw2X,bw2Y))
    board.blit(blackGhora,(bg1X,bg1Y))
    board.blit(blackGhora,(bg2X,bg2Y))
    board.blit(blackHathi,(bh1X,bh1Y))
    board.blit(blackHathi,(bh2X,bh2Y))
    board.blit(blackSanik,(bs1X,bs1Y))
    board.blit(blackSanik,(bs2X,bs2Y))
    board.blit(blackSanik,(bs3X,bs3Y))
    board.blit(blackSanik,(bs4X,bs4Y))
    board.blit(blackSanik,(bs5X,bs5Y))
    board.blit(blackSanik,(bs6X,bs6Y))
    board.blit(blackSanik,(bs7X,bs7Y))
    board.blit(blackSanik,(bs8X,bs8Y))
    

def checkPiece(Value,abcd):
    if Value in ['whiteKing']:
        return whiteKingMovement(abcd)
    elif Value in ['blackKing']:
        return blackKingMovement(abcd)
    elif Value in ['whiteQueen']:
        return whiteQueenMovement(abcd)
    elif Value in ['blackQueen']:
        return blackQueenMovement(abcd)
    elif Value in ['whiteWazir1','whiteWazir2']:
        return whiteWazirMovement(abcd)
    elif Value in ['blackWazir1','blackWazir2']:
        return blackWazirMovement(abcd)
    elif Value in ['whiteGhora1','whiteGhora2']:
        return whiteGhoraMovement(abcd)
    elif Value in ['blackGhora1','blackGhora2']:
        return blackGhoraMovement(abcd)
    elif Value in ['whiteHathi1','whiteHathi2']:
        return whiteHathiMovement(abcd)
    elif Value in ['blackHathi1','blackHathi2']:
        return blackHathiMovement(abcd)
    elif Value in ['whiteSanik1','whiteSanik2','whiteSanik3','whiteSanik4','whiteSanik5','whiteSanik6','whiteSanik7','whiteSanik8']:
        return whiteSanikMovement(abcd)
    elif Value in ['blackSanik1','blackSanik2','blackSanik3','blackSanik4','blackSanik5','blackSanik6','blackSanik7','blackSanik8']:
        return blackSanikMovement(abcd)     

def checkKing():
    global check
    if player == 'white':
        possiblea = whiteKingMovement(pieceDict['whiteKing'])
        possible1 = blackKingMovement(pieceDict['blackKing'])
        possible2 = blackQueenMovement(pieceDict['blackQueen'])
        possible3 = blackWazirMovement(pieceDict['blackWazir1'])
        possible4 = blackWazirMovement(pieceDict['blackWazir2'])
        possible5 = blackGhoraMovement(pieceDict['blackGhora1'])
        possible6 = blackGhoraMovement(pieceDict['blackGhora2'])
        possible7 = blackHathiMovement(pieceDict['blackHathi1'])
        possible8 = blackHathiMovement(pieceDict['blackHathi2'])
        possible9 = blackSanikMovement(pieceDict['blackSanik1'])
        possible10 = blackSanikMovement(pieceDict['blackSanik2'])
        possible11 = blackSanikMovement(pieceDict['blackSanik3'])
        possible12 = blackSanikMovement(pieceDict['blackSanik4'])
        possible13 = blackSanikMovement(pieceDict['blackSanik5'])
        possible14 = blackSanikMovement(pieceDict['blackSanik6'])
        possible15 = blackSanikMovement(pieceDict['blackSanik7'])
        possible16 = blackSanikMovement(pieceDict['blackSanik8'])
        possibles = []
        for a in [possible1,possible2,possible3,possible4,possible5,possible6,possible7,possible8,possible9,possible10,possible11,possible12,possible13,possible14,possible15,possible16]:
            possibles += a
        if pieceDict['whiteKing'] in possibles:
            check = True
            possiblea.remove(pieceDict['whiteKing'])
    elif player == 'black':
        possible1 = whiteKingMovement(pieceDict['whiteKing'])
        possiblea = blackKingMovement(pieceDict['blackKing'])
        possible2 = whiteQueenMovement(pieceDict['whiteQueen'])
        possible3 = whiteWazirMovement(pieceDict['whiteWazir1'])
        possible4 = whiteWazirMovement(pieceDict['whiteWazir2'])
        possible5 = whiteGhoraMovement(pieceDict['whiteGhora1'])
        possible6 = whiteGhoraMovement(pieceDict['whiteGhora2'])
        possible7 = whiteHathiMovement(pieceDict['whiteHathi1'])
        possible8 = whiteHathiMovement(pieceDict['whiteHathi2'])
        possible9 = whiteSanikMovement(pieceDict['whiteSanik1'])
        possible10 = whiteSanikMovement(pieceDict['whiteSanik2'])
        possible11 = whiteSanikMovement(pieceDict['whiteSanik3'])
        possible12 = whiteSanikMovement(pieceDict['whiteSanik4'])
        possible13 = whiteSanikMovement(pieceDict['whiteSanik5'])
        possible14 = whiteSanikMovement(pieceDict['whiteSanik6'])
        possible15 = whiteSanikMovement(pieceDict['whiteSanik7'])
        possible16 = whiteSanikMovement(pieceDict['whiteSanik8'])
        possibles = []
        for a in [possible1,possible2,possible3,possible4,possible5,possible6,possible7,possible8,possible9,possible10,possible11,possible12,possible13,possible14,possible15,possible16]:
            possibles += a
        if pieceDict['blackKing'] in possibles:
            check = True
            possiblea.remove(pieceDict['whiteKing'])
    return possiblea
        


running = True
while running:
    board.fill((255,0,255))
    for aa in range(64):
        if assign[aa] == 'blackKing':
            pieceDict['blackKing'] = aa
        elif assign[aa] == 'blackQueen':
            pieceDict['blackQueen'] = aa
        elif assign[aa] == 'blackWazir1':
            pieceDict['blackWazir1'] = aa
        elif assign[aa] == 'blackWazir2':
            pieceDict['blackWazir2'] = aa
        elif assign[aa] == 'blackGhora1':
            pieceDict['blackGhora1'] = aa
        elif assign[aa] == 'blackGhora2':
            pieceDict['blackGhora2'] = aa
        elif assign[aa] == 'blackHathi1':
            pieceDict['blackHathi1'] = aa
        elif assign[aa] == 'blackHathi2':
            pieceDict['blackHathi2'] = aa
        elif assign[aa] == 'blackSanik1':
            pieceDict['blackSanik1'] = aa
        elif assign[aa] == 'blackSanik2':
            pieceDict['blackSanik2'] = aa
        elif assign[aa] == 'blackSanik3':
            pieceDict['blackSanik3'] = aa
        elif assign[aa] == 'blackSanik4':
            pieceDict['blackSanik4'] = aa
        elif assign[aa] == 'blackSanik5':
            pieceDict['blackSanik5'] = aa
        elif assign[aa] == 'blackSanik6':
            pieceDict['blackSanik6'] = aa
        elif assign[aa] == 'blackSanik7':
            pieceDict['blackSanik7'] = aa
        elif assign[aa] == 'blackSanik8':
            pieceDict['blackSanik8'] = aa
        elif assign[aa] == 'whiteKing':
            pieceDict['whiteKing'] = aa
        elif assign[aa] == 'whiteQueen':
            pieceDict['whiteQueen'] = aa
        elif assign[aa] == 'whiteWazir1':
            pieceDict['whiteWazir1'] = aa
        elif assign[aa] == 'whiteWazir2':
            pieceDict['whiteWazir2'] = aa
        elif assign[aa] == 'whiteGhora1':
            pieceDict['whiteGhora1'] = aa
        elif assign[aa] == 'whiteGhora2':
            pieceDict['whiteGhora2'] = aa
        elif assign[aa] == 'whiteHathi1':
            pieceDict['whiteHathi1'] = aa
        elif assign[aa] == 'whiteHathi2':
            pieceDict['whiteHathi2'] = aa
        elif assign[aa] == 'whiteSanik1':
            pieceDict['whiteSanik1'] = aa
        elif assign[aa] == 'whiteSanik2':
            pieceDict['whiteSanik2'] = aa
        elif assign[aa] == 'whiteSanik3':
            pieceDict['whiteSanik3'] = aa
        elif assign[aa] == 'whiteSanik4':
            pieceDict['whiteSanik4'] = aa
        elif assign[aa] == 'whiteSanik5':
            pieceDict['whiteSanik5'] = aa
        elif assign[aa] == 'whiteSanik6':
            pieceDict['whiteSanik6'] = aa
        elif assign[aa] == 'whiteSanik7':
            pieceDict['whiteSanik7'] = aa
        elif assign[aa] == 'whiteSanik8':
            pieceDict['whiteSanik8'] = aa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            if inMotionStatus == True:
                mX, mY = pygame.mouse.get_pos()
                if inMotionStatus == True:
                    if inHand == 'whiteKing':
                        wkX = mX
                        wkY = mY
                    elif inHand == 'whiteQueen':
                        wqX = mX
                        wqY = mY
                    elif inHand == 'whiteWazir1':
                        ww1X = mX
                        ww1Y = mY    
                    elif inHand == 'whiteWazir2':
                        ww2X = mX
                        ww2Y = mY    
                    elif inHand == 'whiteGhora1':
                        wg1X = mX
                        wg1Y = mY    
                    elif inHand == 'whiteGhora2':
                        wg2X = mX
                        wg2Y = mY    
                    elif inHand == 'whiteHathi1':
                        wh1X = mX
                        wh1Y = mY    
                    elif inHand == 'whiteHathi2':
                        wh2X = mX
                        wh2Y = mY    
                    elif inHand == 'whiteSanik1':
                        ws1X = mX
                        ws1Y = mY    
                    elif inHand == 'whiteSanik2':
                        ws2X = mX
                        ws2Y = mY    
                    elif inHand == 'whiteSanik3':
                        ws3X = mX
                        ws3Y = mY    
                    elif inHand == 'whiteSanik4':
                        ws4X = mX
                        ws4Y = mY    
                    elif inHand == 'whiteSanik5':
                        ws5X = mX
                        ws5Y = mY    
                    elif inHand == 'whiteSanik6':
                        ws6X = mX
                        ws6Y = mY    
                    elif inHand == 'whiteSanik7':
                        ws7X = mX
                        ws7Y = mY    
                    elif inHand == 'whiteSanik8':
                        ws8X = mX
                        ws8Y = mY    
                    elif inHand == 'blackKing':
                        bkX = mX
                        bkY = mY
                    elif inHand == 'blackQueen':
                        bqX = mX
                        bqY = mY
                    elif inHand == 'blackWazir1':
                        bw1X = mX
                        bw1Y = mY    
                    elif inHand == 'blackWazir2':
                        bw2X = mX
                        bw2Y = mY    
                    elif inHand == 'blackGhora1':
                        bg1X = mX
                        bg1Y = mY    
                    elif inHand == 'blackGhora2':
                        bg2X = mX
                        bg2Y = mY    
                    elif inHand == 'blackHathi1':
                        bh1X = mX
                        bh1Y = mY    
                    elif inHand == 'blackHathi2':
                        bh2X = mX
                        wh2Y = mY    
                    elif inHand == 'blackSanik1':
                        bs1X = mX
                        bs1Y = mY    
                    elif inHand == 'blackSanik2':
                        bs2X = mX
                        bs2Y = mY    
                    elif inHand == 'blackSanik3':
                        bs3X = mX
                        bs3Y = mY    
                    elif inHand == 'blackSanik4':
                        bs4X = mX
                        bs4Y = mY    
                    elif inHand == 'blackSanik5':
                        bs5X = mX
                        bs5Y = mY    
                    elif inHand == 'blackSanik6':
                        bs6X = mX
                        bs6Y = mY    
                    elif inHand == 'blackSanik7':
                        bs7X = mX
                        bs7Y = mY    
                    elif inHand == 'blackSanik8':
                        bs8X = mX
                        bs8Y = mY

        
    left, middle, right = pygame.mouse.get_pressed()
    if left:
        for a in range(64):
            if box[a].collidepoint(pygame.mouse.get_pos()):
                if inHand == '':
                    pp = checkKing()
                    if check == True:   
                        if assign[a] == '':
                            continue
                        else:
                            if player == 'white' and 'white' in assign[a]:
                                inMotionStatus = True
                                inHand = assign[a]
                                playerPos = a
                                filled.remove(location[a])
                                if assign[a] in ['whiteQueen','whiteWazir1','whiteWazir2','whiteGhora1','whiteGhora2','whiteHathi1','whiteHathi2','whiteSanik1','whiteSanik2','whiteSanik3','whiteSanik4','whiteSanik5','whiteSanik6','whiteSanik7','whiteSanik8']:
                                    ppp = checkPiece(assign[a],a)
                                    for loca in pp:
                                        if loca in ppp:
                                            continue
                                        else:
                                            ppp.remove(loca)
                                    locList = ppp.append(a)
                                    for ii in locList:
                                        possible.append(ii)
                                else:
                                    for i in checkPiece(assign[a], a):
                                        possible.append(location[i]) 
                                assign[a] = ''
                                break
                            elif player == 'black' and 'black' in assign[a]:
                                inMotionStatus = True
                                inHand = assign[a]
                                playerPos = a
                                filled.remove(location[a])
                                if assign[a] in ['blackQueen','blackWazir1','blackWazir2','blackGhora1','blackGhora2','blackHathi1','blackHathi2','blackSanik1','blackSanik2','blackSanik3','blackSanik4','blackSanik5','blackSanik6','blackSanik7','blackSanik8']:
                                    ppp = checkPiece(assign[a],a)
                                    for loca in pp:
                                        if loca in ppp:
                                            continue
                                        else:
                                            ppp.remove(loca)
                                    locList = ppp.append(a)
                                    for ii in locList:
                                        possible.append(ii)
                                else:
                                    for i in checkPiece(assign[a], a):
                                        possible.append(location[i])
                                assign[a] = ''
                                break
                            else:
                                continue
                    else:
                        if assign[a] == '':
                            continue
                        else:
                            if player == 'white' and 'white' in assign[a]:
                                inMotionStatus = True
                                inHand = assign[a]
                                playerPos = a
                                filled.remove(location[a])
                                possible.append(location[a])
                                for i in checkPiece(assign[a], a):
                                    possible.append(location[i]) 
                                assign[a] = ''
                                break
                            elif player == 'black' and 'black' in assign[a]:
                                inMotionStatus = True
                                inHand = assign[a]
                                playerPos = a
                                filled.remove(location[a])
                                possible.append(location[a])
                                for i in checkPiece(assign[a], a):
                                    possible.append(location[i])
                                assign[a] = ''
                                break
                            else:
                                continue
               
    if right:
        for a in range(64):
            if box[a].collidepoint(pygame.mouse.get_pos()):
                placeValue = assign[a]
                if inHand == '':
                    continue
                elif 'white' in inHand:
                    if placeValue == '':
                        if location[a] in possible:
                            inMotionStatus = False
                            if inHand == 'whiteKing':
                                wkX = location[a][0]
                                wkY = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteKing'
                            elif inHand == 'whiteQueen':
                                wqX = location[a][0]
                                wqY = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteQueen'
                            elif inHand == 'whiteWazir1':
                                ww1X = location[a][0]
                                ww1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteWazir1'    
                            elif inHand == 'whiteWazir2':
                                ww2X = location[a][0]
                                ww2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteWazir2'    
                            elif inHand == 'whiteGhora1':
                                wg1X = location[a][0]
                                wg1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteGhora1'    
                            elif inHand == 'whiteGhora2':
                                wg2X = location[a][0]
                                wg2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteGhora2'    
                            elif inHand == 'whiteHathi1':
                                wh1X = location[a][0]
                                wh1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteHathi1'    
                            elif inHand == 'whiteHathi2':
                                wh2X = location[a][0]
                                wh2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteHathi2'    
                            elif inHand == 'whiteSanik1':
                                ws1X = location[a][0]
                                ws1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik1'    
                            elif inHand == 'whiteSanik2':
                                ws2X = location[a][0]
                                ws2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik2'    
                            elif inHand == 'whiteSanik3':
                                ws3X = location[a][0]
                                ws3Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik3'    
                            elif inHand == 'whiteSanik4':
                                ws4X = location[a][0]
                                ws4Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik4'    
                            elif inHand == 'whiteSanik5':
                                ws5X = location[a][0]
                                ws5Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik5'    
                            elif inHand == 'whiteSanik6':
                                ws6X = location[a][0]
                                ws6Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik6'    
                            elif inHand == 'whiteSanik7':
                                ws7X = location[a][0]
                                ws7Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik7'    
                            elif inHand == 'whiteSanik8':
                                ws8X = location[a][0]
                                ws8Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik8' 
                            filled.append(location[a])
                            possible = []   
                            newPos = a
                            break
                    elif 'white' in placeValue:
                        continue
                    elif 'black' in placeValue:
                        if location[a] in possible:
                            cutPiece.append(placeValue)
                            if assign[a] == 'blackKing':
                                bkY += 1000
                            elif assign[a] == 'blackQueen':
                                bqY += 1000
                            elif assign[a] == 'blackWazir1':
                                bw1Y += 1000
                            elif assign[a] == 'blackWazir2':
                                bw2Y += 1000
                            elif assign[a] == 'blackGhora1':
                                bg1Y += 1000
                            elif assign[a] == 'blackGhora2':
                                bg2Y += 1000
                            elif assign[a] == 'blackHathi1':
                                bh1Y += 1000
                            elif assign[a] == 'blackHathi2':
                                bh2Y += 1000
                            elif assign[a] == 'blackSanik1':
                                bs1Y += 1000
                            elif assign[a] == 'blackSanik2':
                                bs2Y += 1000
                            elif assign[a] == 'blackSanik3':
                                bs3Y += 1000
                            elif assign[a] == 'blackSanik4':
                                bs4Y += 1000
                            elif assign[a] == 'blackSanik5':
                                bs5Y += 1000
                            elif assign[a] == 'blackSanik6':
                                bs6Y += 1000
                            elif assign[a] == 'blackSanik7':
                                bs7Y += 1000
                            elif assign[a] == 'blackSanik8':
                                bs8Y += 1000
                            inMotionStatus = False
                            if inHand == 'whiteKing':
                                wkX = location[a][0]
                                wkY = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteKing'
                            elif inHand == 'whiteQueen':
                                wqX = location[a][0]
                                wqY = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteQueen'
                            elif inHand == 'whiteWazir1':
                                ww1X = location[a][0]
                                ww1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteWazir1'    
                            elif inHand == 'whiteWazir2':
                                ww2X = location[a][0]
                                ww2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteWazir2'    
                            elif inHand == 'whiteGhora1':
                                wg1X = location[a][0]
                                wg1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteGhora1'    
                            elif inHand == 'whiteGhora2':
                                wg2X = location[a][0]
                                wg2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteGhora2'    
                            elif inHand == 'whiteHathi1':
                                wh1X = location[a][0]
                                wh1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteHathi1'    
                            elif inHand == 'whiteHathi2':
                                wh2X = location[a][0]
                                wh2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteHathi2'    
                            elif inHand == 'whiteSanik1':
                                ws1X = location[a][0]
                                ws1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik1'    
                            elif inHand == 'whiteSanik2':
                                ws2X = location[a][0]
                                ws2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik2'    
                            elif inHand == 'whiteSanik3':
                                ws3X = location[a][0]
                                ws3Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik3'    
                            elif inHand == 'whiteSanik4':
                                ws4X = location[a][0]
                                ws4Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik4'    
                            elif inHand == 'whiteSanik5':
                                ws5X = location[a][0]
                                ws5Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik5'    
                            elif inHand == 'whiteSanik6':
                                ws6X = location[a][0]
                                ws6Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik6'    
                            elif inHand == 'whiteSanik7':
                                ws7X = location[a][0]
                                ws7Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik7'    
                            elif inHand == 'whiteSanik8':
                                ws8X = location[a][0]
                                ws8Y = location[a][1]
                                inHand = ''
                                assign[a] = 'whiteSanik8'    
                            filled.append(location[a])
                            possible = []
                            newPos = a
                            break
                elif 'black' in inHand:
                    if placeValue == '':
                        if location[a] in possible:
                            inMotionStatus = False
                            if inHand == 'blackKing':
                                bkX = location[a][0]
                                bkY = location[a][1]
                                inHand = ''
                                assign[a] = 'blackKing'
                            elif inHand == 'blackQueen':
                                bqX = location[a][0]
                                bqY = location[a][1]
                                inHand = ''
                                assign[a] = 'blackQueen'
                            elif inHand == 'blackWazir1':
                                bw1X = location[a][0]
                                bw1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackWazir1'    
                            elif inHand == 'blackWazir2':
                                bw2X = location[a][0]
                                bw2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackWazir2'    
                            elif inHand == 'blackGhora1':
                                bg1X = location[a][0]
                                bg1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackGhora1'    
                            elif inHand == 'blackGhora2':
                                bg2X = location[a][0]
                                bg2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackGhora2'    
                            elif inHand == 'blackHathi1':
                                bh1X = location[a][0]
                                bh1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackHathi1'    
                            elif inHand == 'blackHathi2':
                                bh2X = location[a][0]
                                wh2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackHathi2'    
                            elif inHand == 'blackSanik1':
                                bs1X = location[a][0]
                                bs1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik1'    
                            elif inHand == 'blackSanik2':
                                bs2X = location[a][0]
                                bs2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik2'    
                            elif inHand == 'blackSanik3':
                                bs3X = location[a][0]
                                bs3Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik3'   
                            elif inHand == 'blackSanik4':
                                bs4X = location[a][0]
                                bs4Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik4'    
                            elif inHand == 'blackSanik5':
                                bs5X = location[a][0]
                                bs5Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik5'    
                            elif inHand == 'blackSanik6':
                                bs6X = location[a][0]
                                bs6Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik6'    
                            elif inHand == 'blackSanik7':
                                bs7X = location[a][0]
                                bs7Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik7'    
                            elif inHand == 'blackSanik8':
                                bs8X = location[a][0]
                                bs8Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik8'
                            filled.append(location[a])
                            possible = []
                            newPos = a
                            break
                    elif 'black' in placeValue:
                        continue
                    elif 'white' in placeValue:
                        if location[a] in possible:
                            cutPiece.append(placeValue)
                            if assign[a] == 'whiteKing':
                                wkY += 1000
                            elif assign[a] == 'whiteQueen':
                                wqY += 1000
                            elif assign[a] == 'whiteWazir1':
                                ww1Y += 1000
                            elif assign[a] == 'whiteWazir2':
                                ww2Y += 1000
                            elif assign[a] == 'whiteGhora1':
                                wg1Y += 1000
                            elif assign[a] == 'whiteGhora2':
                                wg2Y += 1000
                            elif assign[a] == 'whiteHathi1':
                                wh1Y += 1000
                            elif assign[a] == 'whiteHathi2':
                                wh2Y += 1000
                            elif assign[a] == 'whiteSanik1':
                                ws1Y += 1000
                            elif assign[a] == 'whiteSanik2':
                                ws2Y += 1000
                            elif assign[a] == 'whiteSanik3':
                                ws3Y += 1000
                            elif assign[a] == 'whiteSanik4':
                                ws4Y += 1000
                            elif assign[a] == 'whiteSanik5':
                                ws5Y += 1000
                            elif assign[a] == 'whiteSanik6':
                                ws6Y += 1000
                            elif assign[a] == 'whiteSanik7':
                                ws7Y += 1000
                            elif assign[a] == 'whiteSanik8':
                                ws8Y += 1000
                            inMotionStatus = False    
                            if inHand == 'blackKing':
                                bkX = location[a][0]
                                bkY = location[a][1]
                                inHand = ''
                                assign[a] = 'blackKing'
                            elif inHand == 'blackQueen':
                                bqX = location[a][0]
                                bqY = location[a][1]
                                inHand = ''
                                assign[a] = 'blackQueen'
                            elif inHand == 'blackWazir1':
                                bw1X = location[a][0]
                                bw1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackWazir1'    
                            elif inHand == 'blackWazir2':
                                bw2X = location[a][0]
                                bw2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackWazir2'    
                            elif inHand == 'blackGhora1':
                                bg1X = location[a][0]
                                bg1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackGhora1'    
                            elif inHand == 'blackGhora2':
                                bg2X = location[a][0]
                                bg2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackGhora2'    
                            elif inHand == 'blackHathi1':
                                bh1X = location[a][0]
                                bh1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackHathi1'    
                            elif inHand == 'blackHathi2':
                                bh2X = location[a][0]
                                wh2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackHathi2'    
                            elif inHand == 'blackSanik1':
                                bs1X = location[a][0]
                                bs1Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik1'    
                            elif inHand == 'blackSanik2':
                                bs2X = location[a][0]
                                bs2Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik2'    
                            elif inHand == 'blackSanik3':
                                bs3X = location[a][0]
                                bs3Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik3'   
                            elif inHand == 'blackSanik4':
                                bs4X = location[a][0]
                                bs4Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik4'    
                            elif inHand == 'blackSanik5':
                                bs5X = location[a][0]
                                bs5Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik5'    
                            elif inHand == 'blackSanik6':
                                bs6X = location[a][0]
                                bs6Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik6'    
                            elif inHand == 'blackSanik7':
                                bs7X = location[a][0]
                                bs7Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik7'    
                            elif inHand == 'blackSanik8':
                                bs8X = location[a][0]
                                bs8Y = location[a][1]
                                inHand = ''
                                assign[a] = 'blackSanik8'
                            filled.append(location[a])
                            possible = []
                            newPos = a
                            break
        
        if playerPos == newPos:
            continue
        else:
            if player == 'white':
                player = 'black'
                playerPos = 0
                newPos = 0
            elif player == 'black':
                player = 'white'
                playerPos = 0
                newPos = 0
    
    
    
    makeBoard()                            
    originalPlace()
     
    pygame.display.update()