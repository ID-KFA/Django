# from django.contrib import admin
#
# from .models import AuthorsModel, ArticleModel, Comment
#
#
# # Register your models here.
# # admin.site.register(ArticleModel)
# # admin.site.register(AuthorsModel)
# # admin.site.register(Comment)
#
#
# # author = models.ForeignKey(AuthorsModel, on_delete=models.CASCADE)
# # title = models.CharField(max_length=200)
# # text = models.TextField()
# # pubicated_date = models.DateTimeField(auto_now_add=True)
# #
# # category = models.CharField(max_length=100)
# # views_count = models.IntegerField(default=0)
# # publicated_flag = models.BooleanField(default=False)
#
# @admin.register(ArticleModel)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ["author", "title", "text", "category"]
#     readonly_fields = ["pubicated_date", "views_count"]
#     fieldsets = [
#         (
#             None,
#             {
#                 'classes': ['wide'],
#                 'fields': ['author'],
#             },
#         ),
#         (
#             'Подробности',
#             {
#                 'classes': ['collapse'],
#                 'description': 'Текст статьи',
#                 'fields': ["title", 'text'],
#             },
#         ),
#         (
#
#             'Категория и дата публикации',
#             {
#                 'fields': ['category', 'pubicated_date'],
#             },
#         ),
#         (
#             'Число просмотров',
#             {
#                 'description': 'Статистика',
#                 'fields': ['views_count',"publicated_flag"],
#             }
#         ), ]
#
#     # name = models.CharField(max_length=100)
#     # surname = models.CharField(max_length=100)
#     # email = models.EmailField()
#     # bio = models.TextField()
#     # dob = models.DateField()
#     # fullname = models.CharField(blank=Tru
#
#
# @admin.register(AuthorsModel)
# class AuthorsAdmin(admin.ModelAdmin):
#
#
#     list_display = ["fullname", "bio", "dob", "email"]
#     readonly_fields = ["dob"]
#
#     fieldsets = [
#         (
#             None,
#             {
#                 'classes': ['wide'],
#                 'fields': ['fullname'],
#             },
#         ),
#         (
#             'Биография автора',
#             {
#                 'classes': ['collapse'],
#                 'description': 'Подробности',
#                 'fields': ["dob","bio"]
#             },
#         ),
#         (
#
#             'Контактные данные',
#             {
#                 'description': 'Электронная почта',
#                 'fields': ['email']
#             },
#         ),
#
#          ]
#
#
#
# # author = models.ForeignKey(AuthorsModel, on_delete=models.CASCADE)
# #     article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
# #     text = models.TextField()
# #     changed_date = mo
#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ["author", "article", "text", "changed_date"]
