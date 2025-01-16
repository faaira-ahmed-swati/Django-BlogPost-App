from django.urls import path
from .views import (
    blog_post_create_view,
    # blog_post_detail_page_by_id,
    # blog_post_detail_page_by_slug,
    blog_post_detail_view,
    blog_post_delete_view,
    blog_post_list_view,
    blog_post_update_view,
)

urlpatterns = [
    path('', blog_post_list_view),
    path('blog-new/', blog_post_create_view),
    path('<str:slug>/', blog_post_detail_view),
    path('<str:slug>/edit/', blog_post_update_view),
    path('<str:slug>/delete/', blog_post_delete_view),
    # path('<str:slug>/', blog_post_detail_page_by_slug),
    # path('<int:id>/', blog_post_detail_page_by_id),
    # # Another way to write the above statement
    # re_path(r'^(?P<id>\d+)/$', blog_post_detail_page_by_id),
]
