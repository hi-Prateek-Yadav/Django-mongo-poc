from django.shortcuts import render
from django.http import JsonResponse
from .models import YourModel  # Import your MongoEngine model
from django.views.decorators.csrf import csrf_exempt
from .serializers import YourModelSerializer

@csrf_exempt
def insert_data(request):
    if request.method == 'POST':
        # Get data from the request
        field1_value = 'hii'
        field2_value = 2
        field3_value = "okkkkkk"
        dynamic_field = 1

        # Create an instance of YourModel and save it to MongoDB
        obj = YourModel(field1=field1_value, field2=field2_value, field3=field3_value, dynamic_field=dynamic_field)
        obj.save()

        return JsonResponse({'message': 'Data inserted successfully!'})

    return JsonResponse({'error': 'POST request required.'}, status=400)

@csrf_exempt
def retrieve_data(request):
    # Retrieve all objects from the MongoDB collection
    objects = YourModel.objects.all()

    for obj in objects :
        print(obj.field1, obj.field2, obj.field3)

    # Serialize
    # 1st way
    serializer = YourModelSerializer(obj)
    serialized_data = serializer.to_dict()

    # other way of serializing
    print(YourModel.objects.to_json())

    return JsonResponse({'data': serialized_data})