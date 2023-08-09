# Schemas help to serialize and convert the MongoDB format JSON to UI required JSON


def studentEntity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "name": db_item["student_name"],
        "email": db_item["student_email"],
        "phone": db_item["student_phone"]
    }

def listOfStudentEntity(db_item_list) -> list:
    return [studentEntity(item) for item in db_item_list]