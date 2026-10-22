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


def main():
	students = []

	print("Grade boundaries: A = 90-100, B = 80-<90, C = 70-<80,")
	print("                 D = 60-<70, F = 0-<60")

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

	print("\nStudent results")
	print(f"{'Name':<24}{'Mark':>8}{'Grade':>8}")
	print("-" * 40)
	for name, mark, grade in students:
		print(f"{name:<24}{mark:>8.2f}{grade:>8}")


if __name__ == "__main__":
	main()
