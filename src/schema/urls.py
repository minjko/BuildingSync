from django.urls import path

from schema.views import node_tree_view, NodeView 


urlpatterns = [
  
  # api
  path("api/nodes/", NodeView.as_view(), name="node-api"),
  # tree
  path("nodes/", node_tree_view, name="node-tree-view")

]