import json
from django.http import JsonResponse
from rest_framework import generics
from dotenv import load_dotenv
from panda.scripts import driver_ctl, routes_ctl, employee_ctl, van_ctl, training_employee_ctl


load_dotenv()

# API
#========================================================================


class PandaApi(generics.GenericAPIView):
    def get(self, _):
        return JsonResponse({"message": "backend_running"}, status=200)


# ========================================================================


class Drivers(generics.GenericAPIView):
    def get(self, req):
        res = driver_ctl["read"]()
        return JsonResponse(res, status=200)

    def post(self, req):
        res = driver_ctl["create"](json.loads(req.body)["data"])
        return JsonResponse(res, status=200)

    def put(self, req):
        req = json.loads(req.body)
        res = driver_ctl["update"](req["driverId"], req["data"], req["type"])
        return JsonResponse(res, status=200)

    def delete(self, req):
        driver_id = req.query_params.get("driver_id")
        res = driver_ctl["delete"](driver_id)
        return JsonResponse(res, status=200)


# ========================================================================


class Employees(generics.GenericAPIView):
    def get(self, req):
        res = employee_ctl["read"]()
        return JsonResponse(res, status=200)
    
    def put(self, request):
        req = json.loads(request.body)
        res = employee_ctl["update"](req["employeeId"], req["data"], req["type"])
        return JsonResponse(res, status=200)
    
    def post(self, req):
        res = employee_ctl["create"](json.loads(req.body)["data"])
        return JsonResponse(res, status=200)
    
    def delete(self, req):
        employee_id = req.query_params.get("employee_id")
        res = employee_ctl["delete"](employee_id)
        return JsonResponse(res, status=200)


# ========================================================================

class Routes(generics.GenericAPIView):
    def get(self, req):
        res = routes_ctl["read"]()
        return JsonResponse(res, status=200)

    def put(self, request):
        req = json.loads(request.body)
        res = routes_ctl["update"](req["routeId"], req["data"], req["type"])
        return JsonResponse(res, status=200)
    
    def post(self, req):
        res = routes_ctl["create"](json.loads(req.body)["data"])
        return JsonResponse(res, status=200)
    
    def delete(self, req):
        route_id = req.query_params.get("route_id")
        res = routes_ctl["delete"](route_id)
        return JsonResponse(res, status=200)


# ========================================================================

class Vans(generics.GenericAPIView):
    def get(self, req):
        res = van_ctl["read"]()
        return JsonResponse(res, status=200)

    def put(self, request):
        req = json.loads(request.body)
        res = van_ctl["update"](req["vanId"], req["data"], req["type"])
        return JsonResponse(res, status=200)
    
    def post(self, req):
        res = van_ctl["create"](json.loads(req.body)["data"])
        return JsonResponse(res, status=200)
    
    def delete(self, req):
        van_id = req.query_params.get("van_id")
        res = van_ctl["delete"](van_id)
        return JsonResponse(res, status=200)


# ========================================================================

class TrainingEmployees(generics.GenericAPIView):
    def get(self, req):
        res = training_employee_ctl["read"]()
        return JsonResponse(res, status=200)

    def put(self, request):
        req = json.loads(request.body)
        res = training_employee_ctl["update"](req["trainingEmployeeId"], req["data"], req["type"])
        return JsonResponse(res, status=200)
    
    def post(self, req):
        res = training_employee_ctl["create"](json.loads(req.body)["data"])
        return JsonResponse(res, status=200)
    
    def delete(self, req):
        training_employee_id = req.query_params.get("training_employee_id")
        res = training_employee_ctl["delete"](training_employee_id)
        return JsonResponse(res, status=200)
