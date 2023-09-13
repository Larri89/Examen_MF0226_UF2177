class Repository:
    def __init__(self, connector_database):
        self.connector = connector_database

    def get_student_by_id(self, user_id):
        query = "SELECT * FROM `people` WHERE id=%d" %user_id
        result = self.connector.execute(query)
        return result


