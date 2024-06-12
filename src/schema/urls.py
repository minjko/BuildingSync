from django.urls import path

from .views import NodeView
from .views import node_tree_view


urlpatterns = [
  
  # api
  path("api/nodes/", NodeView.as_view(), name="node-api"),
  
  # view
  path("nodes/", node_tree_view, name="node-tree-view")

]