
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User 
from .models import CustomUser
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect

class Login(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Authentication was successful, log the user in
            login(request, user)
            return redirect('profile')  # Redirect to the home page or any desired page
        else:
            # Authentication failed, show an error message
            error_message = "Invalid username or password"
            return render(request, self.template_name, {'error_message': error_message})

from myJournal.models import Trade

@login_required  # Use this decorator to ensure the user is logged in
def profile_view(request):
    user = request.user

    # Fetch the counts of winning and losing trades
    winning_trades_count = Trade.objects.filter(custom_user=user, result='Win').count()
    losing_trades_count = Trade.objects.filter(custom_user=user, result='Loss').count()
    total_trades_count = Trade.objects.filter(custom_user=user).count()
    context = {
        'user': user,
        'total_trades': total_trades_count,
        'winning_trades_count': winning_trades_count,
        'losing_trades_count': losing_trades_count,
    }

    return render(request, 'accounts/profile.html', context)

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages  # Add this import for messages
from django.contrib.auth import login
from .models import CustomUser  # Import your CustomUser model

def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        profile_picture = request.FILES.get("profile_picture")

        try:
            # Create a new user with profile picture
            user = CustomUser.objects.create_user(
                username=username, email=email, password=password,
                first_name=first_name, last_name=last_name,
                win_rate=0.0
            )
            print("1")

            # Assign the profile picture to the custom user instance
            user.profile_picture = profile_picture
            print("2")
            # Save the user object with the profile picture
            user.save()
            print("3")

            # Log in the user using the login function
            login(request, user)
            print("4")

            # Redirect to the desired page (e.g., user profile)
            return redirect('profile')
            

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            messages.error(request, error_message)
            print("5 - Exception:", error_message)


    return render(request, 'accounts/signup.html')
