from flask import jsonify


class Routes:
    def __init__(self, app, repository):
        self.repository = repository
        self.app = app
        self.app.route('/v1/student/<int:student_id>', methods=['GET'], endpoint='get_student_id')

    def get_student_id(self, user_id):
            try:
                result = self.repository.get_student_by_id(user_id)
                return jsonify(result), 200
            except Exception as e:
                print(e)
