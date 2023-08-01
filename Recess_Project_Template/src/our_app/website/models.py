
from django.db import models


class InstructorFeedback(models.Model):
    instructorName = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    courseUnit = models.CharField(max_length=100)
    knowledge = models.IntegerField(choices=[(
        20, 'Poor'), (40, 'Fair'), (60, 'Good'), (80, 'Very Good'), (100, 'Excellent')])
    communication = models.IntegerField(choices=[(
        20, 'Poor'), (40, 'Fair'), (60, 'Good'), (80, 'Very Good'), (100, 'Excellent')])
    teachingStyle = models.IntegerField(choices=[(
        20, 'Poor'), (40, 'Fair'), (60, 'Good'), (80, 'Very Good'), (100, 'Excellent')])
    responsiveness = models.IntegerField(choices=[(
        20, 'Poor'), (40, 'Fair'), (60, 'Good'), (80, 'Very Good'), (100, 'Excellent')])
    additional_comments = models.TextField()

    def __str__(self):
        return f"Feedback by {self.instructorName}"


# models.py


class FacilityFeedback(models.Model):
    name = models.CharField(max_length=100)
    facility_college = models.CharField(max_length=100)
    facility_accessibility = models.CharField(max_length=20, choices=[
        ('fully', 'Fully accessible'),
        ('partial', 'Partially accessible'),
        ('not', 'Not accessible'),
    ])
    cleanliness = models.CharField(max_length=20, choices=[
        ('very_good', 'Very Good'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('very_poor', 'Very Poor'),
    ])
    maintenance = models.CharField(max_length=20, choices=[
        ('very_good', 'Very Good'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('very_poor', 'Very Poor'),
    ])
    safety = models.CharField(max_length=20, choices=[
        ('very_good', 'Very Good'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('very_poor', 'Very Poor'),
    ])
    resource_availability = models.CharField(max_length=20, choices=[
        ('very_good', 'Very Good'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('very_poor', 'Very Poor'),
    ])
    facility_rating = models.CharField(max_length=20, choices=[
        ('very_good', 'Very Good'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('very_poor', 'Very Poor'),
    ])
    comment = models.TextField()

    def __str__(self):
        return self.name
