import { createContext, useContext, ReactNode } from "react";
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import axios from "axios";
import { Task, User } from "../types/task";
import { toast } from "react-hot-toast";

interface TaskContextType {
  tasks: Task[];
  users: User[];
  isLoading: boolean;
  createTask: (task: Omit<Task, "id" | "created_at" | "updated_at">) => Promise<void>;
  updateTask: (task: Task) => Promise<void>;
  deleteTask: (id: number) => Promise<void>;
  toggleTaskStatus: (id: number) => Promise<void>;
  createUser: (user: Omit<User, "id">) => Promise<void>;
}

const TaskContext = createContext<TaskContextType | undefined>(undefined);

const API_URL = "http://localhost:5000";

export function TaskProvider({ children }: { children: ReactNode }) {
  const queryClient = useQueryClient();

  const { data: tasks = [], isLoading: tasksLoading } = useQuery({
    queryKey: ["tasks"],
    queryFn: async () => {
      const response = await axios.get<Task[]>(`${API_URL}/tasks/`);
      return response.data;
    },
  });

  const { data: users = [], isLoading: usersLoading } = useQuery({
    queryKey: ["users"],
    queryFn: async () => {
      const response = await axios.get<User[]>(`${API_URL}/users/`);
      return response.data;
    },
  });

  const createTaskMutation = useMutation({
    mutationFn: async (newTask: Omit<Task, "id" | "created_at" | "updated_at">) => {
      await axios.post(`${API_URL}/tasks/`, newTask);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["tasks"] });
      toast.success("Task created successfully");
    },
    onError: () => toast.error("Failed to create task"),
  });

  const updateTaskMutation = useMutation({
    mutationFn: async (task: Task) => {
      await axios.put(`${API_URL}/tasks/${task.id}/`, task);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["tasks"] });
      toast.success("Task updated successfully");
    },
    onError: () => toast.error("Failed to update task"),
  });

  const deleteTaskMutation = useMutation({
    mutationFn: async (id: number) => {
      await axios.delete(`${API_URL}/tasks/${id}/`);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["tasks"] });
      toast.success("Task deleted successfully");
    },
    onError: () => toast.error("Failed to delete task"),
  });

  const createUserMutation = useMutation({
    mutationFn: async (newUser: Omit<User, "id">) => {
      await axios.post(`${API_URL}/users/`, newUser);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["users"] });
      toast.success("User created successfully");
    },
    onError: () => toast.error("Failed to create user"),
  });

  const toggleTaskStatus = async (id: number) => {
    const task = tasks.find((t) => t.id === id);
    if (!task) return;

    const updatedTask = {
      ...task,
      status: task.status === "pending" ? "completed" : "pending",
    };

    await updateTaskMutation.mutateAsync(updatedTask);
  };

  return (
    <TaskContext.Provider
      value={{
        tasks,
        users,
        isLoading: tasksLoading || usersLoading,
        createTask: createTaskMutation.mutateAsync,
        updateTask: updateTaskMutation.mutateAsync,
        deleteTask: deleteTaskMutation.mutateAsync,
        toggleTaskStatus,
        createUser: createUserMutation.mutateAsync,
      }}>
      {children}
    </TaskContext.Provider>
  );
}

export function useTaskContext() {
  const context = useContext(TaskContext);
  if (!context) {
    throw new Error("useTaskContext must be used within a TaskProvider");
  }
  return context;
}
