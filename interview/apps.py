from django.apps import AppConfig


class InterviewConfig(AppConfig):
    name = 'interview'

import json, logging
logger = logging.getLogger('interview.signal_processor')

class CandidateConfig(AppConfig):
    name = 'interview'

    def ready(self):
        logger.info('CandidateConfig ready')
        from interview.signal_processor import post_save_callback
