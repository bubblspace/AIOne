# Llama 3.1 8B Instruct Model Architecture

## Explanation


## Explanation

### 1. Embedding Layer
- **transformer.wte.weight (torch.Size([50257, 768]))**
  - Converts input tokens into dense vectors of size 768.

### 2. Positional Encoding Layer
- **transformer.wpe.weight (torch.Size([1024, 768]))**
  - Adds positional information to the embeddings to make use of the order of the tokens.

### 3. Transformer Blocks
Each transformer block consists of several components:

#### Transformer Block 1 to 12
- **LayerNorm 1 (ln_1)**
  - **Weight:** transformer.h.{i}.ln_1.weight (torch.Size([768]))
  - **Bias:** transformer.h.{i}.ln_1.bias (torch.Size([768]))
- **Self-Attention (attn)**
  - **Query, Key, Value Linear Transformations (c_attn)**
    - **Weight:** transformer.h.{i}.attn.c_attn.weight (torch.Size([768, 2304]))
    - **Bias:** transformer.h.{i}.attn.c_attn.bias (torch.Size([2304]))
  - **Output Linear Transformation (c_proj)**
    - **Weight:** transformer.h.{i}.attn.c_proj.weight (torch.Size([768, 768]))
    - **Bias:** transformer.h.{i}.attn.c_proj.bias (torch.Size([768]))
- **LayerNorm 2 (ln_2)**
  - **Weight:** transformer.h.{i}.ln_2.weight (torch.Size([768]))
  - **Bias:** transformer.h.{i}.ln_2.bias (torch.Size([768]))
- **Feed-Forward Neural Network (MLP)**
  - **Fully Connected Layer 1 (c_fc)**
    - **Weight:** transformer.h.{i}.mlp.c_fc.weight (torch.Size([768, 3072]))
    - **Bias:** transformer.h.{i}.mlp.c_fc.bias (torch.Size([3072]))
  - **Fully Connected Layer 2 (c_proj)**
    - **Weight:** transformer.h.{i}.mlp.c_proj.weight (torch.Size([3072, 768]))
    - **Bias:** transformer.h.{i}.mlp.c_proj.bias (torch.Size([768]))

### 4. Layer Normalization (Final)
- **transformer.ln_f.weight (torch.Size([768]))**
- **transformer.ln_f.bias (torch.Size([768]))**

### 5. Output Linear Layer (lm_head)
- **lm_head.weight (torch.Size([50257, 768]))**
