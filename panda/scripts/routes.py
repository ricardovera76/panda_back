from panda.models import Employee, Route, Driver


def get_routes():
    route_list = Route.objects.all()
    route_acc_list = []
    for route in route_list:
        current_route = route.to_object()
        current_route[
            "name"
        ] = f"{current_route['id']}-{current_route['company']}-{current_route['shift']}".lower()
        current_route["employees"] = Employee.objects.filter(
            route_id=route.to_object()["id"]
        ).values()
        route_acc_list.append(current_route)

    return {"message": "success", "error": False, "data": route_acc_list}


def create_routes(route_data):
    route_data["driver_id"] = Driver.objects.filter(id=route_data["driver_id"])[0]
    route_db = Route(**route_data)
    route_db.save()
    return {"message": "successfully added route", "error": False}


def update_route(route_id, data, types):
    update_types = {
        "dr": "driver_id",
        "ad": "address",
        "sf": "shift",
        "dc": "descr",
        "cp": "company",
    }
    route_db = Route.objects.get(id=route_id)
    data = Driver.objects.filter(id=data) if "dr" == types else data
    setattr(route_db, update_types[types], data[update_types[types]])
    route_db.save()
    return {"message": "success", "error": False}


def delete_route(route_id):
    route_db = Route.objects.get(id=route_id)
    deleted_route = route_db.to_object()
    route_db.delete()
    return {
        "message": "Route deleted successfully!",
        "data": deleted_route,
        "error": False,
    }


routes_ctl = {
    "create": create_routes,
    "read": get_routes,
    "update": update_route,
    "delete": delete_route,
}
