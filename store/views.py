from django.shortcuts import render, redirect
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import store.models as store_models
from store.forms import CustomerRegistrationForm, CustomerLoginForm


def get_categories_platform_context(request):
    game_list = None
    category_list = store_models.Category.objects.all()
    platform_list = store_models.Platform.objects.all()

    category_id = request.GET.get("category_id")
    platform_id = request.GET.get("platform_id")

    search_request = request.POST.get("search_request")

    search_text = "Games"
    if search_request is not None:

        game_list = store_models.Game.objects.filter(name__icontains=search_request)
        search_text = f"Search results for {search_text}"

    elif category_id is not None:
        category = store_models.Category.objects.get(id=category_id)
        game_list = store_models.Game.objects.filter(category=category)
        search_text = f"{category.name} games"

    elif platform_id is not None:
        platform = store_models.Platform.objects.get(id=platform_id)
        game_list = store_models.Game.objects.filter(platform=platform)
        search_text = f"Games for {platform.name}"
    else:
        game_list = store_models.Game.objects.all()

    return {
        "search_text": search_text,
        "game_list": game_list,
        "category_list": category_list,
        "platform_list": platform_list,
        "user": request.user
    }


def index(request):
    template = loader.get_template("store/main_page.html")
    return HttpResponse(template.render(get_categories_platform_context(request), request))


def login_user(request):
    form = CustomerLoginForm()

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse(
                loader.get_template("store/login.html").render({"form": form, "unsuccessful": True}, request))

    return HttpResponse(loader.get_template("store/login.html").render({"form": form, "unsuccessful": False}, request))


def register_user(request):
    form = CustomerRegistrationForm()

    if request.method == "POST":

        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return HttpResponse(loader.get_template("store/register.html").render({"form": form}, request))


def game_detail(request, game_id):
    game = store_models.Game.objects.get(id=game_id)
    keys = store_models.Key.objects.filter(game=game_id)
    context = get_categories_platform_context(request)
    context["game"] = game
    context["keys"] = keys
    return HttpResponse(loader.get_template("store/game_detail.html").render(context, request))


@login_required
def buy_game(request, game_id):
    game = store_models.Game.objects.get(id=game_id)
    key = store_models.Key.objects.filter(user=None, game=game).first()
    context = {"message": "Thanks for your purchase"}

    if key is None or game is None:
        context["message"] = "Something went wrong"
        return HttpResponse(loader.get_template("store/game_bought.html").render(context, request))

    key.user = request.user
    key.save()

    return HttpResponse(loader.get_template("store/game_bought.html").render(context, request))


@login_required
def change_mail(request):

    if request.method == "POST":

        email = request.POST.get("email")

        user = request.user
        keys = store_models.Key.objects.filter(user=request.user)
        if email == user.email:

            return HttpResponse(loader.get_template("store/profile.html").render({"changed": False, "keys": keys}, request))

        user.email = email
        user.save()
        return HttpResponse(loader.get_template("store/profile.html").render({"changed": True, "keys": keys}, request))

    return redirect("user_profile")


@login_required
def user_profile(request):
    keys = store_models.Key.objects.filter(user=request.user)
    return HttpResponse(loader.get_template("store/profile.html").render({"user": request.user, "keys": keys}, request))


def logout_user(request):
    logout(request)
    return redirect('index')
