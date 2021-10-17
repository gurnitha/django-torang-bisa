# app/proyek/models.py

# Django modules
from django.db import models
import uuid # untuk mengesampingkan default id pada table

# Locals

# Create your models here.

# Nama model:Proyek
class Project(models.Model):
    title = models.CharField(
    	max_length=200,
    	blank=False,
    	help_text="Field ini tidak boleh dikosongkan.")
    description = models.TextField(
    	null=True, 
    	blank=True,
    	help_text="Field ini boleh dikosongkan.")
    demo_link = models.CharField(
    	max_length=2000, 
    	null=True, 
    	blank=True,
    	help_text="Field ini boleh dikosongkan.")
    source_link = models.CharField(
    	max_length=2000, 
    	null=True, 
    	blank=True,
    	help_text="Field ini boleh dikosongkan.")
    created = models.DateTimeField(
    	auto_now_add=True,
    	help_text="Bisa dimodifikasi bila diperlukan.")
    '''uuid dimaksudkan untuk mengesampingkan 
	default id pada tabel dan digunakan 
	sebagai primary key dan tidak bisa diedit'''
    id = models.UUIDField(
    	default=uuid.uuid4, 
    	unique=True,
    	primary_key=True, 
    	editable=False,
    	help_text="Tidam bisa diedit.")

    # Men-define string method
    def __str__(self):
    	return self.title




