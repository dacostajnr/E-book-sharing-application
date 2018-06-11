from django.db import models
# Create your models here.

class Year(models.Model):
	name =models.CharField(max_length=100) 

	def __str__(self):
		return "year "+self.name 


class Semester(models.Model):
	year = models.ForeignKey(Year,on_delete=models.CASCADE,related_name='sems')
	name = models.CharField(max_length=50) 
	cumm_name = models.CharField(max_length=50,null=True,blank=True)

	def __str__(self):
		return "{} of year {}".format(self.name,self.year.name)


class Book(models.Model):
	semester = models.ForeignKey(Semester,on_delete=models.CASCADE,related_name='books')
	name = models.CharField(max_length=50)
	date_uploaded = models.DateField(auto_now_add=True)
	file = models.FileField(upload_to='uploads/%Y/%m/%d/',null=True,blank=True)

	def __str__(self):
		return self.name+" {} {}".format(self.semester.year,self.semester)

	class Meta:
		ordering = ('-date_uploaded',)


class Other(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(null=True,blank=True)
	file = models.FileField(upload_to='uploads/%Y/%m/%d/',null=True,blank=True)
	date_uploaded=models.DateField(auto_now_add=True,null=True,blank=True)


	def __str__(self):
		return self.name

	class Meta:
		ordering = ("-date_uploaded",)







