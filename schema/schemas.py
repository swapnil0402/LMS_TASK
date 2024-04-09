from typing import Dict, List
from models.lmsdata import Student,Address


def address_serializer(address) -> dict:
    return {
        "city": address["city"],
        "country": address["country"]
    }

def student_serializer(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "address": address_serializer(student["address"])
    }

def students_list_serializer(students) -> list:
    
    return [student_serializer(student) for student in students]