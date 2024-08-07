import pandas as pd

df1= pd.read_csv('C:/Users/ovidalu/Desktop/TP-1-Parte-3/PANDAS/ecommerce_customers_dataset.csv',encoding='utf-8')
df2= pd.read_csv('C:/Users/ovidalu/Desktop/TP-1-Parte-3/PANDAS/ecommerce_order_items_dataset.csv',encoding='utf-8')
df3= pd.read_csv('C:/Users/ovidalu/Desktop/TP-1-Parte-3/PANDAS/ecommerce_order_payments_dataset.csv',encoding='utf-8')
df4= pd.read_csv('C:/Users/ovidalu/Desktop/TP-1-Parte-3/PANDAS/ecommerce_orders_dataset.csv',encoding='utf-8')
df5= pd.read_csv('C:/Users/ovidalu/Desktop/TP-1-Parte-3/PANDAS/ecommerce_products_dataset.csv',encoding='utf-8')

df1.set_index('customer_id', inplace=True)
df2.set_index('order_id', inplace=True)
df3.set_index('order_id', inplace=True)
df4.set_index('order_id', inplace=True)
df5.set_index('product_id', inplace=True)

clientes_unicos= df1['customer_unique_id'].nunique()#conteo total clientes unicos
print("la cantidad de clientes unicos es", clientes_unicos)

valor_promedio=df3['payment_value'].mean()
print("el valor promedio por pedido es", valor_promedio)

producto_mas_vendido=df5['product_category_name'].value_counts()#identificar cantidad de veces de producto
producto_mas_repetido= producto_mas_vendido.idxmax()# funcion para indentificar el producto mas repetido
print("el producto mas vendido es", producto_mas_repetido)

pedidos_realizados=len(df4)#conteo cantidad de filas en dataframe
print("la cantidad de pedidos realizados es", pedidos_realizados)




