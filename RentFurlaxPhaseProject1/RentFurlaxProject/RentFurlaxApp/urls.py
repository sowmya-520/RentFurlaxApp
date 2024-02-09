from django.urls import path
from .views import *
urlpatterns = [
   
    path('register/',RegisterView.as_view()),         #to get  and create registration details      
    path('register/<int:id>',RegisterView.as_view()), #to get specific user registration details
    path('login/',LoginView.as_view()),               #login
    path('category/',CreateCategoryView.as_view()),   #to create category
    path('categories/',getcategoryView.as_view()),    #to view all categories
    path('categories/<int:id>',getcategoryView.as_view()),  #getting specific category through id
    path('product/',AddProductView.as_view()),        #add products
    path('category/<str:category>',getproductsbycategory_View.as_view()),   #get products by category
    path('invoices/<str:status>',get_invoice_based_on_status.as_view()),
    path('invoice/',CreateInvoiceView.as_view()),
]
