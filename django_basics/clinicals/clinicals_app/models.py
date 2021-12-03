from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()


class ClinicalData(models.Model):
    HEIGHT_WEIGHT = 'height / weight'
    BLOOD_PRESSURE = 'blood pressure'
    HEART_RATE = 'heart rate'

    COMPONENT_NAMES = [('hw', HEIGHT_WEIGHT), ('bp', BLOOD_PRESSURE), ('hr', HEART_RATE)]

    name = models.CharField(max_length=2, choices=COMPONENT_NAMES)
    value = models.CharField(max_length=20)
    measured_time = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)