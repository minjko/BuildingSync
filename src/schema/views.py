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

    # // 자식이 있고 열린 상태의 노드 -> 검은색 세모
    
    # // 자식이 있고 닫힌 상태의 노드 -> 하얀색 세모

    # // 자식이 없고 열린 상태의 노드 -> 세모 없음


def node_tree_view(request):
  
  # a = Node.objects.exclude(dictionary__isnull=True)
  # print(a)
  return render(request, 'schema/node_tree.html')


""" Data 생성 
root = Node.objects.create(name='BuildingSync')

programs = Node.objects.create(name='Programs', parent=root)
facilities = Node.objects.create(name='Facilities', parent=root)

program = Node.objects.create(name='Program', parent=programs)
facility = Node.objects.create(name='Facilitiy', parent=facilities)

programData = Node.objects.create(name='ProgramData' , parent=program, dictionary='[설명] ProgramData')
programFundingSource = Node.objects.create(name='ProgramFundingSource' , parent=program, dictionary='[설명] Program Funding Source')
programClassification = Node.objects.create(name='ProgramClassification' , parent=program, dictionary='[설명] ProgramClassification')
sites = Node.objects.create(name='Sites' , parent=facility)
#systems = Node.objects.create(name='Systems' , parent=facility)
auditCycles = Node.objects.create(name='AuditCycles' , parent=facility)
schedules = Node.objects.create(name='Schedules' , parent=facility)
mesures = Node.objects.create(name='Mesures' , parent=facility)
reports = Node.objects.create(name='Reports' , parent=facility)
contacts = Node.objects.create(name='Contacts' , parent=facility)
tenants = Node.objects.create(name='Tenants' , parent=facility)
userDefinedFields = Node.objects.create(name='UserDefinedFields' , parent=facility)

site = Node.objects.create(name='Site', parent=sites, dictionary='[설명] Site')
#system = Node.objects.create(name='System' , parent=systems)
auditCycle = Node.objects.create(name='AuditCycle' , parent=auditCycles, dictionary='[설명] AuditCycle')
schedule = Node.objects.create(name='Schedule' , parent=schedules)
mesure = Node.objects.create(name='Mesure' , parent=mesures, dictionary='[설명] Mesure')
report = Node.objects.create(name='Report' , parent=reports, dictionary='[설명] Report')
contact = Node.objects.create(name='Contact' , parent=contacts, dictionary='[설명] Contact')
tenant = Node.objects.create(name='Tenant' , parent=tenants)
userDefinedField = Node.objects.create(name='UserDefinedField' , parent=userDefinedFields, dictionary='[설명] UserDefinedField')

schedulePerioBeginDate = Node.objects.create(name='SchedulePerioBeginDate', parent=schedule, dictionary='[설명] SchedulePerioBeginDate')
schedulePerioEndDate = Node.objects.create(name='SchedulePerioEndDate', parent=schedule, dictionary='[설명] SchedulePerioEndDate')
scheduleDetails = Node.objects.create(name='ScheduleDetails', parent=schedule)
linkedPremises = Node.objects.create(name='LinkedPremises', parent=schedule)
tenantName = Node.objects.create(name='TenantName', parent=tenant, dictionary='[설명] TenantName')
contactIDs = Node.objects.create(name='ContactIDs', parent=tenant, dictionary='[설명] ContactIDs')

scheduleDetail = Node.objects.create(name='ScheduleDetail', parent=scheduleDetails)
building = Node.objects.create(name='Building', parent=linkedPremises)
section = Node.objects.create(name='Section', parent=linkedPremises)

dayType = Node.objects.create(name='DayType', parent=scheduleDetail, dictionary='[설명] DayType')
scheduleCategory = Node.objects.create(name='ScheduleCategory', parent=scheduleDetail, dictionary='[설명] ScheduleCategory')
dayStartTime = Node.objects.create(name='DayStartTime', parent=scheduleDetail, dictionary='[설명] DayStartTime')
dayEndTime = Node.objects.create(name='DayEndTime', parent=scheduleDetail, dictionary='[설명] DayEndTime')
partialOperationPercentage = Node.objects.create(name='PartialOperationPercentage', parent=scheduleDetail, dictionary='[설명] PartialOperationPercentage')
linkedBuildingId = Node.objects.create(name='LinkedBuildingID', parent=building)
linkedSectionId = Node.objects.create(name='LinkedSectionID', parent=section, dictionary='[설명] LinkedSectionID')

story = Node.objects.create(name='Story', parent=linkedBuildingId, dictionary='[설명] Story')
Data 생성 끝 """ # 41개