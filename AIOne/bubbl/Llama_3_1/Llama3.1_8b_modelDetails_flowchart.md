# Llama 3.1 8B Instruct Model Architecture

## Flow Diagram

```mermaid
graph TD
  A[Input Tokens] --> B[Embedding Layer]
  B --> C[Transformer Block 0]
  C --> D[Transformer Block 1]
  D --> E[Transformer Block 2]
  E --> F[Transformer Block 3]
  F --> G[...]
  G --> H[Transformer Block 31]
  H --> I[LayerNorm norm]
  I --> J[Output Linear Layer lm_head]
  J --> K[Output Tokens]