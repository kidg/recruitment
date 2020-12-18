# -*- coding: utf-8 -*-
__author__ = 'RedWall'

import time
import logging
import traceback
from interview import dingtalk
from django.http import HttpResponse
from sentry_sdk import capture_exception,capture_message

logger = logging.getLogger(__name__)

def performance_logger_middleware(get_response):
    def middleware(request):
        start_time = time.time()
        response = get_response(request)
        duration = time.time() - start_time
        response["X-Page-Durarion-ms"] = int(duration * 1000)
        logger.error("%s %s %s", duration, request.path, request.GET.dict())
        return response

    return middleware

class PerformanceAndExceptionLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        response["X-Page-Durarion-ms"] = int(duration * 1000)
        logger.info("%s %s %s", duration, request.path, request.GET.dict())
        if duration > 300:
            capture_message("slow request for url:%s duration %s"%(request.build_absolute_uri(), duration))
        return response

    def process_exception(self, request, exception):
        if exception:
            message = "url:{url} ** msg:{error}'''''{tb}''''".format(
                url = request.build_absolute_uri(),
                error = repr(exception),
                tb = traceback.format_exc()
            )
            logger.warning(message)
            dingtalk.send(message)
            capture_exception(exception)

        return HttpResponse("Error processiog the request")

