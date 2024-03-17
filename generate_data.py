from __future__ import annotations
import pandas as pd
import random
from dataclasses import dataclass
from datetime import datetime, timedelta
from faker import Faker
from typing import List

fake = Faker('uk_UA')


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

    @classmethod
    def generate(cls, _id: int) -> Student:
        gender = random.choice(["Male", "Female"])
        first_name = fake.first_name_male() if gender == "Male" else fake.first_name_female()
        return cls(
            id=_id,
            first_name=first_name,
            last_name=fake.last_name(),
            birth_date=fake.date_of_birth(minimum_age=15, maximum_age=30).strftime('%Y-%m-%d'),
            average_mark=random.randint(1, 100),
            count_of_lessons_absent=random.randint(0, 10),
            count_of_lessons_sick=random.randint(0, 10),
            gender=gender
        )

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


@dataclass
class RestaurantReview:
    id: int
    name: str
    reviewer_name: str
    review_text: str
    rating: int
    last_visit_date: str
    city: str

    @classmethod
    def generate(cls, _id: int) -> RestaurantReview:
        return cls(
            id=_id,
            name=fake.company().replace(",", ""),
            reviewer_name=fake.first_name_male() if random.choice(["Male", "Female"]) == "Male" else fake.first_name_female(),
            review_text=fake.paragraph().replace(",", ""),
            rating=random.randint(1, 5),
            last_visit_date=(datetime.now() - timedelta(days=random.randint(0, 730))).strftime('%Y-%m-%d'),
            city=fake.city_name()
        )


def generate_data(cls: type, num_records: int) -> List:
    return [cls.generate(i) for i in range(num_records)]


def save_to_csv(data: List, filename: str):
    df = pd.DataFrame([vars(record) for record in data])
    df.to_csv(filename, index=False)


if __name__ == '__main__':
    students = generate_data(Student, 1000)
    save_to_csv(students, "students.csv")

    restaurant_reviews = generate_data(RestaurantReview, 500)
    save_to_csv(restaurant_reviews, "restaurant_reviews.csv")
