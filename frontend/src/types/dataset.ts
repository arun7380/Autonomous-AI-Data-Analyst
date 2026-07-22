export interface Dataset {
  id: string;
  name: string;
  file_type: string;
  file_size_bytes: number;
  row_count: number;
  column_count: number;
  created_at: string;
  columns: string[];
  column_types: Record<string, string>;
}

export interface ColumnSummary {
  name: string;
  data_type: string;
  semantic_type: 'numerical' | 'categorical' | 'datetime' | 'text' | 'id';
  missing_count: number;
  missing_percentage: number;
  unique_count: number;
}

export interface ProfileResponse {
  dataset_id: string;
  total_rows: number;
  total_columns: number;
  duplicate_rows: number;
  columns_summary: ColumnSummary[];
  quality_score: number;
}
