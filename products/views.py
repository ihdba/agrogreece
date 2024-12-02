from django.shortcuts import render, redirect, get_list_or_404



from .models import Product, Producer
from .forms import ProductForm, ProducerForm




def index(request):
    title = 'Προιοντα'
    
    products = Product.objects.all()
    
    
    ctx = {
        'title': title,
        'products': products,
    }
    
    
    return render(request, 'products/index.html', ctx)




def producers(request):
    title = 'Παραγωγοι'
    producers = Producer.objects.all()
    
    ctx = {
        'title': title,
        'producers': producers,
    }
    
    
    return render(request, 'products/producers.html', ctx)





def producers(request):
    
    
    #list of producers
    producers = Producer.objects.all()
    ctx = {
        'title': "Our Producers",
        'producers': producers,
    }
    
    return render(request, 'products/producers.html', ctx)
    
    


def add_producer(request):
    
    if request.method == "POST":
        form = ProducerForm(request.POST, request.FILES)
        
        if form.is_valid():
            try:
                form.save()
                model=form.instance
                return redirect('products:producers')
            except:
                pass
    else:
        form = ProducerForm()
        return render(request,'products/add_producer.html', {'form': form}) 


def producer_detail(request, id):
    
    product_count = Product.objects.filter(producer=id).count()
    products = Product.objects.filter(producer=id)
    producer = Producer.objects.get(id=id)
    title = 'Πληροφοριες'
    
    ctx = {
        'title': title,
        'producer': producer,
        'product_count': product_count,
        'products': products,
    }
    
    return render(request, 'products/producer_detail.html', ctx)



    
def products(request):
   
    
    # list existing categories
   
    products = Product.objects.all()
    
    context = {
        'title': "Products",
        'products': products,
    }
    
    
    return render(request, 'products/products.html', context = context)


def product_detail(request, id):
    
    product = Product.objects.get(id=id)
    
    title = 'Λεπτομεριες Προιοντος'
    
    ctx = {
        'title': title,
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', ctx )


 
def add_product(request):
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                model=form.instance
                return redirect('products:index')
            except:
                pass
    else:
        form = ProductForm()

    return render(request,'products/add_product.html', {'form': form})
