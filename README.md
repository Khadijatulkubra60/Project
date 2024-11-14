# Student Performance Tracker

This Python program tracks performance of students, calculates their average scores and also determines whether they are passing in all the subjects or failing.
It also calculates the overall class average and generates a performance report for it.

## Features

* ### Student information input
    Allows you to input students' names and scores in multiple subjects (Maths, English, Science etc etc.)

* ### Individual Student report
    Displays each student's average score and whether they are passing or failing.

* ### Class performance Report
    Computes overall average score of the class and displays individual student performance.

* ### Score Validation
    Handles invalid scores inputs (non-integer values) and prompts the users to re-enter them.

## Classes

*Student*

Represents a single student with their name and scores

* ### Methods
    * `__init__(self, name)`: It initializes a new student with the given name and an empty score list.

    * `add_scores(self, scores)`: Adds a list of scores to the student's record.

    *  `calculate_average(self)`: Calculates and returns the average score for the student.

    * `is_passing(self, passing_score=50)`: Checks if the student is passing in all subjects (default passing score is 50)

*PerformanceTracker*

Tracks a collection of students and calculates class level performance metrics.

* ### Methods
   
    * `__init__(self)`: Initializes an empty dictionary to store students.

    * `add_student(self, name, scores)`: Adds a student along with their scores to the tracker.

    * `calculate_class_average(self)`: Calculates the average score for the class.

    * `display_student_performance of each student and the class average.`

## Functionality

* ### Input Handling 
    The program will prompt for students' names and scores, you can type as many student data until you type `done`

* ### Report Generation
    After input, the program generates and prints a detailed report on individual students' average scores and passing status, along with overall class average score.

## How to use?

1- Clone or download this repository.

2- Run the script using a Python 3.x interpreter.

3- Input students' names and scores when prompted. Type `done` to stop input.

4- View the report displaying student performance and class average.

## Example Output

```
Enter student details (type 'done' when finished):
Enter student's name: Maryam
Enter Math score for Maryam: 67
Enter Science score for Maryam: 45
Enter English score for Maryam: 78
Enter student's name: john
Enter Math score for john: 43
Enter Science score for john: 89
Enter English score for john: 34
Enter student's name: done

--- Student Performance Report ---
Maryam: Average Score = 63.33, Status = Passing
john: Average Score = 55.33, Status = Failing

Class Average Score: 59.33
--- End of Report ---

    