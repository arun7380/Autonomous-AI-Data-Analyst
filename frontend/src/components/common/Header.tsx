import React from 'react';
import { Database, Bot, BarChart2, Layers } from 'lucide-react';
import { useDatasetStore } from '../../store/useDatasetStore';

export const Header: React.FC = () => {
  const { activeDataset } = useDatasetStore();

  return (
    <header className="h-16 border-b border-gray-800 bg-gray-950 px-6 flex items-center justify-between text-white">
      <div className="flex items-center space-x-3">
        <Bot className="h-7 w-7 text-indigo-400" />
        <span className="font-bold text-lg tracking-tight bg-gradient-to-r from-indigo-400 to-sky-400 bg-clip-text text-transparent">
          Autonomous AI Data Analyst
        </span>
      </div>

      {activeDataset && (
        <div className="flex items-center space-x-2 bg-gray-900 px-3 py-1.5 rounded-full border border-gray-800 text-xs">
          <Database className="h-4 w-4 text-emerald-400" />
          <span className="text-gray-300 font-medium">{activeDataset.name}</span>
          <span className="text-gray-500">({activeDataset.row_count.toLocaleString()} rows)</span>
        </div>
      )}
    </header>
  );
};
