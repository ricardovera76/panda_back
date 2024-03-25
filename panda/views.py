import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, FileResponse
from rest_framework import generics
from dotenv import load_dotenv
from panda.scripts import driver_ctl, routes_ctl, employee_ctl, single, van_ctl, training_employee_ctl


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
        res = driver_ctl["create"](req.data["data"])
        return JsonResponse(res, status=200)

    def put(self, req):
        req_data = req.data
        res = driver_ctl["update"](req_data["driverId"], req_data["data"], req_data["type"])
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
        req_data = request.data
        res = employee_ctl["update"](req_data["employeeId"], req_data["data"], req_data["type"])
        return JsonResponse(res, status=200)
    
    def post(self, req):
        res = employee_ctl["create"](req.data["data"])
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
        req_data = request.data
        res = routes_ctl["update"](req_data["routeId"], req_data["data"], req_data["type"])
        return JsonResponse(res, status=200)
    
    def post(self, req):
        res = routes_ctl["create"](req.data["data"])
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
        req_data = request.data
        res = van_ctl["update"](req_data["vanId"], req_data["data"], req_data["type"])
        return JsonResponse(res, status=200)
    
    def post(self, req):
        res = van_ctl["create"](req.data["data"])
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
        req_data = request.data
        res = training_employee_ctl["update"](req_data["trainingEmployeeId"], req_data["data"], req_data["type"])
        return JsonResponse(res, status=200)
    
    def post(self, req):
        res = training_employee_ctl["create"](req.data["data"])
        return JsonResponse(res, status=200)
    
    def delete(self, req):
        training_employee_id = req.query_params.get("training_employee_id")
        res = training_employee_ctl["delete"](training_employee_id)
        return JsonResponse(res, status=200)


# ========================================================================
class SingleData(generics.GenericAPIView):
    def post(self, request):
        try:
            data = request.data
            request_type = data.get("type")
            request_data = data.get("data")

            if request_type is None or request_data is None:
                return JsonResponse({"error": "Invalid request format"}, status=400)

            response_data = single.get(request_type)
            if response_data:
                return response_data(request_data)
            else:
                return JsonResponse({"error": "Invalid request type"}, status=400)
        except ObjectDoesNotExist as e:
            return JsonResponse({"error": f"Object not found: {str(e)}"}, status=404)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

