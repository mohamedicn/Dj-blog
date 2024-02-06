from accounts.models import Profile
from django.contrib.auth.models import User

def social(request):
    user_admin = User.objects.get(username='admin')
    socials=Profile.objects.get(user=user_admin)
    return{
        'socials':socials,
    }
