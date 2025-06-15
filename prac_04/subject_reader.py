FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subjects_data(data)


def load_data():
    """Load and format data."""
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject.append(parts)
    input_file.close()
    return subject


def display_subjects_data(subjects):
    """Display subject data."""
    for subject in subjects:
        print("{} is taught by {:12} and has {:3} students".format(*subject))


main()
