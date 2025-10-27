# 🎭 Proyecto CultuVivo  
**Sistema de Gestión de Eventos Culturales**

---

## 🧩 Descripción General  
**CultuVivo** es una aplicación desarrollada en Python que permite gestionar la programación cultural de una institución o entidad. El sistema está orientado a la administración de **eventos, artistas y asistentes**, bajo un modelo de roles (Administrador, Artista y Asistente).

El proyecto fue desarrollado siguiendo la **metodología ágil Scrum**, durante un sprint de 5 días, con el objetivo de construir un **MVP (Producto Mínimo Viable)** funcional que cumpla con las principales historias de usuario priorizadas.

---

## 👥 Equipo de Desarrollo  

| Rol | Integrante |
|-----|-------------|
| **Scrum Master** | Luis Hernán González Ordoñez |
| **Product Owner** | Carlos Rueda |
| **Desarrolladores** | Brayan Espinosa Osorio, Shirly Katherinn Leal Nieves, Andrés Santiago Gómez Rojas |

---

## 🗂️ Estructura del Proyecto  

```
Proyecto_CultuVivo/
│
├── main.py                  # Archivo principal - menú e integración de módulos
├── eventos.py               # CRUD para la gestión de eventos
├── artistas.py              # CRUD para la gestión de artistas
├── asistentes.py            # Registro y cancelación de asistentes
├── asignaciones.py          # Asignación de artistas a eventos
├── persistencia.py          # Manejo de archivos JSON (lectura/escritura)
├── utilidades.py            # Funciones auxiliares y validaciones
├── data/
│   ├── eventos.json         # Base de datos de eventos
│   ├── artistas.json        # Base de datos de artistas
│   ├── asistentes.json      # Base de datos de registros de asistencia
│
└── README.md                # Documento de descripción del proyecto
```

---

## ⚙️ Funcionalidades Principales  

| **Historia de Usuario** | **Descripción** | **Estado** |
|--------------------------|-----------------|-------------|
| **HU-01** | Crear, editar y eliminar eventos con nombre, fecha, hora, lugar, capacidad máxima y descripción. | ✅ Completada |
| **HU-02** | Asignar artistas a eventos, indicando tipo de presentación y duración. | ✅ Completada |
| **HU-04** | Ver lista de eventos disponibles y su estado (cupos disponibles / completo). | ✅ Completada |
| **HU-05** | Registrar asistentes a eventos y controlar capacidad máxima. | ✅ Completada |
| **HU-08** | Registrar y administrar artistas (nombre, tipo de presentación, duración, contacto). | ✅ Completada |

---

## 🧠 Tecnologías Utilizadas  

- **Lenguaje:** Python 3.10+  
- **Persistencia de datos:** Archivos JSON  
- **Metodología:** Scrum  
- **Control de versiones:** Git / GitHub  

---

## ▶️ Instrucciones de Ejecución  

1. **Clonar o descomprimir** el repositorio:  
   ```bash
   git clone https://github.com/usuario/Proyecto_CultuVivo.git
   ```
   o simplemente extraer el archivo `.zip`.

2. **Abrir una terminal** en la carpeta del proyecto.

3. **Ejecutar el programa principal:**
   ```bash
   python main.py
   ```

4. **Interacción por consola:**
   - Selecciona tu rol (Administrador, Artista o Asistente).  
   - Usa las opciones del menú para crear eventos, registrar artistas, asignarlos o inscribir asistentes.  
   - Los datos se almacenan automáticamente en archivos JSON dentro de la carpeta `data/`.

---

## 📊 Resultados del Sprint  

| Métrica | Resultado | Interpretación |
|----------|------------|----------------|
| **Velocidad del equipo** | 1.0 (100%) | Se cumplieron todas las funcionalidades planificadas. |
| **Efectividad de la estimación** | 1.10 (110%) | El tiempo real fue ligeramente superior al estimado (10% adicional). |

