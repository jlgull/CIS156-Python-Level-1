#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: courses.py
#
"""
Generic shell for the CIS156 programs

Ch 8 Programming Assignment, Part B

Create a program called courses.py that has a dictionary with 7 course names
    (for example: CIS105, ENG101, etc.), along with the name of each associated instructor.
Prompt the user for the name of a course to look up, or the word "quit" to exit.
After the user types in a course, it should look up and print that course's instructor.

The program should repeat this until the user enters "quit" at the prompt.

Note: The program does NOT need to gracefully handle the error that may occur if the course
    is not found in the dictionary; for now, your program only needs to work when a course is entered correctly.

"""

#
# Import all required options
#
# import only system from os
from os import system, name

# End of import section

"""

Variable List

Dictionary info:
    course_number   -   Key:  Courses available
        course_descriptor   -   Value: Short descriptor for course
        prerequisites       -   Value: Course Prerequisites   
        course_descriptor_long  -   Value: Long descriptor for course
        course_instructors   -   Value: List of Instructors for the course 

Since there are no arrays in Python, so I used a list. Here is information about the (array) List.
List info:


String variables:
    In main program:.
        do_again    - Holds flag for the while loop, regarding the re-execution of the program. 
        description     - Course Short description for printing
        long_description    - Course Long description for printing
        instructors     - Instructor names for printing
        pre_reqs         - Course prerequisites for printing
         
    In function:
        name    - Information returned by the system, to identify type of OS
                  
Floating point numbers:
    In main program:
  
    In function:

Integers numbers: 
    In main program:
      
    In function:
   
"""

# Function definition section of the program
#


def clear():
    # Define the clear function, which is agnostic to the operating system
    # being used. In PyCharm you have to sent "Emulate terminal in output console",
    # which is found under the "Edit run configuration" tab.

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is "posix")
    else:
        _ = system("clear")

# End of Function definitions


# Create a program called courses.py that has a dictionary with 7 course names
#     (for example: CIS105, ENG101, etc.), along with the name of each associated instructor.

# Fill dictionary with course information
course_number = {
    "AIM100": {"course_descriptor": "Introduction to Artificial Intelligence",
               "prerequisites": "None",
               "course_descriptor_long": "Basic concepts and applications of artificial intelligence (AI), "
                                         "including AI project cycles.",
               "course_instructors": "H. Matar, Staff"},

    "AIM110": {"course_descriptor": "Introduction to Machine Learning",
               "prerequisites": "A grade of C or better in AIM100, CIS156, and MAT206",
               "course_descriptor_long": "Introduction to machine learning concepts and Python applications, "
                                         "including data acquisition, supervised and unsupervised learning, "
                                         "and data modeling.",
               "course_instructors": "H. Matar, Staff"},

    "AIM220": {"course_descriptor": "Artificial Intelligence for Computer Vision",
               "prerequisites": "A grade of C or better in AIM110",
               "course_descriptor_long": "Understand and apply the basic techniques to process images using "
                                         "OpenCV and Python libraries.",
               "course_instructors": "H. Matar"},

    "CIS150AB": {"course_descriptor": "Object-Oriented Programming Fundamentals",
                 "prerequisites": "A grade of C or better in CIS105 or permission of Instructor.",
                 "course_descriptor_long": "Structured and Object-Oriented design and logic tools. "
                                           "Use of computer problems to demonstrate and teach concepts using an "
                                           "appropriate programming language.",
                 "course_instructors": "Staff"},

    "CIS156": {"course_descriptor": "Python Programming: Level I",
               "prerequisites": "A grade of C or better in CIS105 or permission of Instructor.",
               "course_descriptor_long": "Introduction to Python programming. Includes general concepts, "
                                         "program design, development, data types, operators, expressions, "
                                         "flow control, functions, classes, input and output operations, "
                                         "debugging, structured programming, and object-oriented programming.",
               "course_instructors": "C. Stevens, W. Stewart, W. Tagart, S. Hustedde, R. Loy, D. Baker, Staff"},

    "CIS256": {"course_descriptor": "Python Programming: Level II",
               "prerequisites": "A grade of C or better in CIS156 or permission of Instructor.",
               "course_descriptor_long": "Advanced Python object-oriented programming concepts and applications. "
                                         "Emphasis on code documenting, versioning, unit testing strategies, "
                                         "and security practices for Python project/package development. "
                                         "Includes Python applications for data analysis, networking, "
                                         "database manipulation, and web application development.",
               "course_instructors": "Staff"},

    "CIS256DA": {"course_descriptor": "Python for Data Analysis",
                 "prerequisites": "A grade of C or better in CIS156 or permission of Instructor.",
                 "course_descriptor_long": "Advanced Python object-oriented programming concepts and applications. "
                                           "Emphasis on code documenting, versioning, unit testing strategies, "
                                           "and security practices for Python project/package development. "
                                           "Includes Python applications for data analysis, networking, "
                                           "database manipulation, and web application development.",
                 "course_instructors": "Staff"},

    "CIS126RH": {"course_descriptor": "Red Hat System Administration I",
                 "prerequisites": "None",
                 "course_descriptor_long": "Introduction to core administration skills needed to manage a "
                                           "Red Hat Enterprise Linux system. This Red Hat Academy course helps "
                                           "prepare for the Red Hat certification exams using a hands-on, "
                                           "task-focused curriculum.",
                 "course_instructors": "M. Bencic, T. Tumulty, S. Yavelak, Staff"},

    "CIS238RH": {"course_descriptor": "Red Hat System Administration II",
                 "prerequisites": "A grade of C or better in CIS126RH or permission of Instructor.",
                 "course_descriptor_long": "Continue to develop core administration skills needed to manage a "
                                           "Red Hat Enterprise Linux system. This Red Hat Academy course helps to "
                                           "prepare students for the Red Hat certification exams using a hands-on, "
                                           "task-focused curriculum.",
                 "course_instructors": "S. Yavelak, M. Bencic, Staff"},

    "CIS240RH": {"course_descriptor": "Red Hat System Administration III",
                 "prerequisites": "A grade of C or better in CIS238RH or permission of Instructor.",
                 "course_descriptor_long": "Provides solid understanding of how to automate services on a "
                                           "Linux system. Covers use of Ansible to automate provisioning, "
                                           "configuration, application deployment, and orchestration on "
                                           "Red Hat Enterprise Linux 8. Content aligns with the "
                                           "Red Hat Certified Engineer (RHCE - EX294) exam, "
                                           "a professional certification.",
                 "course_instructors": "M. Bencic, Staff"},

    "CIS271RH": {"course_descriptor": "Red Hat System Administration IV",
                 "prerequisites": "A grade of C or better in CIS238RH or permission of Instructor.",
                 "course_descriptor_long": "Provides solid understanding on containers, containerized applications, "
                                           "and orchestration of containers using Kubernetes and Red Hat OpenShift "
                                           "on Red Hat Enterprise Linux. ",

                 "course_instructors": "M. Bencic, Staff"},

    "CIS275DL": {"course_descriptor": "Linux Capstone",
                 "prerequisites": "A grade of C or better in CIS240DL, or CIS240RH, or permission of Instructor.",
                 "course_descriptor_long": "The Linux Capstone course aggregates the skills, knowledge, "
                                           "communication, and critical thinking skills from the Linux Program. "
                                           "This course is to emulate a production environment that prepares "
                                           "students to work as a Linux Systems Administrator. "
                                           "The course helps to prepare students for Linux Industry "
                                           "certification exams. ",
                 "course_instructors": "Staff"},


    }


# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program.
    clear()

    # Print the general program information to the user.
    print("\nWelcome to the General College Catalog.")
    print("  Here is a short list of some of our Computer related courses.")
    print("  The list is sorted by Course ID, for additional information on any specific course,")
    print("  you will be asked to enter the course number below.\n")

    # prior to printing the list, sort by the Course ID
    course_list = sorted(list(course_number.keys()))

    # Print the general course information.
    for course in course_list:
        description = course_number[course].get("course_descriptor")
        print(f"Course ID: {course:.<10s} {description}")

    # Prompt the user for the name of a course to look up, or the word "quit" to exit.
    # Query user for which course they would like information about.
    # Check for valid entries as well.
    # After the user types in a course, it should look up and print that course's instructor.
    print("\nAfter reviewing the list, enter the course number of a class you are interested in.")
    course_id = input("Do not worry about letter case when entering the Course ID. Press \"Enter\" to quit. ").upper()
    if len(course_id) == 0:
        break
    elif course_id not in course_number:
        print(f"You entered a Course ID of, \"{course_id}\", which is not in our system.")
    else:
        pre_reqs = course_number[course_id].get("prerequisites")
        long_description = course_number[course_id].get("course_descriptor_long")
        instructors = course_number[course_id].get("course_instructors")
        print(f"\nHere is additional information on {course_id}")
        print(f"The instructors available are: {instructors}")
        print(f"The course prerequisites are: {pre_reqs}")
        print(f"The complete course description follows:")
        print(f"\t{long_description}")

    """      
    The following code was developed during program development, to test the extraction concepts.
            
    for course in course_number:
        description = course_number[course].get("course_descriptor")
        long_description = course_number[course].get("course_descriptor_long")
        instructors = course_number[course].get("course_instructors")
        print(f"\nHere is the short description for {course}: {description}")
        print(f"\tThe instructors available are {instructors}")
        print(f"\tThe complete course description follows:")
        print(f"\t{long_description}")
    """

    # Ask if the user would like to repeat the program.
    #   Also, validate for the correct response.
    while True:
        print("\nWould you like to review another course offering? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
