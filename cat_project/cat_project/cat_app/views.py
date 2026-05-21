from django.shortcuts import render,redirect

# Create your views here.
from .cat import Cat

cat = None


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            global cat
            cat = Cat(name)
            return redirect('cat_stats')
    return render(request, 'index.html')


def cat_stats(request):
    global cat
    if cat is None:
        return redirect('index')

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'feed':
            cat.feed()
        elif action == 'play':
            cat.play()
        elif action == 'sleep':
            cat.sleep()

    context = {
        'cat': cat,
        'avatar': cat.get_avatar(),
    }
    return render(request, 'cat_stats.html', context)