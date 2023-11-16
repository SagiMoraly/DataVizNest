import axios from "axios";
// import { useState } from "react";

const useAPI = () => {
  const apiUrl = "http://localhost:5000";

  const get_users = async (): Promise<string> => {
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

  const get_users_pie_chart = async (): Promise<string> => {
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
  return {
    get_users,
    get_users_pie_chart,
  };
};

export default useAPI;
