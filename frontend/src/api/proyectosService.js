import authApi from "./authApi";

/**
 * Fetches a single project by its ID.
 * @param {number} projectId - The ID of the project to retrieve.
 * @returns {Promise<object>} A promise that resolves to the project object.
 */
export async function getProyectoById(projectId) {
  try {
    const response = await authApi.get(`/proyectos/${projectId}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching project with ID ${projectId}:`, error);
    throw error; // Re-throw to allow component to handle
  }
}
