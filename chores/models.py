from django.db import models
from clients.models import ClientsUsers


class ChoresPost(models.Model):  # Job post
    ChoresPost_TYPE_CHOICE = (  # job category
        ('1', 'Vodoinstalater\ka'),
        ('2', 'Eelektricar\ka'),
        ('3', 'Moler\ka'),
        ('4', 'Stolar\ka'),
        ('5', 'IT'),
        ('6', 'Zidar\ka'),
        ('7', 'Cistac\ica')
    )
    user_of_post = models.ForeignKey(ClientsUsers, null=True, on_delete=models.CASCADE)
    post_id = models.BigAutoField(primary_key=True)  # ID
    name = models.CharField(max_length=50, null=False, blank=False, db_index=True)  # name of post
    bio = models.TextField(null=False, blank=False)  # description
    date_of_post = models.DateTimeField(auto_now=True)  # time of post
    category = models.CharField(max_length=100, choices=ChoresPost_TYPE_CHOICE)  # category
    budget = models.IntegerField(default=0)  # price
    date = models.DateField(null=True)
    post_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return 'Time of post:{} || Description:{} || Name of post:{}'.format(self.date_of_post, self.bio, self.name)
