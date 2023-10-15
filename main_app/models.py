from django.db import models

# Create your models here.

# Contact form

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=100)
    massage = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'ContactForm'

    def __str__(self):
        return self.name


# Properties

class Profile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pros')
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = ("Profile")
    
    def __str__(self):
        return self.name

class Profile_p(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pros')
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = ("Profile_1")
    
    def __str__(self):
        return self.name


class Profile_2(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pros')
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = ("Profile_2")

    def __str__(self):
        return self.name
    


class Profile_3(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pros')
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = ("Profile_3")

    def __str__(self):
        return self.name


class Profile_4(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pros')
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = ("Profile_4")

    def __str__(self):
        return self.name



class Profile_5(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pros')
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = ("Profile_5")

    def __str__(self):
        return self.name



class Profile_6(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pros')
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = ("Profile_6")

    def __str__(self):
        return self.name
    

class Profile_7(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pros')
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = ("Profile_7")

    def __str__(self):
        return self.name



class Profile_8(models.Model):
    name = models.CharField(max_length=100)
    image =  models.ImageField(upload_to='pros')
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = ("Profile_8")

    def __str__(self):
        return self.name


# about

class About_1(models.Model):
    quality = models.CharField(max_length=300)
    rated = models.CharField(max_length=300)
    easy = models.CharField(max_length=300)
    image = models.ImageField(upload_to='pros')


    class Meta:
        verbose_name_plural = ("About_1")

    def __str__(self):
        return self.quality
    

class About_2(models.Model):
    quality = models.CharField(max_length=300)
    rated = models.CharField(max_length=300)
    easy = models.CharField(max_length=300)
    image = models.ImageField(upload_to='pros')


    class Meta:
        verbose_name_plural = ("About_2")

    def __str__(self):
        return self.quality
    

# Home

class home(models.Model):
    properties = models.CharField(max_length=300)
    rated = models.CharField(max_length=300)
    Legit = models.CharField(max_length=300)
    image = models.ImageField(upload_to='pros')


    class Meta:
        verbose_name_plural = ("home")

    def __str__(self):
        return self.properties

