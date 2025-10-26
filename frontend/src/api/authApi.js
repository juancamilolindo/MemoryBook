import axios from "axios";
import { auth } from "../firebase/config";

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

apiClient.interceptors.request.use(
  async (config) => {
    const user = auth.currentUser;
    if (user) {
      const token = await user.getIdToken(true);
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// NUEVO: Interceptor de respuesta para manejar errores globalmente
apiClient.interceptors.response.use(
  (response) => response, // Si la respuesta es exitosa, la devuelve sin más.
  (error) => {
    // Aquí puedes manejar todos los errores de la API
    console.error(
      "Error en la llamada a la API:",
      error.response ? error.response.data : error.message
    );

    // Opcional: podrías mostrar una notificación al usuario (ej. con una librería de "toasts")
    // toast.error(error.response?.data?.message || "Ocurrió un error inesperado");

    // Es importante rechazar la promesa para que el código que hizo la llamada
    // sepa que la petición falló.
    return Promise.reject(error);
  }
);

export default apiClient;
