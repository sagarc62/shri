import logging

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # Log the request
        logging.info(f"Request path: {request.path}, method: {request.method}")
        # Pass the request to the next middleware or view
        response = self.get_response(request)
        return response
