from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_dept(request):
        LOD=Dept.objects.all()
        d={'dept':LOD}
        if request.method=='POST':
            dt=request.POST['dt']
            dn=request.POST['dn']
            dl=request.POST['dl']
            DO=Dept.objects.get_or_create(deptno=dt,dname=dn,dloc=dl)[0]
            DO.save()

            return render(request,'index.html',d)
        return  render(request,'index.html')


def insert_emp(request):
      LOT=Dept.objects.all()
      d={'deptno':LOT}
      if request.method=='POST':
            no=request.POST['no']
            na=request.POST['na']
            jo=request.POST['jo']
            mg=request.POST['mg']
            date=request.POST['date']
            sal=request.POST['sal']
            de=request.POST['de']
            LO=Dept.objects.get(deptno=de)
            
            WO=Employee.objects.get_or_create(empno=no,empname=na,job=jo,mgr=mg,hiredate=date,sal=sal,deptno=LO)[0]
            WO.save()
            return HttpResponse('succes')
      return render(request,'emp.html',d)
