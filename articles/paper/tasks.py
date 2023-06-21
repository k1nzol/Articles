from celery import shared_task
from django.utils import timezone
from .models import Articles

@shared_task(bind=True)
def publish_articles(self):
    now = timezone.now()
    print(now)
    articles_to_publish = Articles.objects.filter(publication_datetime__lte=now, is_published=False)
    print(articles_to_publish)

    for article in articles_to_publish:
        article.is_published = True
        article.save()

    return 'Done'