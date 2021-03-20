from .models import stu
def searching(search_input : str):
    try:
        record = stu.objects.filter(name=search_input)
        if record:
            print("nisar")
            return record
    except Exception as e:
        print(e)

