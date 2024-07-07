from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Course
import json
import uuid

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
        id = id.strip()
        course_id = uuid.UUID(id)
        course = Course.objects.get(course_id=course_id)
        data = json.loads(request.body)
        course.course_name = data.get("course_name", course.course_name)
        course.course_updated_by = data.get("course_updated_by", course.course_updated_by)
        course.save()
        return JsonResponse({"message": "Course updated"})
    except ValueError:
        return JsonResponse({"message": "Invalid course ID"}, status=400)
    except Course.DoesNotExist:
        return JsonResponse({"message": "Course not found"}, status=404)

@csrf_exempt
@require_http_methods(["DELETE"])
def deleteCourseApi(request, id):
    try:
        id = id.strip()
        course_id = uuid.UUID(id)
        course = Course.objects.get(course_id=course_id)
        course.delete()
        return JsonResponse({"message": "Course deleted"})
    except ValueError:
        return JsonResponse({"message": "Invalid course ID"}, status=400)
    except Course.DoesNotExist:
        return JsonResponse({"message": "Course not found"}, status=404)
