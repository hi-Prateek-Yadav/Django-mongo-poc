from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from temp_pm.config.connectDb import collection


@csrf_exempt
def insert_data(request):
    if request.method == 'POST':
        # Get data from the request
        field1_value = 'foo'
        field2_value = 1

        # Create a document to insert into MongoDB
        document = {
            'field1': field1_value,
            'field2': field2_value
        }

        # Insert the document into the MongoDB collection
        result = collection.insert_one(document)

        if result.acknowledged:
            return JsonResponse({'message': 'Data inserted successfully!'})
        else:
            return JsonResponse({'error': 'Failed to insert data.'}, status=500)

    return JsonResponse({'error': 'POST request required.'}, status=400)

@csrf_exempt
def retrieve_data(request):
    # Retrieve all documents from the MongoDB collection
    documents = collection.find({})  
    # documents = collection.find({'field1' : "foo"})

    # Serialize the documents to JSON
    serialized_data = [{'field1': doc['field1'], 'field2': doc['field2']} for doc in documents]

    return JsonResponse({'data': serialized_data})