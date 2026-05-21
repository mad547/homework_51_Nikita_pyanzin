from django.shortcuts import render, redirect
from cat_app.cat import Cat, load_cats, save_cats


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        age = request.POST.get('age', '').strip()
        if name and age:
            try:
                age = int(age)
                if 1<= age <= 18:
                    cats = load_cats()
                    cats.append(Cat(name, age))
                    save_cats(cats)
                    return redirect('cats_list')
            except:
                pass
        return render(request, 'index.html')
    return render(request, 'index.html')

def cat_list(request):
    cats = load_cats()
    for i, cat in enumerate(cats):
        cat.index = i
    cats_sorted = sorted(cats, key=lambda c: c.average_level, reverse=True)
    return render(request, 'cats_list.html', {'cats': cats_sorted})

def cat_stats(request, cat_index):
    cats = load_cats()
    if cat_index < 0 or cat_index >= len(cats):
        return redirect('cats_list')

    cat = cats[cat_index]
    message = None

    if request.method == 'POST':
        action = request.POST.get('action', '')
        if action == 'feed':
            message = cat.feed()
        elif action == 'play':
            message = cat.play()
        elif action == 'sleep':
            message = cat.sleep()
        save_cats(cats)

    context= {
        'cat': cat,
        'cat_index': cat_index,
        'avatar': cat.get_avatar(),
        'message': message,
    }
    return  render(request, 'cat_stats.html', context)