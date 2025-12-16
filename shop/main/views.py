from django.shortcuts import render, get_object_or_404



def product_list(request):
    return render(request, 'index.html')