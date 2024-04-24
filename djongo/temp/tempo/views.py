from django.shortcuts import render
from django.http import JsonResponse
from .models import YourModel, OurModel  # Import your MongoEngine model
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def insert_data(request):
    if request.method == 'POST':
        # Get data from the request
        field1_value = 'bazzzzzz'
        field2_value = 2
        field3_value = "bar"

        # Create an instance of YourModel and save it to MongoDB
        obj = YourModel(field1=field1_value, field2=field2_value, field3=field3_value)
        obj.save()

        return JsonResponse({'message': 'Data inserted successfully!'})

    return JsonResponse({'error': 'POST request required.'}, status=400)

@csrf_exempt
def retrieve_data(request):
    # Retrieve all objects from the MongoDB collection
    objects = YourModel.objects.all()

    # Serialize the objects to JSON
    serialized_data = [{'field1': obj.field1, 'field2': obj.field2, 'field3': obj.field3} for obj in objects]

    return JsonResponse({'data': serialized_data})
