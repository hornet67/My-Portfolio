from django.db import models

# Create your models here.

class contacts(models.Model):
        name = models.CharField(max_length=20)
        email = models.CharField(max_length=40,unique=True)
        message = models.TextField(max_length=100)

        class Meta:
                verbose_name='Contact'
                verbose_name_plural = 'Contact'
                  

        def __str__(self):
                return self.name 


class Portfolio(models.Model):
        image = models.ImageField(upload_to='upload')
        title = models.CharField(max_length=15)
        descriptions = models.TextField(max_length=160)

        class Meta:
                verbose_name ='Portfolio'
                verbose_name_plural = 'Portfolio'

        def __str__(self):
                return self.title
        
class Document(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')

    class Meta:
        verbose_name ="Document"
        verbose_name_plural = "Document"

    def __str__(self):
           return self.title