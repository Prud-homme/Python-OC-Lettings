from django.shortcuts import render
from profiles.models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget. Fusc faucibus, urna quis auctor pharetra,
# massa dolor cursus neque, quis dictum lacus d
def index(request):
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)
