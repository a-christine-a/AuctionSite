from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Team,Contact
from django.views.generic import CreateView

# Create your views here.
def about(request):
    return render(request, "Common/about.html")

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'Common/index.html',{'category': category,'categories': categories,'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    return render(request,'Common/detail.html',{
        'product': product,   
    })

def about(request):
    team = Team.objects.all()

    return render(
        request, 
        'Common/about us.html',
        {
            'team':team,
    })

class JoinTeam(CreateView):
    model = Team
    fields = 'img','name','position','email','fb_link','twitter_link','whatsapp_link','linkedin'
    template_name = 'Common/join team.html'

def app_success(request):
    return render(request, 'Common/success.html')

class ContactView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'Common/contact.html'