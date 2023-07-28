from Django_GitHub_Actions.car_app.models import Profile


def get_profile(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }
    return context
