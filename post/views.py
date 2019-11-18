from django.shortcuts import render
from .base_context import make_base_context
from .models import Review
from .forms import ReviewForm


def index(request):
    cont = make_base_context()

    return render(request, 'base.html', context=cont)


def license(request):
    cont = make_base_context()

    return render(request, 'license.html', context=cont)


def new(request):
    cont = make_base_context()

    return render(request, 'new_base.html', context=cont)


def reviews(request):
    cont = make_base_context()
    cont.update({'reviews': Review.objects.filter(approved=True)})
    form = ReviewForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.save()

            cont.update({'form': form})
            cont.update({'notification': 'Ваш отзыв будет добавлен после модерации'})
            return render(request, 'reviews.html', context=cont)

        else:
            cont.update({'form': form})
            cont.update({'notification': 'Вы уже оставили отзыв'})
            return render(request, 'reviews.html', context=cont)
    else:
        cont.update({'form': form})
    return render(request, 'reviews.html', context=cont)
