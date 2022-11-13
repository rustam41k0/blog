from mysite.models import *

latest_posts = Posts.objects.order_by('-time_create')[:2]
latest_comments = Comments.objects.order_by('-time_create')[:5]
category = Category.objects.all()
