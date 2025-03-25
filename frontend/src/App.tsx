import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import { Toaster } from 'react-hot-toast';
import { TaskProvider } from './context/TaskContext';
import { CreateTaskForm } from './components/CreateTaskForm';
import { CreateUserForm } from './components/CreateUserForm';
import { TaskList } from './components/TaskList';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <TaskProvider>
        <div className="min-h-screen bg-gray-100">
          <div className="max-w-4xl mx-auto py-8 px-4">
            <div className="flex items-center gap-3 mb-8">
              <span className="text-2xl text-blue-500">📋</span>
              <h1 className="text-3xl font-bold text-gray-900">Podio Task Management</h1>
            </div>

            <div className="grid gap-8 md:grid-cols-[350px,1fr]">
              <div className="space-y-8">
                <div>
                  <h2 className="text-xl font-semibold text-gray-900 mb-4">Create New Task</h2>
                  <CreateTaskForm />
                </div>
                <CreateUserForm />
              </div>

              <div>
                <h2 className="text-xl font-semibold text-gray-900 mb-4">Tasks</h2>
                <TaskList />
              </div>
            </div>
          </div>
        </div>
      </TaskProvider>
      <ReactQueryDevtools />
      <Toaster position="top-right" />
    </QueryClientProvider>
  );
}

export default App;