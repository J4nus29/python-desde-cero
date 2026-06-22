# Git - Guía Rápida 🚀

## Verificar versión de Git

```bash
git --version
```

## Inicializar Git en un proyecto

```bash
git init
```

## Ver estado del repositorio

```bash
git status
```

## Agregar todos los archivos

```bash
git add .
```

## Crear un commit

```bash
git commit -m "Mensaje del commit"
```

Ejemplos:

```bash
git commit -m "Tema 01 completado - Variables"
git commit -m "Tema 02 completado - Strings"
git commit -m "Tema 03 completado - Operadores"
```

## Ver historial de commits

```bash
git log --oneline
```

## Ver repositorios remotos

```bash
git remote -v
```

## Conectar repositorio local con GitHub (solo una vez)

```bash
git remote add origin URL_DEL_REPOSITORIO
```

Ejemplo:

```bash
git remote add origin https://github.com/J4nus29/python-desde-cero.git
```

## Cambiar nombre de rama principal

```bash
git branch -M main
```

## Subir por primera vez a GitHub

```bash
git push -u origin main
```

## Flujo de trabajo diario

```bash
git status
git add .
git commit -m "Descripción de cambios"
git push
```

Ejemplo:

```bash
git add .
git commit -m "Tema 03 completado - Operadores"
git push
```

## Ver ramas

```bash
git branch
```

## Restaurar un archivo

```bash
git restore nombre_archivo.py
```
