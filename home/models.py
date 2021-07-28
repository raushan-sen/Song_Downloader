from django.db import models
# from django.db.models.fields import SlugField
# from django.utils.text import slugify

class Genere(models.Model):
    CategeryName=models.CharField(max_length=50)
    Slug=models.SlugField(max_length=50,unique=True,null=True,blank=True)

    def __str__(self):
        return self.CategeryName
    # def save(gt,*args, **kwargs):
    #     gt.Slug=slugify(gt.CategeryName)
    #     super(Genere.gt).save(*args, **kwargs)
    class Meta:
        ordering = ['-pk']

class Singer(models.Model):
    Name=models.CharField(max_length=50)

    def __str__(self):
        return self.Name
    class Meta:
        ordering = ['-pk']

class Song(models.Model):
    SongName=models.CharField(max_length=1000)
    Lyrics=models.TextField()
    SongWriter=models.CharField(max_length=1000)
    Genere=models.ForeignKey(Genere, on_delete=models.CASCADE)
    singerName=models.ManyToManyField(Singer)
    YoutubeId=models.CharField(max_length=20)
    Short=models.TextField()
    DateTime=models.DateField(auto_now=False, auto_now_add=False)
    Album=models.CharField(max_length=50,null=True,blank=True)
    Slug=models.SlugField(max_length=40,null=True,blank=True,unique=True)
    View=models.IntegerField(default=0)

    def __str__(self):
        return self.SongName
    class Meta:
        ordering = ['-pk']

    # def save(self,*args, **kwargs):
    #     self.Slug=slugify(self.SongName)
    #     super(Song.self).save(*args, **kwargs)

class Setup(models.Model):
    Site_Name=models.CharField(max_length=50,default='Hello World')
    Site_decs=models.CharField(max_length=101,default='site Name')
    Favicon=models.ImageField(upload_to='static/Favicon')
    Short_story=models.TextField()
    Telegram_url=models.CharField(max_length=70)


