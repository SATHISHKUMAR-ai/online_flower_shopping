from django.db import models

class flower_details(models.Model):
	flower_id = models.CharField(max_length=10)
	flower_name = models.CharField(max_length=25)
	flower_category = models.CharField(max_length=25)
	flower_price = models.CharField(max_length=100)
	flower_image = models.FileField(max_length=100, upload_to='', 
									blank=True, null=True )
	class Meta:
		db_table = "flower_details"

class new_login_reaister(models.Model):
	user_name = models.CharField(max_length=10)
	user_phone_no = models.CharField(max_length=10)
	user_email = models.CharField(max_length=50)
	user_password = models.CharField(max_length=15)
	class Meta:
		db_table = "new_login_reaister"

class order_details(models.Model):
	flower_id = models.CharField(max_length=100)
	date = models.CharField(max_length=15)
	image = models.FileField(max_length=100, upload_to='',
							 blank=True, null=True)
	name = models.CharField(max_length=20)
	category = models.CharField(max_length=20)
	phone_no = models.CharField(max_length=10)
	address = models.CharField(max_length=500)
	username = models.CharField(max_length=25)
	order_quantity = models.CharField(max_length=20)
	amount = models.CharField(max_length=20)
	total_amount = models.CharField(max_length=100)
	status = models.CharField(max_length=20)
	review = models.CharField(max_length=30)
	feedback = models.CharField(max_length=50)
	class Meta:
		db_table = "order_details"

class cart(models.Model):
	flower_id = models.CharField(max_length=100)
	username = models.CharField(max_length=10)
	flower_name = models.CharField(max_length=20)		
	category = models.CharField(max_length=20)
	flower_image = models.FileField(max_length=500, upload_to='',
									 blank=True, null=True)
	order_quantity = models.CharField(max_length=10)
	price = models.CharField(max_length=10)
	total_price = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	phone_no = models.CharField(max_length=15)
	class Meta:
		db_table = "Add_cart"