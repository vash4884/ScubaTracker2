from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from uuid import uuid4
from tracker.choices  import *
#for sake of cleanliness this will be used so extra templates won't have to be used. This will never be saved it's just being used for instance.
#if true will be used for loadProject, if false it will be used for newProject
class course(models.Model):

    courseID      = models.CharField(max_length=42, unique=True, null=False, blank=False, default=uuid4)
    date          = models.DateField()
    instuctor1ID    = models.CharField(max_length=42, unique=False, null=True, blank=True, default=uuid4)
    instuctor2ID   = models.CharField(max_length=42, unique=False, null=True, blank=True, default=uuid4)
    instuctor3ID    = models.CharField(max_length=42, unique=False, null=True, blank=True, default=uuid4)

#per student for discover/practice/reactivate
class discoverPracticeReactiveClassStudent(models.Model):
    courseFilter  = models.ForeignKey(course, on_delete=models.CASCADE)
    studentID = models.CharField(max_length=42, unique=True, null=False, blank=False, default=uuid4)


#per student for rescue
class rescueCourseClassStudent(models.Model):
    courseFilter  = models.ForeignKey(course, on_delete=models.CASCADE)
    studentID = models.CharField(max_length=42, unique=True, null=False, blank=False, default=uuid4)

#per student for specialty
class specialtyCourseClassStudent(models.Model):
    courseFilter  = models.ForeignKey(course, on_delete=models.CASCADE)
    studentID = models.CharField(max_length=42, unique=True, null=False, blank=False, default=uuid4)

#per student for open aow
class openAOWStudent(models.Model):
    courseFilter  = models.ForeignKey(course, on_delete=models.CASCADE)
    studentID = models.CharField(max_length=42, unique=True, null=False, blank=False, default=uuid4)

class student(models.Model):
   name = models.CharField(max_length=255, null=False, blank=False)
   studentID = models.CharField(max_length=42, unique=True, null=False, blank=False, default=uuid4)
   #current class ID Delete after Class is over
   # rescueClassID= models.CharField(max_length=42, unique=True, null=False, blank=False, default=uuid4)
   # openAOWClassID= models.CharField(max_length=42, unique=True, null=False, blank=False, default=uuid4)
   # specialtyClassID= models.CharField(max_length=42, unique=True, null=False, blank=False, default=uuid4)
   phoneNumber =  models.CharField(max_length=255, null=False, blank=False,  default = None)
   rescueCert = models.BooleanField(null=False, default=False)
   rescueClassID  = models.CharField(max_length=42, unique=True, null=True, blank=True, default=uuid4)
   rescueorientation      = models.BooleanField(null=False, default=False)
   rescuereview      = models.BooleanField(null=False, default=False)
   rescuepool      = models.BooleanField(null=False, default=False)
   rescueperch      = models.BooleanField(null=False, default=False)
   rescueCPR      = models.BooleanField(null=False, default=False)
   rescuemedical      = models.BooleanField(null=False, default=False)
   rescuecomleted      = models.BooleanField(null=False, default=False)
   rescuecomments    = models.CharField(max_length=255, null=False, blank=False,  default = None)
   discoverpoolPractice      = models.BooleanField(null=False, default=False)
   discoverdiscover      = models.BooleanField(null=False, default=False)
   discoverreactivate      = models.BooleanField(null=False, default=False)
   discoverrental      = models.BooleanField(null=False, default=False)
   discoverpersonal      = models.BooleanField(null=False, default=False)
   discovercomleted      = models.BooleanField(null=False, default=False)
   discovercomments    = models.CharField(max_length=255, null=False, blank=False, default = None)
   openAOWOrientation = models.BooleanField(null=False, default=False)
   openAOWextReactiv = models.BooleanField(null=False, default=False)
   openAOWPool = models.BooleanField(null=False, default=False)
   openAOWBH = models.BooleanField(null=False, default=False)
   openAOWAdvanced = models.BooleanField(null=False, default=False)
   openAOWmedical = models.BooleanField(null=False, default=False)
   openAOWbcd  = models.IntegerField(null=False, choices=BCD_SIZE, default=1, validators=[MinValueValidator(0), MaxValueValidator(5)])
   openAOWwetsuit  = models.IntegerField(null=False, choices=BCD_SIZE, default=1, validators=[MinValueValidator(0), MaxValueValidator(5)])
   openAOWcompleted = models.BooleanField(null=False, default=False)
   openAOWcomments    = models.CharField(max_length=255, null=False, blank=False,  default = None)
   openAOWDeep = models.BooleanField(null=False, default=False)
   openAOWNav = models.BooleanField(null=False, default=False)
   openAOWPeak = models.BooleanField(null=False, default=False)
   openAOWNight = models.BooleanField(null=False, default=False)
   openAOWDSMB = models.BooleanField(null=False, default=False)
   openAOWNitrox = models.BooleanField(null=False, default=False)
   specialtyNav = models.BooleanField(null=False, default=False)
   specialtyDeep  = models.BooleanField(null=False, default=False)
   specialtyAltitude = models.BooleanField(null=False, default=False)
   specialtyPhoto = models.BooleanField(null=False, default=False)
   specialtyFish = models.BooleanField(null=False, default=False)
   specialtyNight = models.BooleanField(null=False, default=False)
   specialtyPeak = models.BooleanField(null=False, default=False)
   specialtySearch = models.BooleanField(null=False, default=False)
   specialtyDSMB = models.BooleanField(null=False, default=False)
   specialtyWreck = models.BooleanField(null=False, default=False)
   specialtyNitrox = models.BooleanField(null=False, default=False)
   specialtySideTech = models.BooleanField(null=False, default=False)
   specialtyDPV = models.BooleanField(null=False, default=False)
   specialtyComments =  models.CharField(max_length=255, null=False, blank=False,  default = None)
class instructor(models.Model):
   name = models.CharField(max_length=255, null=False, blank=False)
   instructorID = models.CharField(max_length=42, unique=True, null=False, blank=False, default=uuid4)
