from rest_framework.exceptions import APIException, ValidationError

class Response400(ValidationError):
    default_code = 'error'

    def __init__(self, detail, status_code=400):
        response = {'detail': detail}
        self.detail = response
        self.status_code = status_code

# response generico -> 404, 409 
class ResponseError(APIException):
    default_code = 'error'

    def __init__(self, detail, code):
        self.detail = detail
        self.status_code = code
