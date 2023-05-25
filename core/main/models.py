from django.db import models

# Create your models here.

class Header(models.Model):

    general_title = models.CharField('General Title', max_length=50)
    img = models.ImageField('Logo Image', upload_to='images')
    path1 = models.CharField('Path 1', max_length=50)
    path2 = models.CharField('Path 2', max_length=50)
    path3 = models.CharField('Path 3', max_length=50)
    path4 = models.CharField('Path 4', max_length=50)
    path5 = models.CharField('Path 5', max_length=50)
    path6 = models.CharField('Path 6', max_length=50)
    path7 = models.CharField('Path 7', max_length=50)

    class Meta:

        verbose_name = 'Header'
        verbose_name_plural = 'Header'

class Home(models.Model):

    img = models.ImageField('Image', upload_to='images')
    title = models.CharField('Title', max_length=80)
    bold_word1 = models.CharField('Bold Part', max_length=30)
    subtitle = models.TextField('SubTitle')
    btn_name = models.CharField('Button Name', max_length=50)

    class Meta:

        verbose_name = 'Home'
        verbose_name_plural = 'Home'

class HomeContent(models.Model):

    img = models.ImageField('Image', upload_to='images')
    title = models.CharField('Title', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=80)

    def __str__(self) -> str:
        return self.title

class About(models.Model):

    img1 = models.ImageField('Image 1', upload_to='images')
    title1 = models.CharField('Title 1', max_length=80)
    text1 = models.TextField('Text 1')
    img2 = models.ImageField('Image 2', upload_to='images')
    title2 = models.CharField('Title 2', max_length=80)
    text2 = models.TextField('Text 2')

    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'About'

class WorkProces(models.Model):

    img = models.ImageField('Image', upload_to='images')
    title = models.CharField('Title', max_length=60)
    text = models.TextField('Text')

class WorkProcessContent(models.Model):

    img = models.ImageField('Image', upload_to='images')
    title = models.CharField('Title', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=100)

class Testimonial(models.Model):

    title = models.CharField('Title', max_length=80)
    text = models.TextField('Text')

class TestimonialContent(models.Model):

    img1 = models.ImageField('Image 1', upload_to='images')
    text = models.TextField('Text')
    img2 = models.ImageField('Image 2', upload_to='images')
    name = models.CharField('Name', max_length=60)
    profession = models.CharField('Profession', max_length=80)

class PricingPlan(models.Model):

    title = models.CharField('Title', max_length=80)
    text = models.TextField('Text')
    img = models.ImageField('Image', upload_to='images')
    btn_name = models.CharField('Button Name', max_length=40)

class PricingPlanOffer(models.Model):

    title = models.CharField('Title', max_length=50)
    price = models.CharField('Price', max_length=15)
    date = models.CharField('Date', max_length=50)
    offer1 = models.CharField('Offer 1', max_length=100, blank=True)
    offer2 = models.CharField('Offer 2', max_length=100, blank=True)
    offer3 = models.CharField('Offer 3', max_length=100, blank=True)
    offer4 = models.CharField('Offer 4', max_length=100, blank=True)
    offer5 = models.CharField('Offer 5', max_length=100, blank=True)
    offer6 = models.CharField('Offer 6', max_length=100, blank=True)

class PricingPlanContent(models.Model):

    count = models.PositiveIntegerField('Count')
    title = models.CharField('Title', max_length=60)
    position = models.CharField('Top Or Bottom', max_length=50)

class BlogEntries(models.Model):

    title = models.CharField('Title', max_length=60)
    text = models.TextField('Text')
    btn_name = models.CharField('Button Name', max_length=40)

    class Meta:

        verbose_name = 'Blog Entries'
        verbose_name_plural = 'Blog Entries'

class BlogEntriesContent(models.Model):

    img = models.ImageField('Image', upload_to='images')
    title = models.CharField('Title', max_length=80)
    text = models.TextField('Text')

class ContactGet(models.Model):

    title = models.CharField('Title', max_length=50)
    text1 = models.TextField('Text 1')
    subtitle = models.CharField('Subtitle', max_length=60)
    text2 = models.TextField('Text 2')
    text3 = models.TextField('Text 3')
    placeholder1 = models.CharField('Placeholder 1', max_length=50)
    placeholder2 = models.CharField('Placeholder 2', max_length=50)
    placeholder3 = models.CharField('Placeholder 3', max_length=50)
    btn_name = models.CharField('Button Name', max_length=40)

    class Meta:

        verbose_name = 'Contact GET'
        verbose_name_plural = 'Contact GET'

class ContactPost(models.Model):

    user_name = models.CharField('Username', max_length=50)
    user_email = models.EmailField('User Email')
    user_message = models.TextField('User Message')

    class Meta:

        verbose_name = 'Contact POST'
        verbose_name_plural = 'Contact POST'

    def __str__(self) -> str:
        return self.user_name
    
class Footer(models.Model):
    social1 = models.CharField('Social 1', max_length=50)
    social_url1 = models.URLField('Social Url 1')
    social2 = models.CharField('Social 2', max_length=50)
    social_url2 = models.URLField('Social Url 2')
    social3 = models.CharField('Social 3', max_length=50)
    social_url3 = models.URLField('Social Url 3')
    social4 = models.CharField('Social 4', max_length=50)
    social_url4 = models.URLField('Social Url 4')
    social5 = models.CharField('Social 5', max_length=50)
    social_url5 = models.URLField('Social Url 5')
    copyright1 = models.CharField('Copyright', max_length=200)

    class Meta:

        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'