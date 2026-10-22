
import importlib.util, os
p=os.path.join(os.path.dirname(__file__),"main.py")
spec=importlib.util.spec_from_file_location("main",p)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
tests=[
("Nombre vacío",("", "ABC123", "equipo", "No enciende", "alta"), False),
("Tipo inválido",("Elvis Quispe", "ABC123", "impresora", "No funciona", "media"), False),
("Datos correctos",("Elvis Quispe", "ABC123", "equipo", "No enciende", "alta"), True),
("Código con formato incorrecto",("Elvis", "12", "software", "Error al abrir", "baja"), False),
("Descripción vacía",("Elvis", "ABC123", "software", "", "baja"), False),
("Prioridad inválida",("Elvis", "ABC123", "conectividad", "Sin internet", "urgente"), False),
]
for name, args, expected_valid in tests:
    errors=m.validar_solicitud(*args)
    got_valid=(len(errors)==0)
    print(f"{name}: {'APROBADA' if got_valid==expected_valid else 'FALLIDA'}")
    if errors: print("  Mensaje(s): "+" | ".join(errors))
