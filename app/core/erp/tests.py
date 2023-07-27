from config.wsgi import *
from core.erp.models import Type,Employee,Category
#Listar

#query=Type.objects.all()
#print(query)

#inserccion
#t=Type()
#t.name='Fatima'
#t.save()***/

#Edicion
#try:
#    t=Type.objects.get(id=1)
 #   t.name="cincox4"
  #  t.save()
#except Exception as e:
 #   print(e)
    
#eliminacion
#t=Type.objects.get(id=1)
#t.delete()

# Filtros
#obj=Type.objects.filter(name__contains='fa')
#obj=Type.objects.filter(name__icontains='fa')
#obj=Type.objects.filter(name__startswith='B')
#obj=Type.objects.filter(name__endswith='a')
obj1=Category.objects.filter(name__contains='Sis')
print(obj1)


for i in Type.objects.filter(name__endswith='a'):
    print(i.name)