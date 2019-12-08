from django.shortcuts import render
from .models import Review
from .forms import ReviewForm


def review(request):
    cont = {}
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
