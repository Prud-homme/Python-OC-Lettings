from django.shortcuts import render
from profiles.models import Profile


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis,
# pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus, it.
# Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
