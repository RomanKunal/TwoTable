from django.db import models

class Doctor(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100)
    user_specialisation = models.CharField(max_length=100)

class Patient(models.Model):
    pat_id=models.IntegerField()
    pat_name=models.CharField(max_length=100)
    disease=models.CharField(max_length=100)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
