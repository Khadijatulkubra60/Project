class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_scores(self, scores):
        """Add scores for the student."""
        self.scores = scores

    def calculate_average(self):
        """Calculate the average score for the student."""
        if self.scores:
            return sum(self.scores) / len(self.scores)
        return 0

    def is_passing(self, passing_score=40):
        """Determine if the student is passing in all subjects."""
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        """Add a new student with their scores to the tracker."""
        student = Student(name)
        student.add_scores(scores)
        self.students[name] = student

    def calculate_class_average(self):
        """Calculate the overall average score for the entire class."""
        total_score = 0
        total_subjects = 0
        for student in self.students.values():
            total_score += sum(student.scores)
            total_subjects += len(student.scores)
        if total_subjects > 0:
            return total_score / total_subjects
        return 0

    def display_student_performance(self):
        """Print out the performance of each student and the class average."""
        print("\n--- Student Performance Report ---")
        for student in self.students.values():
            avg_score = student.calculate_average()
            status = "Passing" if student.is_passing() else "Failing"
            print(f"{student.name}: Average Score = {avg_score:.2f}, Status = {status}")
        
        class_avg = self.calculate_class_average()
        print(f"\nClass Average Score: {class_avg:.2f}")
        print("--- End of Report ---\n")


# Step 3: Input Handling
def input_student_data(tracker):
    print("Enter student details (type 'done' when finished):")
    while True:
        name = input("Enter student's name: ").strip()
        if name.lower() == 'done':
            break

        try:
            scores = []
            for subject in ["Math", "Science", "English"]:
                score = int(input(f"Enter {subject} score for {name}: "))
                scores.append(score)

            # Step 3: Store Data
            tracker.add_student(name, scores)

        except ValueError:
            print("Invalid input. Please enter a valid integer score.")
            continue


# Initialize the performance tracker and gather input
tracker = PerformanceTracker()
input_student_data(tracker)

# Display student performance and class average
tracker.display_student_performance()