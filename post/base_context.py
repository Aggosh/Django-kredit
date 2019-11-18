from .models import Compony, Advertising, Notification


def make_base_context():
    componys = Compony.objects.order_by('position')
    cont = {'componys': componys}
    cont.update({'top_five': Compony.objects.order_by('-reviews_count')[0:5]})
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
