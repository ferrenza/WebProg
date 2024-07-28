from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from .models import Course, User #experiment untuk tambah data
import json
import requests
@csrf_exempt
@require_http_methods(["GET", "POST"])
def apiCourse(request):
    if request.method == "GET":
        courses = list(Course.objects.values())
        return JsonResponse(courses, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        course = Course.objects.create(course_name=data["course_name"], course_created_by=data["course_created_by"])
        return JsonResponse({"message": "Course created", "course_id": course.course_id}, status=201)

@csrf_exempt
@require_http_methods(["PUT"])
def updateCourseApi(request, id):
    try:
        course = Course.objects.get(course_id=id)
        data = json.loads(request.body)
        course.course_name = data.get("course_name", course.course_name)
        course.course_updated_by = data.get("course_updated_by", course.course_updated_by)
        course.save()
        return JsonResponse({"message": "Course updated"})
    except Course.DoesNotExist:
        return JsonResponse({"message": "Course not found"}, status=404)

@csrf_exempt
@require_http_methods(["DELETE"])
def deleteCourseApi(request, id):
    try:
        course = Course.objects.get(course_id=id)
        course.delete()
        return JsonResponse({"message": "Course deleted"})
    except Course.DoesNotExist:
        return JsonResponse({"message": "Course not found"}, status=404)

@csrf_exempt
def consume_api_get(request):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    local_users = User.objects.all()
    local_data = [{
        "id": user.id,
        "name": user.name,
        "username": user.username,
        "email": user.email,
        "address": {
            "street": user.street,
            "suite": user.suite,
            "city": user.city,
            "zipcode": user.zipcode,
            "geo": {
                "lat": user.geo_lat,
                "lng": user.geo_lng
            }
        },
        "phone": user.phone,
        "website": user.website,
        "company": {
            "name": user.company_name,
            "catchPhrase": user.company_catchPhrase,
            "bs": user.company_bs
        }
    } for user in local_users]
    combined_data = data + local_data
    return render(request, "api_get.html", {'data': combined_data})
##BARU
@csrf_exempt
@require_http_methods(["POST"])
def create_user(request):
    if request.method == "POST":
        # Ambil ID Terakhir buat patokan aja untuk data disini ada 10 + data yang akan dibuat
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        data = response.json()
        last_id_placeholder = max([user['id'] for user in data])
        
        # Ambil ID latest dari json
        last_user = User.objects.order_by('-id').first()
        last_id_local = last_user.id if last_user else 0
        
        # Tentukan ID awal untuk pengguna baru
        start_id = max(last_id_placeholder, last_id_local)
        
        data = json.loads(request.body)
        user = User(
            id=start_id + 1,  # Set ID baru
            name=data["name"],
            username=data["username"],
            email=data["email"],
            street=data["address"]["street"],
            suite=data["address"]["suite"],
            city=data["address"]["city"],
            zipcode=data["address"]["zipcode"],
            geo_lat=data["address"]["geo"]["lat"],
            geo_lng=data["address"]["geo"]["lng"],
            phone=data["phone"],
            website=data["website"],
            company_name=data["company"]["name"],
            company_catchPhrase=data["company"]["catchPhrase"],
            company_bs=data["company"]["bs"]
        )
        user.save()
        return JsonResponse({"message": "User created", "user_id": user.id}, status=201)

@csrf_exempt
@require_http_methods(["PUT"])
def update_user(request, id):
    try:
        user = User.objects.get(id=id)
        data = json.loads(request.body)
        user.name = data.get("name", user.name)
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)
        user.street = data["address"].get("street", user.street)
        user.suite = data["address"].get("suite", user.suite)
        user.city = data["address"].get("city", user.city)
        user.zipcode = data["address"].get("zipcode", user.zipcode)
        user.geo_lat = data["address"]["geo"].get("lat", user.geo_lat)
        user.geo_lng = data["address"]["geo"].get("lng", user.geo_lng)
        user.phone = data.get("phone", user.phone)
        user.website = data.get("website", user.website)
        user.company_name = data["company"].get("name", user.company_name)
        user.company_catchPhrase = data["company"].get("catchPhrase", user.company_catchPhrase)
        user.company_bs = data["company"].get("bs", user.company_bs)
        user.save()
        return JsonResponse({"message": "User updated"}, status=200)
    except User.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)