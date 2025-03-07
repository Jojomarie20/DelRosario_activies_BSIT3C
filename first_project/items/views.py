from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods
import json

# A. Return All Items
def index(request):
    items = [
        {
            "id": 1,
            "item": "Laptop",
        },
        {
            "id": 2,
            "item": "Smartphone",
        },
        {
            "id": 3,
            "item": "Headphones",
        },
        {
            "id": 4,
            "item": "Tablet",
        }
    ]
    return JsonResponse({"message": "Successful", "payload": items}, status=200)

# B. Get a specific item by ID
def get_items(request, item_id):
    try:
        payload = request.GET
        
        items = {
            "id": item_id,
            "context": payload
        }
        return JsonResponse({"message": "Fetch successfully", "payload": {"item": items}}, status=200)
    except Exception as e:
        return JsonResponse({"message": f"Failed: {str(e)}"}, status=400)

# C. Add a new item
@csrf_exempt
@require_POST
def add_items(request):
    try:
        # Process request body here if needed
        data = json.loads(request.body) if request.body else {}
        # Add item logic would go here
        
        return JsonResponse(data={"message": "Item added successfully."}, status=200)
    except:
        return JsonResponse(data={"message": "Failed"}, status=400)

# D. Update an existing item
@csrf_exempt
@require_http_methods(["PUT"])
def update_items(request, item_id):
    try:
        data = json.loads(request.body) if request.body else {}
        
        return JsonResponse(data={"message": "Item updated successfully"}, status=200)
    except:
        return JsonResponse(data={"message": "Failed"}, status=400)

# E. Delete an item
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_items(request, item_id):
    try:
        return JsonResponse(data={"message": "Item deleted successfully"}, status=200)
    except:
        return JsonResponse(data={"message": "Failed"}, status=400)