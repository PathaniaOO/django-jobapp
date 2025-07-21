from django.shortcuts import redirect, render
from django.urls import reverse
from subscribe.forms import SubscribeForm  # Import the subscribe form
from subscribe.models import Subscribe # Import the subscribe model

# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error_empty = ""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            # print("valid form")
            # print(subscribe_form.cleaned_data)
            # email = subscribe_form.cleaned_data.get('email')
            # first_name = subscribe_form.cleaned_data.get('firstname')   
            # last_name = subscribe_form.cleaned_data.get('lastname')
            # print("Email:", email)
            # subscribe = Subscribe(firstname=first_name,lastname=last_name,email=email)
            # subscribe.save()
            return redirect(reverse('thanks'))  # Redirect to thank you page after successful subscription
        # print("POST Request received", email)
        # if email=="":
        #     email_error_empty = "No email provided"
            
        # subscribe = Subscribe(firstname=first_name,lastname=last_name,email=email)
        # subscribe.save()
            
        
    context = {"form":subscribe_form,"email_error_empty":email_error_empty}
    return render(request, 'subscribe/subscribe.html', context)

def thank_you(request):
    context = {}
    return render(request, 'subscribe/thank_you.html',context)
    