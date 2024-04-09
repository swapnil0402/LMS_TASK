from fastapi import APIRouter, HTTPException, Query, Path
from models.lmsdata import Student,Address,PatchAddress,PatchStudent
from config.database import myCol
from schema.schemas import students_list_serializer,student_serializer
from bson import ObjectId

router = APIRouter()


@router.post("/students", response_model=dict, status_code=201, description="API to create a student in the system. All fields are mandatory and required while creating the student in the system.")
async def create_student(student: Student):
    result = myCol.insert_one(student.dict())
    if result.inserted_id:
        return {"id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Failed to create student")


@router.get("/students", response_model=dict, description= "An API to find a list of students. You can apply filters on this API by passing the query parameters as listed below.")
async def list_students(country: str = Query(None,description="To apply filter of country. If not given or empty, this filter should be applied."), age: int = Query(None,description="Only records which have age greater than equal to the provided age should be present in the result. If not given or empty, this filter should be applied.")):
    query = {}
    if country:
        query['address.country'] = country
    if age:
        query['age'] = {"$gte": age}
        
    serialized_students = students_list_serializer(myCol.find(query))
    
    return {"data": serialized_students}


@router.get("/students/{id}", response_model=dict)
async def fetch_student(id: str = Path(..., description="The ID of the student previously created.")):
    student = myCol.find_one({"_id": ObjectId(id)})
    if student:
        return student_serializer(student)
    else:
        raise HTTPException(status_code=404, detail="Student not found")


@router.patch("/students/{id}", status_code=204,description="API to update the student's properties based on information provided. Not mandatory that all information would be sent in PATCH, only what fields are sent should be updated in the Database.")
async def update_student(id: str, student1: PatchStudent):
    myCol.find_one_and_update({"_id": ObjectId(id)}, {"$set": student1.dict(exclude_unset =True)})


@router.delete("/students/{id}", response_model=dict)
async def delete_student(id: str = Path(...)):
    result = myCol.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {}
    else:
        raise HTTPException(status_code=404, detail="Student not found")
