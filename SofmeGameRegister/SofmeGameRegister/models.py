from django.db import models

class Form(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game_name = models.CharField(max_length = 256)
    game_id = models.IntegerField()
    description = models.TextField()
    
    panel = models.ImageField()
    panel_path = models.FilePathField()

    img = models.ImageField()
    img_path = models.FilePathField()

    movie = models.FileField(blank = True,null = True)
    movie_path = models.FilePathField(blank = True,null = True)

    game_file = models.FileField()

    submit_time = models.DateTimeField(blank = True,null = True)

    def submit(self):
        self.submit_date = timezone.now()
        self.save()

    def __str__(self):
        return self.game_name