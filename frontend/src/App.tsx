import React from 'react';
import { Header } from './components/common/Header';
import { Database, Upload, MessageSquare, BarChart3, Settings } from 'lucide-react';
import { useDatasetStore } from './store/useDatasetStore';

export const App: React.FC = () => {
  const { activeDataset } = useDatasetStore();

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100 flex flex-col">
      <Header />
      <div className="flex flex-1">
        {/* Sidebar */}
        <aside className="w-64 border-r border-gray-800 bg-gray-900/50 p-4 flex flex-col justify-between">
          <nav className="space-y-1">
            <button className="w-full flex items-center space-x-3 px-3 py-2 rounded-lg bg-indigo-600/20 text-indigo-400 font-medium">
              <Upload className="h-5 w-5" />
              <span>Upload Dataset</span>
            </button>
            <button className="w-full flex items-center space-x-3 px-3 py-2 rounded-lg text-gray-400 hover:bg-gray-800 hover:text-white">
              <MessageSquare className="h-5 w-5" />
              <span>AI Chat</span>
            </button>
            <button className="w-full flex items-center space-x-3 px-3 py-2 rounded-lg text-gray-400 hover:bg-gray-800 hover:text-white">
              <BarChart3 className="h-5 w-5" />
              <span>Dashboard</span>
            </button>
          </nav>
        </aside>

        {/* Main Content Area */}
        <main className="flex-1 p-8">
          <div className="max-w-4xl mx-auto border-2 border-dashed border-gray-800 rounded-2xl p-12 text-center bg-gray-900/30">
            <Upload className="h-12 w-12 text-indigo-400 mx-auto mb-4" />
            <h2 className="text-xl font-semibold mb-2">Upload Dataset to Begin Autonomous Analysis</h2>
            <p className="text-gray-400 text-sm mb-6">Supports CSV, XLSX, Parquet, JSON, SQLite, and SQL databases</p>
            <button className="px-6 py-2.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-medium shadow-lg shadow-indigo-600/30 transition-all">
              Choose File or Drag & Drop
            </button>
          </div>
        </main>
      </div>
    </div>
  );
};

export default App;
