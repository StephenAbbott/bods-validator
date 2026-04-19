export interface ValidationResult {
  valid: boolean;
  schema_valid?: boolean;
  schema_version?: string;
  sample_mode?: boolean;
  error?: string;
  error_type?: string;
  schema_errors: SchemaError[];
  additional_checks: AdditionalCheck[];
  additional_fields: AdditionalField[];
  statistics: Record<string, any>;
  advice: Advice[];
}

export interface SchemaError {
  message: string;
  path: (string | number)[];
  path_ending: string;
  schema_path: (string | number)[];
  validator: string;
  validator_value: any;
  instance: any;
  extra?: Record<string, any>;
}

export interface AdditionalCheck {
  type: string;
  [key: string]: any;
}

export interface AdditionalField {
  [key: string]: any;
}

export interface Advice {
  level: "error" | "warning" | "success";
  message: string;
  guidance: string;
  docs_url: string;
  count: number;
}

export interface ExampleSummary {
  id: string;
  title: string;
  description: string;
  valid: boolean;
  country?: string;
  icon?: string;
  has_original?: boolean;
  original_format?: string;
}

export interface Example extends ExampleSummary {
  data: any;
  original_data?: any;
}
