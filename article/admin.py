from django.contrib import admin
from article.models import Article
from article.models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "publish_date")


admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "article")


admin.site.register(Comment, CommentAdmin)