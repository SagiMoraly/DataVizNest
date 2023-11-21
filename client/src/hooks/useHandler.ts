import { useMemo, useState } from "react";
import {
  get_income_sources,
  get_expenses,
  get_savings_goals,
  create_fake_users,
  get_users_pie_chart,
  get_users_scatter_plot,
  get_users_box_plot,
  get_users_bar_chart,
  get_users_line_chart,
  get_users_heatmap,
  get_users,
} from "../API/useAPI.ts";

const useHandler = () => {
  const [isLoading, setLoading] = useState(false);
  const [error, setError] = useState<null | string>(null);

  const requestStatus = (loading: boolean, errorMessage: null | string) => {
    setLoading(loading);
    setError(errorMessage);
  };

  const handle_get_income_sources = async () => {
    try {
      setLoading(true);
      const users = await get_income_sources();
      requestStatus(false, null);
      return users;
    } catch (error) {
      if (typeof error === "string") requestStatus(false, error);
    }
  };

  const handle_get_expenses = async () => {
    try {
      setLoading(true);
      const users = await get_expenses();
      requestStatus(false, null);
      return users;
    } catch (error) {
      if (typeof error === "string") requestStatus(false, error);
    }
  };

  const handle_get_savings_goals = async () => {
    try {
      setLoading(true);
      const users = await get_savings_goals();
      requestStatus(false, null);
      return users;
    } catch (error) {
      if (typeof error === "string") requestStatus(false, error);
    }
  };

  const handle_create_fake_users = async (num: number) => {
    try {
      setLoading(true);
      const users = await create_fake_users(num);
      requestStatus(false, null);
      return users;
    } catch (error) {
      if (typeof error === "string") requestStatus(false, error);
    }
  };

  const handle_get_users_pie_chart = async () => {
    try {
      setLoading(true);
      const users = await get_users_pie_chart();
      requestStatus(false, null);
      return users;
    } catch (error) {
      if (typeof error === "string") requestStatus(false, error);
    }
  };

  const handle_get_users_scatter_plot = async () => {
    try {
      setLoading(true);
      const users = await get_users_scatter_plot();
      requestStatus(false, null);
      return users;
    } catch (error) {
      if (typeof error === "string") requestStatus(false, error);
    }
  };

  const handle_get_users_box_plot = async () => {
    try {
      setLoading(true);
      const users = await get_users_box_plot();
      requestStatus(false, null);
      return users;
    } catch (error) {
      if (typeof error === "string") requestStatus(false, error);
    }
  };

  const handle_get_users_bar_chart = async () => {
    try {
      setLoading(true);
      const users = await get_users_bar_chart();
      requestStatus(false, null);
      return users;
    } catch (error) {
      if (typeof error === "string") requestStatus(false, error);
    }
  };

  const handle_get_users_line_chart = async () => {
    try {
      setLoading(true);
      const users = await get_users_line_chart();
      requestStatus(false, null);
      return users;
    } catch (error) {
      if (typeof error === "string") requestStatus(false, error);
    }
  };

  const handle_get_users_heatmap = async () => {
    try {
      setLoading(true);
      const users = await get_users_heatmap();
      requestStatus(false, null);
      return users;
    } catch (error) {
      if (typeof error === "string") requestStatus(false, error);
    }
  };

  const handle_get_users = async () => {
    try {
      setLoading(true);
      const users = await get_users();
      requestStatus(false, null);
      return users;
    } catch (error) {
      if (typeof error === "string") requestStatus(false, error);
    }
  };

  const value = useMemo(() => {
    return { isLoading, error };
  }, [isLoading, error]);

  return {
    value,
    handle_get_users,
    handle_get_income_sources,
    handle_get_expenses,
    handle_get_savings_goals,
    handle_create_fake_users,
    handle_get_users_pie_chart,
    handle_get_users_scatter_plot,
    handle_get_users_box_plot,
    handle_get_users_bar_chart,
    handle_get_users_line_chart,
    handle_get_users_heatmap,
  };
};

export default useHandler;
