from .models import Post, Advertising, Notification


def make_base_context():
    posts = Post.objects.order_by('position')
    cont = {'posts': posts}
    cont.update({'top': Post.objects.order_by('-reviews_count')[0:5]})
    cont.update({'notifications': Notification.objects.all()}) 

    try:
        cont.update({'adv_1': Advertising.objects.get(position=1)})
    except Advertising.DoesNotExist:
        pass
    try:
        cont.update({'adv_2': Advertising.objects.get(position=2)})
    except Advertising.DoesNotExist:
        pass
    try:
        cont.update({'adv_3': Advertising.objects.get(position=3)})
    except Advertising.DoesNotExist:
        pass
    return cont
