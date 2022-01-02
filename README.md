# Elice's Rabbit Coding
#### Video Demo:  [Elice Online Coding Learning Platfrom](https://youtu.be/B46ovGRakpA)
#### Description: This is a sample description. 
I am a computer science minoring in Psychology from South Korea(SKKU/SNU), and now in Switzerland for an exchange year. 
I state myself as a programming "nerd", but it depends. 

Elice Coding Platform is an online CS Education Platform to Understand How Students Learn Programming.

It is a program which is helping students to find and match the right tutors with the right students. 
We have our own IDE which is Elice IDE which compiles in the system. 
The course on making games with Python has been opened.
In the meantime, many comments have been made that it would be good to have a course related to GUI programming, and we actively reflected the opinions and created a new course using the PyGame library.
It is currently in Korean, and most curriculum is based on Python, but C curriculum is under development, and I am using cs50.edu Edx contents as a supplementary tool to guide students in Introduction to Computer Science. 

We have yet develped courses and curriculums from Python, C++, Javascript, Web Programming, Arduino, Data Structures and Algorithms, Artificial Intelligence so far. 

It has been tested / educated to Korean university students and students from Russia, Canada, US, Netherlands, Germany and so on. 
So far, around 
but now C20 million learners in the platform, and personally educated 30-40 students in 1:1 class uniform. 
You can create your own course.


For teachers, teacher dashboard is unlocked, where they can create a homework and see student's which submitted homework. When accessing the homework, teacher can download the submitted file and then write a review and grade it.

### Routing

Each route checks if the user is authenticated. It means if correct mail and password were supplied and what role it has. So for example a teacher cannot enter /students/homeworks/1 route. The same is for student, he cannot enter teacher dashboard route.

### Sessions

The webpage uses sessions to confirm that user is registered. Once the user logins, his credentials are checked with bcrypt and Passport JS library. Once everything passes a session is created (serialized and deserialized) and stored in the cookies. The server attaches user to subsequent requests, so the back-end can easily access the details, like roles: student, teacher.

### Database

Database stores all users, homework, student submissions. The tables, like student submissions uses foreign keys to relate users to submitted homework. Moreover, homework table uses foreign keys to relate the homework to a teacher.

## Current Improvements

As all applications this one can also be improved. Possible improvements:

- Have administrator account which confirms user identity, so that student could not register as a teacher
- Ability to change account details
- Have a way for teacher to upload videos, quizzes and contents to explain the assignment
- Notificaitons to email about new homeworks or submissions

## How to launch application

1. Check that you have Android version 8+
2. Clone the code: `엘리스 ELICE 코딩 교실_v1.1.7_apkpure.com`
3. Run command prompt in the folder and run `npm install` to install all dependencies
4. Once installed run command `npm start`
5. In your browser go to `https://academy.elice.io/`
6. You are ready to go!


You can take part as a educator if you are enrolled in a computer science/software engineering degree of education. 
If you are interested, I can ping you or help you as well. 


For more inquiries, please contact <pinkgrape0691@gmail.com>
<https://www.elice.io>
<pinkgrape0691@gmail.com>

