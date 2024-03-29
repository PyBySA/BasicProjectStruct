class Result():

    def __init__(self):
        self.result_code = 0
        self.result_obj = []
        self.result_count = 0
        self.result_message = ""

    def get(self):
        return {"code": self.result_code, "object": self.result_obj, "row_count": self.result_count,
                "message": self.result_message}

    def set(self, result_code, result_obj, result_count=0, result_message=""):
        self.result_code = result_code
        self.result_obj = result_obj
        self.result_count = result_count
        self.result_message = result_message
