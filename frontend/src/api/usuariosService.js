// src/api/usuariosService.js

import authApi from "./authApi";

/**
 * Gets a list of all users.
 * @returns {Promise<Array>} A promise that resolves to an array of user objects.
 */
export async function getUsuarios() {
  try {
    const response = await authApi.get("/usuarios/");
    return response.data;
  } catch (error) {
    console.error("Error fetching users:", error);
    throw error;
  }
}

/**
 * Gets a single user by their email address.
 * @param {string} email - The email of the user to retrieve.
 * @returns {Promise<object>} A promise that resolves to the user object.
 */
export async function getUsuarioByEmail(email) {
  try {
    const response = await authApi.get(`/usuarios/by_email/${email}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching user by email ${email}:`, error);
    throw error;
  }
}

/**
 * Creates a new user.
 * @param {object} userData - The data for the new user.
 * @returns {Promise<object>} A promise that resolves to the created user object.
 */
export async function createUsuario(userData) {
  try {
    const response = await authApi.post("/usuarios/", userData);
    return response.data;
  } catch (error) {
    console.error("Error creating user:", error);
    throw error;
  }
}

/**
 * Gets a user by their ID.
 * @param {number} id - The ID of the user to retrieve.
 * @returns {Promise<object>} A promise that resolves to the user object.
 */
export async function getUsuarioById(id) {
  try {
    const response = await authApi.get(`/usuarios/${id}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching user ${id}:`, error);
    throw error;
  }
}

/**
 * Updates an existing user.
 * @param {number} id - The ID of the user to update.
 * @param {object} userUpdateData - The new data for the user.
 * @returns {Promise<object>} A promise that resolves to the updated user object.
 */
export async function updateUsuario(id, userUpdateData) {
  try {
    const response = await authApi.put(`/usuarios/${id}`, userUpdateData);
    return response.data;
  } catch (error) {
    console.error(`Error updating user ${id}:`, error);
    throw error;
  }
}

/**
 * Gets a list of users for a specific station.
 * @param {number} stationId - The ID of the station.
 * @returns {Promise<Array>} A promise that resolves to an array of user objects.
 */
export async function getUsuariosByEstacion(stationId) {
  try {
    const response = await authApi.get(`/usuarios/by_estacion/${stationId}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching users for station ${stationId}:`, error);
    throw error;
  }
}
