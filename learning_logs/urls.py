"""定义learning_logs中的URL模式"""

from django.urls import path
from . import views

app_name = "learning_logs"

urlpatterns = [
    path(r"", views.index, name="index"),                                           # 主页
    path(r"topics/", views.topics, name="topics"),                                  # 主题
    path(r"topics/<int:topic_id>/", views.topic, name="topic"),                     # 特定主题的详细页
    path(r"new_topic/", views.new_topic, name="new_topic"),                         # 添加新主题
    path(r"new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),          # 添加新条目
    path(r"edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),       # 编辑条目

]