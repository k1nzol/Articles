Russian version

Для запуска сайта необходимо быть в папке ../articles и открыть 3 терминала и вписать туда следующие команды.

Terminal 1: python manage.py runserver
Terminal 2: celery -A articles.celery worker --pool=solo -l info
Terminal 3: celery -A articles beat -l info

Этот пет проект про различные статьи на разные темы. Для создания статьи, просмотра всех ваших статей и создания комментариев необходимо авторизоваться!

Фичи:
1) Celery. Возможность отложить момент выпуска статьи на фиксированное время которое выберите.
2) Пагинация. Все статьи разбиты на несколько страниц, на каждой по 3 статьи.
3) Комментарии. Под каждую статью можно написать комментарии.
4) Ссылки. Все ссылки сделаны со slug-ом. К примеру при открытии статьи про яблоки ссылка будет ../post/apple

Мини фичи:
1) Можно выбрать все статьи определённой категории в меню слева.
2) Система регистрации и авторизации.
3) Возможность открыть полную статью.
4) Кнопка My Articles дает возможность посмотреть все ваши статьи, даже те которые скоро будут опубликованы.


_______________________________________________________________
English version


To launch the website, you need to be in the ../articles directory and open 3 terminals, then enter the following commands:

Terminal 1: python manage.py runserver
Terminal 2: celery -A articles.celery worker --pool=solo -l info
Terminal 3: celery -A articles beat -l info

This pet project is about various articles on different topics. To create an article, view all your articles, and make comments, you need to log in!

Features:
1) Celery: Ability to schedule the release of an article at a specific time of your choice.
2) Pagination: All articles are divided into several pages, with 3 articles per page.
3) Comments: You can write comments for each article.
4) Links: All links are generated with slugs. For example, when opening an article about apples, the link will be ../post/apple.


Mini Features:
1) You can select all articles of a specific category in the left menu.
2) Registration and authentication system.
3) Ability to view the full article.
4) The "My Articles" button allows you to see all your articles, including those that will be published soon.