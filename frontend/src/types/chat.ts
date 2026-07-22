export interface AgentStepDetail {
  agent_name: string;
  thought: string;
  action_taken: string;
  output_summary: string;
}

export interface ChatMessage {
  id: string;
  sender: 'user' | 'assistant';
  text: string;
  agentSteps?: AgentStepDetail[];
  codeExecuted?: string;
  dataTable?: Record<string, any>[];
  timestamp: string;
}
