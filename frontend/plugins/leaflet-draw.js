import L from "leaflet";

import "leaflet-draw";
import "leaflet-draw/dist/leaflet.draw.css";

L.drawLocal.draw.toolbar.buttons.polyline = "Dibujar una línea";
L.drawLocal.draw.toolbar.buttons.polygon = "Dibujar un polígono";
L.drawLocal.draw.toolbar.buttons.rectangle = "Dibujar un rectángulo";
L.drawLocal.draw.toolbar.buttons.circle = "Dibujar un círculo";
L.drawLocal.draw.toolbar.buttons.marker = "Dibujar un marcador";
L.drawLocal.draw.toolbar.buttons.circlemarker = "Dibujar un marcador circular";
L.drawLocal.draw.toolbar.actions.title = "Cancelar dibujo";
L.drawLocal.draw.toolbar.actions.text = "Cancelar";
L.drawLocal.draw.toolbar.undo.title = "Eliminar el último punto dibujado";
L.drawLocal.draw.toolbar.undo.text = "Eliminar el último punto";
L.drawLocal.draw.handlers.polyline.tooltip.start =
  "Haga clic para comenzar a dibujar la línea";
L.drawLocal.draw.handlers.polyline.tooltip.cont =
  "Haga clic para continuar dibujando la línea";
L.drawLocal.draw.handlers.polyline.tooltip.end =
  "Haga clic en el primer punto para cerrar esta línea";
L.drawLocal.draw.handlers.polygon.tooltip.start =
  "Haga clic para comenzar a dibujar el polígono";
L.drawLocal.draw.handlers.polygon.tooltip.cont =
  "Haga clic para continuar dibujando el polígono";
L.drawLocal.draw.handlers.polygon.tooltip.end =
  "Haga clic en el primer punto para cerrar este polígono";
L.drawLocal.draw.handlers.rectangle.tooltip.start =
  "Haga clic y arrastre para dibujar el rectángulo";
L.drawLocal.draw.handlers.circle.tooltip.start =
  "Haga clic y arrastre para dibujar el círculo";
L.drawLocal.draw.handlers.marker.tooltip.start =
  "Haga clic en el mapa para colocar el marcador";
L.drawLocal.draw.handlers.circlemarker.tooltip.start =
  "Haga clic en el mapa para colocar el marcador circular";
L.drawLocal.edit.toolbar.buttons.edit = "Editar dibujos";
L.drawLocal.edit.toolbar.buttons.editDisabled = "No hay dibujos para editar";
L.drawLocal.edit.toolbar.buttons.remove = "Eliminar dibujos";
L.drawLocal.edit.toolbar.buttons.removeDisabled =
  "No hay dibujos para eliminar";
L.drawLocal.edit.toolbar.actions.save.title = "Guardar cambios";
L.drawLocal.edit.toolbar.actions.save.text = "Guardar";
L.drawLocal.edit.toolbar.actions.cancel.title =
  "Cancelar edición, descartar todos los cambios";
L.drawLocal.edit.toolbar.actions.cancel.text = "Cancelar";
L.drawLocal.edit.handlers.edit.tooltip.text =
  "Arrastre los puntos de control o la forma para editar la forma";
L.drawLocal.edit.handlers.edit.tooltip.subtext =
  "Haga clic en cancelar para deshacer los cambios";
L.drawLocal.edit.handlers.remove.tooltip.text =
  "Haga clic en una forma para eliminarla";
L.drawLocal.edit.handlers.remove.tooltip.subtext =
  "Haga clic en cancelar para deshacer los cambios";
L.drawLocal.draw.handlers.simpleshape.tooltip.end =
  "Suelte el mouse para terminar de dibujar";
