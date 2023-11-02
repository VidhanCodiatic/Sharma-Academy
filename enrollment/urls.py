from django.urls import path
from enrollment.views import create_checkout_session, OrderHistoryListView, PaymentFailedView, PaymentSuccessView

urlpatterns = [
    # path('home/', ProductListView.as_view(), name='home'),
    # path('create/', ProductCreateView.as_view(), name='create'),
    # path('detail/<id>/', ProductDetailView.as_view(), name='detail'),
    path('success/', PaymentSuccessView.as_view(), name='success'),
    path('failed/', PaymentFailedView.as_view(), name='failed'),
    path('history/', OrderHistoryListView.as_view(), name='history'),

    path('api/checkout-session/<id>/', create_checkout_session, name='api_checkout_session'),




    # path('payment/', HomePageView.as_view(), name='payment'),
    # path('config/', stripe_config),
    # path('create-checkout-session/', create_checkout_session),
    # path('success/', SuccessView.as_view()),
    # path('cancelled/', CancelledView.as_view()),
    # path('webhook/', stripe_webhook),
]