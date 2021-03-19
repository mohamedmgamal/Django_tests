from django.utils.deprecation import  MiddlewareMixin
class customeMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        print("middleware"+exception.massage)
        return None