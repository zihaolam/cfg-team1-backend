def course_entity(item) -> dict:
	return {
		"id": str(item["_id"]),
		"name": item["name"],
		"description": item["description"]
		"modules": item["modules"]
	}

def course_entities(items) -> list:
	return [course_entity(item) for item in items]