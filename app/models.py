from django.db import models

class InputForm(models.Model):
    name = models.CharField(max_length=200, unique=False)
    roll_number = models.IntegerField(help_text="Enter 6 digit roll number", unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, help_text='Required. Inform a valid email address.',unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Input Form"
        verbose_name_plural = "Input Forms"