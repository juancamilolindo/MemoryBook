# Configuración Inicial del Proyecto Frontend

Este documento es una bitácora de los pasos realizados para configurar el proyecto de frontend desde cero. La idea es que esta guía pueda ser seguida para reconstruir la configuración del proyecto si fuera necesario.

## 1. Creación del Proyecto con Vite

Se utilizó [Vite](https://vitejs.dev/) para generar el esqueleto de la aplicación de React. Vite es un entorno de desarrollo moderno que ofrece un arranque en frío extremadamente rápido y una excelente experiencia de desarrollo.

**Comando a Ejecutar:**
Ejecuta el siguiente comando desde la raíz del repositorio (`/MemoryBook`).

```bash
# Este comando crea el proyecto de React directamente en la carpeta /frontend.
# La plantilla "react" crea un proyecto estándar de React con JavaScript.
npm create vite@latest frontend -- --template react
```

## 2. Instalación de Dependencias

Una vez creado el proyecto, el siguiente paso es instalar las dependencias de Node.js.

**Comandos a Ejecutar:**
Navega a la carpeta del frontend y ejecuta `npm install`.

```bash
cd frontend
npm install
```

## 3. Configuración de Firebase

El frontend se desplegará usando [Firebase Hosting](https://firebase.google.com/docs/hosting).

### 3.1. Prerrequisitos

*   **Tener una cuenta de Firebase:** [Crea una cuenta](https://firebase.google.com/) si no tienes una.
*   **Crear un proyecto en Firebase:** Ve a la [consola de Firebase](https://console.firebase.google.com/) y crea un nuevo proyecto (ej. `memorybook-app`).
*   **Instalar Firebase CLI:** Necesitas las herramientas de línea de comandos de Firebase. Si no las tienes, instálalas globalmente.

    ```bash
    npm install -g firebase-tools
    ```

### 3.2. Inicializar Firebase en el Proyecto

Una vez que tengas la CLI, inicia sesión y luego inicializa Firebase dentro de la carpeta `frontend`.

```bash
# Inicia sesión en tu cuenta de Google/Firebase
firebase login

# Inicia el proceso de configuración dentro de la carpeta /frontend
cd frontend
firebase init
```

Durante el proceso de `firebase init`, responde a las preguntas de la siguiente manera:

1.  **Which Firebase features do you want to set up?** -> Selecciona `Hosting: Set up deployments for static web apps`.
2.  **Please select an option:** -> `Use an existing project`.
3.  **Select a default Firebase project for this directory:** -> Elige el proyecto que creaste en la consola (ej. `memorybook-app`).
4.  **What do you want to use as your public directory?** -> Escribe `dist`. (Vite construye los archivos de producción en una carpeta llamada `dist`).
5.  **Configure as a single-page app (rewrite all urls to /index.html)?** -> `Yes`.
6.  **Set up automatic builds and deploys with GitHub?** -> `No`. (Configuraremos esto manualmente con Cloud Build más adelante).

Al finalizar, se crearán los archivos `firebase.json` y `.firebaserc` en tu carpeta `frontend`.

## 4. Despliegue Manual

Para probar que todo funciona, puedes hacer un despliegue manual desde la carpeta `frontend`.

```bash
# 1. Construye la aplicación de React. Esto crea la carpeta `dist`.
npm run build

# 2. Despliega en Firebase Hosting.
firebase deploy --only hosting
```
Después de unos segundos, la CLI te dará la URL donde tu aplicación está visible.

## 5. Siguientes Pasos

*   Configurar un pipeline de CI/CD en `cloudbuild-frontend-production.yaml`.
*   Desarrollar los componentes de la aplicación.