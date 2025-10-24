# Frontend de MemoryBook

Esta carpeta contiene la aplicación de React para MemoryBook, creada con Vite.

## Cómo empezar (Entorno de Desarrollo)

Sigue estos pasos para configurar y ejecutar el proyecto de frontend en tu máquina local.

### Prerrequisitos

Asegúrate de tener instalados los siguientes programas en tu sistema:

*   [Node.js](https://nodejs.org/) (versión 20 o superior), que incluye `npm`.

### 1. Instalar Dependencias

Si es la primera vez que trabajas en el frontend, necesitas instalar sus dependencias.

```bash
# Navega a la carpeta del frontend
cd frontend

# Instala todas las dependencias listadas en package.json
npm install
```

### 2. Ejecutar el Servidor de Desarrollo

Este comando inicia un servidor local con recarga en caliente (`hot-reloading`), que es ideal para desarrollar.

```bash
# Desde la carpeta /frontend, ejecuta:
npm run dev
```
La aplicación estará disponible en la dirección que te indique la terminal (normalmente `http://localhost:5173`).

### 3. Ejecutar Linter

Para asegurar la calidad del código, puedes ejecutar el linter manualmente.

```bash
# Ejecuta ESLint para encontrar problemas en el código
npm run lint
```

### 4. Construir la Versión de Producción

Este comando empaqueta y optimiza la aplicación para producción. El resultado se genera en la carpeta `dist/`.

```bash
npm run build
```

### 5. Despliegue Manual (Opcional)

Aunque el despliegue a producción está automatizado, a veces es útil hacer un despliegue manual. Como `firebase-tools` se instala como una dependencia de desarrollo, puedes usar `npx` para ejecutar los comandos.

```bash
# 1. Si es la primera vez, inicia sesión en Firebase
# firebase login

# 2. Construye la aplicación para producción
npm run build

# 3. Despliega los cambios en Firebase Hosting
npx firebase deploy --only hosting
```