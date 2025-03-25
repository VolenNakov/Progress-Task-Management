import { format } from 'date-fns';
import { useState } from 'react';
import { useTaskContext } from '../context/TaskContext';
import { Task } from '../types/task';

export function TaskList() {
  const { tasks, users, toggleTaskStatus, deleteTask, updateTask } = useTaskContext();
  const [showCompleted, setShowCompleted] = useState(false);
  const [selectedUser, setSelectedUser] = useState<number | 'all'>('all');
  const [editingTask, setEditingTask] = useState<Task | null>(null);

  const filteredTasks = tasks.filter(task => {
    const completionMatch = showCompleted ? true : task.status === 'pending';
    const userMatch = selectedUser === 'all' ? true : task.assigned_to === selectedUser;
    return completionMatch && userMatch;
  });

  const handleTaskUpdate = async () => {
    if (!editingTask) return;
    await updateTask(editingTask);
    setEditingTask(null);
  };

  return (
    <div className="space-y-4">
      <div className="flex flex-col gap-4 mb-6 sm:flex-row sm:items-center sm:justify-between">
        <label className="flex items-center gap-2">
          <input
            type="checkbox"
            checked={showCompleted}
            onChange={(e) => setShowCompleted(e.target.checked)}
            className="rounded border-gray-300 text-blue-500 focus:ring-blue-500"
          />
          <span className="text-sm text-gray-700">Show completed tasks</span>
        </label>

        <select
          value={selectedUser}
          onChange={(e) => setSelectedUser(e.target.value === 'all' ? 'all' : Number(e.target.value))}
          className="rounded-md p-2 border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
        >
          <option value="all">All Users</option>
          {users.map((user) => (
            <option key={user.id} value={user.id}>
              {user.name}
            </option>
          ))}
        </select>
      </div>

      {filteredTasks.map((task) => {
        const assignedUser = users.find((u) => u.id === task.assigned_to);
        const isEditing = editingTask?.id === task.id;
        
        return (
          <div
            key={task.id}
            className="bg-white rounded-lg shadow p-4 flex items-start justify-between"
          >
            <div className="flex items-start gap-3 flex-grow">
              <button
                onClick={() => toggleTaskStatus(task.id)}
                className="mt-1 px-2 py-1 text-sm rounded-full border border-gray-300 hover:bg-gray-100 transition-colors"
              >
                {task.status === 'completed' ? '✓' : '○'}
              </button>
              
              <div className="flex-grow">
                {isEditing ? (
                  <div className="space-y-2">
                    <input
                      type="text"
                      value={editingTask.title}
                      onChange={(e) => setEditingTask({ ...editingTask, title: e.target.value })}
                      className="w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                    />
                    <textarea
                      value={editingTask.description}
                      onChange={(e) => setEditingTask({ ...editingTask, description: e.target.value })}
                      rows={2}
                      className="w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                    />
                    <div className="flex gap-2">
                      <button
                        onClick={handleTaskUpdate}
                        className="px-3 py-1 text-sm bg-blue-500 text-white rounded-md hover:bg-blue-600"
                      >
                        Save
                      </button>
                      <button
                        onClick={() => setEditingTask(null)}
                        className="px-3 py-1 text-sm bg-gray-100 text-gray-700 rounded-md hover:bg-gray-200"
                      >
                        Cancel
                      </button>
                    </div>
                  </div>
                ) : (
                  <>
                    <h3 
                      className={`font-medium ${task.status === 'completed' ? 'line-through text-gray-500' : ''}`}
                      onClick={() => setEditingTask(task)}
                    >
                      {task.title}
                    </h3>
                    <p 
                      className="text-sm text-gray-600 mt-1"
                      onClick={() => setEditingTask(task)}
                    >
                      {task.description}
                    </p>
                    <div className="mt-2 flex items-center gap-4 text-sm text-gray-500">
                      <span>Assigned to: {assignedUser?.name}</span>
                      <span>Created: {format(new Date(task.created_at), 'MMM d, yyyy HH:MM')}</span>
                    </div>
                  </>
                )}
              </div>
            </div>

            <button
              onClick={() => deleteTask(task.id)}
              className="text-gray-400 hover:text-red-500 transition-colors px-2 py-1 ml-2"
            >
              ×
            </button>
          </div>
        );
      })}

      {filteredTasks.length === 0 && (
        <div className="text-center py-8 text-gray-500">
          No tasks found
        </div>
      )}
    </div>
  );
}