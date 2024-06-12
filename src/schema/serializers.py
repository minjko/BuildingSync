from rest_framework import serializers
from .models import Node


class RecursiveField(serializers.Serializer):
  
  def to_representation(self, value):
    serializer = self.parent.parent.__class__(value, context=self.context)
    return serializer.data



class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'

  
  
class NodeViewSerializer(serializers.ModelSerializer):
  
  children = RecursiveField(many=True)

  class Meta:
    model = Node
    fields = ['nodeId', 'name', 'children']
