"# PFU-111-semana12-BrayanOru-aGuarachi_grupo2_" 

REGISTRO DE PRUEBAS AUTOMATIZADAS

Proyecto: Sistema de registro de solicitudes de soporte técnico

Nota: estas pruebas verifican las reglas de validación del código. Las pruebas interactivas de menú deben completarse ejecutando main.py y tomando capturas reales.

Nombre vacío: APROBADA
  Mensaje(s): El nombre no puede estar vacío.

Tipo inválido: APROBADA
  Mensaje(s): El tipo debe ser: equipo, software o conectividad.

Datos correctos: APROBADA
Código con formato incorrecto: APROBADA
  Mensaje(s): El código debe tener entre 6 y 12 caracteres alfanuméricos.

Descripción vacía: APROBADA
  Mensaje(s): La descripción no puede estar vacía.

Prioridad inválida: APROBADA
  Mensaje(s): La prioridad debe ser: baja, media o alta.

Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/spreadsheet_warmup.py", line 718, in _warm_feature_flows
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/spreadsheet_warmup.py", line 509, in _warm_drawing_and_image_flows
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/generated/interface/models.py", line 32861, in bring_to_front
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/rpc/remote.py", line 764, in __call__
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/rpc/client.py", line 175, in call
artifact_tool.rpc.client.RemoteError: Element ordering requires an owning element collection.

Pruebas manuales pendientes de evidencia:
1. Consultar antes de registrar: debe indicar que no hay solicitud.
2. Registrar datos válidos: debe mostrar confirmación y permitir consulta.
3. Limpiar: debe reiniciar la solicitud actual.
4. Elegir una opción de menú inexistente: debe mostrar mensaje de error y continuar.
5. Salir: debe finalizar correctamente.
