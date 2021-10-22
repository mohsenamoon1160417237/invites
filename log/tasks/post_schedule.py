from celery import shared_task
from celery.utils.log import get_task_logger
from log.models.PostLog import PostLog
from django.shortcuts import get_object_or_404

logger = get_task_logger(__name__)


@shared_task
def post_schedule(post_id):
    post = get_object_or_404(PostLog , id=post_id)
    post.status = PostLog.PUBLISH
    post.save()
    logger.info("the post saved as publish!")