from django.urls import path
from . import views

urlpatterns=[
	path('',views.index),
	path('services/',views.services),
	path('about/',views.about),
	path('contact/',views.contact),
	path('gallery/',views.gallery),
    path('single/',views.single),
    path('get/',views.get),


##########################################admin############################################################	

    path('admin_index/',views.admin_index),
    path('admin_login/',views.admin_login),
    path('admin_register/',views.admin_register),
    path('admin_logout/',views.admin_logout),
    path('admin_forms/',views.admin_forms),
    path('admin_cform/',views.admin_cform),
    path('admin_table/',views.admin_table),
    path('admin_update/',views.admin_update),
    path('admin_delete/',views.admin_delete),
    path('admin_gallery/',views.admin_gallery),
    path('admin_gallerytb/',views.admin_gallerytb),
    path('admin_galldlt/',views.admin_galldlt),
    path('admin_contacttb/',views.admin_contacttb),
    path('admin_ctable/',views.admin_ctable),
    path('admin_cupdate/',views.admin_cupdate),
    path('admin_tform/',views.admin_tform),
    path('admin_ttable/',views.admin_ttable),
    path('admin_tupdate/',views.admin_tupdate),
    path('admin_tdelete/',views.admin_tdelete),
    path('admin_booking/',views.admin_booking)

]