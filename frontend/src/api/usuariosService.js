// src/api/usuariosService.js

import authApi from "./authApi";

/**
 * Gets a list of all users.
 * @returns {Promise<Array>} A promise that resolves to an array of user objects.
 */
export async function getUsuarios() {
  const response = await authApi.get("/usuarios/");
  return response.data;
}

/**
 * Gets a single user by their email address.
 * @param {string} email - The email of the user to retrieve.
 * @returns {Promise<object>} A promise that resolves to the user object.
 */
export async function getUsuarioByEmail(email) {
  const response = await authApi.get(`/usuarios/by_email/${email}`);
  return response.data;
}

/**
 * Creates a new user.
 * @param {object} userData - The data for the new user.
 * @returns {Promise<object>} A promise that resolves to the created user object.
 */
export async function createUsuario(userData) {
  const response = await authApi.post("/usuarios/", userData);
  return response.data;
}

/**
 * Gets a user by their ID.
 * @param {number} id - The ID of the user to retrieve.
 * @returns {Promise<object>} A promise that resolves to the user object.
 */
export async function getUsuarioById(id) {
  const response = await authApi.get(`/usuarios/${id}`);
  return response.data;
}

/**
 * Updates an existing user.
 * @param {number} id - The ID of the user to update.
 * @param {object} userUpdateData - The new data for the user.
 * @returns {Promise<object>} A promise that resolves to the updated user object.
 */
export async function updateUsuario(id, userUpdateData) {
  const response = await authApi.put(`/usuarios/${id}`, userUpdateData);
  return response.data;
}
