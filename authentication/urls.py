from django.urls import path
from authentication import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('employee-register/',views.employee_register,name="employee-register"),
    path('edit-employee/<int:id>/<str:token>/<str:name>',views.edit_employee,name="edit-employee"),
    path('update-profile/<int:id>/<str:token>/<str:name>',views.update_profile,name="update-profile"),
    path('user-delete/<int:pk>',views.user_delete,name="user-delete"),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('login/',views.login,name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('manager-list/',views.manager_list,name="manager-list"),
    path('manager-del/<int:pk>/',views.manager_del,name="manager-del"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(), 
        name="password_reset_done"), 

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(), 
        name="password_reset_complete"),

    path('change_password/',
        auth_views.PasswordChangeView.as_view(),
        name="change_password"),

    path('group/',views.groups,name="group"),
    path('group_add/',views.group_add,name="group_add"),
    path('group_del/<str:name>',views.group_del,name="group_del"),
    path('user-group/<int:pk>/',views.user_group,name="user-group"),
    path('add-user-group/<int:pk>/',views.add_user_group,name="add-user-group"),
    path('del-user-group/<int:pk>/<str:name>/',views.del_user_group,name="del-user-group"),

    path('perms/',views.perms,name="perms"),
    path('perms-del/<str:name>',views.perms_del,name="perms-del"),
    path('perms-add/',views.perms_add,name="perms-add"),
    path('user-perms/<int:pk>',views.user_perms,name="user-perms"),
    path('add-user-perms/<int:pk>',views.add_user_perms,name="add-user-perms"),
    path('del-user-perms/<int:pk>/<str:name>',views.del_user_perms,name="del-user-perms"),

    path('group-perms/<str:name>/',views.group_perms,name="group-perms"),
    path('add-group-perms/<str:name>/',views.add_group_perms,name="add-group-perms"),
    path('del-group-perms/<str:gname>/<str:name>/',views.del_group_perms,name="del-group-perms"),
]