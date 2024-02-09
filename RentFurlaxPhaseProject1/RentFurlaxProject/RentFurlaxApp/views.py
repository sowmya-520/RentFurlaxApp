from django.shortcuts import render
from .models import Customer,Category,Product,Invoice
from rest_framework.views import APIView
from .serializers import CustomerSerialilizer,CategorySerialilizer,ProductSerializer,InvoiceSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):

    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        if id:
            result=Customer.objects.get(id=id)
            serializer=CustomerSerialilizer(result)
            return Response({'status':'success','customers':serializer.data},status=status.HTTP_200_OK)
        else:
            result=Customer.objects.all()
            serializer=CustomerSerialilizer(result,many=True)
            return Response({'status':'success','customers':serializer.data},status=status.HTTP_200_OK)
    
    def post(self,request):   
        try:    
            serializer=CustomerSerialilizer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':'success!! Data Added Successfully','data':serializer.data},status=status.HTTP_200_OK)
        except:
                return Response({'status':'error','data':"Enter Unique data"},status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user=Customer.objects.get(username=username)
            if user.password==password:
                return Response({"username":username,"password":password},status=status.HTTP_200_OK)
            else:
                return Response({"error":"Invalid password"},status=status.HTTP_404_NOT_FOUND)
        except:
                 return Response({'error': 'User Doesn\'t Exists'},status=status.HTTP_400_BAD_REQUEST)



class CreateCategoryView(APIView):
    permission_classes=[IsAuthenticated]  
    def post(self,request):
        try:    
            serializer=CategorySerialilizer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        except:
                return Response({'status':'error','data':"Category already exists"},status=status.HTTP_400_BAD_REQUEST)



class getcategoryView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        if id:
            result=Category.objects.get(id=id)
            serializer=CategorySerialilizer(result)
            return Response({'status':'success','categories':serializer.data},status=status.HTTP_200_OK)
        else:
            result=Category.objects.all()
            serializer=CategorySerialilizer(result,many=True)
            return Response({'status':'success','categories':serializer.data},status=status.HTTP_200_OK)

class AddProductView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer= ProductSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class getproductsbycategory_View(APIView):
    def get(self, request, *args, **kwargs):
        categoryname= kwargs.get("category")
        try:
            id= Category.objects.get(type=categoryname).id
            products= Product.objects.filter(category=id)
            serializer= ProductSerializer(products, many=True)
            return Response({'message': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'error', 'data': "category doesnot exists"}, status=status.HTTP_400_BAD_REQUEST)

class CreateInvoiceView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
            serializer = InvoiceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class get_invoice_based_on_status(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            status = kwargs.get("status")
            print(status)
            if status in ["ORDERED", "DELIVERED", "CANCELLED"]:
                result = Invoice.objects.filter(status=status)
                serializer = InvoiceSerializer(result, many=True)
                if len(serializer.data) != 0:
                    return Response({'message': "success", "invoices": serializer.data})
                else:
                    result = Invoice.objects.all()
                    serializer = InvoiceSerializer(result, many=True)
                    return Response({"message": "SUCCESS", "invoices": serializer.data})
            else:
                return Response({"message": "error", "invoices": "invoice doesn't exist!!"})
        except Invoice.DoesNotExist:
            return Response({"message": "No invoices with the given status found."})


     
        
