from django.contrib import admin
from .models import *


class TbPlatAdmin(admin.ModelAdmin):
    list_dispaly = ['id', 'plat_name']


class TbModuAdmin(admin.ModelAdmin):
    list_dispaly = ['id', 'modu_name']


class TbModuleVersionadmin(admin.ModelAdmin):
    list_display = ['pre_plat_id', 'pre_module_id', 'v1', 'v2', 'v3', 'v4', 'last_update_time', 'pre_tag_path']
    list_per_page = 10
    list_filter = ['pre_module_id']    #后台页面右侧过滤项指定字段
    #search_fields = ['pre_module_id']   #后台页面查询项指定字段


class TbRecordadmin(admin.ModelAdmin):
    list_display = ['bef_plat_id', 'bef_module_id', 'bef_version', 'update_date', 'cause', 'bef_tag_path']
    list_per_page = 10


admin.site.register(TbPlat, TbPlatAdmin)
admin.site.register(TbModu, TbModuAdmin)
admin.site.register(TbModuleVersion, TbModuleVersionadmin)
admin.site.register(TbRecord, TbRecordadmin)
