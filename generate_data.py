from dataclasses import dataclass
from typing import List

import faker

# Generate dataset of students, each student should have the following attributes:
# - id
# - first_name
# - last_name
# - birth_date
# - average mark
# - count of lessons absent
# - count of lessons sick
# - gender
# - city

# first_name, last_name, city should be from Ukraine
# birth_date should be from 1990-01-01 to 2005-01-01

# Generate 1000 students and save them to a csv file

# Set ukrainian locale
fake = faker.Faker('uk_UA')

@dataclass
class Student:
    id: int
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    count_of_lessons_absent: int
    count_of_lessons_sick: int
    gender: str
    city: str


def generate_students() -> List[Student]:
    students = []

    for i in range(1000):
        count_of_lessons_absent = fake.random_int(min=0, max=10)
        count_of_lessons_sick = fake.random_int(min=0, max=count_of_lessons_absent)

        gender = fake.random_int(min=0, max=1)
        first_name = fake.first_name_male() if gender == 1 else fake.first_name_female()
        city = fake.city_name()

        student = Student(
            id=i,
            first_name=first_name,
            last_name=fake.last_name(),
            birth_date=fake.date_of_birth(minimum_age=15, maximum_age=30).strftime('%Y-%m-%d'),
            average_mark=fake.random_int(min=1, max=100),
            count_of_lessons_absent=count_of_lessons_absent,
            count_of_lessons_sick=count_of_lessons_sick,
            gender="Male" if gender == 1 else "Female",
            city=city
        )
        students.append(student)

    # For the 1% of random students, set the average mark to None
    for student in fake.random_elements(elements=students, length=int(len(students) * 0.01)):
        student.average_mark = None

    return students


def save_students_to_csv(students: List[Student]):
    with open('students.csv', 'w') as f:
        f.write('id,first_name,last_name,birth_date,average_mark,count_of_lessons_absent,count_of_lessons_sick,gender,city\n')

        for student in students:
            f.write(f'{student.id},{student.first_name},{student.last_name},{student.birth_date},{student.average_mark},{student.count_of_lessons_absent},{student.count_of_lessons_sick},{student.gender},{student.city}\n')


if __name__ == '__main__':
    students = generate_students()
    save_students_to_csv(students)
