from django.db import models

class ClassPeriod(models.Model):
    start_time = models.TimeField()
end_time = models.TimeField() 
classroom = models.ForeignKey('Classroom', on_delete=models.CASCADE)
day_of_week = models.CharField(max_length=3)
course = models.ForeignKey('Course', on_delete=models.CASCADE)




def __str__(self):
     return f" {self.start_time} {self.end_time}"


