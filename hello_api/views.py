import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from hello_api.entities.user import User
from hello_api.entities.animal import Animal
from hello_api.models import Ticket


# Create your views here.


def index(request):
    return JsonResponse({
        "message": "hello world"

    })


@csrf_exempt
@require_POST
def save_user(request):
    data = json.loads(request.body)

    user = User(data["id"], data["name"], data["account"])

    return JsonResponse({
       "success": True,
       "message": f"User {user.name} saved successfully"
    }, status=201)


@require_GET
def get_ticket(request):
    data = list(Ticket.objects.all().values())
    return JsonResponse({
        "success": True,
        "message": f"Se encontraron {len(data)} tickets",
        "data": data
    }, status=200)
@csrf_exempt
@require_POST
def save_ticket (request):
    data =json.loads(request.body)
    
    if len(data["title"]) < 5:
        return JsonResponse({
            "success": False,
            "message": "El título debe tener al menos 5 caracteres"
        }, status=400)
    elif data["description"] == "":
        return JsonResponse({
            "success": False,
            "message": "La descripción no puede estar vacía"
        }, status=400)
    elif data["priority"] not in ["alta", "media", "baja"]:
        return JsonResponse({
            "success": False,
            "message": "La prioridad debe ser alta, media o baja"
        }, status=400)

    ticket= Ticket.objects.create(
        title=data["title"],
        description=data["description"],
        priority=data["priority"])
        
    return JsonResponse({ 
        "success": True,
        "message": f"Ticket {ticket.title} saved successfully"
        }, status=201)

@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def ticket_by_id(request, id):
    try:
        ticket = Ticket.objects.get(id=id)
    except Ticket.DoesNotExist:
        return JsonResponse({
            "success": False,
            "message": f"El ticket con id {id} no existe"
        }, status=404)

    if request.method == "GET":
        return JsonResponse({
            "success": True,
            "message": f"Ticket {ticket.title} encontrado",
            "data": {
                "id": ticket.id,
                "title": ticket.title,
                "description": ticket.description,
                "priority": ticket.priority,
                "status": ticket.status,
                "created_at": ticket.created_at
            }
        }, status=200)

    elif request.method == "DELETE":
        ticket.delete()
        return JsonResponse({
            "success": True,
            "message": f"Ticket {ticket.title} eliminado"
        }, status=200)

    elif request.method == "PUT":
        if ticket.status == "cerrado":
            return JsonResponse({
                "success": False,
                "message": f"El ticket #{id} está cerrado y no se puede modificar"
            }, status=409)

        data = json.loads(request.body)
        ticket.title = data.get("title", ticket.title)
        ticket.description = data.get("description", ticket.description)
        ticket.priority = data.get("priority", ticket.priority)
        ticket.status = data.get("status", ticket.status)
        ticket.save()

        return JsonResponse({
            "success": True,
            "message": f"Ticket {ticket.title} actualizado",
            "data": {
                "id": ticket.id,
                "title": ticket.title,
                "description": ticket.description,
                "priority": ticket.priority,
                "status": ticket.status,
                "created_at": ticket.created_at
            }
        }, status=200)
    















"""@csrf_exempt
@require_POST
def save_animal(request):
    data = json.loads(request.body)

    animal = Animal(data["name"], data["color"])

    return JsonResponse({
        "name": animal.name,
        "color": animal.color
    }, status=201)"""
