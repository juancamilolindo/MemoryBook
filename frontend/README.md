# Frontend de MemoryBook

Esta carpeta contiene la aplicación de React para MemoryBook, creada con Vite.

## Cómo empezar (Entorno de Desarrollo)

Sigue estos pasos para configurar y ejecutar el proyecto de frontend en tu máquina local.

### Prerrequisitos

Asegúrate de tener instalados los siguientes programas en tu sistema:

- [Node.js](https://nodejs.org/) (versión 20 o superior), que incluye `npm`.
- [Pre-commit](https://pre-commit.com/#installation) para la gestión de hooks de Git.

### 1. Instalar Dependencias y Hooks

Si es la primera vez que trabajas en el proyecto, necesitas instalar las dependencias y configurar las herramientas de calidad de código.

```bash
# 1. Navega a la carpeta del frontend
cd frontend

# 2. Instala todas las dependencias listadas en package.json
npm install

# 3. Instala los hooks de git definidos en el proyecto
# Esto ejecutará Prettier y ESLint automáticamente antes de cada commit.
pre-commit install
```

### 2. Ejecutar el Servidor de Desarrollo

Este comando inicia un servidor local con recarga en caliente (`hot-reloading`), que es ideal para desarrollar.

```bash
# Desde la carpeta /frontend, ejecuta:
npm run dev
```

La aplicación estará disponible en la dirección que te indique la terminal (normalmente `http://localhost:5173`).

### 3. Calidad y Formato de Código

El proyecto utiliza dos herramientas principales para mantener un código limpio y consistente:

- **ESLint**: Analiza el código para encontrar errores potenciales y asegurar que se sigan ciertas reglas de estilo. Su configuración está en `eslint.config.js`.
- **Prettier**: Formatea el código automáticamente para garantizar un estilo visual uniforme. Su configuración se encuentra en el archivo `.prettierrc` en la raíz del proyecto.

Ambas herramientas están configuradas para ejecutarse **automáticamente antes de cada commit** gracias a `pre-commit`.

#### Integración con el Editor (Recomendado)

Para la mejor experiencia de desarrollo, se recomienda instalar las siguientes extensiones en tu editor (por ejemplo, VS Code):

- [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
- [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

Configura tu editor para que formatee el código al guardar (`"editor.formatOnSave": true`) para que Prettier se ejecute cada vez que guardes un archivo.

#### Uso Manual

Aunque el proceso es automático, puedes ejecutar las herramientas manualmente:

```bash
# Ejecuta ESLint para encontrar problemas y corregirlos si es posible
npm run lint

# Formatea todo el código del frontend con Prettier
npx prettier --write .
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
