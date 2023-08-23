create database RecommendationDB

use RecommendationDB

create table Users(Userno int primary key identity,UserId varchar(50),Upassword varchar(50),Name varchar(50))

select * from Users




create table  Actors(ActorsId int primary key identity, ActorName varchar(50))

insert into Actors values('Prabhas')
insert into Actors values('Rana Daggubati')
insert into Actors values('Ramya Krishna')
insert into Actors values('Sathyaraj')
insert into Actors values('Anushka Shetty')

insert into Actors values('Yash')
insert into Actors values('Sanjay Dutt')
insert into Actors values('Raveena Tandon')
insert into Actors values('Srinidhi Shetty')
insert into Actors values('Prakash Raj')

insert into Actors values('Aamir Khan')
insert into Actors values('Sakshi Tanwar')
insert into Actors values('Fatima Sana Shaikh')
insert into Actors values('Sanya Malhotra')

insert into Actors values('Ranbir Kapoor')
insert into Actors values('Paresh Rawal')
insert into Actors values('Vicky Kaushal')
insert into Actors values('Anushka Sharma')
insert into Actors values('Sonam Kapoor')

insert into Actors values('Sushant Singh Rajput')
insert into Actors values('Boman Irani')
insert into Actors values('Saurabh Shukla')

insert into Actors values('Salman Khan')
insert into Actors values('Katrina Kaif')

insert into Actors values('Kareena Kapoor Khan')
insert into Actors values('Nawazuddin Siddiqui')

insert into Actors values('Hrithik Roshan')
insert into Actors values('Tiger Shroff')
insert into Actors values('Vaani Kapoor')

insert into Actors values('Deepika Padukone')
insert into Actors values('Shahid Kapoor')
insert into Actors values('Ranveer Singh')

insert into Actors values('Kiara Advani')

insert into Actors values('Ajay Devgn')
insert into Actors values('Saif Ali Khan')
insert into Actors values('Kajol')

insert into Actors values('Abhishek Bachchan')
insert into Actors values('Jackie Shroff')
insert into Actors values('Uday Chopra')

insert into Actors values('N. T. Rama Rao Jr.')
insert into Actors values('Ram Charan')
insert into Actors values('Alia Bhatt')

insert into Actors values('Mithun Chakraborty')
insert into Actors values('Anupam Kher')
insert into Actors values('Darshan Kumar')
insert into Actors values('Pallavi Joshi')

insert into Actors values('Yami Gautam')

insert into Actors values('Sonu Sood')
insert into Actors values('Sara Ali Khan')

insert into Actors values('Randeep Hooda')
insert into Actors values('Jacqueline Fernandez')

insert into Actors values('Vivek Oberoi')
insert into Actors values('Priyanka Chopra')
insert into Actors values('Kangana Ranaut')

insert into Actors values('Shah Rukh Khan')

insert into Actors values('Disha Patani')
insert into Actors values('Sunil Grover')

insert into Actors values('Akshay Kumar')
insert into Actors values('Riteish Deshmukh')
insert into Actors values('Bobby Deol')
insert into Actors values('Kriti Sanon')
insert into Actors values('Pooja Hegde')

insert into Actors values('Parineeti Chopra')
insert into Actors values('Arshad Warsi')
insert into Actors values('Tushar Kapoor')
insert into Actors values('Shreyas Talpade')
insert into Actors values('Johny Lever')

insert into Actors values('Diljit Dosanjh')

insert into Actors values('Vidya Balan')
insert into Actors values('Sonakshi Sinha')
insert into Actors values('Taapsee Pannu')
insert into Actors values('Sharman Joshi')

insert into Actors values('R. Madhavan')
insert into Actors values('Omi Vaidya')

insert into Actors values('Kalki Koechlin')
insert into Actors values('Aditya Roy Kapur')

insert into Actors values('Anil Kapoor')
insert into Actors values('Madhuri Dixit')

insert into Actors values('Shraddha Kapoor')
insert into Actors values('Varun Sharma')

insert into Actors values('Varun Dhawan')

insert into Actors values('Siddhant Chaturvedi')
insert into Actors values('Ayushmann Khurrana')

insert into Actors values('Robert Downey Jr.')
insert into Actors values('Chris Evans')
insert into Actors values('Mark Ruffalo')
insert into Actors values('Scarlett Johansson')
insert into Actors values('Chris Hemsworth')
insert into Actors values('Brie Larson')

insert into Actors values('Dakota Johnson')
insert into Actors values('Jamie Dornan')

insert into Actors values('Matthew McConaughey')

insert into Actors values('Bae Doona')
insert into Actors values('Gong Yoo')
insert into Actors values('Lee Joon')

insert into Actors values('John Abraham')

insert into Actors values('Sidharth Malhotra')

insert into Actors values('Nargis Fakhri')

insert into Actors values('Kartik Aaryan')
insert into Actors values('Nushrat Bharucha')
insert into Actors values('Sunny Singh')

insert into Actors values('Vera Farmiga')
insert into Actors values('Patrick Wilson')
insert into Actors values('Lili Taylor')

insert into Actors values('Franka Potente')

insert into Actors values('Annabelle Wallis')
insert into Actors values('Ward Horton')

insert into Actors values('Stephanie Sigman')
insert into Actors values('Talitha Bateman')
insert into Actors values('Anthony LaPaglia')
insert into Actors values('Miranda Otto')

insert into Actors values('Madison Iseman')

insert into Actors values('Demi�n Bichir')
insert into Actors values('Taissa Farmiga')
insert into Actors values('Jonas Bloquet')

insert into Actors values('Park Ji-hu')
insert into Actors values('Yoon Chan-young')
insert into Actors values('Cho Yi-hyun')

insert into Actors values('Ammy Virk')
insert into Actors values('Sargun Mehta')
insert into Actors values('Nimrat Khaira')

insert into Actors values('Sonam Bajwa')

insert into Actors values('Neeru Bajwa')
insert into Actors values('Mandy Takhar')
insert into Actors values('Diljit Dosanjh')

insert into Actors values('Nina Dobrev')
insert into Actors values('Paul Wesley')
insert into Actors values('Ian Somerhalder')
insert into Actors values('Candice King')
insert into Actors values('Joseph Morgan')

insert into Actors values('Daniel Gillies')
insert into Actors values('Claire Holt')

insert into Actors values('Hailee Steinfeld')
insert into Actors values('Woody Harrelson')

select * from Actors



create table Directors(DirectorId int primary key identity , DirectorName varchar(50))

insert into Directors values('S. S. Rajamouli')
insert into Directors values('Prashanth Neel')
insert into Directors values('Nitesh Tiwari')
insert into Directors values('Rajkumar Hirani')
insert into Directors values('Ali Abbas Zafar')
insert into Directors values('Kabir Khan')
insert into Directors values('Siddharth Anand')
insert into Directors values('Sanjay Leela Bhansali')
insert into Directors values('Sandeep Reddy Vanga')
insert into Directors values('Om Raut')
insert into Directors values('Vijay Krishna Acharya')
insert into Directors values('Vivek Agnihotri')
insert into Directors values('Aditya Dhar')
insert into Directors values('Rohit Shetty')
insert into Directors values('Sajid Nadiadwala')
insert into Directors values('Rakesh Roshan')
insert into Directors values('Sajid Khan')
insert into Directors values('Sooraj R. Barjatya')
insert into Directors values('Raj Mehta')
insert into Directors values('Jagan Shakti')
insert into Directors values('Farah Khan')
insert into Directors values('Ayan Mukerji')
insert into Directors values('Rahul Dholakia')
insert into Directors values('Anurag Singh')
insert into Directors values('Indra Kumar')
insert into Directors values('Siddique')
insert into Directors values('Vikas Bahl')
insert into Directors values('Zoya Akhtar')
insert into Directors values('David Dhawan')
insert into Directors values('Amit Ravindrenath Sharma')
insert into Directors values('Neeraj Pandey')
insert into Directors values('Tinu Suresh Desai')
insert into Directors values('Meghna Gulzar')
insert into Directors values('Karan Malhotra')
insert into Directors values('Anthony Russo')
insert into Directors values('Sam Taylor-Johnson')
insert into Directors values('Christopher Nolan')
insert into Directors values('Choi Hang-yong')
insert into Directors values('Mohit Suri')
insert into Directors values('Rohit Dhawan')
insert into Directors values('Karan Johar')
insert into Directors values('Imtiaz Ali')
insert into Directors values('Luv Ranjan')
insert into Directors values('James Wan')
insert into Directors values('Michael Chaves')
insert into Directors values('John R. Leonetti')
insert into Directors values('David F. Sandberg')
insert into Directors values('Gary Dauberman')
insert into Directors values('Corin Hardy')
insert into Directors values('Lee Jae-kyoo')
insert into Directors values('Amarjit Singh Saron')
insert into Directors values('Simerjit Singh')
insert into Directors values('Rohit Jugraj')
insert into Directors values('Kevin Williamson')
insert into Directors values('Julie Plec')
insert into Directors values('Kelly Fremon Craig')

select * from Directors 

create table Movies(MovieId int primary key identity , MovieName varchar(50) , DirectorId int references Directors(DirectorId), Genre varchar(50),ImageName varchar(50))

insert into Movies values('Baahubali 2 The Conclusion',1,'Action','Bahubali2.jpg')
insert into Movies values('Baahubali: The Beginning',1,'Action','Bahubali1.jpg')
insert into Movies values('KGF Chapter 2',2,'Action','KGF2.jpg')
insert into Movies values('KGF Chapter 1',2,'Action','KGF1.jpg')
insert into Movies values('Dangal',3,'Sports,Bio-pic','Dangal.jpg')
insert into Movies values('Sanju',4,'Bio-pic','Sanju.jpg')
insert into Movies values('PK',4,'Sci-fi','PK.jpg')
insert into Movies values('Tiger Zinda Hai',5,'Action,Thriller','Tiger Zinda Hai.jpg')
insert into Movies values('Bajrangi Bhaijaan',6,'Comedy','Bajrangi Bhaijaan.jpg')
insert into Movies values('War',7,'Action,Thriller','War.jpg')
insert into Movies values('Padmaavat',8,'Romantic,History','Padmaavat.jpg')
insert into Movies values('Sultan',5,'Sports,Romantic','Sultan.jpg')
insert into Movies values('Kabir Singh',9,'Romantic','Kabir Singh.jpg')
insert into Movies values('Tanhaji',10,'Action','Tanhaji.jpg')
insert into Movies values('Dhoom 3',11,'Action,Thriller','Dhoom 3.jpg')
insert into Movies values('RRR',1,'Action','RRR.jpg')
insert into Movies values('The Kashmir Files',12,'History','The Kashmir Files.jpg')
insert into Movies values('URI The Surgical Strike',13,'History','URI The Surgical Strike.jpg')
insert into Movies values('Simmba',14,'Action,Comedy','Simmba.jpg')
insert into Movies values('Kick',15,'Action,Comedy','Kick.jpg')
insert into Movies values('Krrish 3',16,'Superhero','Krrish 3.jpg')
insert into Movies values('Chennai Express',14,'Romantic,Action,Comedy','Chennai Express.jpg')
insert into Movies values('Bharat',5,'Drama','Bharat.jpg')
insert into Movies values('Housefull 4',17,'Comedy','Housefull 4.jpg')
insert into Movies values('Prem Ratan Dhan Payo',18,'Romantic','Prem Ratan Dhan Payo.jpg')
insert into Movies values('Golmaal Again',14,'Comedy,Horror','Golmaal Again.jpg')
insert into Movies values('Good Newwz',19,'Comedy','Good Newwz.jpg')
insert into Movies values('Mission Mangal',20,'Sci-fi','Mission Mangal.jpg')
insert into Movies values('3 Idiots',4,'Comedy','3 Idiots.jpg')
insert into Movies values('Happy New Year',21,'Comedy,Action','Happy New Year.jpg')
insert into Movies values('Ek Tha Tiger',6,'Action,Thriller','Ek Tha Tiger.jpg')
insert into Movies values('Yeh Jawaani Hai Deewani',22,'Romantic,Comedy','Yeh Jawaani Hai Deewani.jpg')
insert into Movies values('Bajirao Mastani',8,'Romantic,History','Bajirao Mastani.jpg')
insert into Movies values('Bang Bang!',7,'Romantic,Action,Comedy','Bang Bang!.jpg')
insert into Movies values('Raees',23,'Action','Raees.jpg')
insert into Movies values('Kesari',24,'History','Kesari.jpg')
insert into Movies values('Total Dhamaal',25,'Comedy','Total Dhamaal.jpg')
insert into Movies values('Chhichhore',3,'Comedy,Romantic','Chhichhore.jpg')
insert into Movies values('Bodyguard',26,'Comedy,Romantic,Action','Bodyguard.jpg')
insert into Movies values('Dilwale',14,'Comedy,Romantic,Action','Dilwale.jpg')
insert into Movies values('Super 30',27,'Sci-fi,Bio-pic','Super 30.jpg')
insert into Movies values('Gully Boy',24,'Romantic,Musical','Gully Boy.jpg')
insert into Movies values('Judwaa 2',29,'Comedy,Romantic,Action','Judwaa 2.jpg')
insert into Movies values('Badhaai Ho',30,'Comedy,Romantic','Badhaai Ho.jpg')
insert into Movies values('M.S. Dhoni: The Untold Story',31,'Bio-pic,Romantic,Sports','M.S. Dhoni.jpg')
insert into Movies values('Rustom',32,'Action,Romantic','Rustom.jpg')
insert into Movies values('Raazi',33,'Action,Romantic,Thriller','Raazi.jpg')
insert into Movies values('Gangubai Kathiawadi',8,'Crime,Adult','Gangubai Kathiawadi.jpg')
insert into Movies values('Agneepath',34,'Action,Crime,Thriller','Agneepath.jpg')
insert into Movies values('Avengers End Game',35,'Action,Superhero','Avengers End Game.jpg')
insert into Movies values('Interstellar',37,'Sci-fi','Interstellar.jpg')
insert into Movies values('Fifty Shades of Darker',36,'Romantic,Adult','Fifty Shades of Darker.jpg')
insert into Movies values('Fifty Shades of Freed',36,'Romantic,Adult','Fifty Shades of Freed.jpg')
insert into Movies values('Fifty Shades of Grey',36,'Romantic,Adult','Fifty Shades of Grey.jpg')
insert into Movies values('The Silent Sea',38,'Sci-fi','The Silent Sea.jpg')
insert into Movies values('Aashiqui 2',39,'Romantic','Aashiqui 2.jpg')
insert into Movies values('Dishoom',40,'Romantic,Action,Thriller','Dishoom.jpg')
insert into Movies values('Student Of The Year',41,'Romantic,Action,Sports','Student Of The Year.jpg')
insert into Movies values('Rockstar',42,'Romantic,Action,Thriller,Musical','Rockstar.jpg')
insert into Movies values('Tees Maar Khan',21,'Romantic,Comedy,Thriller','Tees Maar Khan.jpg')
insert into Movies values('Sonu Ke Titu Ki Sweety',43,'Romantic,Drama,Comedy','Sonu Ke Titu Ki Sweety.jpg')
insert into Movies values('The Conjuring',44,'Horror','The Conjuring.jpg')
insert into Movies values('The Conjuring 2',44,'Horror','The Conjuring2.jpg')
insert into Movies values('The Conjuring 3',45,'Horror','The Conjuring 3.jpg')
insert into Movies values('Annabelle',46,'Horror','Annabelle.jpg')
insert into Movies values('Annabelle: Creation',47,'Horror','Annabelle2.jpg')
insert into Movies values('Annabelle Comes Home',48,'Horror','Annabelle3.jpg')
insert into Movies values('The Nun',49,'Horror','The Nun.jpg')
insert into Movies values('All of Us Are Dead',50,'Action,Thriller','All of Us Are Dead.jpg')
insert into Movies values('Saunkan Saunkne',51,'Comedy','Saunkan Saunkne.jpg')
insert into Movies values('Nikka Zaildar',52,'Comedy','Nikka Zaildar.jpg')
insert into Movies values('Nikka Zaildar 2',52,'Comedy','Nikka Zaildar2.jpg')
insert into Movies values('Nikka Zaildar 3',52,'Comedy','Nikka Zaildar3.jpg')
insert into Movies values('Sardaarji',53,'Comedy','Sardaarji.jpg')
insert into Movies values('Sardaarji 2',53,'Comedy','Sardaarji2.jpg')
insert into Movies values('Jatt & Juliet',24,'Comedy','Jatt & Juliet.jpg')
insert into Movies values('Jatt & Juliet 2',24,'Comedy','Jatt & Juliet2.jpg')
insert into Movies values('The Vampire Diaries',54,'Superhero,Action,Thriller','The Vampire Diaries.jpg')
insert into Movies values('The Originals',55,'Superhero,Action,Thriller','The Originals.jpg')
insert into Movies values('The Edge of Seventeen',56,'Drama','The Edge of Seventeen.jpg')


update Movies set MovieName = 'The Conjuring 2' where MovieId=63

select * from Movies



create table Casts(SerialNo int primary key identity , MovieId int references Movies(MovieId),ActorsId int references Actors(ActorsId))

insert into Casts values(1,1)
insert into Casts values(1,2)
insert into Casts values(1,3)
insert into Casts values(1,4)
insert into Casts values(1,5)

insert into Casts values(2,1)
insert into Casts values(2,2)
insert into Casts values(2,3)
insert into Casts values(2,4)
insert into Casts values(2,5)

insert into Casts values(3,6)
insert into Casts values(3,7)
insert into Casts values(3,8)
insert into Casts values(3,9)
insert into Casts values(3,10)

insert into Casts values(4,6)
insert into Casts values(4,9)

insert into Casts values(5,11)
insert into Casts values(5,12)
insert into Casts values(5,13)
insert into Casts values(5,14)

insert into Casts values(6,15)
insert into Casts values(6,16)
insert into Casts values(6,17)
insert into Casts values(6,18)
insert into Casts values(6,19)

insert into Casts values(7,11)
insert into Casts values(7,18)
insert into Casts values(7,20)
insert into Casts values(7,7)
insert into Casts values(7,21)
insert into Casts values(7,22)

insert into Casts values(8,23)
insert into Casts values(8,24)

insert into Casts values(9,23)
insert into Casts values(9,25)
insert into Casts values(9,26)

insert into Casts values(10,27)
insert into Casts values(10,28)
insert into Casts values(10,29)

insert into Casts values(11,30)
insert into Casts values(11,31)
insert into Casts values(11,32)

insert into Casts values(12,18)
insert into Casts values(12,23)

insert into Casts values(13,31)
insert into Casts values(13,33)

insert into Casts values(14,34)
insert into Casts values(14,35)
insert into Casts values(14,36)

insert into Casts values(15,38)
insert into Casts values(15,39)
insert into Casts values(15,37)
insert into Casts values(15,24)
insert into Casts values(15,11)

insert into Casts values(16,34)
insert into Casts values(16,40)
insert into Casts values(16,41)
insert into Casts values(16,42)

insert into Casts values(17,43)
insert into Casts values(17,44)
insert into Casts values(17,45)
insert into Casts values(17,46)

insert into Casts values(18,47)
insert into Casts values(18,17)
insert into Casts values(18,16)

insert into Casts values(19,48)
insert into Casts values(19,49)
insert into Casts values(19,32)

insert into Casts values(20,26)
insert into Casts values(20,23)
insert into Casts values(20,43)
insert into Casts values(20,50)
insert into Casts values(20,51)

insert into Casts values(21,53)
insert into Casts values(21,52)
insert into Casts values(21,54)
insert into Casts values(21,27)

insert into Casts values(22,55)
insert into Casts values(22,30)

insert into Casts values(23,56)
insert into Casts values(23,57)
insert into Casts values(23,38)
insert into Casts values(23,23)
insert into Casts values(23,24)

insert into Casts values(24,58)
insert into Casts values(24,59)
insert into Casts values(24,61)
insert into Casts values(24,62)
insert into Casts values(24,60)

insert into Casts values(25,23)
insert into Casts values(25,19)

insert into Casts values(26,63)
insert into Casts values(26,64)
insert into Casts values(26,65)
insert into Casts values(26,66)
insert into Casts values(26,34)
insert into Casts values(26,67)

insert into Casts values(27,68)
insert into Casts values(27,25)
insert into Casts values(27,58)
insert into Casts values(27,33)

insert into Casts values(28,69)
insert into Casts values(28,70)
insert into Casts values(28,71)
insert into Casts values(28,71)
insert into Casts values(28,58)

insert into Casts values(29,72)
insert into Casts values(29,73)
insert into Casts values(29,74)
insert into Casts values(29,11)
insert into Casts values(29,21)
insert into Casts values(29,25)

insert into Casts values(30,55)
insert into Casts values(30,37)
insert into Casts values(30,30)
insert into Casts values(30,48)
insert into Casts values(30,21)

insert into Casts values(31,23)
insert into Casts values(31,24)

insert into Casts values(32,75)
insert into Casts values(32,76)
insert into Casts values(32,30)
insert into Casts values(32,15)

insert into Casts values(33,30)
insert into Casts values(33,32)
insert into Casts values(33,53)

insert into Casts values(34,27)
insert into Casts values(34,24)

insert into Casts values(35,55)
insert into Casts values(35,26)

insert into Casts values(36,58)
insert into Casts values(36,63)

insert into Casts values(37,77)
insert into Casts values(37,78)
insert into Casts values(37,64)
insert into Casts values(37,67)
insert into Casts values(37,59)
insert into Casts values(37,34)
insert into Casts values(37,21)

insert into Casts values(38,79)
insert into Casts values(38,80)
insert into Casts values(38,20)

insert into Casts values(39,25)
insert into Casts values(39,23)

insert into Casts values(40,81)
insert into Casts values(40,61)
insert into Casts values(40,36)
insert into Casts values(40,55)

insert into Casts values(41,27)
insert into Casts values(41,26)

insert into Casts values(42,82)
insert into Casts values(42,42)
insert into Casts values(42,32)

insert into Casts values(43,81)
insert into Casts values(43,71)
insert into Casts values(43,51)


insert into Casts values(44,83)
insert into Casts values(44,14)

insert into Casts values(45,20)
insert into Casts values(45,33)
insert into Casts values(45,44)
insert into Casts values(45,56)

insert into Casts values(46,58)

insert into Casts values(47,17)
insert into Casts values(47,42)

insert into Casts values(48,42)

insert into Casts values(49,7)
insert into Casts values(49,27)
insert into Casts values(49,53)

insert into Casts values(50,84)
insert into Casts values(50,85)
insert into Casts values(50,86)
insert into Casts values(50,87)
insert into Casts values(50,88)
insert into Casts values(50,89)

insert into Casts values(51,92)

insert into Casts values(52,90)
insert into Casts values(52,91)

insert into Casts values(53,90)
insert into Casts values(53,91)

insert into Casts values(54,91)
insert into Casts values(54,90)

insert into Casts values(55,95)
insert into Casts values(55,94)
insert into Casts values(55,93)

insert into Casts values(56,76)
insert into Casts values(56,79)

insert into Casts values(57,51)
insert into Casts values(57,81)
insert into Casts values(57,96)

insert into Casts values(58,42)
insert into Casts values(58,81)
insert into Casts values(58,97)

insert into Casts values(59,15)
insert into Casts values(59,98)


insert into Casts values(60,24)
insert into Casts values(60,58)

insert into Casts values(61,99)
insert into Casts values(61,100)
insert into Casts values(61,101)

insert into Casts values(62,102)
insert into Casts values(62,103)
insert into Casts values(62,104)

insert into Casts values(63,102)
insert into Casts values(63,103)
insert into Casts values(63,104)
insert into Casts values(63,105)

insert into Casts values(64,102)
insert into Casts values(64,103)

insert into Casts values(65,106)
insert into Casts values(65,107)

insert into Casts values(66,108)
insert into Casts values(66,109)
insert into Casts values(66,110)
insert into Casts values(66,111)


insert into Casts values(67,102)
insert into Casts values(67,103)
insert into Casts values(67,112)


insert into Casts values(68,113)
insert into Casts values(68,114)
insert into Casts values(68,115)

insert into Casts values(69,116)
insert into Casts values(69,117)
insert into Casts values(69,118)

insert into Casts values(70,119)
insert into Casts values(70,120)
insert into Casts values(70,121)

insert into Casts values(71,119)
insert into Casts values(71,122)


insert into Casts values(72,119)
insert into Casts values(72,122)

insert into Casts values(73,119)
insert into Casts values(73,122)

insert into Casts values(74,123)
insert into Casts values(74,124)
insert into Casts values(74,125)

insert into Casts values(75,125)
insert into Casts values(75,122)

insert into Casts values(76,125)
insert into Casts values(76,123)

insert into Casts values(77,125)
insert into Casts values(77,123)

insert into Casts values(78,126)
insert into Casts values(78,127)
insert into Casts values(78,128)
insert into Casts values(78,129)
insert into Casts values(78,130)

insert into Casts values(79,132)
insert into Casts values(79,131)
insert into Casts values(79,130)

insert into Casts values(80,133)
insert into Casts values(80,134)


select * from Casts


create table Rating(RatingId int identity,MovieId int references Movies(MovieId),Userno int references Users(Userno),Rating float)

select * from Rating
