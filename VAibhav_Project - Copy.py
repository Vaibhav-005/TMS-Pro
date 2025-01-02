import sqlite3
t = 0

#******************************************************FUNCTIONS********************************************************************************
#_________________________________________________________________________________________________________________________________

def Entry(w):
    F = 1
    while F == 1:
        con = sqlite3.connect("VS Pro.db")
        cur = con.cursor()
        print('''_________________________________________________________________________________________________________________________
\t\t\t\t\t\tMARKS
_________________________________________________________________________________________________________________________''')
        print('''\nTo enter the marks of students - enter 1
To see the marks entered - enter 2
To go to homepage - enter 3''')

        try:
            v = int(input('\nEnter the response :')) 
            while v != 1 and v != 2 and v != 3 :
                print('''\nTo enter the marks of students - enter 1
To see the marks entered - enter 2
To go to homepage - enter 3''')
                v = int(input('\nEnter the response :'))

            if v == 3:
                return

            elif v == 2:
                P = cur.execute(''' select Name from Teacher where TID = ?;''',(w,))
                q = P.fetchall()
                e = cur.execute('''select * from Class_List where Name = ?;''',q[0])
                f = e.fetchall()
                print('''_________________________________________________________________________________________________________________________
\t\t\t\t\t\tCLASSES
_________________________________________________________________________________________________________________________''')
                D = 1
                while D == 1:
                    print()
                    for i in f:
                        print(count,'.',i[1],'th class',',  enter -',i[1])
                        count += 1
                    count = 1
                    print('''To go to back - enter 14''')
                    while True:
                        try:
                            U = int(input("\nEnter your response:"))
                            break
                        except:
                            print('Invalid Input')

                    if U == 14 :
                        break

                    elif U != 14 :
                        g = cur.execute('''select * from Marks where Tid = ? and Class = ?;''',(w,U))
                        n = g.fetchall()
                        if n == []:
                            print('\n\t\t\t\t\tNo marks entered')
                        else:
                            for i in n:
                                print('''_________________________________________________________________________________________________________________________
_________________________________________________________________________________________________________________________''')
                                print('\nExam -\t\t',i[2],'\nSakshi Yadav -\t',i[3],'\nRoopam Bisht -\t',i[4],'\nBhakti Biswas -\t',i[5],'\nDeepika Chauhan -\t',i[6],'\nTina Sharma -\t',i[7])
                    print('''\nTo go to menu - enter any no.''')
                    while True:
                        try:
                            c = int(input('\nenter the response :'))
                            break
                        except:
                            print('Invalid Input')

                    if c == 1:
                        D = 2
                    D = 1

            elif v == 1:
                while True:
                    C = input('\nEnter the class:')
                    e = input('\nEnter the exam name:')
                    while True:
                        try:
                            s = int(input('\nSakshi Yadav -'))
                            break
                        except:
                            print('Invalid Input')

                    while True:
                        try:
                            r = int(input('\nRoopam Bisht -'))
                            break
                        except:
                            print('Invalid Input')

                    while True:
                        try:
                            d = int(input('\nBhakti Biswas -'))
                            break
                        except:
                            print('Invalid Input')

                    while True:
                        try:
                            z = int(input('\nDeepika Chauhan -'))
                            break
                        except:
                            print('Invalid Input')

                    while True:
                        try:
                            m = int(input('\nTina Sharma -'))
                            break
                        except:
                            print('Invalid Input')

                    cur.execute('''insert into Marks values(?,?,?,?,?,?,?,?);''',(w,C,e,s,r,d,z,m))
                    con.commit()
                    con.close()
                    print('\nMarks have been updated')
                    print('''\nTo continue adding marks - enter yes
To exit - enter no''')

                    k = input('\nEnter the reponse:')

                    if k.lower() == 'yes':
                        continue

                    if k.lower() == 'no':
                        break
        except:
            print('Invalid Input')
    con.commit()
    con.close()

##    cur.execute('''create table Marks
##(Tid int ,
##Class varchar(10) ,
##Exam varchar(30) ,
##Sakshi Yadav int, 
##Roopam Bisht int ,
##Bhakti Biswas int ,
##Deepika Chauhan int ,
##Tina Sharma int
##);''')
    
##Entry()

#************************************************************************************************************************************************************
#************************************************************************************************************************************************************

def Details(f):
    con = sqlite3.connect("VS Pro.db")
    cur = con.cursor()
    cur.execute('''select * from Student where Name = ?;''',(f,)) 

##    cur.execute('''insert into Student values(1126,'Sakshi Yadav','Karan Yadav','Meena Yadav',2489347245,'sakshi12@gamil.com','Yellow');''')
##    cur.execute('''insert into Student values(1127,'Roopam Bisht','Suresh Bisht','Siya Bisht',9012564783,'roopam113@gamil.com','Green');''')
##    cur.execute('''insert into Student values(1128,'Bhakti Biswas','Ayush Biswas','Radhika Devi',8944267190,'bhakti47@gamil.com','Blue');''')
##    cur.execute('''insert into Student values(1129,'Deepika Chauhan','Ramesh Chauhan','Yamini Chauhan',4478563317,'deepika801@gamil.com','Red');''')
##    cur.execute('''insert into Student values(1130,'Tina Sharma','Bhopal Sharma','Riya Sharma',8057006783,'tina444@gamil.com','Green');''')
##    cur.execute('''create table Student
##(Admn int ,
##Name varchar(50) ,
##Fname varchar(50) ,
##Mname varchar(50) ,
##Contact int ,
##Email_id varchar(50) ,
##House varchar(50)
##);''')

    s = cur.fetchall()

    if s == []:
        print('\nNo such student exists')

    else:
        print('''_________________________________________________________________________________________________________________________
\t\t\t\t\t\t''',f)
        print('''_________________________________________________________________________________________________________________________''')
        for i in s :
            print('\nAdmission no. -\t',i[0],'\nName -\t\t',i[1],'\nFather name -\t',i[2],'\nMother name -\t',i[3],'\nContact no. -\t',i[4],'\nEmail id -\t',i[5],'\nHouse -\t\t',i[6]) 
    con.commit()
    con.close()
    return

##Details()

#************************************************************************************************************************************************************
#************************************************************************************************************************************************************

def Att(e):
    con = sqlite3.connect("VS Pro.db")
    cur = con.cursor()
    cur.execute(''' select Class from Teacher where TID = ?;''',(e,))
    q = cur.fetchall()

    if q == []:
        print('''_________________________________________________________________________________________________________________________
\t\t\t\t\t\tATTENDANCE
_________________________________________________________________________________________________________________________''')
        print('You are not the class teacher of any class')
        return

    else :
        f = 1
        while f == 1:
            print('''_________________________________________________________________________________________________________________________
\t\t\t\t\t\tATTENDANCE
_________________________________________________________________________________________________________________________''')
            print('''\nTo mark the Attendance - enter 1
To see the Attendance - enter 2
To go to homepage - enter 3''')
            try:
                v = int(input('\nEnter the resoponse :'))
                while v != 1 and v != 2 and v != 3 :
                    print('''\nTo mark the Attendance - enter 1
To see the Attendance - enter 2
To go to homepage - enter 3''')
                    v = int(input('\nEnter the resoponse :'))

                if v == 3:
                    return

                if v== 2 :
                    g = cur.execute('''select Name,count(Present),count(Absent) from Attendance group by Name;''')
                    n = g.fetchall()
                    print('''_________________________________________________________________________________________________________________________
_________________________________________________________________________________________________________________________''')
                    for i in n:
                        print('\nName -',i[0],'\nPresent -',i[1],'\n Absent -',i[2])
                    print('''\nTo go to menu - enter any no.''')
                    while True:
                        try:
                            c = int(input('\nenter the response :'))
                            break
                        except:
                            print('Invalid Input')

                    if c == 1:
                        f = 2
                    f = 1

                if v == 1:
                    l = []
                    y = cur.execute('''select Name from Attendance;''')
                    h = y.fetchall()
                    print('''_________________________________________________________________________________________________________________________
_________________________________________________________________________________________________________________________''')
                    print('''Enter 'P' for present and 'A' for absent''')
        
                    for i in h:

                        if i[0] in l:
                            continue

                        else:
                            print('\n',i[0])
                            l.append(i[0])
                            A = input('Enter -')

                            if A.upper() == 'P':
                                cur.execute('''insert into Attendance values(?,?,NULL);''',(i[0],A))

                            elif A.upper() == 'A' :
                                cur.execute('''insert into Attendance values(?,NULL,?);''',(i[0],A))
                    print('\nAttendance has been marked')
                    print('''\nTo go to menu - enter any no.''')
                    while True:
                        try:
                            c = int(input('\nenter the response :'))
                            break
                        except:
                            print('Invalid Input')

                    if c == 1:
                        f = 2
                    f = 1
            except:
                print('Invalid Input')

#************************************************************************************************************************************************************
#************************************************************************************************************************************************************

def Message(k):
    d = 1
    while d==1:
        print('''_________________________________________________________________________________________________________________________
\t\t\t\t\t\tMESSAGE
_________________________________________________________________________________________________________________________''')
        print('''\nTo send messge - 1
Messge history - 2
To go to homepage - 3''')

        try:
            m = int(input('\nEnter the response :'))
            while m != 1 and m != 2 and m != 3:
                print('''\nTo send messge - 1
Messge history - 2
To go to homepage - 3''')
                m = int(input('\nEnter your response : '))

            if m ==1:
                con = sqlite3.connect("VS Pro.db")
                cur = con.cursor()
                cur.execute(''' select Name from Teacher where TID = ?;''',(k,))
                q = cur.fetchall()
                print('''_________________________________________________________________________________________________________________________
_________________________________________________________________________________________________________________________''')
                S = input('\nEnter the name of student or the name of class if sending to everyone :')
                g = input('Enter the date :')
                print('\nMessage has been sent')
                cur.execute('''Insert into Messages values(?,?,?);''',(q[0][0],S,g))
                con.commit()
                con.close()
                print('\nTo go to menu - enter any no.')
                while True:
                    try:
                        v = int(input('\nEnter the response :'))
                        break
                    except:
                        print('Invalid Input')

                if v == 4:
                    d = 2
                d = 1

            if m == 2:
                con = sqlite3.connect("VS Pro.db")
                cur = con.cursor()
                cur.execute(''' select Name from Teacher where TID = ?;''',(k,))
                q = cur.fetchall()
                h = cur.execute('''select * from Messages where Name = ?;''',q[0])
                l = h.fetchall()
                print('''_________________________________________________________________________________________________________________________
\t\t\t\t\t\tHISTORY
_________________________________________________________________________________________________________________________''')

                if l == [] :
                    print('\n\t\t\t\t\tNO MESSAGE HISTORY')

                else :
                    for i in l:
                        print('\nName -',i[0],'\nSent to -',i[1],'\nDate -',i[2])
                    print('\nTo go to menu - enter any no.')
                    while True:
                        try:
                            v = int(input('\nEnter the response :'))
                            break
                        except:
                            print('Invalid Input')

                    if v == 4:
                        d = 2
                    d = 1

            if m == 3:
                return
        except:
            print('Invalid Input')

#************************************************************************************************************************************************************
#************************************************************************************************************************************************************

def homepage():
    print(''' ________________________________________________________________________________________________________________________''')
    print('''To go to Profile - Press 1
To go to Class List - Press 2
To go to Messages - Press 3
To go to Managment's Note - Press 4
To go to Attendance - Press 5
To go to Marks - Press 6
To log out - Press 7''')

#************************************************************************************************************************************************************
#************************************************************************************************************************************************************

def main_menu():
    print('''\n\t\t\t\t\tLogin as a Teacher : press 2
            \t\t\t\t\tRegister as a Teacher : press 3
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
    
#************************************************************************************************************************************************************
#************************************************************************************************************************************************************

def teacher():
    global t
    con = sqlite3.connect("VS Pro.db")
    cur = con.cursor()

##    cur.execute('''insert into Attendance values('Sakshi Yadav','P',NULL);''')
##    cur.execute('''insert into Attendance values('Sakshi Yadav',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Sakshi Yadav','P',NULL);''')
##    cur.execute('''insert into Attendance values('Sakshi Yadav',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Sakshi Yadav','P',NULL);''')
##    cur.execute('''insert into Attendance values('Sakshi Yadav','P',NULL);''')
##    cur.execute('''insert into Attendance values('Sakshi Yadav',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Sakshi Yadav',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Sakshi Yadav','P',NULL);''')
##    cur.execute('''insert into Attendance values('Sakshi Yadav','P',NULL);''')
##    cur.execute('''insert into Attendance values('Sakshi Yadav','P',NULL);''')
##    cur.execute('''insert into Attendance values('Roopam Bisht','P',NULL);''')
##    cur.execute('''insert into Attendance values('Roopam Bisht','P',NULL);''')
##    cur.execute('''insert into Attendance values('Roopam Bisht','P',NULL);''')
##    cur.execute('''insert into Attendance values('Roopam Bisht','P',NULL);''')
##    cur.execute('''insert into Attendance values('Roopam Bisht','P',NULL);''')
##    cur.execute('''insert into Attendance values('Roopam Bisht','P',NULL);''')
##    cur.execute('''insert into Attendance values('Deepika Chauhan',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Deepika Chauhan',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Deepika Chauhan',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Deepika Chauhan',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Deepika Chauhan',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Bhakti Biswas',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Bhakti Biswas',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Bhakti Biswas','P',NULL);''')
##    cur.execute('''insert into Attendance values('Bhakti Biswas','P',NULL);''')
##    cur.execute('''insert into Attendance values('Bhakti Biswas',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Bhakti Biswas','P',NULL);''')
##    cur.execute('''insert into Attendance values('Bhakti Biswas',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Tina Sharma','P',NULL);''')
##    cur.execute('''insert into Attendance values('Tina Sharma','P',NULL);''')
##    cur.execute('''insert into Attendance values('Tina Sharma','P',NULL);''')
##    cur.execute('''insert into Attendance values('Tina Sharma','P',NULL);''')
##    cur.execute('''insert into Attendance values('Tina Sharma',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Tina Sharma',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Tina Sharma',NULL,'A');''')
##    cur.execute('''insert into Attendance values('Tina Sharma',NULL,'A');''')
    
##    print(x)
##    cur.execute('''Insert into Class_List values('Ankita Sharma',4);''')
##    cur.execute('''Insert into Class_List values('Ankita Sharma',5);''')
##    cur.execute('''Insert into Class_List values('Ankita Sharma',6);''')
##    cur.execute('''Insert into Class_List values('Ankita Sharma',8);''')
##    cur.execute('''Insert into Class_List values('Sneha Jiaswal',5);''')
##    cur.execute('''Insert into Class_List values('Sneha Jiaswal',6);''')
##    cur.execute('''Insert into Class_List values('Deepika Sammal',2);''')
##    cur.execute('''Insert into Class_List values('Deepika Sammal',5);''')
##    cur.execute('''Insert into Class_List values('Deepika Sammal',1);''')

    cur.execute('''select * from Teacher;''')
    x = cur.fetchall()
    t = x[-1][0]
    n= input('Name =')
    while True:
        try:
            c = int(input('Enter the contact no:'))
            break
        except:
            print('Invalid Input')
    e = input('Enter the House in which you are:')
    f = input('Enter the Class of which you are class teacher, if not enter None:')
    g = input('Enter your designation:')
    while True:
        try:
            p = int(input('Enter the no. of classes you teach:'))
            break
        except:
            print('Invalid Input')
    t+=1
    cur.execute('''Insert into Teacher values(?,?,?,?,?,?);''',(t,n,c,e,f,g))
    for i in range(p):

         if i == 0:
             while True:
                 try:
                    h = int(input("Enter the class you teach:"))
                    cur.execute('''Insert into Class_List values(?,?);''',(n,h))
                    break
                 except:
                    print('Invalid Input')

         else:
             while True:
                 try:
                     h = int(input("Enter the next class you teach:"))
                     cur.execute('''Insert into Class_List values(?,?);''',(n,h))
                     break
                 except:
                     print('Invalid Input')
    con.commit()
    con.close()

##    cur.execute('''Create table Attendance
##( Name varchar(50) ,
##Present varchar(10) ,
##Absent varchar(10) );''')
##    cur.execute('''Create table Teacher
##(TID int Primary Key ,
##Name varchar(50),
##Contact_no int ,
##House varchar(20),
##Class varchar(10) ,
##Designation varchar(40));''')
##    cur.execute('''Create table Class_List
##(Name varchar(50),
##Class int);''')
##    cur.execute('''Create table Messages
##( Name varchar(50) ,
##Sent_to varchar(20) ,
##Date date);''')
     
##    cur.execute('''delete from Class_List where Name = 'Himanshi K';''')
##    cur.execute('''delete from Teacher where Name = 'Himanshi K';''')
##    cur.execute('''Insert into Teacher values(101,'Ankita Sharma',9012668921,'Green','2','TGT Computer Science');''')
##    cur.execute('''Insert into Teacher values(102,'Sneha Jaiswal',4780238826,'Red','2','TGT Economics');''')
##    cur.execute('''Insert into Teacher values(103,'Deepika Sammal',7017622435,'Blue','10','TGT Sanskrit' );''')
##    cur.execute(''' select * from Teacher;''')
##    a = cur.fetchall()
##    for i in a:
##        print(i)

##teacher()

#************************************************************************************************************************************************************
#************************************************************************************************************************************************************

def Class(n) :
    count = 1
    con = sqlite3.connect("VS Pro.db")
    cur = con.cursor()
    cur.execute(''' select Name from Teacher where TID = ?;''',(n,))
    q = cur.fetchall()
    e = cur.execute('''select * from Class_List where Name = ?;''',q[0])
    f = e.fetchall()

    while True:
        print('''_________________________________________________________________________________________________________________________
\t\t\t\t\t\tCLASS LIST
_________________________________________________________________________________________________________________________''')
        print()
        for i in f:
            print(count,'.',i[1],'th class',',  enter -',count)
            count += 1
        count = 1
        print('''To go to home page - enter 14''')
        while True:
            try:
                v = int(input("\nEnter your response:"))
                break
            except:
                print('Invalid Input')

        if v == 14:
            return

        elif v != 14:
            o = 1
            while o == 1:
                print('''_________________________________________________________________________________________________________________________
\t\t\t\t\t\tSTUDENTS
_________________________________________________________________________________________________________________________''')
                print('''\nStudents in the class:
1. Sakshi Yadav
2. Roopam Bisht
3. Bhakti Biswas
4. Deepika Chauhan
5. Tina Sharma''')
                print('''\nTo see student detail - enter the name of student
To see classes again - enter 9''')
                while True:
                    try:
                        n = input('\nEnter the response :')
                        break
                    except:
                        print('Invalid Input')

                if n == '9':
                    break
                else :
                    Details(n)
                    print('\nTo go to student list - enter any no.')
                    while True:
                        try:
                            d = int(input('\nEnter the response :'))
                            break
                        except:
                            print('Invalid Input')
                    if d :
                        o = 2
                    o = 1
    con.commit()
    con.close()

#************************************************************************************************************************************************************
#************************************************************************************************************************************************************
        
def Note() :
    print('''_________________________________________________________________________________________________________________________
\t\t\tChairman's Message -:
_________________________________________________________________________________________________________________________
Columbus Public School was founded by the Hon’ble Chairman Shri Bali Ram Khera Ji in the year 1997 with an objective to provide quality education. With the belief that character building and personality development are the core aspects of all learning process, the school aims at moulding the students into good citizens, making them responsible individuals and grooming them into complete men fit to compete in the present world scenario.

Over these twenty four years since establishment, with the blessings of the almighty, the school has engraved a place for itself as one of the leading educational institutes of the town. Besides academic excellence and intellectual development, the school endeavours to help each child discover and develop one’s innate talents and abilities. It seeks to instil in the children proper habits, positive attitude, moral values commensurate with Indian culture, freedom of mind and scientific temperament.

The school has been constantly achieving excellent board results. Also, the children have won many laurels in co-scholastic and sports activities at the city, state and national level. The endless achievements of 24 years can never be penned down on this single page but the glory of the school itself has a million words to say. The tremendous pace at which the school has grown speaks a lot about the never ending saga of success.

Keeping pace with development in technology, the school has now taken foresighted steps by inculcating technology in education. The school has tied-up with Helix Technologies Ltd. to set-up smart classrooms and provide e-learning modules in order to make the delivery of lessons fascinating and enhance the learning experience of students. Also, the school has also entered into an accord with M/s Franciscan Solutions Pvt. Ltd. to offer e-care services in the school so as to encourage effective communication among all stakeholders including the child’s parents. Also, it helps parents to continuously monitor the child’s progress; resulting in effective monitoring of the child’s developments.

While on one hand the school management is committed to making all amenities available to the school; the Principal with his team of diligent, dedicated and sincere teachers is all set to take the school to greater heights and set exemplary standards in school education.

Kesar Das Khera
(Chairman) \n''')
    print('''________________________________________________________________________________________________________________________
\t\t\tManaging Director's Message -:
________________________________________________________________________________________________________________________
Columbus Public School has a rich tradition of academic excellence, fostering a nurturing environment where students can thrive both academically and personally. Our commitment to providing a well-rounded education is unwavering, and we take pride in our ability to prepare students for the challenges and opportunities of the future.

In today's rapidly evolving world, education plays a pivotal role in shaping the leaders of tomorrow. At Columbus Public School, we understand the importance of equipping our students with not only the knowledge and skills necessary for academic success but also the values and character traits that will guide them in becoming responsible and compassionate individuals.

Our dedicated team of educators, administrators, and support staff is committed to creating a dynamic and engaging learning environment. We embrace innovative teaching methodologies, leverage cutting-edge technology, and continuously strive for excellence in all aspects of education. Our goal is to empower students to think critically, solve problems creatively, and become lifelong learners.

As we look ahead, we are excited about the initiatives and programs that will enhance the educational experience at Columbus Public School. From curriculum enhancements to extracurricular activities, we are focused on providing a holistic education that prepares students for a globalized and interconnected world.

I encourage parents, guardians, and the entire community to actively participate in our school's journey. Your involvement and support are integral to the success of our students. Together, we can create an environment where every child can reach their full potential and excel in their academic and personal pursuits.

In closing, I want to express my gratitude for the trust you place in Columbus Public School. We are committed to fostering an educational environment that instills a love for learning, promotes diversity and inclusion, and prepares students for a bright and successful future.

Mr. Manoj Kumar Khera
( Managing Director) \n''')
    print('''________________________________________________________________________________________________________________________
\t\t\tPrincipal's Message -:
________________________________________________________________________________________________________________________
“If we want to reach real peace in this world, we should start educating children”
Mahatma Gandhi

The objective of Columbus Public School is not only to widen the mental horizons of the students, but also to build their characters and enhance their aesthetic faculties, to teach them tolerance and broadmindedness so that they become cultured, self-reliant, confident and worthy citizens of a new modern world and are well equipped to meet the challenges of the 21 st century skills.

Our curriculum comprises not only the academic subjects but it also includes manifold activities like debating, elocutions, dramatics, hobbies, camps, treks, and of course, games and sports whose educational value is undisputable. Thus in our schools, the teaching of subjects is used to promote the child’s power of observation, deduction, critical analysis, originality, his ability to pass independent value judgment, to express individual opinion and the implementation of the facts taught in the class-room to real life situations.

Our endeavour is to facilitate the all-round development of the personality which stands in sharp contrast to the lop-sided emphasis on cramming and reproducing which characterizes the general run of the mill schools. By far the most vital function of our school is to inculcate right value systems and positive, healthy attitudes.

Keeping the above mentioned points in mind, teachers in our school are appointed not merely on the basis of their academic qualifications but by their ability to relate to the children so as to bear a strong moral influence on their lives and on the basis of their devotion to their work and their understanding of the public school system, as they are expected to contribute to all aspects of the student’s development. We in our school, try never to lose sight of the fact that, ‘an average teacher tells, a good teacher explains, a superior teacher demonstrates and an exceptional teacher inspires.’ In the class-room, we avoid spoon-feeding, we encourage the child to develop the initiative to gather information, comprehend it, assimilate it and apply it. As such, we try not merely to teach, but to educate in the true sense of the word. Besides scholastic pursuits, we identify individual talents and provide a congenial environment to promote them.

Here, all barriers of caste, community, and sect are demolished; no religious dogmas and political philosophies are advocated and the personality of the child is allowed to grow and flower in a free, friendly, unprejudiced, liberal, progressive and humanistic environment.

Manoj Kumar
(Principal) \n''')
    print('''________________________________________________________________________________________________________________________
\t\t\tVice Principal's Message -:
________________________________________________________________________________________________________________________
Excellence is the gradual result of always striving to do better -Pat Riley

The above quote perfectly delineates today’s fast-changing educational setup, collaborated with digital media, and we at Columbus, aim to provide the best education to our students to become valuable global citizens of tomorrow and excel in every aspect of life including knowledge, attitude, skills, and behaviour which are necessary tools to thrive in today's interconnected world. At the same time, we constantly endeavour to instil moral and spiritual values in our students to help them achieve academic excellence along with critical thinking capabilities. We focus on the holistic development of our students, so that they can differentiate good from bad, right from wrong, and grab opportunities that help them to reach the epitome of success in their chosen fields.

Just like a finger cannot pick up a pebble, in the same way the management and the staff works in collaboration and mutual support, to leave no stone unturned to ensure that the students soar higher in the skies of learning. One of the most important pillar in building a prosperous nation is Education which ignites the young minds and helps in channelizing their own path as a waterfall does through rocks.

We have a team of highly qualified and experienced faculty members who display boundless energy and intense commitment towards children to help them to achieve new heights in the field of academic, and co-curricular activities and establish them in the fast-paced world. We believe in a joyful learning system wherein; each child is encouraged to participate wholeheartedly. We believe in empowering our children in such a manner that they are able to take responsibilities on their shoulders, of a meaningful and value-based society.

I express my happiness on my association with this renowned school in and around the city along with its hardworking and caring staff.

GLORIA IN EXCELSIS.

Dr. Kamesh Mittal
Vice Principal
________________________________________________________________________________________________________________________''')


#____________________________________________________________________________________________________________________________________
#****************************************************MAIN CODE********************************************************************************************************
#______________________________________________________________________________________________________________________________________________

print(''' ************************************************************************************************************************
            \t\t\t\t\t    ___________________________________  
            \t\t\t\t\t ---------------------------------------------------         
            \t\t\t\t\t | |               Welcome to TMS                 | |
            \t\t\t\t\t ---------------------------------------------------
            \t\t\t\t\t   ___________________________________

*************************************************************************************************************************''')

z = 1
while z == 1:
    main_menu()
    try:
        a = int(input('\t\t\t\t\tEnter your response : '))
        while a != 2 and a != 3:
            main_menu()
            a = int(input('\t\t\t\t\tEnter your response : '))
        d = []

#***********************************************Logged in as a TEACHER******************************************************************88
#______________________________________________________________________________________________________________________________________-

        if a == 2:
            while True:
                try:
                    T = int(input('\nEnter your TID ='))
                    break
                except:
                    print('Invalid Input')
            con = sqlite3.connect("VS Pro.db")
            cur = con.cursor()
            cur.execute(''' select * from Teacher where TID = ?;''',(T,))
            q = cur.fetchall()
            if q == []:
                print("user do not exist")
            else :
                print('\t\t\t\t\t!! Successfully Logged In !!')
                x = 1
                while x == 1:
                    homepage()
                    while True:
                        try:
                            b= int(input('\t\t\t\t\tEnter your response :'))
                            break
                        except:
                            print('Invalid Input')

                    if b == 6:
                        Entry(T)
                        print('''\nTo log out - enter 1
To go to home page - enter 2''')
                        while True:
                            try:
                                a = int(input('\nEnter your response:'))
                                break
                            except:
                                print('Invalid Input')
                        if a == 1:
                            x = 2
                        elif a == 2:
                            z = 2
                        z = 1

                    if b == 7:
                        x = 2

                    if b == 5:
                        Att(T)
                        print('''\nTo log out - enter 1
To go to home page - enter 2''')
                        while True:
                            try:
                                a = int(input('\nEnter your response:'))
                                break
                            except:
                                print('Invalid Input')
                        if a == 1:
                            x = 2
                        elif a == 2:
                            z = 2
                        z = 1

                    if b == 3:
                        Message(T)
                        print('''\nTo log out - enter 1
To go to home page - enter 2''')
                        while True:
                            try:
                                a = int(input('\nEnter your response:'))
                                break
                            except:
                                print('Invalid Input')
                        if a == 1:
                            x = 2
                        elif a == 2:
                            z = 2
                        z = 1

                    if b == 2:
                       Class(T)
                       print('''\nTo log out - enter 1
To go to home page - enter 2''')
                       while True:
                           try:
                               a = int(input('\nEnter your response:'))
                               break
                           except:
                               print('Invalid Input')
                       if a == 1:
                           x = 2
                       elif a == 2:
                           z = 2
                       z = 1

                    if b== 1:
                        cur.execute(''' select * from Teacher where TID = ?;''',(T,))
                        q = cur.fetchall()
                        print('''_________________________________________________________________________________________________________________________
\t\t\t\t\t\tPROFILE
_________________________________________________________________________________________________________________________''')
                        for i in q:
                            print('Tid -\t\t',i[0],'\n','Name -\t\t',i[1],'\n','Contact no. -\t',i[2],'\n','House -\t\t',i[3],'\n','Class Teacher -\t',i[4],'\n','Designation -\t',i[5])
                        print('''\nTo log out - enter 1
To go to home page - enter 2''')
                        while True:
                            try:
                                a = int(input('\nEnter your response:'))
                                break
                            except:
                                print('Invalid Input')
                        if a == 1:
                            x = 2
                        elif a == 2:
                            z = 2
                        z = 1

                    if b == 4 :
                        print('''________________________________________________________________________________________________________________________
\t\t\t\t\tManagment's Note --:''')
                        Note()
                        print('''\nTo log out - enter 1
To go to home page - enter 2''')
                        while True:
                            try:
                                a = int(input('\nEnter your response:'))
                                break
                            except:
                                print('Invalid Input')
                        if a == 1:
                            x = 2
                        elif a == 2:
                            z = 2
                        z = 1
            con.commit()
            con.close()

#**************************************************Register as a TEACHER*********************************************************************************************8
#___________________________________________________________________________________________________________________________________

        if a == 3 :
            teacher()
            print("\t\t\t\t\tYou have been successfully registered")
            x = 1
            while x == 1:
                homepage()
                while True:
                    try:
                        b= int(input('\t\t\t\t\tEnter your response :'))
                        break
                    except:
                        print('Invalid Input')

                if b == 6:
                    Entry(t)
                    print('''\nTo log out - enter 1
To go to home page - enter 2''')
                    while True:
                        try:
                            a = int(input('\nEnter your response:'))
                            break
                        except:
                            print('Invalid Input')
                    if a == 1:
                        x = 2
                    elif a == 2:
                        z = 2
                    z = 1

                if b == 7:
                    x = 2

                if b == 5:
                    Att(t)
                    print('''\nTo log out - enter 1
To go to home page - enter 2''')
                    while True:
                        try:
                            a = int(input('\nEnter your response:'))
                            break
                        except:
                            print('Invalid Input')
                    if a == 1:
                        x = 2
                    elif a == 2:
                        z = 2
                    z = 1

                if b == 3:
                    Message(t)
                    print('''\nTo log out - enter 1
To go to home page - enter 2''')
                    while True:
                        try:
                            a = int(input('\nEnter your response:'))
                            break
                        except:
                            print('Invalid Input')
                    if a == 1:
                        x = 2
                    elif a == 2:
                        z = 2
                    z = 1

                if b == 2:
                    Class(t)
                    print('''\nTo log out - enter 1
To go to home page - enter 2''')
                    while True:
                        try:
                            a = int(input('\nEnter your response:'))
                            break
                        except:
                            print('Invalid Input')
                    if a == 1:
                        x = 2
                    elif a == 2:
                        z = 2
                    z = 1

                if b== 1:
                    con = sqlite3.connect("VS Pro.db")
                    cur = con.cursor()
                    cur.execute(''' select * from Teacher where TID = ?;''',(t,))
                    q = cur.fetchall()
                    for i in q:
                        print('Tid -\t\t',i[0],'\n','Name -\t\t',i[1],'\n','Contact no. -\t',i[2],'\n','House -\t\t',i[3],'\n','Class Teacher -\t',i[4],'\n','Designation -\t',i[5])
                    con.commit()
                    con.close()
                    print('''\nTo log out - enter 1
To go to home page - enter 2''')
                    while True:
                        try:
                            a = int(input('\nEnter your response:'))
                            break
                        except:
                            print('Invalid Input')
                    if a == 1:
                        x = 2
                    elif a == 2:
                        z = 2
                    z = 1

                if b == 4 :
                    print('''________________________________________________________________________________________________________________________
\t\t\t\t\tManagment's Note --:''')
                    Note()
                    print('''\nTo log out - enter 1
To go to home page - enter 2''')
                    while True:
                        try:
                            a = int(input('\nEnter your response:'))
                            break
                        except:
                            print('Invalid Input')
                    if a == 1:
                        x = 2
                    elif a == 2:
                        z = 2
                    z = 1
    except:
        print('Invalid Input')

#_____________________________________________________________________________________________________________________________________________________
#****************************************************END OF CODE*************************************************************************
#______________________________________________________________________________________________________________________________________
