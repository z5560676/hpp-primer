# Edge Case: Missing Required Fields in Student Creation

## Description
When a `POST /students` request is made to create a new student, if the request body is missing required fields (e.g., `name` or `course`), the API should return a **400 Bad Request** error. The error response should include information about which fields are missing.

## Handling Method
1. **Check Request Body**: Upon receiving the `POST /students` request, check if all required fields (e.g., `name` and `course`) are present in the request body.
2. **Return an Error**: If any required fields are missing, the server should respond with a **400 Bad Request** status, and the error message should clearly indicate which fields are missing.

## Code Implementation
Below is the code to handle this edge case:

```python
@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()  # Get JSON data from the request
    name = data.get('name')
    course = data.get('course')

    # Check if required fields are missing
    if not name or not course:
        return {"error": "Missing required fields: name and course"}, 400  # Return 400 error if fields are missing

    # If all required fields are present, proceed with the logic to add the student
    new_student = db.insert_student(name, course)
    return jsonify(new_student), 201  # Return the created student with status code 201
