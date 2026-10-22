import sys


# Grade cutoffs are inclusive at the lower end of each range.
GRADE_RANGES = {
	"A": "90 to 100",
	"B": "80 to less than 90",
	"C": "70 to less than 80",
	"D": "60 to less than 70",
	"F": "0 to less than 60",
}

# Reusable prompt template for asking any student's mark.
MARK_PROMPT_TEMPLATE = "Enter {student_name}'s mark (0-100): "

# Expected results at every grade boundary and just below each cutoff.
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

INVALID_MARK_TEST_CASES = ("not a number", -0.01, 100.01, float("nan"))


def validate_mark(value):
	"""Convert a mark to a number and ensure it is between 0 and 100."""
	try:
		mark = float(value)
	except (TypeError, ValueError):
		raise ValueError("Mark must be a number from 0 to 100.") from None

	if not 0 <= mark <= 100:
		raise ValueError("Mark must be between 0 and 100, inclusive.")
	return mark


def grade_for(mark):
	"""Return the grade for a validated mark."""
	mark = validate_mark(mark)
	if mark >= 90:
		return "A"
	if mark >= 80:
		return "B"
	if mark >= 70:
		return "C"
	if mark >= 60:
		return "D"
	return "F"


def read_mark(student_name):
	"""Prompt again until a valid mark is entered."""
	while True:
		prompt = MARK_PROMPT_TEMPLATE.format(student_name=student_name)
		try:
			return validate_mark(input(prompt))
		except ValueError as error:
			print(f"{error} Please try again.")


def run_tests():
	"""Check grade cutoffs and marks that must be rejected."""
	for mark, expected_grade in BOUNDARY_TEST_CASES:
		actual_grade = grade_for(mark)
		assert actual_grade == expected_grade, (
			f"Mark {mark}: expected {expected_grade}, got {actual_grade}"
		)

	for mark in INVALID_MARK_TEST_CASES:
		try:
			validate_mark(mark)
		except ValueError:
			continue
		raise AssertionError(f"Invalid mark {mark!r} was accepted")

	print(
		f"All {len(BOUNDARY_TEST_CASES)} boundary tests and "
		f"{len(INVALID_MARK_TEST_CASES)} invalid-mark tests passed."
	)


def main():
	students = []

	print("Grade boundaries (marks out of 100):")
	for grade, mark_range in GRADE_RANGES.items():
		print(f"  {grade}: {mark_range}")

	for student_number in range(1, 6):
		name = input(f"Enter the name of student {student_number}: ").strip()
		while not name:
			print("Name cannot be blank. Please enter a name.")
			name = input(f"Enter the name of student {student_number}: ").strip()

		mark = read_mark(name)
		students.append((student_number, name, mark, grade_for(mark)))

	print("\nFINAL STUDENT RESULTS")
	print("-" * 78)
	print(f"{'No.':<5} {'Student':<20} {'Mark / 100':>12}  {'Grade':<8} Grade range")
	print("-" * 78)
	for number, name, mark, grade in students:
		print(
			f"{number:<5} {name:<20} {mark:>12.2f}  "
			f"{grade:<8} {GRADE_RANGES[grade]}"
		)


if __name__ == "__main__":
	if len(sys.argv) == 2 and sys.argv[1] == "--test":
		run_tests()
	else:
		main()
