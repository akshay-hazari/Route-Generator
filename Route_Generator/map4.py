# 0 : geonameid         : integer id of record in geonames database
# 1 : name              : name of geographical point (utf8) varchar(200)
# 2 : asciiname         : name of geographical point in plain ascii characters, varchar(200)
# 3 : alternatenames    : alternatenames, comma separated varchar(5000)
# 4 : latitude          : latitude in decimal degrees (wgs84)
# 5 : longitude         : longitude in decimal degrees (wgs84)
# 6 : feature class     : see http://www.geonames.org/export/codes.html, char(1)
# 7 : feature code      : see http://www.geonames.org/export/codes.html, varchar(10)
# 8 : country code      : ISO-3166 2-letter country code, 2 characters
# 9 : cc2               : alternate country codes, comma separated, ISO-3166 2-letter country code, 60 characters
# 10 : admin1 code       : fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code; varchar(20)
# 11 : admin2 code       : code for the second administrative division, a county in the US, see file admin2Codes.txt; varchar(80) 
# 12 : admin3 code       : code for third level administrative division, varchar(20)
# 13 : admin4 code       : code for fourth level administrative division, varchar(20)
# 14 : population        : bigint (8 byte int) 
# 15 : elevation         : in meters, integer
# 16 : dem               : digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
# 17 : timezone          : the timezone id (see file timeZone.txt) varchar(40)
# 18 : modification date : date of last modification in yyyy-MM-dd format
import math
import re

f = open ("IN.txt","r")

dataz = f.read()
strrx=str(dataz)
strrx=strrx.split('\n')
strrrx=[]
o=[]
uz=0
for i in strrx:
    bz=i.split('\t')
    strrrx.append(bz)
    uz=uz+1
strrrx.pop(-1)

rdictt={}

for i in strrrx:
    if i[2] not in rdictt:
        rdictt[i[2]]=[]
        rdictt[i[2]].append(i)
    else:
        rdictt[i[2]].append(i)

strr=str(dataz)

strr=strr.split('\n')
strrr=[]
j=[]
k=0
for i in strr:
    b=i.split('\t')
    strrr.append(b)
    k=k+1
#    if k>1000:
 #       break
dictt= {}

strrr.pop(-1)

#latlonstr=strrr
latlon={}
for i in strrr:
    nos=int(float(i[4][:2]))
    if nos not in latlon:
        latlon[nos]=[]
        latlon[nos].append(i)
    else:
        latlon[nos].append(i)

def popul():
    n=[]
    for i in strrr:
        if int(i[14])>10000:
            n.append(i)
   # print len(strrr)-len(n)
    return n

newlist=popul()

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

lonlat={}
for i in strrr:
    nos=int(float(i[5][:2]))
    if nos not in lonlat:
        lonlat[nos]=[]
        lonlat[nos].append(i)
    else:
        lonlat[nos].append(i)

latlon1={}
for i in newlist:
    nos=int(float(i[4][:2]))
    if nos not in latlon1:
        latlon1[nos]=[]
        latlon1[nos].append(i)
    else:
        latlon1[nos].append(i)

lonlat1={}
for i in newlist:
    nos=int(float(i[5][:2]))
    if nos not in lonlat1:
        lonlat1[nos]=[]
        lonlat1[nos].append(i)
    else:
        lonlat[nos].append(i)

# for i in strrr:    
#     alpha=i[2][:2]
#     if alpha not in dictt :
#         dictt[alpha]={}
        
#         if int(float(i[4])) not in dictt[alpha]:
#             dictt[alpha][int(float(i[4]))]=[]
#             dictt[alpha][int(float(i[4]))].append(i)
#         else:
#             dictt[alpha][int(float(i[4]))].append(i)
        
#     else:
#         if int(float(i[4])) not in dictt[alpha]:
#             dictt[alpha][int(float(i[4]))]=[]
#             dictt[alpha][int(float(i[4]))].append(i)
#         else:
#             dictt[alpha][int(float(i[4]))].append(i)

# for i in strrr:    
#     alpha=i[2][:2]
#     if alpha not in dictt :
#         dictt[alpha]={}
        
#         if (i[2]) not in dictt[alpha]:
#             dictt[alpha][i[2]]=i
#             #dictt[alpha][i[2]].append(i)
#         else:
#             #dictt[alpha][i[2]].append(i)
#             if (int(float(i[4])) == int(float(dictt[alpha][i[2]][4])+0.5)) or (int(float(i[4])+0.5) == int(float(dictt[alpha][i[2]][4]))) : 
#             #int(float(i[4])) == int(float(dictt[alpha][i[2]][4])):
#                 continue
#             else:
#                 break


#     else:
#         if (i[2]) not in dictt[alpha]:
#             dictt[alpha][i[2]]=i
#            # dictt[alpha][i[2]].append(i)
#         else:
#             print "error"
#             print i
#             if (int(float(i[4])) == int(float(dictt[alpha][i[2]][4])+0.5)) or (int(float(i[4])+0.5) == int(float(dictt[alpha][i[2]][4]))) :
#                 continue
#             else:
#                 break

States={'Andhra Pradesh':'Hyderabad','Manipur':'Imphal','Meghalaya':'Shillong','Mizoram':'Aizawl','West Bengal':'Kolkata','Uttarakhand':'Dehradun','Uttar Pradesh':'Lucknow','Tripura':'Agartala','Tamil Nadu':'Chennai','Rajasthan':'Jaipur','Punjab':'Chandigarh','Odisha':'Bhubaneswar','Nagaland':'Kohima','Madhya Pradesh':'Bhopal','Andaman and Nicobar':'Port Blair','Chhattisgarh':'Raipur','Goa':'Panaji','Bihar':'Patna','Kerala':'Thiruvananthapuram','Jharkhand':'Ranchi','Jammu and Kashmir':'Srinagar','Himachal Pradesh':'Shimla','Haryana':'Chandigarh','Lakshadweep':'Kavaratti','Karnataka':'Bangalore','Assam':'Dispur','Arunachal Pradesh':'Itanagar','Maharashtra':'Mumbai','Gujrat':'Gandhinagar',"Delhi":"New Delhi"}

States1={'Andhra Pradesh':'50,51,52,53','Manipur':'79','Meghalaya':'79','Mizoram':'79','West Bengal':'70,71,72,73,74','Uttarakhand':'20,21,22,23,24,25,26,27,28','Uttar Pradesh':'20,21,22,23,24,25,26,27,28','Tripura':'79','Tamil Nadu':'60,61,62,63,64','Rajasthan':'30,31,32,33,34','Punjab':'14,15,16','Odisha':'75,76,77','Nagaland':'79','Madhya Pradesh':'45,46,47,48,49','Andaman and Nicobar':'25','Chhattisgarh':'45,46,47,48,49','Bihar':'80,81,82,83,84,85','Kerala':'67,68,69','Jharkhand':'80,81,82,83,84,85','Jammu and Kashmir':'18,19','Himachal Pradesh':'17','Haryana':'12,13','Lakshadweep':'5','Karnataka':'56,57,58,59','Assam':'78','Arunachal Pradesh':'79','Maharashtra':'40,41,42,43,44','Gujrat':'36,37,38,39',"Goa":"403","Delhi":"11"}

#EleCap={'Hyderabad':,'Imphal':,'Shillong':,'Aizawl':,'Kolkata':,'Dehradun':,'Lucknow':,'Agartala':,'Chennai':,'Jaipur':,'Chandigarh':,'Bhubaneswar':,'Kohima':,'Bhopal':,'Port Blair':,'Raipur':,'Panaji':,'Patna':,'Thiruvananthapuram':,'Ranchi':,'Srinagar':,'Shimla':,'Haryana':'Chandigarh','Lakshadweep':'Kavaratti','Karnataka':'Bengaluru','Assam':'Dispur','Arunachal Pradesh':'Itanagar','Maharashtra':'Mumbai','Gujrat':'Gandhinagar'}

transittime={"Ele100":5,"Dist100":8,"Pop20":-8}

def tt(sources,city,state,strr):
    temp=shortest(sources,city,state,strr)
    ttime=(temp[1]/100)*transittime["Dist100"]
    ele=temp[0][15]
    if(ele==''):
        Capital=States[temp[2]]
        Capital=strr[Capital[:2]][Capital][0]
#        print Capital
        ele=Capital[15]
#    if(int(ele)>500):
 #       ttime=ttime+(int(ele)/500)
    pop=temp[0][14]
    if(int(pop)>2000000):
        ttime=ttime+(int(pop)/2000000)
    return ttime

def nearestto(state,city,strr): 
    Capital=States[state]
    res=strr[city[:2]][city]
    dist=9999
    
    latc=float(strr[Capital[:2]][Capital][0][4])                                                                                        
    longc=float(strr[Capital[:2]][Capital][0][5]) 
    for i in res:
        temp=distance1(i[4],i[5],latc,longc,strr)
        if temp<dist:
            dist=temp
            temp1=i
    return temp1
    # two=city[:2]
    # latc=float(strr[Capital[:2]][Capital][0][4])
    # longc=float(strr[Capital[:2]][Capital][0][5])
    # latt=latc
    # longg=longc
    # for i in strr[two][city]:
    #     if abs(i[4] - latc)<latt:
    #         latt=abs(i[4] - latc)
    #         c=i



import math
def areClockwise(v1, v2):
    return ((((-1*v1[0])*v2[1]) + v1[1]*v2[0]) > 0)


def isWithinRadius(v,radiusSquared):
    return (((v[0]*v[0]) + (v[1]*v[1])) <= radiusSquared)




def isInsideSector(point, center, sectorStart, sectorEnd, radius):
    x = point[0] - center[0]
    y= point[1] - center[1]
    relPoint=[x,y]
    return (not(areClockwise(sectorStart, relPoint)))and(areClockwise(sectorEnd, relPoint))and((distance1(center[0],center[1],point[0],point[1],dictt)-radius)<0)
#(isWithinRadius(relPoint,radiusSquared))

def angle1(lat1,lon1,lat2,lon2):
    from math import sin, cos, sqrt, atan2, radians, degrees 
    lat1 = radians(float(lat1))
    lon1 = radians(float(lon1))
    lon2 = radians(float(lon2))
    lat2 = radians(float(lat2))
    dlong=lon2-lon1
    thetaa = atan2(sin(dlong)*cos(lat2), cos(lat1)*sin(lat2) - sin(lat1)*cos(lat2)*cos(dlong))
    return math.degrees(thetaa)


def angle(point1,point2):
    from math import sin, cos, sqrt, atan2, radians ,degrees
    delx=point2[0]-point1[0]
    dely=point2[1]-point1[1]
    return math.degrees(atan2(radians(delx),radians(dely)))


#print math.degrees(angle([0,0],[100,100]))

def pts(theta,r):
    return [round(r*math.cos(math.radians(theta))),round(r*math.sin(math.radians(theta)))]

#print"test", pts(45,120)

def ptinsec(point,pointc,pointe,r,theta):
    point0=float(point[0])
    point1=float(point[1])
    pointc0=float(pointc[0])
    pointc1=float(pointc[1])
    pointe0=float(pointe[0])
    pointe1=float(pointe[1])
    point=[point0,point1]
    pointc=[pointc0,pointc1]
    pointe=[pointe0,pointe1]
    thet=angle1(pointc[0],pointc[1],pointe[0],pointe[1])
    if ((thet-theta)>0):
        ptstart=pts(thet-theta,r)
    else :
        ptstart=pts(360+thet-theta,r)
    if ((thet+theta) < 360):
        ptend=pts(thet+theta,r)
    else:
        ptend=pts(thet+theta-360,r)
   # print "Angle",thet
 #   print "Pt end",ptend
  #  print "Pt start",ptstart
    return isInsideSector(point,pointc,ptstart,ptend,r)
    
#print "Result Ptinsec",ptinsec([84,84],[0,0],[85,85],120,30)


def distance2(city1,state1,city2,state2,strr,r,theta):
    city1=nearestto(state1,city1,strr)
    city2=nearestto(state2,city2,strr)
    ptc=[city1[4],city1[5]]
    pte=[city2[4],city2[5]]
    fl0=0
    distan=0
    temp=0
    lat1=int(city1[4][:2])
    lat2=int(city2[4][:2])
    print city1

    while((ptc[0]!=pte[0])and(ptc[1]!=pte[1])):
        distan=distan+temp
        if(fl0==1):
            ptc=[locatn[0][4],locatn[0][5]]
            lat1=int(locatn[0][4][:2])
            lat2=int(city2[4][:2])
        thet=angle1(ptc[0],ptc[1],pte[0],pte[1])
        ptstart=pts(thet-theta,r)
        ptend=pts(thet+theta,r)
        ptss=[]
        if lat1<lat2:
            s=lat1
            e=lat2
        else:
            e=lat1
            s=lat2
        ang=angle1(ptc[0],ptc[1],pte[0],pte[1])
        for i in range(s,e+1):
            for j in latlon[i]:
                pt=[j[4],j[5]]
                if ptinsec(pt,ptc,pte,r,theta):
                    ptss.append([j,abs(angle1(ptc[0],ptc[1],pt[0],pt[1])-ang)])    
        anglee=360
        for i in ptss:
            if i[1]<anglee:
                anglee=i[1]
                locatn=i
        temp=distance1(ptc[0],ptc[1],locatn[0][4],locatn[0][5],dictt)
        fl0=1
        locatn
    return distan


def distancegpop(city1,state1,city2,state2,strr,r,theta):
    city1=nearestto(state1,city1,strr)
    city2=nearestto(state2,city2,strr)
    ptc=[city1[4],city1[5]]
    pte=[city2[4],city2[5]]
    fl0=0
    distan=0
    temp=0
    flgr=0
    lat1=int(city1[4][:2])
    lat2=int(city2[4][:2])
    print city1
    store=[]
    while((ptc[0]!=pte[0])and(ptc[1]!=pte[1])):
        distan=distan+temp

        if(fl0==1):
            ptc=[locatn[0][4],locatn[0][5]]
            lat1=int(locatn[0][4][:2])
            lat2=int(city2[4][:2])
        thet=angle1(ptc[0],ptc[1],pte[0],pte[1])
        ptstart=pts(thet-theta,r)
        ptend=pts(thet+theta,r)
        ptss=[]
        #ptss.append([city2,abs(angle1(ptc[0],ptc[1],pt[0],pt[1])-ang)]
        if lat1<lat2:
            s=lat1
            e=lat2
        else:
            e=lat1
            s=lat2
        ang=angle1(ptc[0],ptc[1],pte[0],pte[1])
        for i in range(s,e+1):
            for j in latlon1[i]:
                pt=[j[4],j[5]]
                if ptinsec(pt,ptc,pte,r,theta):
                    ptss.append([j,abs(angle1(ptc[0],ptc[1],pt[0],pt[1])-ang)])    
        anglee=360
        for i in ptss:
            if i[1]<anglee and i[0][2] not in store:
                anglee=i[1]
                locatn=i
        if(flgr==1):
            r=tempr
            flgr=0
        if locatn[0][2] in store:
            tempr=r
            r=r+50
            flgr=1
        store.append(locatn[0][2])
        temp=distance1(ptc[0],ptc[1],locatn[0][4],locatn[0][5],dictt)
        if distance1(pte[0],pte[1],locatn[0][4],locatn[0][5],dictt)<r/2:
            distan=distan+temp+distance1(pte[0],pte[1],locatn[0][4],locatn[0][5],dictt)
            return distan    
        fl0=1
        if locatn[0][2]==city2[2]:
            distan=distan+temp
            return distan
        print locatn
        print distan
    return distan

from Tkinter import *

def distance4(city1,state1,city2,state2,strr,r,theta):
    city1=nearestto(state1,city1,strr)
    city2=nearestto(state2,city2,strr)
    ptc=[city1[4],city1[5]]
    pte=[city2[4],city2[5]]
    fli=0
    fl0=0
    distan=0
    temp=0
    lat1=int(city1[4][:2])
    lat2=int(city2[4][:2])
#    print city1
    store=[]
    temp=0
    flgr=0
    inc=50
    tempr=r
    tinc=50
    while((ptc[0]!=pte[0])and(ptc[1]!=pte[1])):
        distan=distan+temp
        if(fl0==1):
            ptc=[locatn[4],locatn[5]]
            lat1=int(locatn[4][:2])
            lat2=int(city2[4][:2])
        thet=angle1(ptc[0],ptc[1],pte[0],pte[1])
        ptstart=pts(thet-theta,r)
        ptend=pts(thet+theta,r)
        ptss=[]
        if lat1<lat2:
            s=lat1
            e=lat2
        else:
            e=lat1
            s=lat2
        ang=angle1(ptc[0],ptc[1],pte[0],pte[1])
        for i in range(s,e+1):
            for j in latlon1[i]:
                pt=[j[4],j[5]]
                if ptinsec(pt,ptc,pte,r,theta):
                    ptss.append(j)    
        anglee=0
        distt=9999
        for i in ptss:
            if i[2]==city2:
                locatn=i
                break;
            if (int(i[14])>anglee) and (i[2] not in store) and not(i[2].find("State")!=-1): #and (abs(distance1(i[4],i[5],pte[0],pte[1],dictt)-temp)<distt):
                anglee=int(i[14])
                locatn=i
                if fli==0:
                    fli=1
                    r=tempr
    
                #distt=(distance1(i[4],i[5],pte[0],pte[1],dictt)-temp)
              
        if fli==0 and flgr!=1:
            r=r+inc
            flgr=1
            continue;
        else:
            if fli==0:
                r=r+inc
                continue;
        if(flgr==1) and (locatn[2] not in store) :
            r=tempr
            flgr=0
            
        if locatn[2] in store:
           # tempr=r
            r=r+inc
            flgr=1
                
        temp=distance1(ptc[0],ptc[1],locatn[4],locatn[5],dictt)
        if distance1(pte[0],pte[1],locatn[4],locatn[5],dictt)<(r/2):
             distan=distan+temp+distance1(pte[0],pte[1],locatn[4],locatn[5],dictt)
             return distan    

        fl0=1
        store.append(locatn[2])
#        if(len(store)>7):
#           store.pop(0)
     #   print locatn
      #  print distan
    return distan

def distance5(city1,state1,city2,state2,strr,r,theta):
    city1=nearestto(state1,city1,strr)
    city2=nearestto(state2,city2,strr)
    ptc=[city1[4],city1[5]]
    pte=[city2[4],city2[5]]
    fli=0
    fl0=0
    distan=0
    temp=0
    
    lat1=float(city1[4][:2])
    lat2=float(city2[4][:2])
#    print city1
    arrtwo=[]
    arrtwo.append([ptc[0],ptc[1]])
    store=[]
    temp=0
    flgr=0
    inc=50
    tempr=r
    tinc=50
    while((ptc[0]!=pte[0])and(ptc[1]!=pte[1])):
        distan=distan+temp
        if(fl0==1):
            ptc=[locatn[4],locatn[5]]
            lat1=float(locatn[4][:2])
            lat2=float(city2[4][:2])
        thet=angle1(ptc[0],ptc[1],pte[0],pte[1])
        ptstart=pts(thet-theta,r)
        ptend=pts(thet+theta,r)
        ptss=[]
        if lat1<lat2:
            s=lat1
            e=lat2
        else:
            e=lat1
            s=lat2
        ang=angle1(ptc[0],ptc[1],pte[0],pte[1])
        for i in range(int(s),int(e)+1):
            for j in latlon1[i]:
                pt=[j[4],j[5]]
                if ptinsec(pt,ptc,pte,r,theta):
                    ptss.append(j)    
        anglee=0
        distt=9999
        for i in ptss:
            if i[2]==city2:
                locatn=i
                break;
            if (int(i[14])>anglee) and (i[2] not in store) and not(i[2].find("State")!=-1): #and (abs(distance1(i[4],i[5],pte[0],pte[1],dictt)-temp)<distt):
                anglee=int(i[14])
                locatn=i
                if fli==0:
                    fli=1
                    r=tempr
    
                #distt=(distance1(i[4],i[5],pte[0],pte[1],dictt)-temp)
              
        if fli==0 and flgr!=1:
            r=r+inc
            flgr=1
            continue;
        else:
            if fli==0:
                r=r+inc
                continue;
        if(flgr==1) and (locatn[2] not in store) :
            r=tempr
            flgr=0
            
        if locatn[2] in store:
           # tempr=r
            r=r+inc
            flgr=1
                
        temp=distance1(ptc[0],ptc[1],locatn[4],locatn[5],dictt)
        if distance1(pte[0],pte[1],locatn[4],locatn[5],dictt)<(r/2):
             distan=distan+temp+distance1(pte[0],pte[1],locatn[4],locatn[5],dictt)
	     arrtwo.append([pte[0],pte[1]])
             return [arrtwo,distan]    

        fl0=1
        store.append(locatn[2])
 	arrtwo.append([locatn[4],locatn[5]])	
#        if(len(store)>7):
#           store.pop(0)
#        print locatn
 #       print distan
    return [arrtwo,distan]

def sources(s,d):
    minnd=9000
    
    for i in s:
        temp=distance4(i[0],i[1],d[0],d[1],dictt,50,45)
        if(temp<minnd):
            minnd=temp
            source=i
    return [source,d,minnd]
        
def failsrc(s,d):
    minnd=9000
    secnd=9000
    flag=0
    ssrc=0
    for i in s:
        temp=distance4(i[0],i[1],d[0],d[1],dictt,50,45)
        if(temp<minnd):
            minnd=temp
            # if flag==0:
            #     secnd=temp
            source=i
            
#            flag=1
        elif(temp<secnd):
            secnd=temp
            ssrc=i
    if(ssrc==0):
        return [source,d,minnd]
    return [[source,minnd],[ssrc,secnd],d,(minnd/2)+secnd]
        
def distance3(city1,state1,city2,state2,strr,r,theta):
    city1=nearestto(state1,city1,strr)
    city2=nearestto(state2,city2,strr)
    ptc=[city1[4],city1[5]]
    pte=[city2[4],city2[5]]
    fl0=0
    distan=0
    temp=0
    print city1
    if(fl0==1):
        ptc=[locatn[0][4],locatn[0][5]]
    thet=angle1(ptc[0],ptc[1],pte[0],pte[1])
    ptstart=pts(thet-theta,r)
    ptend=pts(thet+theta,r)
    lat1=int(city1[4][:2])
    lat2=int(city2[4][:2])
    ptss=[]
    if lat1<lat2:
        s=lat1
        e=lat2
    else:
        e=lat1
        s=lat2
    ang=angle1(ptc[0],ptc[1],pte[0],pte[1])
    for i in range(s,e+1):
        for j in latlon[i]:
            pt=[j[4],j[5]]
            if ptinsec(pt,ptc,pte,r,theta):
                ptss.append([j,abs(angle1(ptc[0],ptc[1],pt[0],pt[1])-ang)])
    anglee=360
    for i in ptss:
        if i[1]<anglee:
            anglee=i[1]
            locatn=i
    print locatn
    temp=distance1(ptc[0],ptc[1],locatn[0][4],locatn[0][5],dictt)
    return temp


def shortest(sources,city,state,strr):
    city=nearestto(state,city,strr)
    dist=9999
    for i in sources:          # sources = [[city,state],[city1,state1]]
        temp1=nearestto(i[1],i[0],strr)
        temp=distance1(temp1[4],temp1[5],city[4],city[5],strr)
        if(dist>temp):
            dist=temp
            temp2=temp1
            st=i[1]
    return [temp2,dist,st]

def distance1(lat1,lon1,lat2,lon2,strr):
    from math import sin, cos, sqrt, atan2, radians
    
    R = 6373.0
    lat1=radians(float(lat1))
    lon1 = radians(float(lon1))
    lon2 = radians(float(lon2))
    lat2 = radians(float(lat2))
   
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance

            
def distance(city1,state1,city2,state2,strr):
    from math import sin, cos, sqrt, atan2, radians
    
    R = 6373.0
    res=strr[city1[:2]][city1]
    res1=strr[city2[:2]][city2]
    t1=city1
    t2=city2
    city1=res[0]
    city2=res1[0]
    if(len(res)>1):
        city1=nearestto(state1,t1,strr)
    if(len(res1)>1):
        city2=nearestto(state2,t2,strr)
        
 #   print city1
  #  print city2
    lat1 = radians(float(city1[4]))
    lon1 = radians(float(city1[5]))
    lon2 = radians(float(city2[5]))
    lat2 = radians(float(city2[4]))
   
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c

#    print "Result", distance
    return distance

cnt=0
arrr={}
for i in strrr:    
    alpha=i[2][:2]
    if alpha not in dictt :
        dictt[alpha]={}
        
        if i[2] not in dictt[alpha]:
            dictt[alpha][(i[2])]=[]
            dictt[alpha][(i[2])].append(i)
        else:
            dictt[alpha][(i[2])].append(i)
            # if i[2]!='Sati' and i[2]!='Rampur' and i[2]!='Ramnagar' and i[2]!='Fatehpur' and i[2]!='Raipur' and i[2]!='Rampura' and i[2]!='Ramgarh' and i[2]!='Shahpur' and i[2]!='Rajpur' and i[2]!='Khera' and i[2]!='Haripur' and i[2]!='Gurudwara' and i[2]!='Rasulpur' and i[2]!='Tanda' and i[2]!='Sultanpur' and i[2]!='Pali' and i[2]!='Nayagaon' and i[2]!='Alipur' and i[2]!='Manpur' and i[2]!='Gopalpur' and i[2]!='Mau' and i[2]!='Kotra'and i[2]!='Lalpur' and i[2]!='Gura' and i[2]!='Bahadurpur' and i[2]!='Baragaon' and i[2]!='Akbarpur'and i[2]!='Ratanpur' and i[2]!='Maharajpur' and i[2]!='Hasanpur' and i[2]!='Narayanpur' and i[2]!='Ganeshpur' and i[2]!='Hirapur' and i[2]!='Nawada' and i[2]!='Sherpur' and i[2]!='Bara' and i[2]!='Umri' and i[2]!='Khanpur' and i[2]!='Rajpura' and i[2]!='Garhi' and i[2]!='Nizampur' and i[2]!='Kamalpur' and i[2]!='Kheri' and i[2]!='Bhagwanpur' and i[2]!='Bori' and i[2]!='Rajgarh' and i[2]!='Khanapur':
            #    # if len(dictt[alpha][(i[2])])>2 and len(dictt[alpha][(i[2])])<19:
            #     #    arrr[len(dictt[alpha][(i[2])])]=i[2]
            #     if len(dictt[alpha][(i[2])]) not in arrr:
            #         arrr[len(dictt[alpha][(i[2])])]=[]
            #         arrr[len(dictt[alpha][(i[2])])].append(i[2])
            #     else:        
            #         if i[2] not in arrr[len(dictt[alpha][(i[2])])]: 
            #             arrr[len(dictt[alpha][(i[2])])].append(i[2])
            #     cnt=len(dictt[alpha][(i[2])])
            #     abc=dictt[alpha][(i[2])]
    else:
        if (i[2]) not in dictt[alpha]:
            dictt[alpha][(i[2])]=[]
            dictt[alpha][(i[2])].append(i)
        else:
            dictt[alpha][i[2]].append(i)

            # if i[2]!='Sati' and i[2]!='Rampur' and i[2]!='Ramnagar' and i[2]!='Fatehpur' and i[2]!='Raipur' and i[2]!='Rampura' and i[2]!='Ramgarh' and i[2]!='Shahpur' and i[2]!='Rajpur' and i[2]!='Khera' and i[2]!='Haripur'and i[2]!='Gurudwara' and i[2]!='Rasulpur' and i[2]!='Tanda' and i[2]!='Sultanpur' and i[2]!='Pali' and i[2]!='Nayagaon' and i[2]!='Alipur' and i[2]!='Manpur' and i[2]!='Gopalpur' and i[2]!='Mau' and i[2]!='Kotra' and i[2]!='Lalpur' and i[2]!='Gura' and i[2]!='Bahadurpur' and i[2]!='Baragaon' and i[2]!='Akbarpur' and i[2]!='Ratanpur' and i[2]!='Maharajpur' and i[2]!='Hasanpur' and i[2]!='Narayanpur' and i[2]!='Ganeshpur' and i[2]!='Hirapur' and i[2]!='Nawada' and i[2]!='Sherpur' and i[2]!='Bara' and i[2]!='Umri' and i[2]!='Khanpur' and i[2]!='Rajpura'and i[2]!='Garhi' and i[2]!='Nizampur' and i[2]!='Kamalpur' and i[2]!='Kheri' and i[2]!='Bhagwanpur' and i[2]!='Bori' and i[2]!='Rajgarh' and i[2]!='Khanapur':
            #     if len(dictt[alpha][(i[2])])>1 and len(dictt[alpha][(i[2])])<19:
            #         if len(dictt[alpha][(i[2])]) not in arrr:
            #             arrr[len(dictt[alpha][(i[2])])]=[]
            #             if i[2] not in arrr[len(dictt[alpha][(i[2])])]: 
            #                 arrr[len(dictt[alpha][(i[2])])].append(i[2])
            #         else:
            #             if i[2] not in arrr[len(dictt[alpha][(i[2])])]: 
            #                 arrr[len(dictt[alpha][(i[2])])].append(i[2])
            #     cnt=len(dictt[alpha][(i[2])])
            #     abc=dictt[alpha][(i[2])]

#print arrr
# #  Places with Similar Names :- # # Sati = 83 , Rampur = 56 , Ramnagar = 50, Fatehpur = 43, Raipur = 43 , Rampura=39 , Ramgarh=35 , Shahpur=29 , Rajpur=26, Khera=26 , Haripur=24, Gurudwara=22, Rusulpur=22, Tanda=21, Sultanpur=21 , Pali=21 , Nayagaon=20 , Alipur=20 , Manpur=20 , Gopalpur=20, Mau=20, Kotra=19, Lalpur=18
#Gura=18, Bahadurpur=18 , Baragaon=17 , Akbarpur=16, Ratanpur=16 , Maharajpur=16 Hasanpur=16, Narayanpur=16, Ganeshpur=15 , Hirapur=15 , Nawada=15 , Sherpur=15, Bara=15 , Umri=14 , Khanpur=14 , Rajpura=14 ,Garhi=13 , Nizampur=13 , Kamalpur=13 , Kheri=13, Bhagwanpur=13, Bori=13 , Rajgarh=12 , Khanapur=12

#print dictt['Pu']['Pune'][0][14]

#distance("Pune","Maharastra","Mumbai","Maharashtra",dictt)
#print shortest([["Pune","Maharashtra"],["Mumbai","Maharashtra"],["Aurangabad","Maharashtra"]],"Bara","Uttar Pradesh",dictt);
#print tt([["Pune","Maharashtra"],["Mumbai","Maharashtra"],["Aurangabad","Maharashtra"]],"Bara","Uttar Pradesh",dictt);

# resul1= distance4("Pune","Maharashtra","New Delhi","Delhi",dictt,100,45)
# resul4= distance4("Pune","Maharashtra","Bara","Uttar Pradesh",dictt,100,45)

# resul6= distance4("Ajmer","Rajasthan","Vishakhapatnam","Andhra Pradesh",dictt,100,45)
# resul2= distancegpop("Pune","Maharashtra","Mumbai","Maharashtra",dictt,50,45)
# resul3= distance4("Pune","Maharashtra","Mumbai","Maharashtra",dictt,50,45)
#resul5= distance4("Pune","Maharashtra","Kolkata","West Bengal",dictt,100,45)
#print resul5





#print sources([["Mumbai","Maharashtra"],["Ajmer","Rajasthan"],["Pune","Maharashtra"],["Kolkata","West Bengal"]],["Bara","Uttar Pradesh"])
#print ""
#print "Fail",failsrc([["Mumbai","Maharashtra"],["Ajmer","Rajasthan"],["Pune","Maharashtra"],["Kolkata","West Bengal"]],["Bara","Uttar Pradesh"])





# print "Pune - Delhi : ",resul1
# print "Pune - Bara : ",resul4
# print "Ajmer - Vishakhapatnam : ",resul6
# print "Pune - Kolkata : ",resul5
# print "Pune - Mumbai : ",resul2
# print "Pune - Mumbai : ",resul3



#print distance("Pune","Maharashtra","Mumbai","Maharashtra",dictt)
#print distance("Pune","Maharashtra","Bara","Uttar Pradesh",dictt)


#print newlist
#print cnt    
#print abc
#print dictt['Ba']['Bara']
# print dictt


def initFun():
    glClearColor(1.0,1.0,1.0,0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,700,0,700)

def outputs( x, y, r, g, b, string):
    glColor3f( r, g, b );
    glRasterPos2f(x, y);
    for i in range(0,len(string)):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_10, ord(string[i]))
    return

def outputs1( x, y, r, g, b, string):
    glColor3f( r, g, b );
    glRasterPos2f(x, y);
    for i in range(0,len(string)):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(string[i]))
    return

def reshapeFun(w,h):
    if w>h:
        glViewport((w-h)/2,0,h,h)
    else:
        glViewport(0,(h-w)/2,w,w)

root = Tk()
var2 = StringVar()
label2 = Label( root, textvariable=var2, relief=RAISED )
var2.set("Please enter the Shipment Source location")
label2.pack()
e2 = Entry(root)
e2.pack()
e2.focus_set()


var5 = StringVar()
label5 = Label( root, textvariable=var5, relief=RAISED )
var5.set("Please enter the Source State")
label5.pack()
e5 = Entry(root)
e5.pack()
e5.focus_set()


var3 = StringVar()
label3 = Label( root, textvariable=var3, relief=RAISED )
var3.set("Please enter the Shipment Destination location")
label3.pack()
e3 = Entry(root)
e3.pack()
e3.focus_set()


var6 = StringVar()
label6 = Label( root, textvariable=var6, relief=RAISED )
var6.set("Please enter the Destination State")
label6.pack()
e6 = Entry(root)
e6.pack()
e6.focus_set()


var4 = StringVar()
label4 = Label( root, textvariable=var4, relief=RAISED )
var4.set("Please enter the speed of travel(Kms/Hr)")
label4.pack()
e4 = Entry(root)
e4.pack()
e4.focus_set()

var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )
var.set("Please enter current location of Shipment")
label.pack()
e = Entry(root)
e.pack()
e.focus_set()

var1 = StringVar()
label1 = Label( root, textvariable=var1, relief=RAISED )
var1.set("Please enter name of the State(Current)")
label1.pack()
e1 = Entry(root)
e1.pack()
e1.focus_set()
inputarray=[]
def callback():
    global inputarray
    inputarray.append(str(e2.get()))
    inputarray.append(str(e5.get()))
    inputarray.append(str(e3.get()))
    inputarray.append(str(e6.get()))
    inputarray.append(str(e4.get()))
    inputarray.append(str(e.get()))
    inputarray.append(str(e1.get()))
    root.destroy()
    
b = Button(root, text = "OK", width = 10, command=callback)
b.pack()

root.mainloop()

def route(city1,state1,city2,state2,strr,r,theta,speed,ccity,cstate):
    arrn=distance5(city1,state1,city2,state2,strr,r,theta)
    carrn=distance5(ccity,cstate,city2,state2,strr,r,theta)
    distan=arrn[1]
    cdistan=carrn[1]
    arrn=arrn[0]
    carrn=carrn[0]
    xpts1=[]
    ypts1=[]
    cxpts1=[]
    cypts1=[]
    
    outputs(-1500+float(arrn[0][1])*22.5,-150+float(arrn[0][0])*22.5,0.5,0,0.5,city1)
    outputs(-1500+float(arrn[-1][1])*22.5,-150+float(arrn[-1][0])*22.5,0.5,0,0.5,city2)
    dotno=(str(distan).find("."))+3
    distanceof="Total Distance : "+str(distan)[:dotno] +" Km"
    dotno=(str(float(distan)/float(speed)).find("."))+3
    timet="Total Time : "+str(float(distan)/float(speed))[:dotno] + " Hrs"
    dotno1=(str(cdistan).find("."))+3
    distanceof1="Distance Reqd : "+str(cdistan)[:dotno1] +" Km"
    dotno1=(str(float(cdistan)/float(speed)).find("."))+3
    timet1="Time Reqd: "+str(float(cdistan)/float(speed))[:dotno1] + " Hrs"

    info=str(city1)+" : "
    info1=" Population : "+str(dictt[city1[:2]][city1][0][14])
    info2=" Elevation : "+str(dictt[city1[:2]][city1][0][16])
    einfo=str(city2)+" : "
    einfo1=" Population : "+str(dictt[city2[:2]][city2][0][14])
    einfo2=" Elevation : "+str(dictt[city2[:2]][city2][0][16])

    outputs(375,675,0,0.75,0.75,info)
    outputs(385,660,0,0.75,0.75,info1)
    outputs(385,645,0,0.75,0.75,info2)
    outputs(525,675,0,0.75,0.75,einfo)
    outputs(535,660,0,0.75,0.75,einfo1)
    outputs(535,645,0,0.75,0.75,einfo2)
    #outputs(375,125,0,0.75,0.75,info)
    outputs1(400,125,0,0.75,0.75,distanceof)
    outputs1(400,100,0,0.75,0.75,timet)
    outputs1(400,195,0,0.75,0.75,distanceof1)
    outputs1(400,170,0,0.75,0.75,timet1)
    for i in arrn:
      #  xpts1.append(700+100-float(i[0])*20)
     #   ypts1.append(700+1300-float(i[1])*20)
        xpts1.append(-1500+float(i[1])*22.5)
        ypts1.append(-150+float(i[0])*22.5)
#    print xpts1,ypts1

    for i in carrn:
      #  xpts1.append(700+100-float(i[0])*20)
     #   ypts1.append(700+1300-float(i[1])*20)
        cxpts1.append(-1500+float(i[1])*22.5)
        cypts1.append(-150+float(i[0])*22.5)

    glBegin(GL_LINES)
    glColor3f(0.0,1.0,0.0)
    for j in range(0,len(xpts1)-1):
        glVertex2f(xpts1[j],ypts1[j])
        glVertex2f(xpts1[j+1],ypts1[j+1])
    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glColor3f(1.0,0.0,1.0)
    for j in range(0,len(cxpts1)-1):
        glVertex2f(cxpts1[j],cypts1[j])
        glVertex2f(cxpts1[j+1],cypts1[j+1])
    glEnd()
    glFlush()
    return


def displayFun():
    glClearColor(1.0,1.0,1.0,0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,1.0)
    xpts=[]
    ypts=[]
    N=len(newlist)

    for i in range(0,N):
     #   xpts.append(700+100-float(newlist[i][4])*20)
      #  ypts.append(700+1300-float(newlist[i][5])*20)
        xpts.append(-1500+float(newlist[i][5])*22.5)
        ypts.append(-150+float(newlist[i][4])*22.5)

    glBegin(GL_POINTS)
    for j in range(0,N):	
        glVertex2f(xpts[j],ypts[j])
	
        #glVertex2f(xpts[j],ypts[j])
        #glEnd()
    glEnd()
    glFlush()
    global inputarray
    scity=inputarray[0]
#    print "ENTER SOURCE CITY"
#    scity=raw_input()
    while(scity not in rdictt):
     
        print "The city does not appear to be in the list of locations. Please enter a valid city or a well known location very close to your entered location"
        scity=raw_input()
 #   print "ENTER SOURCE STATE"
    
    #sstate=raw_input()
    sstate=inputarray[1]
    while(sstate not in States):
        print "The State does not appear to be in the list of States. Please enter valid State."
        sstate=raw_input()
  #  print "ENTER DESTINATION CITY"
#    ecity=raw_input()
    ecity=inputarray[2]
    while(ecity not in rdictt):
        print "The city does not appear to be in the list of locations. Please enter a valid city or a well known location very close to your entered location"
        ecity=raw_input()
   # print "ENTER DESTINATION STATE"
#    estate=raw_input()
    estate=inputarray[3]
    while(estate not in States):
        print "The State does not appear to be in the list of States. Please enter valid State."
        estate=raw_input()
    currcity=inputarray[5]
    while(currcity not in rdictt):
        print "Enter Current City Again"
        print "The city does not appear to be in the list of locations. Please enter a valid city or a well known location very close to your entered location"
        currcity=raw_input()
    currstate=inputarray[6]
    while(currstate not in States):
        print "Enter Current State Again"
        print "The State does not appear to be in the list of States. Please enter valid State."
        currstate=raw_input()
    
#    print "ENTER SPEED OF TRAVEL"
    
#    speed=float(raw_input())
    speed=inputarray[4]
    route(scity,sstate,ecity,estate,dictt,100,45,speed,currcity,currstate)
    glFlush()
    # print "Enter 1 to check another Route"
    # rno=raw_input()
    # if len(rno)>1 or len(rno)==0:
    #     while len(rno)<1 or len(rno)>1:
    #         print "Incorrect Please Enter 1"
    #         rno=raw_input()
    # if ord(rno)==49:
    #     float(rno)
    # else:
    #     while (len(rno)>1 or len(rno)==0) and (ord(rno)!=49):
    #         print "Please Enter 1"
    #         rno=raw_input()

    print "Enter 1 to check another Route"
    rno=raw_input()
    if len(rno)>1 or len(rno)==0:
        while len(rno)<1 or len(rno)>1:
            print "Incorrect input Please Enter 1"
            rno=raw_input()
    if ord(rno)==49:
        float(rno)
    else:
        while len(rno)<1 or len(rno)>1:
            print "Incorrect input Please Enter 1"
            rno=raw_input()
        while (ord(rno)!=49):
            print "Incorrect input Please Enter 1"
            rno=raw_input()
            while len(rno)<1 or len(rno)>1:
                print "Incorrect input Please Enter 1"
                rno=raw_input()
    glutPostRedisplay()

# def displayFun():
#     rno=1
#     while True:
#         glClearColor(1.0,1.0,1.0,0.0)
#         glClear(GL_COLOR_BUFFER_BIT)
#         glColor3f(0.0,0.0,1.0)
#         xpts=[]
#         ypts=[]
#         N=len(newlist)

#         for i in range(0,N):
#             #   xpts.append(700+100-float(newlist[i][4])*20)
#             #  ypts.append(700+1300-float(newlist[i][5])*20)
#             xpts.append(-1500+float(newlist[i][5])*22.5)
#             ypts.append(-150+float(newlist[i][4])*22.5)

#         glBegin(GL_POINTS)
#         for j in range(0,N):	
#             glVertex2f(xpts[j],ypts[j])
            
#         #glVertex2f(xpts[j],ypts[j])
#         #glEnd()
#         glEnd()
#         glFlush()
#         global inputarray
#         scity=inputarray[0]
#         #    print "ENTER SOURCE CITY"
#         #    scity=raw_input()
#         while(scity not in rdictt):
     
#             print "The city does not appear to be in the list of locations. Please enter a valid city or a well known location very close to your entered location"
#             scity=raw_input()
#     #   print "ENTER SOURCE STATE"
            
#     #sstate=raw_input()
#         sstate=inputarray[1]
#         while(sstate not in States):
#             print "The State does not appear to be in the list of States. Please enter valid State."
#             sstate=raw_input()
#             #  print "ENTER DESTINATION CITY"
#             #    ecity=raw_input()
#         ecity=inputarray[2]
#         while(ecity not in rdictt):
#             print "The city does not appear to be in the list of locations. Please enter a valid city or a well known location very close to your entered location"
#             ecity=raw_input()
#             # print "ENTER DESTINATION STATE"
#             #    estate=raw_input()
#         estate=inputarray[3]
#         while(estate not in States):
#             print "The State does not appear to be in the list of States. Please enter valid State."
#             estate=raw_input()
#         currcity=inputarray[5]
#         while(currcity not in rdictt):
#             print "Enter Current City Again"
#             print "The city does not appear to be in the list of locations. Please enter a valid city or a well known location very close to your entered location"
#             currcity=raw_input()
#         currstate=inputarray[6]
#         while(currstate not in States):
#             print "Enter Current State Again"
#             print "The State does not appear to be in the list of States. Please enter valid State."
#             currstate=raw_input()
    
#         #    print "ENTER SPEED OF TRAVEL"
#         #    speed=float(raw_input())
#         speed=inputarray[4]
#         route(scity,sstate,ecity,estate,dictt,100,45,speed,currcity,currstate)
#         glFlush()
#         # print "Enter 1 to check another Route"
#         # rno=raw_input()
#         # if len(str(rno))>1 or len(str(rno))==0:
#         #     while len(str(rno))<1 or len(str(rno))>1:
#         #         print "Incorrect Please Enter 1"
#         #         rno=raw_input()
#         # if ord(str(rno))==49:
#         #     float(rno)
#         # else:
#         #     while (len(str(rno))>1 or len(str(rno))==0) and (ord(rno)!=49):
#         #         print "Please Enter 1"
#         #         rno=raw_input()
#         print "Press any key to check another Route"
#         keyy=raw_input()
                
#     #     print "Enter 1 to check another Route"
#     #     rno=raw_input()
#     #     if len(rno)>1 or len(rno)==0:
#     #         while len(rno)<1 or len(rno)>1:
#     #             print "Incorrect input Please Enter 1"
#     #             rno=raw_input()
#     #     if ord(rno)==49:
#     #         float(rno)
#     #     else:
#     #         while len(rno)<1 or len(rno)>1:
#     #             print "Incorrect input Please Enter 1"
#     #             rno=raw_input()
#     #             while (ord(rno)!=49):
#     #                 print "Incorrect input Please Enter 1"
#     #                 rno=raw_input()
#     #             while len(rno)<1 or len(rno)>1:
#     #                 print "Incorrect input Please Enter 1"
#     #                 rno=raw_input()
#     glutPostRedisplay()

 	
if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(700,700)
    glutCreateWindow("My Display")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    #glutReshapeFunc(reshapeFun)
    initFun()
    glutMainLoop()
f.close()
