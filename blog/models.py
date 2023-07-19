from django.db import models


class Category(models.Model):
    name = models.CharField('カテゴリー名', max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField('タイトル', max_length=50)
    text = models.TextField('テキスト')
    created_at = models.DateField('作成日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)
    category = models.ForeignKey(
        Category, verbose_name='カテゴリー',
        on_delete=models.PROTECT
    )
    created_at = models.DateField('作成日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ブログ'
        verbose_name_plural = 'ブログ'


class Comment(models.Model):
    text = models.TextField('本文')
    target = models.ForeignKey(
        Blog, on_delete=models.CASCADE,
        verbose_name='対象記事'
        )

