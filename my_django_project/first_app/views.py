from django.shortcuts import render
from first_app.models import Visitor


def get_new_visitor_by_post(request):
    if request.method == "POST":
        visitor_name = request.POST.get("visitor_name")
        visitor_surname = request.POST.get("visitor_surname")
        visitor_age = request.POST.get("visitor_age")
        visitor_gender = request.POST.get("visitor_gender")
        visitor_work_status = request.POST.get("visitor_work_status")
        visitor_favorite_genre = request.POST.get("visitor_favorite_genre")
        visitor_visiting_time = request.POST.get("visitor_visiting_time")
        visitor_favorite_platform = request.POST.get("visitor_favorite_platform")
        visitor_country = request.POST.get("visitor_country")
        visitor_opinion = request.POST.get("visitor_opinion")

        Visitor.objects.create(name=visitor_name,
                               surname=visitor_surname,
                               age=visitor_age,
                               gender=visitor_gender,
                               work_status=visitor_work_status,
                               favorite_genre=visitor_favorite_genre,
                               visiting_time=visitor_visiting_time,
                               favorite_platform=visitor_favorite_platform,
                               country=visitor_country,
                               opinion=visitor_opinion)

    return render(request, "index.html")
