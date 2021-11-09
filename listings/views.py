from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_choices, bedroom_choices, state_choices

from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
    'listings': paged_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request, listing_id):
   listing = get_object_or_404(Listing, pk=listing_id)

   context = {
      'listing': listing
   }

   return render(request,'listings/listing.html',context)

def search(request):
   queryset_list = Listing.objects.order_by('-list_date')

   # Search từ khóa
   if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      if keywords:
         # Kiếm từ khóa trong phần description
         queryset_list = queryset_list.filter(description__icontains=keywords)

   # Search thành phố
   if 'city' in request.GET:
      city = request.GET['city']
      if city:
         # Kiếm thành phố trong phần vị trí 
         queryset_list = queryset_list.filter(city__iexact=city)
   
   # Search tiểu bang
   if 'state' in request.GET:
      state = request.GET['state']
      if state:
         # Kiếm tiểu bang trong phần vị trí 
         queryset_list = queryset_list.filter(state__iexact=state)

   # Search phòng ngủ
   if 'bedrooms' in request.GET:
      bedrooms = request.GET['bedrooms']
      if bedrooms:
         # Số phòng ngủ lên đến
         queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

   # Search giá
   if 'price' in request.GET:
      price = request.GET['price']
      if price:
         # Giá lên đến
         queryset_list = queryset_list.filter(price__lte=price)

   context = {
      'state_choices': state_choices,
      'bedroom_choices': bedroom_choices,
      'price_choices': price_choices,
      'listings': queryset_list,
      'values':request.GET
   }

   return render(request,'listings/search.html', context)

def new_listing_form(request):
   # if request.method == 'POST' and request.method == 'FILES':
   #    realtor = request.POST['realtor']
   #    title = request.POST['title']
   #    address = request.POST['address']
   #    city = request.POST['city']
   #    state = request.POST['state']
   #    zipcode = request.POST['zipcode']
   #    description = request.POST['description']
   #    price = request.POST['price']
   #    bedrooms = request.POST['bedrooms']
   #    bathrooms = request.POST['bathrooms']
   #    garage = request.POST['garage']
   #    sqft= request.POST['sqft']
   #    lot_size= request.POST['lot_size']
   #    photo_main = request.FILES['photo_main']
   #    photo_1 = request.FILES['photo_1']
   #    photo_2 = request.FILES['photo_2']
   #    photo_3 = request.FILES['photo_3']
   #    photo_4 = request.FILES['photo_4']
   #    photo_5 = request.FILES['photo_5']
   #    photo_6 = request.FILES['photo_6']
   #    is_published = request.POST['is_published']
   #    list_date = request.POST['list_date']

   #    if Listing.objects.filter(realtor=realtor).exists():
   #       messages.error(request, 'Realtor is taken')
   #       return redirect('new_listing_form')
   #    else:
   #       listing = Listing.objects.create_listing(realtor=realtor, title=title, address=address, city=city, state=state, zipcode=zipcode
   #       ,description=description,price=price,bedrooms=bedrooms,bathrooms=bathrooms, garage=garage, sqft=sqft,lot_size=lot_size, photo_main=photo_main
   #       ,photo_1=photo_1, photo_2=photo_2, photo_3=photo_3, photo_4=photo_4, photo_5=photo_5, photo_6=photo_6,is_published=is_published,list_date=list_date)
   #       listing.save()
   #       messages.success(request, 'You are post new listing successfully')
   #       return redirect('listings')


   # else:
   #    return render(request,'listings/new_listing_form.html')

   if request.method == 'POST':
      form = NewListingForm(request.POST, request.FILES)

      if form.is_valid():
         # form = NewListingForm(photo_main = request.FILES['photo_main'])
         # form = NewListingForm(photo_1 = request.FILES['photo_1'])
         # form = NewListingForm(photo_2 = request.FILES['photo_2'])
         # form = NewListingForm(photo_3 = request.FILES['photo_3'])
         # form = NewListingForm(photo_4 = request.FILES['photo_4'])
         # form = NewListingForm(photo_5 = request.FILES['photo_5'])
         # form = NewListingForm(photo_6 = request.FILES['photo_6'])

         instance = form.save(commit=False)
         instance.is_published = False
         instance.save()

         messages.success(request,'You have successfully')
         return redirect('simple_checkout')
      else:
         messages.error(request, 'You not post')
         return redirect('new_listing_form')
   else:

      form = NewListingForm()

 
   return render(request,'listings/new_listing_form.html', 
      {
         'form': form,
         # 'listing': listing,
      }
   )

def simple_checkout(request, pk):
   
   return render(request,'listings/simple_checkout.html')