from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone


# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.caption}'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_addres = models.EmailField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


    def __str__(self):
        return self.full_name()



class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=400)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    # creeare relatie foreignKey
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True ,related_name="posts")
    tag = models.ManyToManyField(Tag)



class Transfer(models.Model):
    player_name = models.CharField(max_length=100)
    from_team = models.CharField(max_length=100)
    to_team = models.CharField(max_length=100)
    fee = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField(default='description')
    image = models.ImageField(upload_to='players/', null=True, blank=True)

    def __str__(self):
        return f"{self.player_name}: {self.from_team} → {self.to_team}"




class Rumor(models.Model):
    player_name = models.CharField(max_length=100)
    from_team = models.CharField(max_length=100)
    source = models.CharField(max_length=100 , default='necunoscut')
    credibility = models.IntegerField(default=3)  
    date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='rumors/', null=True, blank=True)

    def __str__(self):
        return f"Zvon: {self.player_name} de la {self.from_team}"




class Player(models.Model):
    POSITION_CHOICES = [
        ('GK', 'Goalkeepr'),
        ('DF', 'Defender'),
        ('MF', 'Midfielde'),
        ('FW', 'Forward'),
    ]

    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField()
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    photo = models.ImageField(upload_to='players/')  
    is_starting = models.BooleanField(default=False)  
    x_pos = models.FloatField(null=True, blank=True)  
    y_pos = models.FloatField(null=True, blank=True)  

    def __str__(self):
        return f"{self.name} ({self.number})"
    


    from django.db import models



class Match(models.Model):
    opponent = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"Real Madrid vs {self.opponent} on {self.date}"


    


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)  # Poți adăuga validare manuală dacă vrei

    def __str__(self):
        return f"Comment by {self.name}"



class Legend(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='legends/')
    position = models.CharField(max_length=50)
    years_active = models.CharField(max_length=100)

    def __str__(self):
        return self.name
