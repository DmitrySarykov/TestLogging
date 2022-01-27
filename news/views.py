from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.debug('Debug sample')
    logger.info('Info sample')
    logger.warning('Warning sample')
    logger.error('Error sample')
    logger.critical('Critical sample')

    return render(request,'index.html')