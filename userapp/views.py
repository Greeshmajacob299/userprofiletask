from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from userapp.forms import ProjectForm, ExperienceForm, QualificationForm, CertificateForm
from userapp.models import UserProfile, Project, Experience, Qualifications, Certification


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email already taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, first_name=first_name,
                                                last_name=last_name, email=email,
                                                password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Password does not match')
            return redirect('register')

    return render(request, 'users/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.info(request, "please provide correct credentials")
            return redirect('login')

    return render(request, 'users/login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'users/logout.html')


def home(request):
    return render(request, 'users/home.html')


def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'users/profile.html', {'user_profile': user_profile})


def editprofile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_profile.address = request.POST.get('address')
        user_profile.postcode = request.POST.get('postcode')
        user_profile.city = request.POST.get('city')
        user_profile.state = request.POST.get('state')
        user_profile.qualification = request.POST.get('qualification')
        user_profile.skill1 = request.POST.get('skill1')
        user_profile.skill2 = request.POST.get('skill2')
        user_profile.skill3 = request.POST.get('skill3')

        user_profile.save()

        return redirect('profile')

    return render(request, 'users/editprofile.html', {'user_profile': user_profile})


def add_project(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user_profile = user_profile
            project.save()
            return redirect('profile')
    else:
        form = ProjectForm()

    return render(request, 'users/addproject.html', {'form': form})

def view_project(request):
    user_profile = request.user.userprofile
    projects = Project.objects.filter(user_profile=user_profile)

    return render(request, 'users/viewproject.html', {'projects': projects})

def add_experience(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user_profile = user_profile
            experience.save()
            return redirect('viewexperience')
    else:
        form = ExperienceForm()

    return render(request, 'users/addexperience.html', {'form': form})


def view_experience(request):
    user_profile = request.user.userprofile
    experiences = Experience.objects.filter(user_profile=user_profile)

    return render(request, 'users/viewexperience.html', {'experiences': experiences})

def add_qualification(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = QualificationForm(request.POST)
        if form.is_valid():
            qualification = form.save(commit=False)
            qualification.user_profile = user_profile
            qualification.save()
            return redirect('viewqualification')
    else:
        form = QualificationForm()

    return render(request, 'users/addqualification.html', {'form': form})

def view_qualification(request):
    user_profile = request.user.userprofile
    qualifications = Qualifications.objects.filter(user_profile=user_profile)

    return render(request, 'users/viewqualification.html', {'qualifications': qualifications})

def add_certificate(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.user_profile = user_profile
            certificate.save()
            return redirect('viewcertificate')
    else:
        form = CertificateForm()

    return render(request, 'users/addcertificate.html', {'form': form})

def view_certificate(request):
    user_profile = request.user.userprofile
    certificates = Certification.objects.filter(user_profile=user_profile)

    return render(request, 'users/viewcertificate.html', {'certificates': certificates})

