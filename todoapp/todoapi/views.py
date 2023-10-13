from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Todo
from .serializers import TodoSerializer

class TodoListApiView(APIView):
  permission_classes = [permissions.IsAdminUser]

  # Get the list of todo
  def get(self, request, *args, **kwargs):
    todos = Todo.objects.filter(user = request.user.id)

    serializer = TodoSerializer(todos, many=True)

    return Response(
      {
        "Message": "List of Todo",
        "Data": serializer.data
      }, 
      status = status.HTTP_200_OK
    )
  
  # Post a new todo
  def post(self, request, *args, **kwargs):
    data = {
      'title': request.data.get('title'),
      'description': request.data.get('description'),
      'user': request.user.id,
    }

    serializer = TodoSerializer(data=data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(
        {
          "Message": "Successfully create a new Todo",
          "Data": serializer.data
        }, 
        status = status.HTTP_201_CREATED
      )
    
    return Response(
      serializer.errors,
      status = status.HTTP_400_BAD_REQUEST
    )

class TodoDetailApiView(APIView):
  permission_classes = [permissions.IsAuthenticated]
  
  # get objects from database
  def get_object(self, todo_id, user_id):
    try:
      return Todo.objects.get(
        id = todo_id, 
        user = user_id
      )
    except Todo.DoesNotExist:
      return None
    

  # get detail object
  def get(self, request, todo_id, *args, **kwargs):

    todo_instance = self.get_object(
      todo_id, 
      request.user.id
    )

    if not todo_instance:
      return Response(
        {
          "Message": "Object with todo id does not exists",
        },
        status = status.HTTP_400_BAD_REQUEST
      )
    
    serializer = TodoSerializer(todo_instance)

    return Response(
      {
        "Message": "Todos found",
        "Data": serializer.data
      },
      status = status.HTTP_200_OK 
    )
  
  # update object
  def put(self, request, todo_id, *args, **kwargs):

    todo_instance = self.get_object(
      todo_id,
      request.user.id
    )

    if not todo_instance:
      return Response(
        {
          "Message": "Todo with todo id does not exists",
        },
        status = status.HTTP_400_BAD_REQUEST
      )
    
    data = {
      "title": request.data.get("title"),
      "description": request.data.get("description"),
      "user": request.user.id
    }
    
    serializer = TodoSerializer(
      instance = todo_instance,
      data = data,
      partial = True
    )

    if serializer.is_valid():
      serializer.save()
      return Response(
        {
          "Message": "Successfully updated a Todo",
          "Data": serializer.data
        },
        status = status.HTTP_200_OK
      )
    
    return Response(
      serializer.errors,
      status = status.HTTP_400_BAD_REQUEST
    )
  
  # delete object
  def delete(self, request, todo_id, *args, **kwargs):

    todo_instance = self.get_object(
      todo_id,
      request.user.id
    )

    if not todo_instance:
      return Response(
        {
          "Message": "Todo with todo id does not exists",
        },
        status = status.HTTP_400_BAD_REQUEST
      )
    
    todo_instance.delete()

    return Response(
      {
        "Message": "Todo deleted!",
      },
      status = status.HTTP_200_OK
    )
