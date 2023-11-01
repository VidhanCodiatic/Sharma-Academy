from django.urls import path
from enrollment.views import EnrollView, HomePageView, stripe_config, create_checkout_session, SuccessView, CancelledView, stripe_webhook

urlpatterns = [
    path('enroll/', EnrollView.as_view(), name = 'enroll'),
    path('payment/', HomePageView.as_view(), name='payment'),
    path('config/', stripe_config),
    path('create-checkout-session/', create_checkout_session),
    path('success/', SuccessView.as_view()),
    path('cancelled/', CancelledView.as_view()),
    path('webhook/', stripe_webhook),
]