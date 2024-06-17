from django.contrib import admin
from schema.models import Node

""" SUPER USER """
# username: schema
# pw: schema1234
# email: schema@gmail.com

""" 기본 """
# admin.site.register(Node)

""" 지정 """
@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
  list_display = [  
                  'nodeId', 
                  'reg_dt', 'chg_dt', 
                  'name', 'dictionary', 'enumerations', 'parent', 
                  'sub_name', 'sub_display_name', 'enumerations_html', 
                  'name_capital'  # temp
                ]
  list_display_links = ['name']
  list_filter = ['parent']
  search_fields = ['name']
  
  
  
  def name_capital(self, node):
    return node.name[0]
  
