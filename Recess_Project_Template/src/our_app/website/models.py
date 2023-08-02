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



class Course(models.Model):
    courseName = models.CharField(max_length=100)
    courseCode = models.CharField(max_length=100)
    courseDescription = models.CharField(max_length=1000)
    effectiveness = models.IntegerField(
        choices=[(20, 'Poor'), (40, 'Fair'), (60, 'Good'), (80, 'Very Good'), (100, 'Excellent')])
    interest = models.IntegerField(
        choices=[(20, 'Poor'), (40, 'Fair'), (60, 'Good'), (80, 'Very Good'), (100, 'Excellent')])
    improvement = models.TextField()
# Create the model class for the feedback form
class FacilityFeedback(models.Model):
    # Fields for Facility Information
    name = models.CharField(max_length=100, verbose_name="Facility name")
    facility_college = models.CharField(
        max_length=100, verbose_name="College of facility")
    facility_accessibility = models.CharField(max_length=20, choices=[
        ('fully', 'Fully accessible'),
        ('partial', 'Partially accessible'),
        ('not', 'Not accessible'),
    ], verbose_name="Facility accessibility")

    # Fields for Facility Ratings
    cleanliness = models.CharField(max_length=20, choices=[
        ('very_good', 'Very Good'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('very_poor', 'Very Poor'),
    ], verbose_name="Cleanliness and Hygiene")

    maintenance = models.CharField(max_length=20, choices=[
        ('very_good', 'Very Good'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('very_poor', 'Very Poor'),
    ], verbose_name="Maintenance")

    safety = models.CharField(max_length=20, choices=[
        ('very_good', 'Very Good'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('very_poor', 'Very Poor'),
    ], verbose_name="Safety and Security")

    resource_availability = models.CharField(max_length=20, choices=[
        ('very_good', 'Very Good'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('very_poor', 'Very Poor'),
    ], verbose_name="Resource Availability")

    facility_rating = models.CharField(max_length=20, choices=[
        ('very_good', 'Very Good'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('very_poor', 'Very Poor'),
    ], verbose_name="Overall facility rating")

    # Field for Additional Comments
    comment = models.TextField(
        verbose_name="Additional Comments or Suggestions", blank=True)

    def __str__(self):
        return self.name
