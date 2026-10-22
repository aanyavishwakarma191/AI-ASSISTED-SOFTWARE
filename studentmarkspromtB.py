import sys


# A mark exactly on a boundary receives the grade for that boundary.
GRADE_RANGES = {
	"A": "90 to 100",
	"B": "80 to less than 90",
	"C": "70 to less than 80",
	"D": "60 to less than 70",
	"F": "0 to less than 60",
}

# Boundary values and the expected grade for each one.
BOUNDARY_TEST_CASES = (
	(0, "F"),
	(59.99, "F"),
	(60, "D"),
	(69.99, "D"),
	(70, "C"),
	(79.99, "C"),
	(80, "B"),
	(89.99, "B"),
	(90, "A"),
	(100, "A"),
)


def grade_for(mark):
	if mark >= 90:
		return "A"
	if mark >= 80:
		return "B"
	if mark >= 70:
		return "C"
	if mark >= 60:
		return "D"
	return "F"


def run_boundary_tests():
	for mark, expected_grade in BOUNDARY_TEST_CASES:
		actual_grade = grade_for(mark)
		assert actual_grade == expected_grade, (
			f"Mark {mark}: expected {expected_grade}, got {actual_grade}"
		)
	print(f"All {len(BOUNDARY_TEST_CASES)} boundary tests passed.")


def main():
	students = []

	print("Grade boundaries (marks out of 100):")
	for grade, mark_range in GRADE_RANGES.items():
		print(f"  {grade}: {mark_range}")

	for student_number in range(1, 6):
		name = input(f"Enter the name of student {student_number}: ").strip()
		while not name:
			print("Name cannot be blank.")
			name = input(f"Enter the name of student {student_number}: ").strip()

		while True:
			try:
				mark = float(input(f"Enter {name}'s mark (0-100): "))
			except ValueError:
				print("Invalid mark. Please enter a number from 0 to 100.")
				continue

			if not 0 <= mark <= 100:
				print("Mark out of range. Please enter a number from 0 to 100.")
				continue
			break

		students.append((name, mark, grade_for(mark)))

	print("\n" + "=" * 40)
	print("FINAL STUDENT RESULTS")
	print("=" * 40)
	for student_number, (name, mark, grade) in enumerate(students, start=1):
		print(f"\nStudent {student_number}: {name}")
		print(f"  Mark:  {mark:.2f} out of 100")
		print(f"  Grade: {grade} (marks {GRADE_RANGES[grade]})")


if __name__ == "__main__":
	if len(sys.argv) == 2 and sys.argv[1] == "--test":
		run_boundary_tests()
	else:
		main()
