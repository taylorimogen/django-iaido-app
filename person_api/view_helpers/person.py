from person_api.models import Person

def get_filtered_queryset(request):
    queryset = Person.objects.all()
    first_name = request.query_params.get('first_name')
    last_name = request.query_params.get('last_name')
    age = request.query_params.get('age')
    if first_name is not None:
        queryset = queryset.filter(first_name=first_name)
    if last_name is not None:
        queryset = queryset.filter(last_name=last_name)
    if age is not None:
        queryset = queryset.filter(age=age)
    return queryset