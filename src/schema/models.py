from django.db import models
from django.utils.translation import gettext as _

from mptt.models import MPTTModel, TreeForeignKey


class Node(MPTTModel):
  nodeId = models.BigAutoField(_('ID'), primary_key=True, db_column='ID')
  reg_dt = models.DateTimeField(_('생성일'), auto_now_add=True, db_column='REG_DT')
  chg_dt = models.DateTimeField(_('수정일'), auto_now=True, db_column='CHG_DT')
  name = models.CharField(_('이름'), max_length=255, db_column='NAME')
  parent = TreeForeignKey('self', verbose_name=_('상위분류'), null=True, blank=True, on_delete=models.CASCADE, related_name='children', db_index=True, db_column='PARENT')
  
  sub_name = models.CharField(_('서술용 이름'), max_length=255, null=True, db_column='SUB_NAME')
  sub_display_name = models.CharField(_('화면용 이름'), max_length=255, null=True, db_column='SUB_DISPLAY-NAME')
  dictionary = models.CharField(_('설명'), max_length=255, null=True, db_column='DICTIONARY')
  
  enumerations = models.JSONField(default=dict, db_column='ENMERATIONS') # SQLite 외 : models.ArrayField(_('속성값 목록'), models.CharField(max_length=255), null=True, blank=True, db_column='ENUMERATIONS')  
  enumerations_html = models.CharField(_('속성값 목록 HTML'), max_length=255, null=True, blank=True, db_column='ENUMERATIONS_HTML')

  class Meta:
    ordering = ['nodeId']
    db_table = u'NODE'  
    
  class MPTTMeta:
    order_insertion_by = ['nodeId']
    
  def __str__(self):
    return f'{self.nodeId}: {self.name}'
    
    
  
  
# class LeafNode(models.Model):
#   leafNodeId = models.BigAutoField(_('ID'), primary_key=True, db_column='ID')
#   name = models.CharField(_('이름'), max_length=255)
#   parent = TreeForeignKey('Node', verbose_name=_('상위분류'), on_delete=models.SET_NULL, null=True, blank=True, db_index=True, db_column='Node')
  
#   sub_name = models.CharField(_('서술용 이름'), max_length=255, null=True, db_column='SUB_NAME')
#   sub_display_name = models.CharField(_('화면용 이름'), max_length=255, null=True, db_column='SUB_DISPLAY-NAME')
#   dictionary = models.CharField(_('설명'), max_length=255, null=True, db_column='DOCUMENTATION')
  
#   enumerations = models.JSONField(default=dict) # SQLite 외 : models.ArrayField(_('속성값 목록'), models.CharField(max_length=255), null=True, blank=True, db_column='ENUMERATIONS')  
#   enumerations_html = models.CharField(_('속성값 목록 HTML'), max_length=255, null=True, blank=True, default='', db_column='ENUMERATIONS_HTML')