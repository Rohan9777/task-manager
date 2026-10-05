from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer

# Create your views here.
class TaskListCreateView(APIView):
    
    def listTasks(self,request):
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks,many=True)
        
        return Response(serializer.data)
    
    
    def createTask(self,request):
        serializer=TaskSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
            
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
    def get(self,request):
        return self.listTasks(request)
    
    def post(self,request):
        return self.createTask(request)
    

class TaskDetailView(APIView):
    
    def listTaskById(self,request,taskId):
        try:
            task=Task.objects.get(id=taskId)
        
        except Task.DoesNotExist:
            return Response(
                {"errors":"Task not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer=TaskSerializer(task)
        
        return Response(serializer.data)
    
    def updateTaskById(self,request,taskId):
        try:
            task=Task.objects.get(id=taskId)
        
        except Task.DoesNotExist:
            return Response(
                {"errors":"Task not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer=TaskSerializer(task,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def deleteTaskById(self,request,taskId):
        try:
            task=Task.objects.get(id=taskId)
            
        except Task.DoesNotExist:
            return Response(
                {"error":"Task not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        task.delete()
        
        return Response(
            {"message":"Task deleted successfully"},
            status=status.HTTP_200_OK
        )
    
    def get(self,request,taskId):
        return self.listTaskById(request,taskId)
    
    def put(self,request,taskId):
        return self.updateTaskById(request,taskId)
    
    def delete(self,request,taskId):
        return self.deleteTaskById(request,taskId)

