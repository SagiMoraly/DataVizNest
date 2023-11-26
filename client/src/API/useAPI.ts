import axios from "axios";

const apiUrl = "http://localhost:5000";

export const get_users = async (): Promise<string> => {
  try {
    const { data } = await axios.get<string>(`${apiUrl}/get_users`);
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) return Promise.reject(error.message);
    return Promise.reject(
      "An unexpected error occurred!, couldn't get the users."
    );
  }
};

export const reset_and_create_tables = async (): Promise<string> => {
  try {
    const { data } = await axios.patch<string>(
      `${apiUrl}/reset_and_create_tables`
    );
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) return Promise.reject(error.message);
    return Promise.reject(
      "An unexpected error occurred!, couldn't get the users."
    );
  }
};

export const get_sum_users = async (): Promise<string> => {
  try {
    const { data } = await axios.get<string>(`${apiUrl}/get_sum_users`);
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) return Promise.reject(error.message);
    return Promise.reject(
      "An unexpected error occurred!, couldn't get the users."
    );
  }
};

export const get_income_sources = async (): Promise<string> => {
  try {
    const { data } = await axios.get<string>(`${apiUrl}/get_income_sources`);
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) return Promise.reject(error.message);
    return Promise.reject(
      "An unexpected error occurred!, couldn't get the users."
    );
  }
};

export const get_expenses = async (): Promise<string> => {
  try {
    const { data } = await axios.get<string>(`${apiUrl}/get_expenses`);
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) return Promise.reject(error.message);
    return Promise.reject(
      "An unexpected error occurred!, couldn't get the users."
    );
  }
};

export const get_savings_goals = async (): Promise<string> => {
  try {
    const { data } = await axios.get<string>(`${apiUrl}/get_savings_goals`);
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) return Promise.reject(error.message);
    return Promise.reject(
      "An unexpected error occurred!, couldn't get the users."
    );
  }
};

export const create_fake_users = async (num: number): Promise<string> => {
  try {
    const { data } = await axios.post<string>(
      `${apiUrl}/create_fake_users/${num}`
    );
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) return Promise.reject(error.message);
    return Promise.reject(
      "An unexpected error occurred!, couldn't get the users."
    );
  }
};

export const get_users_pie_chart = async (): Promise<string> => {
  try {
    const { data } = await axios.get<string>(`${apiUrl}/get_users_pie_chart`);
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) return Promise.reject(error.message);
    return Promise.reject(
      "An unexpected error occurred!, couldn't get the users pie chart."
    );
  }
};

export const get_users_scatter_plot = async (): Promise<string> => {
  try {
    const { data } = await axios.get<string>(
      `${apiUrl}/get_users_scatter_plot`
    );
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) return Promise.reject(error.message);
    return Promise.reject(
      "An unexpected error occurred!, couldn't get the users."
    );
  }
};

export const get_users_box_plot = async (): Promise<string> => {
  try {
    const { data } = await axios.get<string>(`${apiUrl}/get_users_box_plot`);
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) return Promise.reject(error.message);
    return Promise.reject(
      "An unexpected error occurred!, couldn't get the users."
    );
  }
};

export const get_users_bar_chart = async (): Promise<string> => {
  try {
    const { data } = await axios.get<string>(`${apiUrl}/get_users_bar_chart`);
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) return Promise.reject(error.message);
    return Promise.reject(
      "An unexpected error occurred!, couldn't get the users."
    );
  }
};

export const get_users_line_chart = async (): Promise<string> => {
  try {
    const { data } = await axios.get<string>(`${apiUrl}/get_users_line_chart`);
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) return Promise.reject(error.message);
    return Promise.reject(
      "An unexpected error occurred!, couldn't get the users."
    );
  }
};

export const get_users_heatmap = async (): Promise<string> => {
  try {
    const { data } = await axios.get<string>(`${apiUrl}/get_users_heatmap`);
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) return Promise.reject(error.message);
    return Promise.reject(
      "An unexpected error occurred!, couldn't get the users."
    );
  }
};
