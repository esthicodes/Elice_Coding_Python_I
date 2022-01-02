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

The webpage uses sessions to confirm that user is registered. Once the user logins, his credentials are checked. Once everything passes a session is created (serialized and deserialized) and stored in the cookies. The server attaches user to subsequent requests, so the back-end can easily access the details, like roles: learner, educator.

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

# Learn to Program [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
#### Foundation in Web Development

The Internet is filled with an ever-expanding number of courses, books and guides for programmers of all skill levels to improve their skills. Unfortunately, these resources are either hard to find or of low quality.

This list aims to be a curated set of high quality educational resources. The availability of free content on the platform is highlighted along with the primary topics covered.

## Beginner

#### [Mozilla Webmaker](https://webmaker.org/)
**Free** community and toolset to learn to create web pages and apps\
*(HTML, CSS, JavaScript?)*

#### [Codecademy](https://www.codecademy.com/)
**Free** platform for learning to code in web technologies\
*(HTML, CSS, JavaScript, jQuery, Python, Ruby, Rails, PHP)*

#### [Khan Academy's Hour of Code](https://www.khanacademy.org/hourofcode)
**Free** interactive 1-hour course to learn the very basics of web development\
*(HTML, CSS, JavaScript, SQL)*

#### [UpLeveled Bootcamp Prep Course](https://learn.upleveled.io/)
**Freemium** platform for learning the basics of web development\
*(HTML, CSS, JavaScript, Node.js, Git, GitHub)*

#### [Treehouse](https://teamtreehouse.com/)
**Paid** platform for courses how to build websites & apps\
*(Web Design, Front End Web Development, Rails, iOS, Android, PHP)*

#### [Learn CSS Layout](https://learnlayout.com/)
**Free** tutorial for how to do layout with CSS\
*(CSS)*

#### Udemy [Programming](https://www.udemy.com/courses/search/?q=programming), [Development](https://www.udemy.com/courses/Development/)
**Freemium** marketplace of courses from third party providers. Quality may vary.\
*(HTML, CSS, JavaScript, Ruby, Rails, Python, iOS, Android)*

#### [Code Avengers](https://www.codeavengers.com/)
**Freemium** platform for basic web and app develoment courses\
*(HTML, CSS, JavaScript)*

#### [learn.shayhowe.com](https://learn.shayhowe.com/)
**Free** beginner to intermediate guides on web development\
*(HTML, CSS, JavaScript)*

#### [HTML Dog](https://www.htmldog.com/)
**Free** beginner and intermediate guides on web development\
*(HTML, CSS, JavaScript)*

#### Degreed [Web Development](https://degreed.com/learning/web%20development), [Programming](https://degreed.com/learning/programming)
**Mixed** directory of courses, videos and other learning resources for web development and programming. Quality may vary.\
*(HTML, CSS, JavaScript, AngularJS, Rails)*

#### [Platzi](https://courses.platzi.com/)
**Free** Platform for classes on Design, Marketing, Startup and Code. Learn the future of the web.\
*(RethinkDB, SailsJs, NodeJS, Git, Startup Class, etc)*

#### [Free Code Camp](https://www.freecodecamp.org/)
**Free** Learn to code and help nonprofits. An open source community of people who learn to code and help nonprofits.\
*(HTML, CSS, JavaScript, Databases, Git & GitHub, Node.js, React.js, D3.js)*

#### [Vertabelo Academy](https://academy.vertabelo.com/)
**Free** SQL courses with interactive exercises and quizzes\
*(SQL, database concepts)*

#### [GitHub Learning Lab](https://lab.github.com/)
**Free** Self paced, interactive projects to learn Git and GitHub. Created and maintained by GitHub's training team.\
*(Git, GitHub)*

#### [Grid Garden](https://cssgridgarden.com/)
**Free** game that teaches the CSS grid system created by [@thomaspark](https://github.com/thomaspark)\
*(CSS)*

#### [Hexlet.io](https://en.hexlet.io)
**Mixed** Self paced, interactive projects to learn JavaScript, C, Regular Expressions and computer science in general.  
*(JavaScript, Regular Expressions, Bash, computer science, Ansible)*

#### [Programming Historian](https://programminghistorian.org/en/lessons/)
**Free** Peer reviewed introductory courses for digital humanists.\
*(Python, R, Unity, QGIS, HTML, Regular Expressions)*

#### [Software Carpentry](https://software-carpentry.org/lessons/)
**Free** Foundational coding and data science skills for researchers.\
*(Python, R, OpenRefine, Unix Shell, Git)*

#### [Hyperskill by JetBrains Academy](https://hi.hyperskill.org/)
**Free** teaches programming in Java by creating small applications built step by step\
*(Java, OOP, Gradle, Maven, Spring Boot)*

## Intermediate

#### Khan Academy [Computer Programming](https://www.khanacademy.org/computing/computer-programming), [Computer Science](https://www.khanacademy.org/computing/computer-science)
**Free** intermediate to advanced courses on how to program drawings, animations, games and webpages and more advanced computer science topics\
*(HTML, CSS, JavaScript, algorithms, cryptography)*

#### [Udacity](https://www.udacity.com/)
**Free** platform for computer science and web development courses\
*(HTML, CSS, JavaScript, data science, Python, computer science topics)*

#### [Learn Python the Hard Way](https://learnpythonthehardway.org/book/)
**Paid** book and course for beginner through intermediate Python programming\
*(Python, object-oriented programming, web development)*

#### [Michael Hartl's Ruby on Rails Tutorial](https://www.railstutorial.org/book)
**Free** online book covering all stages of creating a Ruby on Rails application\
*(HTML, CSS, JavaScript, Ruby, Rails)*

#### Lynda.com [Developer](https://www.lynda.com/Developer-training-tutorials/50-0.html), [Web](https://www.lynda.com/Web-training-tutorials/88-0.html), [IT](https://www.lynda.com/IT-training-tutorials/2057-0.html)
**Freemium** platform for video courses on web development and intermediate programming\
*(HTML, CSS, JavaScript, programming fundamentals, system administration, ...)*

#### [Thinkful](https://www.thinkful.com/)
**Paid** platform for mentored web and mobile development courses from industry experts\
*(web development, frontend web development, AngularJS, Android, iOS)*

#### [exercism.io](https://exercism.io/)
**Free** crowdsourced mentorship platform of programming exercises and code reviews\
*(Clojure, CoffeeScript, C++, C#, Elixir, Erlang, F#, Go, Haskell, JavaScript, Common Lisp, Lua, Objective-C, OCaml, Perl 5, PL/SQL, Python, Ruby, Scala, Swift)*

#### [Stanford on iTunes U](https://itunes.stanford.edu/)
**Free** programming and mobile development courses on iTunes from Stanford University\
*(programming, startups, iOS)*

#### [PluralSight](https://www.pluralsight.com/tag/developer?pageSize=48&sort=popular)
**Paid** platform for web development courses\
*(JavaScript, AngularJS, Java)*

#### [CodeChef Problems](https://www.codechef.com/problems/easy/)
**Free** intermediate to advanced programming problems\
*(programming)*

#### [CodingBat](https://codingbat.com/)
**Free** practice problems in Python and Java\
*(Python, Java)*

#### [Codewars](https://www.codewars.com/)
**Free** code challenges. Compare your solution with those of others.\
*(JavaScript, CoffeeScript, Ruby, Python, Clojure, Haskell, Java)*

#### [CodinGame](https://www.codingame.com/)
**Free** Learn to code and game at the same time.\
*(C#, C++, Java, JavaScript, Python, Bash, C, Clojure, Dart, F#, Go, Groovy, Haskell, Lua, ObjectiveC, Pascal, Perl, PHP, Ruby, Rust, Scala, Swift, VB.NET)*

#### [1 Million Women To Tech Summer of Code](https://github.com/1millionwomentotech/toolkitten/tree/master/summer-of-code)
**Free** programming course material for beginner, intermediate and advanced levels\
*(Python, JavaScript, Data Science, artificial intelligence, machine learning, AR & VR)*

#### [Wes Bos](https://wesbos.com/courses/)
**Mixed** guided video courses to build products using new technologies\
*(JavaScript, CSS, React, Node.js, GraphQL, Redux)*
 
## Advanced


#### [Paqmind](http://paqmind.com)
**Free** Quiz your knowledge of programming\
*(JavaScript, Node.js, React, functional programming)*

#### [MIT Courseware](https://ocw.mit.edu/courses/find-by-topic/#cat=engineering&subcat=computerscience)
**Free** courses from MIT on advanced computer science topics\
*(varied and extensive computer science topics, C, C++, ..)*

#### [EDX](https://www.edx.org/course/subject/computer-science)
**Free** courses from Harvard, MIT, and other universities\
*(varied computer science subjects including theory and programming, data science, algorithms, ...)*

#### [Coursera](https://www.coursera.org/courses?categories=cs-ai,cs-programming,cs-systems,cs-theory,infotech)
**Free** platform for courses from universities and organizations worldwide\
*(varied computer science subjects including theory and programming, data science, algorithms, ...)*

#### [Awesome CS Courses](https://github.com/prakhar1989/awesome-courses/blob/master/README.md)
**Free** university-level courses scoured from around the internet.\
*(varied and extensive computer science topics, ...)*

#### Metacademy [Roadmaps](https://metacademy.org/roadmaps/), [Course Guides](https://metacademy.org/course_guides/)
**Free** graphs of interconnected topics required to master concepts\
*(programming, machine learning)*

#### [HackerRank](https://www.hackerrank.com/)
**Free** programming challenges and contests\
*(artificial intelligence, algorithms, functional programming, machine learning)*

#### [HackerEarth](https://www.hackerearth.com/)
**Free** programming challenges, hackathons and contests\
*(dynamic programming, artificial intelligence, algorithms, functional programming, machine learning)*

#### [Project Euler](https://projecteuler.net/)
**Free** mathematical/computer programming problems\
*(programming, mathematics)*

#### [CodeSignal](https://codesignal.com/)
**Free** programming challenges\
*(Java, C++, Python, JavaScript, Ruby, C#, PHP and Perl)*

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Karl Horky](https://github.com/karlhorky) has waived all copyright and related or neighboring rights to this work.

## Contributing

In lieu of a formal style guide, take care to maintain the existing style of this list.



You can take part as a educator if you are enrolled in a computer science/software engineering degree of education. 
If you are interested, I can ping you or help you as well. 


For more inquiries, please contact <pinkgrape0691@gmail.com>
<https://www.elice.io>
<pinkgrape0691@gmail.com>

