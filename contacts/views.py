from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def contact1(request):
    send_mail(
        'Property Listing Inquiry',
        'There has been an inquiry for.',
        'cmrajib20@yahoo.com',
        ['cmrajib@gmail.com'],
        # fail_silently=False,
    )

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made inquity already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already contacted')
                return redirect('/listings/'+listing_id)



        contact = Contact(listing=listing, listing_id= listing_id, name=name,
            email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        #send Email
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for.',
        #     'cmrajib100@gmail.com',
        #     ['cmrajib@gmail.com'],
        #     fail_silently=False,
        # )
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for ' + listing + 'Sign up',
        #     'cmrajib100@gmail.com',
        #     ['cmrajib@gmail.com'],
        #     # fail_silently=False

        # )

        messages.success(request, 'Your request has been submited')

        return redirect('/listings/'+listing_id)
