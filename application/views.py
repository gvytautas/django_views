from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Service, Order, OrderDetail


# Create your views here.
# function based views

# def index(request):
#    return render(request, 'index.html')


# def show_services(request):
#    services = Service.objects.values()
#    return render(request, 'show_services.html', context={'services': services})


# def show_orders(request):
#    orders = Order.objects.filter(vehicle__model__brand__startswith='Model').all()
#    return render(request, 'show_orders.html', context={'orders': orders})

# class based views

class IndexView(TemplateView):
    template_name = 'index.html'


class ShowServicesView(ListView):
    model = Service
    template_name = 'show_services.html'
    context_object_name = 'services'


class ShowOrdersView(ListView):
    model = Order
    template_name = 'show_orders.html'
    context_object_name = 'orders'
    object_list = None

    def post(self, request):
        brand = request.POST.get('brand')
        if brand:
            self.queryset = Order.objects.filter(vehicle__model__brand__contains=brand)
        self.object_list = self.get_queryset()
        return self.render_to_response(self.get_context_data())


class ShowOrderDetailView(ListView):
    model = OrderDetail
    template_name = 'show_order_detail.html'
    context_object_name = 'order_detail'

    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        order_detail = OrderDetail.objects.filter(order=order_id)
        return order_detail
