# Better Code Hub

Using the Better Code Hub at https://bettercodehub.com I ran my entire price_alerter_app repository against the clean code standards to measure whether my coding standards where good or bad. Below is the coding compliance result it gave me.

[![BCH compliance](https://bettercodehub.com/edge/badge/EgbieAndersonUku1/the_Moodle_Project?branch=master)](https://bettercodehub.com/)

I lost one mark in **Automate test** compliance

## Project Moodle: 

**What is moodle?**

`Moodle is a learning platform designed to provide educators, administrators and learners with a single robust, secure and integrated system to create personalised learning environments`

**My goal**

In this project I am going to build a framework from the ground up using Python Selenium (Selenium is a tool that can be used for automating/testing a website). This framework will then be used to test a specific Moodle application.

`**Things that framework would be able to test once completed**` 

1. Can a user ONLY log in with the correct username and password
2. Is the username not case sensitive
3. Can the user self-enrol to a course
4. Can a user self-un-enrol from a course
4. Can a cohort of students be enrolled to the application by a course-creator
5. Can a course-creator enrol/un-enrol any student
5. Can ONLY a course-creator enable/disable self-enrolment
5. Can a user enrol to a course if the option for enrolling is disable
5  Can a guest enrol onto a course (Should not be possible)
5. Can courses/content be CREATED ONLY by a course creator.
5. Can courses/content be DELETED ONLY by the course-creator
7. Is a badge awarded if a student completes and passes a quiz
8. Is a badge be awarded if a student completes and passes the entire course
9. Is a badge still awarded if a student fails either a course/quiz (Should not be possible)
10. Does a guest have read-only permissions (Guest should have read-only permission)
11. Are the question displayed in random order meaning there are not in the order loaded.


For each of the test cases listed above, individual test scripts can be written for each one. So why have I chosen to build a framework instead, seems like a lot of hassle. The answer is simple, by building a framework and wrapping the selenium objects into a page model objects this prevents my tests from breaking should the UI change. Because the selenium objects are not embedded with the logic of my code any changes made to page model objects because of changes to the UI does not force me to re-write the logic of the code each time the UI changes nor does it break any tests using it. And finally I love to challenge myself to push myself outside my comfort zone.


**Technologies used**

Python 2.7x: programming language

Python-Selenium: The driver that enables the Moodle application to be tested.

