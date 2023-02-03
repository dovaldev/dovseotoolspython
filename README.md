# dovseotoolspython
Un proyecto para ayudarte con el contenido scrapeado si eres SEO.

## Instalar librerias
pip install es_core_news_sm

<p><b>Para instalar el archivo de requerimientos puedes hacer lo siguiente:</b></p>
Si tienes el archivo <b>"requirements.txt"</b> puedes instalar todas las librerías en PyCharm escribiendo en la terminal el siguiente comando:
```
pip install -r requirements.txt
```

## Como funciona el script
Aquí puedes encontrar el funcionamiento del script
### 1. Quitar líneas en blanco y duplicadas
Con esta función eliminas las líneas en blanco y los valores duplicados entre las dos listas.

### Quitar líneas en blanco, duplicadas y eliminar similitudes
Con esta función eliminas las líneas en blanco, los valores duplicados entre las dos listas y también elimina los strings que se parecen..

### Obtener los elementos que no se repiten
Con esta función obtienes las líneas de las dos listas y guarda solo aquellos que no sean duplicados ni similares.
<p><b>Puedes elegir un valor entre (1, 0.5, 0.4, 0):</b></p>
<li>(1) que es completamente igual.</li>
<li>(2) que es completamente desigual.</li>