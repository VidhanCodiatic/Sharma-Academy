from django.shortcuts import render, redirect, HttpResponse

from enrollment.forms import EnrollForm
from enrollment.models import *
from django.views import View


class EnrollView(View):
    form_class = EnrollForm

    def get(self, request, *args, **kwargs):
        return HttpResponse('method get')

    def post(self, request, *args, **kwargs):
        enroll_form = self.form_class(request.POST)
        enroll_stu = request.user
        print('------------------',enroll_stu)
        enroll_obj = CustomUser.objects.get(id = enroll_stu)
        if enroll_obj.user_type == 'student':
            enroll_form = EnrollForm(request.POST)
            if enroll_form.is_valid():
                enroll_form.save()
                return HttpResponse(" enrolled")
            else:
                return HttpResponse('Not enrolled')
        else:
            return HttpResponse('not a student')
        
        return render(request, self.template_name, {"enroll_form" : enroll_form })
    
from django.views.generic.base import TemplateView
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.http.response import JsonResponse, HttpResponse

class HomePageView(TemplateView):
    template_name = 'enrollment/payment.html'

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)
    
@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/enrollment/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'T-shirt',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': '2000',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
class SuccessView(TemplateView):
    template_name = 'enrollment/success.html'


class CancelledView(TemplateView):
    template_name = 'enrollment/cancelled.html'

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        # TODO: run some custom code here

    return HttpResponse(status=200)
