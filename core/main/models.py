from django.db import models

# Create your models here.

class HomeSliderActive(models.Model):
    name1 = models.CharField('HomeSlider name1', max_length=30)
    name2 = models.CharField('HomeSlider name2', max_length=30)
    about = models.TextField('HomeSlider about')
    img = models.ImageField('HomeSlider image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeSliderActive'
        verbose_name_plural = 'HomeSlidersActive'


class HomeSlider(models.Model):
    name1 = models.CharField('HomeSlider name1', max_length=30)
    name2 = models.CharField('HomeSlider name2', max_length=30)
    about = models.TextField('HomeSlider about')
    img = models.ImageField('HomeSlider image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeSlider'
        verbose_name_plural = 'HomeSliders'

class HomeInfo(models.Model):
    name = models.CharField('HomeInfo name', max_length=30)
    about = models.TextField('HomeInfo about')
    img = models.ImageField('HomeInfo image', upload_to='media')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeInfo'
        verbose_name_plural = 'HomeInfos'

class Inf(models.Model):
    name1 = models.CharField('Inf name1', max_length=30)
    name2 = models.TextField('Inf name2', max_length=30)
    img = models.ImageField('Inf image', upload_to='media')


    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'Inf'
        verbose_name_plural = 'Infs'



class HomeProduct(models.Model):
    name = models.CharField('Product name', max_length=30)
    img = models.ImageField('Product image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeProduct'
        verbose_name_plural = 'HomeProducts'


class HomeSlider1Active(models.Model):
    name1 = models.CharField('HomeSlider1 name1', max_length=30)
    name2 = models.CharField('HomeSlider1 name2', max_length=30)
    about = models.TextField('HomeSlider1 about')


    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeSlider1Active'
        verbose_name_plural = 'HomeSlider1sActive'


class HomeSlider1(models.Model):
    name1 = models.CharField('HomeSlider1 name1', max_length=30)
    name2 = models.CharField('HomeSlider1 name2', max_length=30)
    about = models.TextField('HomeSlider1 about')


    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeSlider1'
        verbose_name_plural = 'HomeSlider1s'