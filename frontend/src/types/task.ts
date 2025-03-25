export interface Task {
  id: number;
  title: string;
  description: string;
  status: string;
  assigned_to: number;
  created_at: string;
  updated_at: string;
}

export interface User {
  id: number;
  name: string;
}