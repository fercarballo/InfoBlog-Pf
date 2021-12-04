# Log de Cambios

En este archivo se definen en profundidad los cambios realizados en cada commit.

Al marcar los cambios, se utiliza la fecha del cambio y se sigue el estándar de [Versionado Semántico 2.0.0].  
(Solo se usa el concepto MAYOR.MENOR.PARCHE para no complicarse la vida)

Este sistema funciona de la siguiente manera:

- La versión **MAYOR** cuando realizas un cambio incompatible con el resto del proyecto. (Ejemplo: Se cambia o agrega un modelo)
- La versión **MENOR** cuando añades funcionalidad que es compatible con versiones anteriores. (Ejemplo: Se modifica un .html o .css)
- La versión **PARCHE** cuando reparas errores compatibles con versiones anteriores. (Ejemplo: Se soluciona un bug/error pequeño)

---

## Vesión (0.1.0) (04/11/21)

### Cambios

### app/post/models.py

- Añadida función `user_directory_path`: Devuelve un string con la dirección donde se debe guardar la imagen de cada post.
- Cambio de atributo `img`; de `URLField` a `ImageField`.

### app/categoria/models.py

- Pequeños cambios estéticos en la estructura del código.

### app/comentario/models.py

- Pequeños cambios estéticos en la estructura del código.

### BlogIngoBase/

- Movida carpeta `static` a `BlogInfoBase/`

### BlogInfoBase/settings/base.py

- Eliminado código redundante en línea 132.
- Eliminada coma final en línea 134 debido a una incompatibilidad en el sistema de imágenes.

### BlogInfoBase/templates/base/base.html

- Solucionado error en línea 25; eliminado un Enter de sobra

### BlogInfoBase/templates/base/index.html

- Cambiada `src` de tag `img` en línea 12 a `{{post.img.url}}`

[//]: #
[Versionado Semántico 2.0.0]: <https://semver.org/lang/es/>
