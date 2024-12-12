from django.contrib.auth.models import User
from app.models import Profile  # Import your Profile model

def user_profile_context(request):
    if request.user.is_authenticated:  # Ensure the user is logged in
        try:
            UO = request.user
            PO = Profile.objects.get(username=UO)
            return {'UO': UO, 'PO': PO}
        except Profile.DoesNotExist:
            return {'UO': UO, 'PO': None}
    return {'UO': None, 'PO': None}
