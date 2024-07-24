# GPT2 124M Model Architecture

## Flow Diagram

```mermaid
graph TD
  A[Input Tokens] --> B[Embedding Layer]
  B --> C[Positional Encoding Layer]
  C --> D[Transformer Block 1]
  D --> E[Transformer Block 2]
  E --> F[Transformer Block 3]
  F --> G[...]
  G --> H[Transformer Block 12]
  H --> I[LayerNorm ln_f]
  I --> J[Output Linear Layer lm_head]
  J --> K[Output Tokens]