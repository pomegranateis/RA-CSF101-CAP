# pema tshering yangchen
# section A
# 02230295
# REFERENCES
# Links that you referred while solving 
# https://www.phind.com/
# https://chat.openai.com/

# SOLUTION
# There were 20000 people assigned and there are 6425 overlapping space assignments
# There were 2556 assignments that overlap completely.

# 77671685

def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

input_file = "input_5_cap2.txt"
assignments = read_input(input_file)
print(assignments)

def calculate_overlapping(assignments):
    total_people = 0
    overlapping_sections = 0

    for line in assignments:
        people = [list(map(int, person.split('-'))) for person in line.split(', ')]
        total_people += len(people)

        for i in range(len(people)):
            for j in range(i + 1, len(people)):
                person1 = people[i]
                person2 = people[j]
                if person1[1] >= person2[0] and person1[0] <= person2[1]:
                    overlapping_sections += 1

    return total_people, overlapping_sections

def calculate_completely_overlapping(assignments):
    completely_overlapping_assignments = 0

    for line in assignments:
        sections = [list(map(int, section.split('-'))) for section in line.split(', ')]
        for i in range(len(sections)):
            for j in range(i + 1, len(sections)):
                if sections[i][0] <= sections[j][0] and sections[i][1] >= sections[j][1]:
                    completely_overlapping_assignments += 1

    return completely_overlapping_assignments

#Task 1
total_people, overlapping_sections = calculate_overlapping(assignments)
print(f"There were {total_people} people assigned and there are {overlapping_sections} overlapping space assignments")

#Task 2
completely_overlapping_assignments = calculate_completely_overlapping(assignments)
print(f"There were {completely_overlapping_assignments} assignments that overlap completely.")
