student_names = []
subjects = ["Maths", "English", "Chemistry", "Physics", "Biology", "Further Maths"]
scores = []


def get_name():
    while True:
        name = input("Please enter your name (or type 'stop' to finish): ").strip()

        if name.lower() == "stop":
            return "STOP"

        if name == "":
            print("Name cannot be empty.")
            continue

        if not name.isalpha():
            print("Name should contain only letters.")
            continue

        return name


def get_scores(name):
    student_scores = []

    for subject in subjects:
        while True:
            try:
                score = int(input(f"Enter {subject} score for {name}: "))

                if 0 <= score <= 100:
                    student_scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    return student_scores


def print_results():
    print("\n{:<12}".format("Name"), end="")

    for subject in subjects:
        print("{:<12}".format(subject), end="")

    print("{:<12}".format("Average"))
    print("-" * (12 * (len(subjects) + 2)))

    for i in range(len(student_names)):
        avg_score = sum(scores[i]) / len(subjects)

        print("{:<12}".format(student_names[i]), end="")

        for score in scores[i]:
            print("{:<12}".format(score), end="")

        print("{:<12.2f}".format(avg_score))



while True:
    name = get_name()

    if name == "STOP":
        break

    student_names.append(name)
    student_scores = get_scores(name)
    scores.append(student_scores)

print_results()