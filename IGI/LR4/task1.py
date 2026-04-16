# task1.py
"""
Lab 4 - Task 1
Author: Lenchevski Vladimir
Date: 15.04.2026
Version: 1.0
Purpose: Store applicant data in CSV and pickle, search by surname.
"""

import csv
import pickle
import os
from typing import List, Dict

class Applicant:
    _total_applicants = 0

    INSTRUMENT_TO_SPECIALTY = {
        'piano': 'Piano Exam',
        'violin': 'String Instruments Exam',
        'cello': 'String Instruments Exam',
        'flute': 'Wind Instruments Exam',
        'clarinet': 'Wind Instruments Exam',
        'trumpet': 'Brass Instruments Exam',
        'guitar': 'String Instruments Exam',
        'drums': 'Percussion Exam',
        'voice': 'Vocal Exam',
        'accordion': 'Folk Instruments Exam',
        'saxophone': 'Wind Instruments Exam',
        'harp': 'String Instruments Exam'
    }

    def __init__(self, surname: str, instrument: str):
        if not surname or not surname.strip():
            raise ValueError("Surname cannot be empty")
        if instrument.lower() not in self.INSTRUMENT_TO_SPECIALTY:
            raise ValueError(f"Unknown instrument: {instrument}")

        self._surname = surname.strip()
        self._instrument = instrument.lower()
        Applicant._total_applicants += 1

    @property
    def surname(self) -> str:
        return self._surname

    @property
    def instrument(self) -> str:
        return self._instrument

    @property
    def exam_specialty(self) -> str:
        return self.INSTRUMENT_TO_SPECIALTY[self._instrument]

    def __str__(self) -> str:
        return f"{self._surname} ({self._instrument}) -> {self.exam_specialty}"

    @classmethod
    def get_total_applicants(cls) -> int:
        return cls._total_applicants


class FacultyAdmission:
    def __init__(self):
        self._applicants: List[Applicant] = []

    def add_applicant(self, applicant: Applicant):
        self._applicants.append(applicant)

    def save_to_csv(self, filename: str):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Surname', 'Instrument', 'ExamSpecialty'])
            for applicant in self._applicants:
                writer.writerow([applicant.surname, applicant.instrument, applicant.exam_specialty])

    def load_from_csv(self, filename: str):
        self._applicants.clear()
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                applicant = Applicant(row['Surname'], row['Instrument'])
                self._applicants.append(applicant)

    def save_to_pickle(self, filename: str):
        with open(filename, 'wb') as f:
            pickle.dump(self._applicants, f)

    def load_from_pickle(self, filename: str):
        with open(filename, 'rb') as f:
            self._applicants = pickle.load(f)

    def find_applicant_by_surname(self, surname: str) -> List[Applicant]:
        surname_lower = surname.lower().strip()
        return [a for a in self._applicants if a.surname.lower() == surname_lower]

    def get_exam_groups(self) -> Dict[str, List[Applicant]]:
        groups = {}
        for applicant in self._applicants:
            specialty = applicant.exam_specialty
            if specialty not in groups:
                groups[specialty] = []
            groups[specialty].append(applicant)
        return groups


def task1():
    print("\n" + "=" * 60)
    print("=== Task 1: Music Pedagogical Faculty ===")
    print("=" * 60)

    os.makedirs("data", exist_ok=True)

    faculty = FacultyAdmission()

    sample_applicants = [
        Applicant("Petrov", "piano"),
        Applicant("Ivanova", "violin"),
        Applicant("Sidorov", "guitar"),
        Applicant("Kuznetsova", "flute"),
        Applicant("Smirnov", "piano"),
        Applicant("Volkova", "cello"),
        Applicant("Morozov", "drums"),
        Applicant("Novikova", "voice"),
        Applicant("Popov", "trumpet"),
        Applicant("Sokolova", "clarinet")
    ]

    for app in sample_applicants:
        faculty.add_applicant(app)

    faculty.save_to_csv("data/music_faculty.csv")
    faculty.save_to_pickle("data/music_faculty.pkl")

    faculty2 = FacultyAdmission()
    faculty2.load_from_csv("data/music_faculty.csv")

    print("\n" + "-" * 40)
    print("SEARCH APPLICANT")
    print("-" * 40)

    while True:
        surname = input("\nEnter surname to search (or 'quit' to exit): ").strip()
        if surname.lower() == 'quit':
            break

        results = faculty2.find_applicant_by_surname(surname)
        if results:
            print(f"\nFound {len(results)} applicant(s):")
            for app in results:
                print(f"  • {app}")
        else:
            print(f"No applicant found with surname '{surname}'")

        cont = input("\nSearch again? (y/n): ").strip().lower()
        if cont != 'y':
            break