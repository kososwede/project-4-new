from django.shortcuts import render_to_response


def handler404(request, exception, template_name="errors/error_404.html"):
    '''
    404 Error Handler
    '''
    response = render_to_response(template_name)
    response.status_code = 404
    return response


def handler500(request, template_name="errors/error_500.html"):
    '''
    500 Error Handler
    '''
    response = render_to_response(template_name)
    response.status_code = 500
    return response