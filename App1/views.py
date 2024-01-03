from django.shortcuts import render
from .models import Customer, Orders, Product, Orderitems, Purchase, Payments
from django.views.decorators.csrf import csrf_exempt
from .serializers import CustomSerializers, OrderSerializers, ProductSerializers, OrderItemSerializer, PurchaseSerializer, PaymentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from datetime import datetime
from django.db.models import Q


@api_view(['GET'])
def CustomerAPI(request):
    if request.method == 'GET':
        obj = Customer.objects.all()
        email_customer = request.query_params.get('email') # successful orders so far from customer email
        t_shirt = request.query_params.get('t_shirt') == 'true' # how many t shirt bought customer with email
        user_email = request.query_params.get('user_email') # customer who bought t shirt
        revenue_by_user = request.query_params.get('customer_email') # total revenue earn by user
        print(t_shirt)

        if email_customer:
            try:
                obj = Customer.objects.get(email=email_customer)

                total_order = Orders.objects.filter(Q(status='delivered') & Q(customer_id=obj.id))
                # serializers = CustomSerializers(obj)
                # serializers = OrderSerializers(total_order, many=True)
                count = 0
                for i in total_order:
                    count += 1
                return Response(data={"message":f"total number of customer {email_customer} order succssfully deliver {count}"}, status=status.HTTP_200_OK)
            except Customer.DoesNotExist as e:
                return Response(data={'message':' Email with customer Does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if t_shirt:
            try:
                obj = Customer.objects.get(email=user_email)
                print('userobject',obj)
                try:
                    t_order = Orders.objects.filter(Q(status='delivered') & Q(customer_id=obj))
                    print(t_order)
                    quantity = 0
                    for i in t_order:
                        # a = i.id
                        # print(a)
                        order_item = Orderitems.objects.filter(order=i.id)
                        for i in order_item:
                            quantity += i.qantity
                    return Response(data={'message':f'total {quantity} t_shirt bought by {user_email}'})
                        
                        # except Orders.DoesNotExist:
                        #     return Response(data={'message':f'orderitem not delivered'}, status=status.HTTP_200_OK)
                    # return Response(data={'message':f'{t_order}'}, status=status.HTTP_200_OK)
                    
                    # print(t_order)

                    # for i in t_order:
                    #     print(i)
                        # quantity = Orderitems.objects.filter(order=t_order)
                        
                    # return Response(data={'message':f"{quantity}"}, status=status.HTTP_200_OK)
                    
                except Orders.DoesNotExist:
                    return Response(data={'message':f'any order does not delivered'},  status=status.HTTP_200_OK)
                
            except Customer.DoesNotExist:
                return Response(data={'message':f'customer with {user_email} does not exist'}, status=status.HTTP_404_NOT_FOUND)
            
        if revenue_by_user:
            try:
                obj = Customer.objects.get(email=revenue_by_user)
                try:
                    p_order = Orders.objects.filter(Q(status='delivered') & Q(customer_id=obj))
                    total_purchase = 0
                    for i in p_order:
                        payment_order = Payments.objects.filter(Q(status='success') & Q(order=i.id))
                        for i in payment_order:
                            total_purchase += i.amount
                    
                    return Response(data={'message':f'total {total_purchase} earn by {revenue_by_user}'})

                
                except Orders.DoesNotExist:
                    return Response(data={'message':f'any order does not exist'},)
            except Customer.DoesNotExist:
                return Response(data={'message':f'customer with {revenue_by_user} does not exist'}, status=status.HTTP_404_NOT_FOUND)


        serializers = CustomSerializers(obj)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
    

class OrderAPI(APIView):
    def get(self, request):

        obj = Orders.objects.all()

        s_status = request.query_params.get('status') # check the status of order pending/success/failed
        c_status = request.query_params.get('count')  
        d_s_status = request.query_params.get('s_date') # total pending orders between start date
        d_e_status = request.query_params.get('e_date') # toal pending orders between end sate
        # email_customer = request.query_params.get('email')


        if s_status:
            obj = Orders.objects.filter(status=s_status)
            serializer = OrderSerializers(obj, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        

        if c_status:
            obj = Orders.objects.filter(status=c_status)
            c_count = 0
            for i in obj:
                c_count += 1
            return Response(data={"message":f"total number of {c_status} status {c_count}"}, status=status.HTTP_200_OK)
        

        if d_s_status:
            # x = datetime(d_s_status)
            # y = datetime(d_e_status)
            obj = Orders.objects.filter(Q(status='pending') & Q(created_date__date__range=(d_s_status,d_e_status)))
            serializer = OrderSerializers(obj, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        

        # if email_customer:
        #     obj = Orders.objects.filter(customer_id=email_customer)
        #     serializer = CustomSerializers(obj)
        #     return Response(data=serializer.data, status=status.HTTP_200_OK)


        serializer = OrderSerializers(obj, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductAPI(APIView):


    def get(self, request):
        product_name = request.query_params.get('t_shirt') # stock remain of t shirt
        obj = Product.objects.all()

        if product_name:
            try:
                obj = Product.objects.get(name=product_name)
                try:
                    stock_remail = Purchase.objects.get(product=obj)
                    remain_stock = stock_remail.qantity

                    return Response(data={"message":f" total remain {product_name}  {remain_stock}"}, status=status.HTTP_200_OK)
                
                except Purchase.DoesNotExist:
                    return Response(data={"message":f"product does not Exist"}, status=status.HTTP_204_NO_CONTENT)
            
            except Exception as e:
                return Response(data={"message":f"{e}"}, status=status.HTTP_204_NO_CONTENT)

        serializer = ProductSerializers(obj, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class PaymnetAPI(APIView):

    def get(self, request):
        obj = Payments.objects.all()
        d_revenue = request.query_params.get('date')

        if d_revenue:
            obj = Payments.objects.filter(Q(status='success') & Q(created_date__date=d_revenue))
            total_revenue = 0
            for i in obj:
                total_revenue += i.amount
            return Response(data={'message':f'total {total_revenue} revenue generate on date {d_revenue}'}, status=status.HTTP_200_OK)

        serializer = PaymentSerializer(obj, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)