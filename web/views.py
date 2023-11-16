import json

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.response import HttpResponse

from web.models import Testimonial,Promoters,Faq, Subscribe


def index(request):

# STEP 13
    #                               all() ella valusum konduvaran
    tesimonials = Testimonial.objects.all()
    promoter = Promoters.objects.all()
    rent_tracking = Faq.objects.filter(faq_type="rent_tracking")
    new_deposit = Faq.objects.filter(faq_type="new_deposit")
    existing_deposit = Faq.objects.filter(faq_type="existing_deposit")

    context = {
        "tesimonials" : tesimonials,
        "promoter" : promoter,
        "rent_tracking" : rent_tracking,
        "new_deposit" : new_deposit,
        "existing_deposit" : existing_deposit,

    }

    
    

    #                                   context pass cheyyanam
    return render(request, "index.html", context=context)

#  data colloction (form save cheyyan)
def subscribe(request):
    # POST = elladatasum ithilan
    email = request.POST.get("email")

    if not Subscribe.objects.filter(email=email).exists():


        Subscribe.objects.create(
        email = email
        )
        responsdata = {
            "status" : "success",
            "title":"Successfully Registerd",
            "message" : "Thank you for subscribing"
        }
    else :
        responsdata = {
            "status" : "error",
            "title":"You are already registerd",
            "message" : "You are alredy a member"
        }
    #  submit button click cheythal ed pagilekk redirect cheyyanam enn an
    return HttpResponse(json.dumps(responsdata),content_type="application/javascript")


    


# STEP 14 -> index.html display items
