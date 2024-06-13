from rest_framework import generics
from rest_framework import views

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from django.shortcuts import render

from .models import Node
from .serializers import NodeViewSerializer

# https://velog.io/@duo22088/DRF-Renderer-%EB%A5%BC-%ED%86%B5%ED%95%9C-%EB%8B%A4%EC%96%91%ED%95%9C-%EC%9D%91%EB%8B%B5

class NodeView(views.APIView):
  #queryset = Node.objects.all()
  #renderer_classes = [TemplateHTMLRenderer] 
  #template_name = 'schema/detail.html'
  
  def get(self, request, *args, **kwargs):
    
    nodes = Node.objects.filter(parent=None)
    serializer = NodeViewSerializer(nodes, many=True)
    
    return Response(serializer.data) # render(request, 'schema/detail.html') #, {'schema': self.queryset})



def node_tree_view(request):
  
  return render(request, 'schema/node_tree.html')


""" Data 생성 
root = Node.objects.create(name='BuildingSync')

programs = Node.objects.create(name='Programs', parent=root, dictionary='[설명] Programs')
facilities = Node.objects.create(name='Facilities', parent=root, dictionary='[설명] Facilities')

program = Node.objects.create(name='Program', parent=programs, dictionary='[설명] Program')
facility = Node.objects.create(name='Facility', parent=facilities, dictionary='[설명] Facility')

programData = Node.objects.create(name='ProgramData' , parent=program, dictionary='[설명] ProgramData')
programFundingSource = Node.objects.create(name='ProgramFundingSource' , parent=program, dictionary='[설명] Program Funding Source')
programClassification = Node.objects.create(name='ProgramClassification' , parent=program, dictionary='[설명] ProgramClassification')
sites = Node.objects.create(name='Sites' , parent=facility, dictionary='[설명] Sites')
#systems = Node.objects.create(name='Systems' , parent=facility, dictionary='[설명] Systems')
auditCycles = Node.objects.create(name='AuditCycles' , parent=facility, dictionary='[설명] AuditCycles')
schedules = Node.objects.create(name='Schedules' , parent=facility, dictionary='[설명] Schedule')
mesures = Node.objects.create(name='Mesures' , parent=facility, dictionary='[설명] Mesures')
reports = Node.objects.create(name='Reports' , parent=facility, dictionary='[설명] Reports')
contacts = Node.objects.create(name='Contacts' , parent=facility, dictionary='[설명] Contacts')
tenants = Node.objects.create(name='Tenants' , parent=facility, dictionary='[설명] Tenants')
userDefinedFields = Node.objects.create(name='UserDefinedFields' , parent=facility, dictionary='[설명] UserDefinedFields')

site = Node.objects.create(name='Site', parent=sites, dictionary='[설명] Site')
#system = Node.objects.create(name='System' , parent=systems, dictionary='[설명] System')
auditCycle = Node.objects.create(name='AuditCycle' , parent=auditCycles, dictionary='[설명] AuditCycle')
schedule = Node.objects.create(name='Schedule' , parent=schedules, dictionary='[설명] Schedule')
mesure = Node.objects.create(name='Mesure' , parent=mesures, dictionary='[설명] Mesure')
report = Node.objects.create(name='Report' , parent=reports, dictionary='[설명] Report')
contact = Node.objects.create(name='Contact' , parent=contacts, dictionary='[설명] Contact')
tenant = Node.objects.create(name='Tenant' , parent=tenants, dictionary='[설명] Tenant')
userDefinedField = Node.objects.create(name='UserDefinedField' , parent=userDefinedFields, dictionary='[설명] UserDefinedField')

schedulePerioBeginDate = Node.objects.create(name='SchedulePerioBeginDate', parent=schedule, dictionary='[설명] SchedulePerioBeginDate')
schedulePerioEndDate = Node.objects.create(name='SchedulePerioEndDate', parent=schedule, dictionary='[설명] SchedulePerioEndDate')
scheduleDetails = Node.objects.create(name='ScheduleDetails', parent=schedule, dictionary='[설명] ScheduleDetails')
linkedPremises = Node.objects.create(name='LinkedPremises', parent=schedule, dictionary='[설명] LinkedPremisses')
tenantName = Node.objects.create(name='TenantName', parent=tenant, dictionary='[설명] TenantName')
contactIDs = Node.objects.create(name='ContactIDs', parent=tenant, dictionary='[설명] ContactIDs')

scheduleDetail = Node.objects.create(name='ScheduleDetail', parent=scheduleDetails, dictionary='[설명] ScheduleDetail')
building = Node.objects.create(name='Building', parent=linkedPremises, dictionary='[설명] Building')
section = Node.objects.create(name='Section', parent=linkedPremises, dictionary='[설명] Section')

dayType = Node.objects.create(name='DayType', parent=scheduleDetail, dictionary='[설명] DayType')
scheduleCategory = Node.objects.create(name='ScheduleCategory', parent=scheduleDetail, dictionary='[설명] ScheduleCategory')
dayStartTime = Node.objects.create(name='DayStartTime', parent=scheduleDetail, dictionary='[설명] DayStartTime')
dayEndTime = Node.objects.create(name='DayEndTime', parent=scheduleDetail, dictionary='[설명] DayEndTime')
partialOperationPercentage = Node.objects.create(name='PartialOperationPercentage', parent=scheduleDetail, dictionary='[설명] PartialOperationPercentage')
linkedBuildingId = Node.objects.create(name='LinkedBuildingID', parent=building, dictionary='[설명] LinkedBuildingID')
linkedSectionId = Node.objects.create(name='LinkedSectionID', parent=section, dictionary='[설명] LinkedSectionID')

story = Node.objects.create(name='Story', parent=linkedBuildingId, dictionary='[설명] Story')
Data 생성 끝 """ # 41개