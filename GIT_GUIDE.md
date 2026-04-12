# Guía de Git y GitHub - Alke Wallet

## Estructura de Ramas

El proyecto utiliza la estrategia Git Flow con las siguientes ramas:

### 1. **main**
- Código estable y listo para producción
- Solo recibe merge de release branches
- Cada commit en main debe tener un tag de versión

### 2. **feature/modelos**
- Desarrollo de modelos de base de datos
- Contiene definición de Cliente, Cuenta, Transacción, etc.
- Se actualiza desde esta rama cuando se hacen cambios en models.py

### 3. **feature/crud**
- Implementación de vistas CRUD
- Contiene views.py, urls.py, templates
- Se actualiza cuando se agregan nuevas operaciones

## Configuración de Git Local

```bash
# Configurar usuario global (una sola vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@example.com"

# Configurar usuario para este proyecto solamente
git config user.name "Tu Nombre"
git config user.email "tu.email@example.com"

# Verificar configuración
git config --list
```

## Workflow de Desarrollo

### 1. Crear una Nueva Rama (Feature Branch)

```bash
# Actualizar main
git checkout main
git pull origin main

# Crear rama de feature basada en main
git checkout -b feature/nombre-funcionalidad
```

### 2. Realizar Cambios

```bash
# Ver estado de cambios
git status

# Ver diferencias
git diff

# Agregar cambios al staging area
git add archivo.py
git add .  # Agregar todos los cambios

# Hacer commit
git commit -m "Descripción clara de los cambios"

# Push a repositorio remoto
git push origin feature/nombre-funcionalidad
```

### 3. Sintaxis de Mensajes de Commit

Utilizar formato descriptivo:

```
[TIPO] Descripción breve (máximo 50 caracteres)

Descripción más detallada si es necesario (máximo 72 caracteres por línea)
- Punto 1
- Punto 2
```

**Tipos de commits:**
- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `style:` Cambios en formato (sin lógica)
- `refactor:` Refactorización de código
- `perf:` Mejoras de rendimiento
- `test:` Agregar o actualizar tests
- `chore:` Cambios en build, dependencias, etc.

**Ejemplos:**
```
feat: Agregar modelo de transacciones
fix: Corregir validación de email en Cliente
docs: Actualizar README con instrucciones de instalación
refactor: Simplificar lógica de CRUD de cuentas
```

### 4. Actualizar Rama Antes de Merge

```bash
# Traer cambios remotos
git fetch origin

# Rebasear en main (opcional pero recomendado)
git rebase origin/main

# O hacer merge si prefieres
git merge origin/main
```

### 5. Crear Pull Request (en GitHub)

1. Push a tu rama feature
2. Ir a GitHub
3. Crear Pull Request
4. Escribir descripción clara
5. Esperar revisión
6. Hacer merge a main

### 6. Sincronizar Local con Remoto

```bash
# Traer todos los cambios remotos
git fetch --all

# Actualizar rama actual con remoto
git pull origin nombre-rama

# Forzar actualización (cuidado: pierde cambios locales)
git pull origin nombre-rama --force
```

## Comandos Útiles

### Ver historial

```bash
# Ver log simple
git log

# Ver log en una línea
git log --oneline

# Ver log con gráfico de ramas
git log --graph --oneline --all

# Ver commits de un autor
git log --author="Nombre Autor"

# Ver commits del último día
git log --since="1 day ago"
```

### Trabaja con cambios

```bash
# Ver cambios no comiteados
git diff

# Ver cambios en staging
git diff --cached

# Ver cambios entre ramas
git diff main feature/modelos

# Descartar cambios locales
git checkout -- archivo.py

# Descartar todos los cambios
git reset --hard
```

### Trabajo con ramas

```bash
# Listar ramas locales
git branch

# Listar ramas remotas
git branch -r

# Listar todas las ramas
git branch -a

# Cambiar de rama
git checkout nombre-rama

# Crear y cambiar a rama
git checkout -b nombre-rama

# Eliminar rama local
git branch -d nombre-rama

# Deletear rama remota
git push origin --delete nombre-rama

# Ver rama actual
git rev-parse --abbrev-ref HEAD
```

## Flujo de Trabajo Completo

### Escenario: Agregar nueva funcionalidad

```bash
# 1. Actualizar main local
git checkout main
git pull origin main

# 2. Crear rama feature
git checkout -b feature/nueva-funcionalidad

# 3. Hacer cambios
# ... editar archivos ...

# 4. Ver estado
git status

# 5. Agregar cambios
git add .

# 6. Hacer commit(s)
git commit -m "feat: Describir cambios"

# 7. Push a repositorio
git push origin feature/nueva-funcionalidad

# 8. (En GitHub) Crear Pull Request
# 9. (Después de aprobación) Mergear a main
# 10. (Local) Limpiar rama local
git checkout main
git pull origin main
git branch -d feature/nueva-funcionalidad
```

### Escenario: Correcciones en production (hotfix)

```bash
# 1. Crear rama de hotfix basada en main
git checkout main
git pull origin main
git checkout -b hotfix/nombre-del-bug

# 2. Hacer correcciones
# ... editar archivos ...

# 3. Hacer commit
git add .
git commit -m "fix: Describir corrección"

# 4. Push y crear PR
git push origin hotfix/nombre-del-bug

# 5. Mergear a main
# 6. (Recomendado) Mergear también a develop si existe
```

## Resolución de Conflictos

Cuando hay conflictos durante un merge:

```bash
# 1. Ver archivos en conflicto
git status

# 2. Editar archivos manualmente
# Los conflictos se ven así:
# <<<<<<< HEAD
# código actual
# =======
# código entrante
# >>>>>>> rama-conflictiva

# 3. Resolver manualmente y guardar

# 4. Marcar como resuelto
git add archivo-resuelto.py

# 5. Completar el merge
git commit -m "Merge: Resolver conflictos en archivo.py"

# 6. Push
git push origin nombre-rama
```

## Mejores Prácticas

✅ **Hacer:**
- Hacer commits pequeños y enfocados
- Escribir mensajes descriptivos
- Actualizar antes de hacer push
- Crear ramas para cada funcionalidad
- Usar .gitignore adecuadamente
- Revisar cambios antes de commit
- Documentar cambios significativos

❌ **No hacer:**
- Commits directos a main (usar branches)
- Mensajes de commit genéricos ("actualizar", "cambios")
- Push fuerza sin necesidad (--force)
- Ignorar conflictos de merge
- Commits con código incompleto
- Ramas con tiempo de vida muy largo sin mergear

## Configuración de .gitignore

El proyecto incluye un .gitignore que excluye:
- `__pycache__/` - Archivos compilados de Python
- `*.pyc` - Archivos compilados
- `db.sqlite3` - Base de datos local
- `.env` - Variables de entorno
- `venv/` - Entorno virtual
- `.vscode/` - Configuración de IDE
- `staticfiles/` - Archivos estáticos compilados

**Para actualizar .gitignore:**
```bash
# Remover archivos ya tracked
git rm --cached archivo.txt --cached -r directorio/

# Aplicar nuevo .gitignore
git add .gitignore
git commit -m "Update .gitignore"
```

## Comandos de Emergencia

```bash
# Deshacer último commit (mantener cambios)
git reset --soft HEAD~1

# Deshacer último commit (perder cambios)
git reset --hard HEAD~1

# Deshacer múltiples commits
git reset --hard HEAD~3

# Restaurar rama a estado remoto
git fetch origin
git reset --hard origin/main

# Ver qué fue eliminado
git reflog

# Recuperar rama eliminada
git checkout -b recuperada @ {numero}
```

## Integración con GitHub

### Crear repositorio en GitHub

1. Ir a github.com/new
2. Nombrar repositorio
3. No inicializar con README (ya tenemos uno)
4. Crear repositorio

### Conectar repositorio local a GitHub

```bash
# Agregar remoto
git remote add origin https://github.com/tu-usuario/alke-wallet.git

# Verificar remoto
git remote -v

# Push a GitHub
git branch -M main  # Renombrar branch a main si es necesario
git push -u origin main

# Push de todas las ramas
git push -u origin feature/modelos
git push -u origin feature/crud
```

### Push regular

```bash
# Después del primer push con -u
git push
git push origin nombre-rama
```

## Protección de Ramas en GitHub

En configuración del repositorio:

1. Settings > Branches
2. Crear reglas para main:
   - Requerir pull request reviews
   - Requerir status checks
   - Requiere que rama esté actualizada
3. Hacer push al repositorio requiere PR

## Colaboración en Equipo

```bash
# Traer cambios de compañero
git fetch origin
git pull origin main

# Ver quién cambió cada línea
git blame archivo.py

# Ver historial de un archivo
git log -p archivo.py

# Ver cambios después de un commit
git show commit-hash
```

## Recursos Adicionales

- [Documentación oficial de Git](https://git-scm.com/doc)
- [GitHub Learning Lab](https://lab.github.com/)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)
- [Git Cheat Sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)

---

**Última actualización:** Abril 2026
