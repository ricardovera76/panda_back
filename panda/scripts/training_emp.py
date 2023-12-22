from panda.models import TrainingEmployee


def get_training_employees():
    employee_list = TrainingEmployee.objects.all()
    employee_acc_list = []
    for employee in employee_list:
        employee_acc_list.append(employee.to_object())
    return employee_acc_list


def create_training_employee(data):
    pass


def update_training_employee(trainingEmployeeId, data, types):
    pass


def delete_training_employee(trainingEmployeeId,):
    pass


training_employee_ctl = {
    "create": create_training_employee,
    "read": get_training_employees,
    "update": update_training_employee,
    "delete": delete_training_employee,
}
