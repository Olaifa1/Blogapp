from django.shortcuts import render

# Render helps to display things in our function
# Create your views here.
def post_list(request):
    return render(request, 'blogapp/post_list.html', {})
