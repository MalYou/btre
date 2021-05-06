from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail

import os

from .models import Contact

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

        # Check if user has already an inquery
        if request.user.is_authenticated:
            user_id = request.user.id
            contact = Contact.objects.filter(listing_id=listing_id, user_id=user_id)

            if contact:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect(f'/listings/{listing_id}')

        contact = Contact(
            listing_id=listing_id,
            listing=listing,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id
        )
        
        contact.save()
        messages.success(request, 'Your request has been submitted, a \
                         realtor will get back to you soon')

        send_mail(
            subject='Property listing inquiry',
            message=f'There has been an inquiry for {listing}. Sign into the admin panel for more informations',
            from_email=os.environ.get('G_USER'),
            recipient_list=[realtor_email],
            fail_silently=True)

        return redirect(f'/listings/{listing_id}')
