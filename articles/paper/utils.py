from django.db.models import *

from .models import *

menu = [{'title': 'Home', 'url': 'home'},
        {'title': 'Add Article', 'url': 'add_page'},
        {'title': 'My Articles', 'url': 'my_articles'},]

class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.annotate(Count('articles'))


        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu = user_menu[0:1]

        context['menu'] = user_menu
        context['categories'] = categories

        if "cat_selected" not in context:
            context["cat_selected"] = 0
        return context
