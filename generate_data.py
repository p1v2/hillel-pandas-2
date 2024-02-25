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


@dataclass
class RestaurantReview:
    id: int
    name: str
    reviewer_name: str
    review_text: str
    rating: int
    last_visit_date: str
    city: str
    
    
def generate_restaurant() -> List[RestaurantReview]:
    restaurants = []
    
    for i in range(500):
        
        gender = fake.random_int(min=0, max=1)
        name = fake.company().replace(",", "")
        reviewer_name = fake.first_name_male() if gender == 1 else fake.first_name_female()
        review_text = fake.paragraph().replace(",", "")
        rating = fake.random_int(1, 5)
        last_visit_date = fake.date_time_between(start_date="-2y", end_date="now").strftime('%Y-%m-%d')
        city = fake.city_name()
        
        restaurant = RestaurantReview(
            id=i,
            name=name,
            reviewer_name=reviewer_name,
            review_text=review_text,
            rating=rating,
            last_visit_date=last_visit_date,
            city=city
        )
        restaurants.append(restaurant)
        
        for restaurant in fake.random_elements(elements=restaurants, length=int(len(restaurants) * 0.01)):
            restaurant.rating = fake.random_int(min=6, max=20)
            restaurant.last_visit_date = None

    
        
    return restaurants
    

def save_students_to_csv(students: List[Student]):
    with open('students.csv', 'w', encoding='utf-8') as f:
        f.write('id,first_name,last_name,birth_date,average_mark,count_of_lessons_absent,count_of_lessons_sick,gender,city\n')

        for student in students:
            f.write(f'{student.id},{student.first_name},{student.last_name},{student.birth_date},{student.average_mark},{student.count_of_lessons_absent},{student.count_of_lessons_sick},{student.gender},{student.city}\n')
            

def saves_restaurants_to_csv(restaurants: List[RestaurantReview]):
    with open('restaurant_review.csv', 'w', encoding='utf-8') as f:
        f.write('id,name,reviewer_name,review_text,rating,last_visit_date,city\n')

        for restaurant in restaurants:
             f.write(f"{restaurant.id},{restaurant.name},{restaurant.reviewer_name},{restaurant.review_text},{restaurant.rating},{restaurant.last_visit_date},{restaurant.city}\n")

if __name__ == '__main__':
    # students = generate_students()
    # save_students_to_csv(students)
    restorans_review = generate_restaurant()
    saves_restaurants_to_csv(restorans_review)
