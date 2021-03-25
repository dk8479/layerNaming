from krita import DockWidgetFactory, DockWidgetFactoryBase

from .docker_template1 import layerMeimei

DOCKER_ID = 'template_docker1'
instance = Krita.instance()
dock_widget_factory = DockWidgetFactory(DOCKER_ID,
                                        DockWidgetFactoryBase.DockRight,
                                        layerMeimei)

instance.addDockWidgetFactory(dock_widget_factory)
