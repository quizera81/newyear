from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name="index"), 
    path("Kwizera",views.kwizera, name="Kwizera"),
    path("david",views.david,name="david"),
    path("ghislain",views.ghislain, name="ghislain"),
    path("didier",views.didier ,name="didier"),
    path("manzi",views.manzi , name="manzi"),
    path("<str:name>",views.greet, name="greet")

]
 