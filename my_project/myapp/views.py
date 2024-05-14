from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.info("Index page accessed")
    return HttpResponse("Hello, world. You're at the best site in the world")


def about(request):
    try:
        #  some code that might raise an exception
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse('Oops! Something went wrong.')
    else:
        logger.debug(f'About page accessed')
        return HttpResponse("This is about page")
