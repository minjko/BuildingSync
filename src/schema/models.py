from django.db import models
from django.utils.translation import gettext as _

from mptt.models import MPTTModel, TreeForeignKey


class TimeStampedModel(models.Model):
  reg_dt = models.DateTimeField(auto_now_add=True)
  edt_dt = models.DateTimeField(auto_now=True)
  


class Node(TimeStampedModel, MPTTModel):
  nodeId = models.BigAutoField(_('ID'), primary_key=True, db_column='ID')
  name = models.CharField(_('이름'), max_length=255)
  parent = TreeForeignKey('self', verbose_name=_('상위분류'), null=True, blank=True, on_delete=models.CASCADE, related_name='children', db_index=True, db_column='PARENT')
  
  sub_name = models.CharField(_('서술용 이름'), max_length=255, null=True, db_column='SUB_NAME')
  sub_display_name = models.CharField(_('화면용 이름'), max_length=255, null=True, db_column='SUB_DISPLAY-NAME')
  dictionary = models.CharField(_('설명'), max_length=255, null=True, db_column='DOCUMENTATION')
  
  enumerations = models.JSONField(default=dict) # SQLite 외 : models.ArrayField(_('속성값 목록'), models.CharField(max_length=255), null=True, blank=True, db_column='ENUMERATIONS')  
  enumerations_html = models.CharField(_('속성값 목록 HTML'), max_length=255, null=True, blank=True, default='', db_column='ENUMERATIONS_HTML')

  class Meta:
    ordering = ['nodeId']
    db_table = 'NODE'  
    
  class MPTTMeta:
    order_insertion_by = ['nodeId']
    
  def __str__(self):
    return f'{self.id} -> {self.nodeId}: {self.name}'
    
    
  
  
# class LeafNode(TimeStampedModel):
#   leafNodeId = models.BigAutoField(_('ID'), primary_key=True, db_column='ID')
#   name = models.CharField(_('이름'), max_length=255)
#   parent = TreeForeignKey('Node', verbose_name=_('상위분류'), on_delete=models.SET_NULL, null=True, blank=True, db_index=True, db_column='Node')
  
#   sub_name = models.CharField(_('서술용 이름'), max_length=255, null=True, db_column='SUB_NAME')
#   sub_display_name = models.CharField(_('화면용 이름'), max_length=255, null=True, db_column='SUB_DISPLAY-NAME')
#   dictionary = models.CharField(_('설명'), max_length=255, null=True, db_column='DOCUMENTATION')
  
#   enumerations = models.JSONField(default=dict) # SQLite 외 : models.ArrayField(_('속성값 목록'), models.CharField(max_length=255), null=True, blank=True, db_column='ENUMERATIONS')  
#   enumerations_html = models.CharField(_('속성값 목록 HTML'), max_length=255, null=True, blank=True, default='', db_column='ENUMERATIONS_HTML')