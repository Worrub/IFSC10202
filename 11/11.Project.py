

def load_students(filename):
    """Load student names and IDs into a dictionary."""
    students = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                student_id, name = line.split(',', 1)
                students[student_id.strip()] = name.strip()
    return students


def load_scores(filename):
    """Load scores by student ID into a dictionary."""
    scores = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                student_id, score = line.split(',', 1)
                student_id = student_id.strip()
                score = float(score.strip())
                scores.setdefault(student_id, []).append(score)
    return scores


def calculate_letter_grade(avg):
    """Determine letter grade from average score."""
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'


def main():
    students = load_students("Students.txt")
    scores = load_scores("Scores.txt")

    print(f"{'ID':<6} {'Name':<20} {'Avg Score':<10} {'Letter Grade':<12} Running Average Details")
    print("-" * 70)

    for student_id, name in students.items():
        student_scores = scores.get(student_id, [])
        if not student_scores:
            print(f"{student_id:<6} {name:<20} {'N/A':<10} {'N/A':<12} No scores")
            continue

        # Calculate running averages
        running_avgs = []
        total = 0
        for i, score in enumerate(student_scores, start=1):
            total += score
            running_avg = total / i
            running_avgs.append(round(running_avg, 2))

        semester_avg = round(sum(student_scores) / len(student_scores), 2)
        letter = calculate_letter_grade(semester_avg)

        print(f"{student_id:<6} {name:<20} {semester_avg:<10} {letter:<12} {running_avgs}")
