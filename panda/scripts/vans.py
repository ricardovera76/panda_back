from panda.models import Driver, Van


def get_vans():
    van_list = Van.objects.all()
    van_acc_list = []
    for van in van_list:
        current_van = van.to_object()
        current_van["driver"] = Driver.objects.filter(_d=current_van["driver_id"])[
            0
        ].to_object()
        van_acc_list.append(current_van)

    return {"message": "success", "error": False, "data": van_acc_list}


def create_van(van_data):
    van_data["driver_id"] = Driver.objects.filter(id=van_data["driver_id"])[0]
    van_db = Van(**van_data)
    van_db.save()
    return {"message": "successfully added van", "error": False}


def update_van(vanId, data, types):
    update_types = {"dr": "driver_id", "id": "_id"}
    van_db = Van.objects.get(id=vanId)
    data = Driver.objects.filter(id=data[update_types[types]])[0] if "dr" == types else data
    setattr(van_db, update_types[types], data[update_types[types]])
    van_db.save()
    return {"message": "success", "error": False}


def delete_van(van_id):
    print(van_id)
    van_db = Van.objects.get(id=str(van_id))
    deleted_van = van_db.to_object()
    van_db.delete()
    return {
            "message": "Van deleted successfully!",
            "data": deleted_van,
            "error": False,
        }


van_ctl = {
    "create": create_van,
    "read": get_vans,
    "update": update_van,
    "delete": delete_van,
}
