from django.db import models

class Destination(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    main_image = models.ImageField(upload_to='travel_pics/') # വലിയ ഫോട്ടോയ്ക്കായി
    small_image = models.ImageField(upload_to='travel_pics/') # നീല ബോക്സിലെ ചെറിയ ഫോട്ടോയ്ക്കായി
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
