# No se importa directamente desde los otros módulos aquí.
def navegar_a_ventana_principal(rol, usuario):
    from src.ventana_principal import crear_ventana_principal
    return crear_ventana_principal(rol, usuario)


def navegar_a_iniciar_sesion():
    from src.iniciar_sesion import crear_ventana_iniciar_sesion
    return crear_ventana_iniciar_sesion()
