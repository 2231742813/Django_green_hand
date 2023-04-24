from django.shortcuts import render


# Create your views here.
def runoob(request) :
    context = {'hello' : 'Hello World!'}
    return render(request, 'runoob.html', context)


def runoob1(request) :
    views_name = "菜鸟教程"
    return render(request, "runoob1.html", {"name" : views_name})

def runoob2(request):
    import datetime
    now = datetime.datetime.now()
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    name1 = ['runoob2',123,now,'ter',{"age":25},{"addres":"anhui"},views_str]
    return render(request, "runoob2.html", {"name1" : name1})

def runoob3(request):
    json = {"grade":20,"list":[1,2,3],"views_list" :["a", "b", "c", "d", "e"]}
    return render(request, "runoob3.html", {"json" : json})

def runoob4(request):
    name = "菜鸟教程"
    return render(request, "runoob4.html", {"name" : name})

# @register.filter
# def my_filter(v1, v2):
#     return v1 * v2