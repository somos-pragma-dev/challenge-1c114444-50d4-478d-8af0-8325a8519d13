# Desarrollo de una aplicación web con funcionalidades de administración

Debes desarrollar una aplicación web que incluya un panel de administración. La aplicación permitirá a los usuarios registrarse, iniciar sesión y gestionar sus perfiles. El panel de administración permitirá a los administradores crear, leer, actualizar y eliminar usuarios. La aplicación debe manejar correctamente los errores de validación y proporcionar retroalimentación adecuada al usuario.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | aplicación web con panel de administración |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 10 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Configuración del proyecto y autenticación de usuarios

**Objetivo:** Configurar el proyecto Django y habilitar la autenticación de usuarios.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Crear un nuevo proyecto Django.
- Configurar las vistas y plantillas para el registro y login de usuarios.
- Implementar la validación de datos de registro y login.

**Entregable:** Proyecto Django con funcionalidades de registro y login de usuarios.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo manejar los errores de validación y proporcionar retroalimentación al usuario.
- Piensa en la estructura de las URLs y cómo organizar las vistas y plantillas.

</details>

### Fase 2: Gestión de perfiles de usuario

**Objetivo:** Permitir a los usuarios gestionar sus perfiles.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Crear una vista y plantilla para que los usuarios puedan ver y editar sus perfiles.
- Implementar la validación de datos de edición de perfil.
- Asegurar que los cambios se guarden correctamente en la base de datos.

**Entregable:** Vista y plantilla para la gestión de perfiles de usuario.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo mostrar los errores de validación en la plantilla de edición de perfil.
- Piensa en la estructura de la URL para la gestión de perfiles.

</details>

### Fase 3: Panel de administración para gestión de usuarios

**Objetivo:** Crear un panel de administración para que los administradores puedan gestionar usuarios.

**Tiempo estimado:** 4 horas

**Instrucciones:**

- Crear un panel de administración con vistas y plantillas para crear, leer, actualizar y eliminar usuarios.
- Implementar la validación de datos para las operaciones de administración.
- Asegurar que los cambios se reflejen correctamente en la base de datos.

**Entregable:** Panel de administración con funcionalidades CRUD para usuarios.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo manejar los permisos de acceso al panel de administración.
- Piensa en la estructura de las URLs y cómo organizar las vistas y plantillas del panel de administración.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una aplicación web con panel de administración y cuáles son sus componentes principales?
- **paraQueSirve**: ¿Para qué sirve un panel de administración en una aplicación web y cuáles son sus funcionalidades principales?
- **comoSeUsa**: ¿Cómo se usa un panel de administración para gestionar usuarios en una aplicación web?
- **erroresComunes**: ¿Cuáles son los errores comunes que pueden ocurrir al desarrollar una aplicación web con panel de administración y cómo se pueden evitar?

## Criterios de Evaluacion

- Configuración correcta del proyecto Django.
- Implementación de la autenticación de usuarios con registro y login.
- Gestión de perfiles de usuario con validación de datos.
- Creación de un panel de administración con funcionalidades CRUD para usuarios.

## Como trabajar con un asistente de IA

- **AGENTS.md** — instrucciones nativas del repo (Cursor, Codex, Copilot, Gemini, Claude Code). Abrí el proyecto y el agente las carga solo.
- **PROMPT_MEJORA.md** — el mismo prompt, para copiar y pegar en un chat (claude.ai, ChatGPT, etc.).

---

*Reto generado automaticamente por Challenge Generator - Pragma*
