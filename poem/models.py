from django.db import models

class Poem(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    author = models.CharField(max_length=100, verbose_name="작가")
    content = models.TextField(verbose_name="내용")
    published_year = models.IntegerField(blank=True, null=True, verbose_name="발표 연도")
    
    tags = models.ManyToManyField('Tag', blank=True, related_name="poems", verbose_name="태그")  # 추가

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")

    def __str__(self):
        return f"{self.title} - {self.author}"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="태그명")

    def __str__(self):
        return self.name

class Appreciation(models.Model):
    poem = models.ForeignKey('Poem', on_delete=models.CASCADE, related_name="appreciations", verbose_name="시")
    reviewer_name = models.CharField(max_length=100, verbose_name="작성자명")
    content = models.TextField(verbose_name="감상문")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")

    def __str__(self):
        return f"{self.reviewer_name}의 감상문"
