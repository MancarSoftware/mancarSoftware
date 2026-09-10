# Mancar Software — GitHub profile kit

El perfil final está en [profile/README.md](profile/README.md). El contenido está en inglés, siguiendo el brief. Los SVG son archivos editables, sin scripts, fuentes remotas ni servicios externos.

## Estructura

```text
README.md                     Instrucciones de instalación
profile/
├── README.md                 Perfil público
└── assets/
    ├── mancar-header.svg     Monograma y cabecera animados
    └── mancar-divider.svg    Separador animado
```

## Instalar en una organización

1. Usa un repositorio público llamado `.github` dentro de la organización.
2. Copia la carpeta `profile/` completa a la raíz de ese repositorio.
3. Conserva los SVG en `profile/assets/`. Las imágenes del README usan rutas relativas a esa carpeta.
4. Completa los datos pendientes y publica los archivos en la rama predeterminada.
5. Revisa el perfil público de la organización para confirmar imágenes y enlaces.

GitHub requiere `profile/README.md` dentro del repositorio `.github` para el perfil público de una organización: [documentación oficial](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile#adding-a-public-organization-profile-readme).

## Instalar en un perfil personal

En el repositorio público que tenga exactamente el nombre del usuario, copia **el contenido de `profile/`** a la raíz: `README.md` y `assets/` juntos. No copies este archivo de instrucciones como perfil. Las rutas de imágenes se mantienen sin cambios.

## Completar antes de publicar

- Reemplaza cada `TODO_*` por información verificada. Convierte las URLs en enlaces Markdown descriptivos y el correo en un enlace `mailto:`.
- Confirma cuáles de OdontoCare, VetCare Pro y GymCare deben aparecer. Cada entrada necesita una descripción real, tecnologías verificadas y un enlace público autorizado. Elimina las entradas que no correspondan.
- Confirma el ecosistema tecnológico propuesto. Retira la nota de pendiente únicamente después de validarlo.
- Elimina los canales de contacto que no quieras mostrar y los avisos de pendiente cuando estén resueltos.
- Para añadir un proyecto, duplica una entrada y actualiza número, nombre, descripción y enlace.

No hay contactos, resultados comerciales, stacks de proyectos ni enlaces de repositorio inventados.

## Decisiones visuales y accesibilidad

Grafito, blanco y verde apagado; monograma M estructural; tipografía del sistema; texto alineado a la izquierda. La cabecera mantiene su propio fondo oscuro y el texto Markdown se adapta al tema de GitHub. El titular y toda la información esencial son texto real fuera de las imágenes.

Hay dos detalles animados: el trazo del monograma y el pequeño acento del separador. Ambos incluyen `prefers-reduced-motion`, usan ciclos lentos y siguen siendo legibles cuando el visor no reproduce animaciones. El SVG contiene estilos internos para la animación; el README no depende de CSS externo, JavaScript ni HTML interactivo.

## Verificación final

- Comprueba el README renderizado en GitHub y en la portada de la organización, con temas claro y oscuro.
- Revisa a 375 px de ancho y en escritorio: titular legible, imágenes dentro del contenedor y contenido en una sola columna.
- Activa la preferencia del sistema para reducir movimiento y confirma que las animaciones se detienen en los clientes que la soportan.
- Comprueba cada enlace y busca `TODO_` antes de publicar.
- La reproducción de SVG puede variar según el cliente, especialmente en aplicaciones móviles. El contenido no depende de ella.

Los archivos están preparados para instalación; la revisión en GitHub publicado requiere subirlos al repositorio correspondiente. Este kit no publica ni modifica repositorios remotos.
