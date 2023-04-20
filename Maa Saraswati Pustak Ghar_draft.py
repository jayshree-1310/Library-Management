import mysql.connector as lib
pwd=input("enter the server pwd:")
mc=lib.connect(host='localhost',user='root',password=pwd,database='lib')
cursor=mc.cursor()

import datetime
from datetime import date, timedelta
k=0
r=1
g=1
jh=1
now = date.today()
due=date.today() + timedelta(7)


lst1=['13 reasons why', 'Jay asher',4,200]
lst2=['Lost symbol', 'Dan brown', 6, 250]
lst3=['Fault in our star', 'John green',7,277]
lst4=['Murder on the orient express','Agatha Christie',5,198]
lst5=['What light','Jay asher',6, 275]
lst6=['Otheollo', 'William shakespear', 2, 233]
lst7=['Sherlock holmes:Hounds of the baskervilles','Arthur canon doyle',5,250]
lst8=['A christmas carol', 'Charles dickens', 3, 320]
lst9=['Wings of fire','A.P.J Abdul kalam',4,300]
lst10=['Someone like you','Nikita singh',6,327]
lst11=['3 men in a boat','Jerome k jerome',4,295]
lst12=['The diary of a young girl','Anne frank',7,250]
lst13=['The story of my life','Helen keller',4,235]
lst14=['Vision 20-20','A.P.J Abdul kalam',9,226]
lst15=['Harry Potter:The Philosopher\'s stone','J.K Rowling',4,300]



fu=open("user.txt","r+")
lst42=fu.readlines()
lst100=[]

for mk in range(0,len(lst42)):
    dm=(lst42[mk].strip()).split(',')
    lst100.append(dm) 


dlib={}


print("\nWelcome to 'Maa Saraswati Pustak Ghar':)!")
sp=input("Do you want to create a new database?(y/n):")
if sp=='y':
    cursor.execute("drop database if exists lib")           #retreiving all the data from notepad to sql for permanency
    cursor.execute("create database lib")
    cursor.execute("use lib")

    cursor.execute('''create table issue(Name varchar(30),
       Book_Name Varchar(1000),
       Author varchar(30),
       Roll_number varchar(30),
       Due_date date,
       issue_date date)''')

    cursor.execute('''create table user(Roll_number varchar(30),
       password varchar(30),
       Name varchar(30))''')


    cursor.execute('''create table books(Name varchar(1000),
       author varchar(1000),
       copies int,
       price int)''')
    fi=open("issue.txt","r+")
    list1=fi.readlines()

    for i in range(0,len(list1)-1):                                   #check issue books for this section
        list123=list1[i].split(",") 
        q=list123[0] 
        w=list123[1]                                                          #notepad to SQL for issue info
        e=list123[2]
        r=list123[3]
        t=list123[4]
        y=list123[5]
        cursor.execute("INSERT INTO issue VALUES(%s, %s, %s, %s, %s, %s)", (q,w,e,r,t,y))
        mc.commit()



    fi.close()

    fu=open("user.txt","r+")
    list1=fu.readlines()

    for i in range(0,len(list1)):                                   
        list123=list1[i].split(",")                  #check new user section
        q=list123[0] 
        w=list123[1]                                                          #notepad to SQL for issue info
        e=list123[2]
        cursor.execute("INSERT INTO user VALUES(%s, %s, %s)",(q,w,e))
        mc.commit()
    fu.close()


    fb=open("books.txt","r+")
    list123=fb.readlines()



    for i in range(0,len(list123)):
        l=list123[i].split(",")
        q=l[0]
        w=l[1]                                                                 #notepad to SQL for books info
        e=l[2]
        r=l[3]
        cursor.execute("INSERT INTO books VALUES(%s, %s, %s, %s)",(q,w,e,r))
        mc.commit()
    fb.close()
                    
else:
    pass
dmemb={}
while jh==1:
    yx=int(input('''1.New Member
2.Existing Member
Enter 1/2: '''))
            
    if yx==1:
        fm=input("Enter your name:")
        oo=int(input("Enter roll number:"))
        hh=input("Enter your password:")
        cursor.execute("SELECT * FROM user")
        lst20=cursor.fetchall()                #tupples inside a list
        mj=[]
        mk=[]
        for i in range(0,len(lst20)):
            ddlj=list(lst20[i])
            mj.append(ddlj)
        for k in range(0,len(mj)):
            asa=int(mj[k][0])
            mk.append(asa)
        for j in range(0,len(mk)):
            if oo==mk[j]:                                 
                print('''This user already exists!
Try again :)''')
                break
            else:
                continue
            
        else:
            m=[oo,hh,fm]
            dmemb[oo]=m
            cursor.execute("INSERT INTO user VALUES({},'{}', '{}')".format(oo,hh,fm))
            mc.commit()
            print('''Congratulations you have registered sucessfully!
Login again to continue :)''')
            cursor.execute("SELECT * FROM user")
            lst20=cursor.fetchall()                #tupples inside a list
            mj=[]
            for i in range(0,len(lst20)):
                ddlj=list(lst20[i])
                mj.append(ddlj)                     #list containing the above tupples as lists
                dmemb[int(mj[i][0])]=ddlj   #member library created everytime a new user logins to add it along all previous data 
            continue

    elif yx==2:
        uu=int(input("Enter roll number:"))
        ss=input("Enter password: ")
        cursor.execute("SELECT * FROM user")
        lst20=cursor.fetchall()
        mj=[]
        
        for i in range(0,len(lst20)):
            ddlj=list(lst20[i])                     #same happening as above for the old user as well with the new users added
            mj.append(ddlj)                         #advatantage of connectivity
       
        lsts=[]
        t1=[]
        for i in range(0,len(lst20)):
            ddlj=mj[i][0]
            dd1=mj[i]
            lsts.append(ddlj)       #list having roll nos.
            t1.append(mj[i])
        
        for j in range(0,len(lsts)):
            dmemb[int(mj[j][0])]=t1[j]
        
        ps=dmemb.get(uu)
        ph=dmemb.keys()
        la=list(ph)
        if uu not in la:
            print("Wrong Credentials!!")    
            print(ps[1])   
                
        if ss==ps[1]:
            print("Welcome", ps[2])
            print("\nTo know what all books are available in the Library,Enter 1 in the index.")
            while k<8:                      
                
                k = int(input('''\n==========Library Index============
1.Display all available Books
2.Issue Books
3.Add Books
4.Return Book
5.Defaulters
6.Exit
7.Save data
Enter a no. from Index:'''))

                if k==1:
                    print('''\nAvailable Books:
====================''')
                    cursor.execute("SELECT * FROM books")
                    lst20=cursor.fetchall()
                    mj=[]
                    for i in range(0,len(lst20)):
                        ddlj=list(lst20[i])
                        mj.append(ddlj)
                        dlib[i+1]=ddlj
                    for a in dlib:
                        i=dlib.get(a)
                        f=str(a)+"."+i[0]
                        print(f)
                    print("=========================================")
                  
                elif k==2:
                    se=input("Enter your name:")
                    sm=se.lower()
                    n=int(input("\nEnter the book number from Available Books: "))
                    cursor.execute("SELECT * FROM books")
                    lst20=cursor.fetchall()
                    mj=[]
                    for i in range(0,len(lst20)):
                        ddlj=list(lst20[i])
                        mj.append(ddlj)
                        dlib[i+1]=ddlj
                    l=dlib.get(n)
                    print(l[0])
                    count=l[2]
                   
                    
                    b=input('''\nDo you want to know the details?
                                Yes/No: ''')

                    if b=="yes" or b=="Yes" or b=="YES" or b=="yES" or b=="y" or b=="Y":    
                        print("\n-Book name:",l[0])
                        print("-Book Author:",l[1])
                        print("-Book Price:",l[3])
                        print("-No. of copies:",l[2])

                        print("Are you sure you want to issue book,",l[0],"?")  
                        j=input("Yes/No:")
                        if j=="yes" or j=="Yes" or j=="YES" or j=="yES" or j=="y" or j=="Y":
                            count=count-1
                            cursor.execute("UPDATE books SET copies='{}' WHERE copies='{}'".format(count,l[2]))
                            if count<0:
                                print("Book is not available at the moment!") 
                                break
                            print("\n*Your date of issue is:",now)
                            print("*Your due date is:",due)
                            print("Thanks for visiting!")
                            print("=============================")
                            
                            cursor.execute("INSERT INTO issue VALUES('{}','{}', '{}', {}, '{}', '{}')".format(sm,l[0],l[1],uu,due,now))
                            mc.commit()



                              
                        else:   
                            print("Thanks for visiting!")
                            
                        
                    else:
                        print("Are you sure you want to issue book,",l[0],"?")
                        j=input("Yes/No:")
                        if j=="yes" or j=="Yes" or j=="YES" or j=="yES" or j=="y" or j=="Y":
                            count=count-1
                            if count<0:
                                print("Book is not available at the moment!")
                                cursor.execute("UPDATE books SET copies='{}' WHERE copies='{}'".format(count,l[2]))
                                break
                            print("\n*Your date of issue is:",now)
                            print("*Your due date is:",due)
                            print("Thanks for visiting!")
                            print("=============================")
                            count=count-1
                           
                            cursor.execute("INSERT INTO issue VALUES('{}','{}', '{}', {}, '{}', '{}')".format(sm,l[0],l[1],uu, due, now))
                            mc.commit()


                            
                        else:
                            print("Thanks for visiting!")
                            print("=============================")  
                    

                elif k==3:
                    print('''\nTo Add a Book to this Library,
            Enter book number and a list containg its details
            in following way:
            \n['Book name','Author',No. of copies,Price]''')
                    mkv=dlib.keys()
                    maxm=max(mkv)   
                    q=maxm+1      
                    e=eval(input("Enter a 'LIST' of format as mentioned above:"))
                    cursor.execute("INSERT INTO books VALUES('{}','{}',{},{})".format(e[0],e[1],e[2],e[3]))
                    mc.commit()
                    print("\nYour book is added to the Library, to check Enter 1 in index.")
                    print("================================================")
                    cursor.execute("SELECT * FROM books")
                    lst20=cursor.fetchall()
                    mj=[]
                    for i in range(0,len(lst20)):
                        ddlj=list(lst20[i])
                        mj.append(ddlj)
                        dlib[i+1]=ddlj
                
                      
                    while r==1:         
                        t=input('''\nDo you want to add another book:
            yes/no?''')
                        if t=="yes" or t=="Yes" or t=="YES" or t=="yES" or t=="y" or t=="Y":
                            par=dlib.keys()
                            maxm=max(par)   
                            q=maxm+mk 
                            mk+=1
                            e=eval(input("Enter a 'LIST' of format as mentioned above:"))
                            dlib[q]=e
                            cursor.execute("INSERT INTO books VALUES('{}','{}',{},{})".format(e[0],e[1],e[2],e[3]))
                            mc.commit()
                            print("\nYour book is added to the Library, to check Enter 1 in index.")
                            print("================================================")
                            
                            
                           
                        else:           
                            print("Thanks for visiting!")
                            break

                elif k==4:
                    y1=input("enter your name:")
                    w1=y1.lower()
                    cursor.execute("SELECT * FROM issue")
                    lst20=cursor.fetchall()
                    mj=[]
                    mk=[]
                    
                    for i in range(0,len(lst20)):
                        ddlj=list(lst20[i])
                        mj.append(ddlj)
                    
                    for j in range(0,len(mj)):
                        dd=mj[j][0].lower()
                        mk.append(dd)
                    
                    for f in range(0,len(mk)):
                        if w1==mk[f]:   
                            cursor.execute("DELETE FROM issue WHERE Name='{}'".format(w1))
                            mc.commit()
                        else:
                            pass
                        
                    print(y1,"has returned the book","Thanks!")
                    print("=========================================================================")

                elif k==5:
                    print("\nThe Defaulters are:")
                    cursor.execute("Select * from Issue where due<curdate1")
                    cd=cursor.fetchall()
                    for cd1 in cd:
                        print(cd1)

                    cursor.execute("Select due from Issue where due<curdate1")
                    defa=cursor.fetchall()
                    for bg in defa:
                        if curdate1-bg==1:
                            print("You have to pay Rs10 as a fine.")
                        elif curdate1-bg==2:
                            print("You have to pay Rs20 as a fine.")
                        elif curdate1-bg==3:
                            print("You have to pay Rs30 as a fine.")
                        elif curdate1-bg==4:
                            print("You have to pay Rs40 as a fine.")
                        elif curdate1-bg==5:
                            print("You have to pay Rs50 as a fine.")
                        elif curdate1-bg==6:
                            print("You have to pay Rs60 as a fine.")
                        else:
                            print("You have to pay the total cost of the book as a fine that is",l[3])
                    

                elif k==6:
                    exit()

                '''elif k==7:
                    cursor.execute("SELECT * FROM issue")
                    mj=cursor.fetchall()
                    fi=open("issue.txt","r+")
                    for i in mj:
                        io=fi.write(str(i))
                        fi.write('\n')                            #still working on this
                    fi.close()
                    cursor.execute("SELECT * FROM user")
                    mi=cursor.fetchall()
                    fu=open("user.txt","r+")
                    for i in mi:
                        uo=fu.write(str(i))
                        fu.write('\n')
                    fu.close()
                    cursor.execute("SELECT * FROM books")
                    ml=cursor.fetchall()
                    fb=open("books.txt","r+")
                    for i in ml:
                        bo=fb.write(str(i))
                        fb.write('\n')
                    fb.close()'''

       
            
        else:
            print("invalid cridentials!")
  
           
            
    
 

    
        
            
    
        
 
                
     
                
        
        

