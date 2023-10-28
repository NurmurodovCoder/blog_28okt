from django.db import models
from ckeditor.fields import RichTextField


class Person(models.Model):
    name = models.CharField(max_length=100)
    bio = RichTextField()
    img = models.ImageField(upload_to='media/person')
    mini_bio = models.CharField(max_length=100)

    twitter = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)

    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

 
class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class Post(models.Model):
    title = models.CharField(max_length=250)
    text = RichTextField()
    img = models.ImageField(upload_to='media/post')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)
    comment = models.ForeignKey('Comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # @property
    # def reate_time(self):
    #     l = len(self.text)
    #     print(l, '------------------------------------------------------------------------------------------------')


class Comments(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.CharField(max_length=50)
    text = models.CharField(max_length=250)

    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @property
    def getReplies(self):
        return Comments.objects.filter(parent=self).reverse()
    
    @property
    def isParent(self):
        if self.parent is None:
            return True
        return False


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

