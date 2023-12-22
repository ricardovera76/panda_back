from panda.models import Driver, Employee, Route


def get_drivers():
    driver_list = Driver.objects.all()
    drivers = [driver.to_object() for driver in driver_list]
    for driver in drivers:
        driver["routes"] = [route.to_object() for route in Route.objects.filter(driver_id=driver["id"])]
    
    for driver in drivers:
        for index, driver_route in enumerate(driver["routes"]):
            driver["routes"][index]["employees"] = [employee.to_object() for employee in Employee.objects.filter(route_id=driver_route["id"])]
    return {"message": "success", "error": False, "data": drivers}

def create_driver(driver_data):
    driver_db = Driver(**driver_data)
    driver_db.save()
    return {"message": "successfully added driver", "error": False}

def update_driver(driver_id, data, types):
    update_types = {
        "ad": "address",
        "nm": "name",
        "ph": "phone"
    }

    driver_db = Driver.objects.get(id=driver_id)
    setattr(driver_db, update_types[types], data[update_types[types]])
    driver_db.save()
    return {"message": "success", "error": False}

def delete_driver(driver_id):
    driver_db = Driver.objects.get(id=driver_id)
    deleted_driver = driver_db.to_object()
    driver_db.delete()
    return {
            "message": "Driver deleted successfully!",
            "data": deleted_driver,
            "error": False,
        }
    
driver_ctl = {
    "create":create_driver,
    "read":get_drivers,
    "update":update_driver,
    "delete":delete_driver,
}