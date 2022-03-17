from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所以的主题
    path('topics/', views.topics, name='topics'),
    # 显示测试内容
    path('selfmade/', views.selfmade, name='selfmade'),
    # 点击相应主题显示内容
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 添加新主题的页面
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面。
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 用于编辑已有条目的页面
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
