from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from flower_shop_app.models import flower_details,new_login_reaister,order_details,cart
import datetime

#This firstpage function
def firstpage(request):
	return render(request,'firstpage.html')

#This firstpage nav bar function. The click home nav bar go to  
#customer page.  
def homepage(request):
	res=flower_details.objects.all()
	print(res)
	return render(request, 'homepage.html',
					{'result':res})

#This firstpage nav bar function. The click admin nav bar go to adminlogin page.  
def adminlogin(request):
	return render(request, 'adminlogin.html')

#This is admin password checking.
def checklog(request):
	if request.method=='POST':
		un = request.POST['name']
		ps = request.POST['pass']	
		if un == "admin" and ps == "admin":
			
			request.session['user'] = un
			return HttpResponseRedirect('adminpage')
		else:
			re = "invalid login"
		return render(request,'adminlogin.html',
						{'result':re})
#This admin home.
def adminpage(request):
	if request.session.has_key('user'):
		un = request.session['user']
		res = flower_details.objects.all()
		print(res)
		return render(request,'adminpage.html',
						{'result':res,'uname':un})
	else:
		return render(request, 'adminlogin.html')

#This admin flower list add page. 
def addflower1(request):
	return render(request, 'addflower.html')		

#This flower lists store in database
def adminstore(request):
	if request.method == 'POST':
		i = request.POST['id']
		name = request.POST['name']
		cat = request.POST['cat']
		price = request.POST['price']
		image = request.FILES['image']

		flowerDetails = flower_details()
		flowerDetails.flower_id = i
		flowerDetails.flower_name = name
		flowerDetails.flower_category = cat
		flowerDetails.flower_price = price
		flowerDetails.flower_image = image
		flowerDetails.save()
		messages.success(request,"Data Stored Successfully")
		res = flower_details.objects.all()
		print(res)
		return render(request,'adminpage.html',
						{'result':res})
#The admiin view flower lists.
def adminhome(request):	
	res = flower_details.objects.all()
	print(res)
	return render(request,'adminpage.html',
					{'result':res})

#This admin flower details edit page 
def adminrecord(request,id):
		res = flower_details.objects.get(id=id)
		return render(request,'adminediter.html',
						{'user':res})

#This admin flower details update database
def adminupdata(request,id):
	if request.method == 'POST':
		i = request.POST['id']
		name = request.POST['name']
		cat = request.POST['cat']
		price = request.POST['price']
		image = request.FILES['image']

		flowerDetails = flower_details.objects.get(id=id)
		flowerDetails.flower_id = i
		flowerDetails.flower_name=name
		flowerDetails.flower_category = cat
		flowerDetails.flower_price = price
		flowerDetails.flower_image = image
		flowerDetails.save()
		messages.success(request,"Data Updated Successfully")
		return HttpResponseRedirect('/adminhome')

def adminvieworder(request):
	res = order_details.objects.all()
	print(res)
	return render(request, 'adminorder.html',
					{'result':res})

def goback(request):
	res = flower_details.objects.all()
	print(res)
	return render(request,'adminpage.html',
					{'result':res})

#This flower details delete in database 
def deleterecord(request,id):
	res = flower_details.objects.get(id=id)
	res.delete()
	res1 = flower_details.objects.all()
	print(res)
	return render(request,'adminpage.html',
					{'result':res1})

#The admin is customer status update page
def statusupdate(request,id):
	res = order_details.objects.get(id=id)
	return render(request,'statusupdate.html',
					{'user':res})

#The admin is customer status update save in data base
def orderstatusupdate(request,id):
	if request.method == 'POST':
		status = request.POST['update']

		orderDetails = order_details.objects.get(id=id)
		orderDetails.status = status
		orderDetails.save()
		messages.success(request,'Successfully')
		return render(request,'statusupdate.html')			

def adminrevieworder(request):
	res = order_details.objects.all()
	return render(request,'revieworder.html',
					{'result':res})

#The cusomer server feedback view in admin page.
def adminfeedbackview(request):
	res = order_details.objects.all()
	return render(request,'adminfeedback.html',
					{'result':res})							

#This is admin logout
def adminlogout(request):
	del request.session['user']
	return render(request,'firstpage.html')

#This customer login page
def customerlogin(request):
	return render(request,'customerlogin.html')

#This customer user name and password checking
def customerchecklog(request):
	if request.method == 'POST':
		uname = request.POST['name']
		pwd = request.POST['pass']
		if new_login_reaister.objects.filter(user_name=uname,
												user_password=pwd).exists():
			#return render(request,'newuser.html')
			request.session['user'] = uname
			return HttpResponseRedirect('customerhomepage')
		else:
			#return HttpResponse("Invalid Login")
			#return render(request, 'index.html', {res:"Invalid Login"})
			messages.info(request,"Invalid Login")
			return render(request, 'customerlogin.html')

	else: 
		return render(request, 'customerlogin.html')

#This customer home 
def customerhomepage(request):
	if request.session.has_key('user'):
		un = request.session['user']
		res = flower_details.objects.all()
		print(res)
		return render(request,'customerhomepage.html',
						{'result':res,'uname':un})
	else:
		return render(request, 'customerlogin.html')	

#This is customer create new id page
def customersignup(request):
	return render(request,'customersignup.html')

#This customer new id save 
def customerstore(request):
	if request.method == 'POST':
		name = request.POST['name']
		phoneno = request.POST['Phone']
		emailid = request.POST['email']
		password = request.POST['pass']

		newLoginRegistration = new_login_reaister()
		newLoginRegistration.user_name = name
		newLoginRegistration.user_phone_no = phoneno
		newLoginRegistration.user_email = emailid									
		newLoginRegistration.user_password = password
		
		newLoginRegistration.save()
		messages.success(request,'Save Successfully')
		return render(request,'customerlogin.html')

def customertable(request):
	res = flower_details.objects.all()
	print(res)
	return render(request,'customerhomepage.html',
							{'result':res})

def hometable(request):
	return HttpResponseRedirect('homepage')

#This  cart page 
def cartpage(request):
	if request.session.has_key('user'):
		un = request.session['user']
		res = cart.objects.filter(username=un)
		return render(request,'cart.html',
						{'result':res})
	else:
		return render(request,'customerlogin.html')	

#Thia cart is save in data base
def cartstore(request,id):
	if request.method == 'POST':
		ids = request.POST['id']
		username = request.session['user']
		image = request.POST['image']
		name = request.POST['name']
		category = request.POST['category']
		price = request.POST['price']
		quantity = request.POST['qty']
		total = request.POST['total']

		print(ids)
		print(image)
		print(name)
		print(category)
		print(price)
		print(quantity)
		print(total)
		print(username)

		cartDetails = cart()
		cartDetails.flower_id = ids
		cartDetails.username = username
		cartDetails.flower_name = name
		cartDetails.category = category
		cartDetails.flower_image =image
		cartDetails.order_quantity = quantity
		cartDetails.price = price
		cartDetails.total_price = total
		cartDetails.save()
	return HttpResponseRedirect('/cartpage')

#This customer buy order details save page.
def	cartorder(request):
	if request.session.has_key('user'):
		un = request.session['user']
		res1 = cart.objects.filter(username=un)
		address = request.POST['address']
		phone = request.POST['phone']
		for s in res1:
			x = datetime.datetime.now()
			date=(x.strftime(
					"%d""/""%m""/""%Y"))

			orderDetails = order_details()
			orderDetails.flower_id = s.flower_id
			orderDetails.date = date
			orderDetails.image = s.flower_image	
			orderDetails.name = s.flower_name
			orderDetails.category = s.category
			orderDetails.address = address
			orderDetails.phone_no = phone
			orderDetails.username = s.username
			orderDetails.order_quantity = s.order_quantity
			orderDetails.amount = s.price
			orderDetails.total_amount = s.total_price
			orderDetails.save()

		res1. delete()	
		return HttpResponseRedirect('/cartpage')

def buypage(request,id):
	if request.session.has_key('user'):
		un = request.session['user']
		res = flower_details.objects.get(id=id)
		return render(request,'buypage.html',{'user':res})
	else:
		return render(request,'customerlogin.html')	

def orderstore(request,id):
	if request.method == 'POST':
		ids = request.POST['id']
		image = request.POST['image']
		name = request.POST['name']
		category = request.POST['category']
		phone = request.POST['phone']
		address = request.POST['address']
		username = request.session['user']
		order = request.POST['qty']
		amount = request.POST['price']
		total = request.POST['total']
		x = datetime.datetime.now()
		date = (x.strftime("%d""/""%m""/""%Y"))
 

	 	
		orderDetails = order_details()
		orderDetails.flower_id = ids
		orderDetails.date = date
		orderDetails.image = image
		orderDetails.name = name
		orderDetails.category = category
		orderDetails.phone_no = phone
		orderDetails.address = address
		orderDetails.username = username
		orderDetails.order_quantity = order
		orderDetails.amount = amount
		orderDetails.total_amount = total
		orderDetails.save()
		messages.success(request,'Save Successfully')
		return HttpResponseRedirect('/yourorder')

#This customer order view page.
def yourorder(request):
	if request.session.has_key('user'):
		un = request.session['user']
		res = order_details.objects.filter(username=un)
		return render(request,'customerorderview.html',
						{'result':res})
	else:
		return render(request,'customerorderview.html')	

#This customer product review page.
def review(request,id):
	res = order_details.objects.get(id=id)
	return render(request,'review.html',
					{'user':res})

def reviewstore(request,id):
	if request.method == 'POST':
		review = request.POST['review']

		orderDetails = order_details.objects.get(id=id)
		orderDetails.review = review
		order_details.save()
		messages.success(request,'Save Successfully')
		return render(request,'review.html')

#This customer server feedback page 
def yourfeedback(request,id):
	res = order_details.objects.get(id=id)
	return render(request,'feedback.html',
					{'user':res})

def customerfeedback(request,id):	
	if request.method == 'POST':
		feedback = request.POST['feedback']

		orderDetails = order_details.objects.get(id=id)
		orderDetails.feedback = feedback
		orderDetails.save()

		return render(request,'feedback.html')

#This customer logout.
def customerlogout(request):
	if request.session.has_key('user'):
		del request.session['user']
		return render(request,'firstpage.html')
	else:
		return render(request,'firstpage.html')


# def statusuodate(request,id):
# 	res=order_details.objects.get(id=id)
# 	return render(request,'statusupdate.html',{'user':res})



# def admintable(request):
# 		res=addflower.objects.all()/
# 		return render(request,'addflower.html',{'result':res})

		


	
	
# Create your views here.