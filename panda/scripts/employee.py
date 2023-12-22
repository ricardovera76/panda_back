from panda.models import Employee, Driver, Route


def get_employees():
    employee_db = Employee.objects.all()
    employee_list = [employee.to_object() for employee in employee_db]
    for employee in employee_list:
        employee["driver_name"] = Driver.objects.filter(id=employee["driver_id"])[
            0
        ].to_object()["name"]
        employee_route = Route.objects.filter(id=employee["route_id"])[0].to_object()
        employee["route_descr"] = employee_route["descr"]
        employee["route_address"] = employee_route["address"]
    return {"message": "success", "error": False, "data": employee_list}


def create_employees(employee_data):
    employee_data["driver_id"] = Driver.objects.filter(id=employee_data["driver_id"])[0]
    employee_data["route_id"] = Route.objects.filter(id=employee_data["route_id"])[0]
    employee_db = Employee(**employee_data)
    employee_db.save()
    return {"message": "successfully added employee", "error": False}


def update_employee(employee_id, data, types):
    update_types = {
        "ad": "address",
        "nm": "name",
        "ph": "phone",
        "sf": "shift",
        "dr": "driver_id",
        "rt": "route_id",
        "cp": "company",
        "cm": "comments",
    }

    employee_db = Employee.objects.get(id=employee_id)
    data = Driver.objects.filter(id=data)[0] if "dr" == types else data
    data = Route.objects.filter(id=data)[0] if "rt" == types else data
    setattr(employee_db, update_types[types], data[update_types[types]])
    employee_db.save()
    return {"message": "success", "error": False}


def delete_employee(employee_id):
    employee_db = Employee.objects.get(id=employee_id)
    deleted_employee = employee_db.to_object()
    employee_db.delete()
    return {
        "message": "Employee deleted successfully!",
        "data": deleted_employee,
        "error": False,
    }


employee_ctl = {
    "create": create_employees,
    "read": get_employees,
    "update": update_employee,
    "delete": delete_employee,
}
