
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, DeactivateOrderView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('deactivate/', DeactivateOrderView.as_view(), name='order-deactivte'),
    path('', OrderListCreateView.as_view(), name='order-list'),

]