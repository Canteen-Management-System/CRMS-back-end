from django.urls import include, path
from accounts.api.viewset import CustomTokenObtainPairView, UsersList, DepartmentList, DepartmentDetail, RoleDetail, RoleList, JobTitleDetail, JobTitleList

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token'),
    path('users', UsersList.as_view(), name='users_list'),
    # Department
    path('department-list', DepartmentList.as_view(), name='department_list'),
    path('department-detail/<int:pk>',
         DepartmentDetail.as_view(), name='department_detail'),
    # Role
    path('role-list', RoleList.as_view(), name='role_list'),
    path('role-detail/<int:pk>', RoleDetail.as_view(), name='role_detail'),
    # Job Title
    path('positions-list', JobTitleList.as_view(), name='positions_list'),
    path('positions-detail/<int:pk>',
         JobTitleDetail.as_view(), name='positions_detail'),
]
