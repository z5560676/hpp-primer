from flask import Flask, jsonify, request
from flask_cors import CORS

import db

app = Flask(__name__)
CORS(app)

# Instructions:
# - Use the functions in backend/db.py in your implementation.
# - You are free to use additional data structures in your solution
# - You must define and tell your tutor one edge case you have devised and how you have addressed this

@app.route("/students")
def get_students():
    """
    Route to fetch all students from the database
    return: Array of student objects
    """
<<<<<<< HEAD
    try:
        students = db.get_all_students()  # 获取所有学生信息
        return jsonify(students), 200  # 返回学生数据，状态码 200
    except Exception as e:
        return {"error": str(e)}, 500  # 如果查询数据库时出错，返回 500 错误

@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()  # 获取请求中的 JSON 数据
    name = data.get('name')
    course = data.get('course')
    mark = data.get('mark')  # `mark` 是必选字段，不能为 `None`

    if not name or not course or mark is None:
        return {"error": "Missing required fields"}, 400  # 如果缺少必填字段，返回 400 错误

    try:
        # 调用 db 方法将学生信息插入到数据库
        new_student = db.insert_student(name, course, mark)
        return jsonify(new_student), 201  # 返回创建的学生信息，状态码 201
    except Exception as e:
        return {"error": str(e)}, 500  # 如果数据库插入失败，返回 500 错误

@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()  # 获取更新数据
    
    try:
        student = db.get_student_by_id(student_id)  # 查找学生
        if not student:
            return {"error": "Student not found"}, 404  # 如果学生不存在，返回 404
        
        # 更新学生信息
        updated_student = db.update_student(student_id, data)
        return jsonify(updated_student), 200  # 返回更新后的学生信息
    except Exception as e:
        return {"error": str(e)}, 500  # 如果出现异常，返回 500 错误
=======
    # TODO: replace with your implementation. This is a mock response
    return jsonify([
        {'course': 'COMP1531', 'id': 1, 'mark': 85, 'name': 'Alice Zhang'},
        {'course': 'COMP1531', 'id': 2, 'mark': 72, 'name': 'Bob Smith'}
    ]), 200


@app.route("/students", methods=["POST"])
def create_student():
    """
    Route to create a new student
    param name: The name of the student (from request body)
    param course: The course the student is enrolled in (from request body)
    param mark: The mark the student received (from request body)
    return: The created student if successful
    """

    # Getting the request body - replace with your implementation
    student_data = request.json

    pass


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    """
    Route to update student details by id
    param name: The name of the student (from request body)
    param course: The course the student is enrolled in (from request body)
    param mark: The mark the student received (from request body)
    return: The updated student if successful
    """
    pass  # replace with your implementation
>>>>>>> origin/eric/stats-feature


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
<<<<<<< HEAD
    try:
        student = db.get_student_by_id(student_id)  # 查找学生
        if not student:
            return {"error": "Student not found"}, 404  # 如果学生不存在，返回 404
        
        db.delete_student(student_id)  # 删除学生
        return '', 204  # 删除成功，返回空响应和 204 状态码
    except Exception as e:
        return {"error": str(e)}, 500  # 如果出现异常，返回 500 错误
=======
    """
    Route to delete student by id
    return: The deleted student
    """
    pass  # replace with your implementation
>>>>>>> origin/eric/stats-feature


@app.route("/stats")
def get_stats():
<<<<<<< HEAD
    try:
        stats = db.get_stats()  # 获取统计信息
        return jsonify(stats), 200  # 返回统计信息，状态码 200
    except Exception as e:
        return {"error": str(e)}, 500  # 如果出现异常，返回 500 错误
=======
    """
    Route to show the stats of all student marks 
    return: An object with the stats (count, average, min, max)
    """
    pass  # replace with your implementation
>>>>>>> origin/eric/stats-feature


@app.route("/")
def health():
    """Health check."""
    return {"status": "ok"}


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0", port=5001)
=======
    app.run(host="0.0.0.0", port=5000)
>>>>>>> origin/eric/stats-feature
