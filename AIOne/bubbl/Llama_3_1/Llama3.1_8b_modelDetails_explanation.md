# Llama 3.1 8B Instruct Model Architecture





## Explanation

### 1. Embedding Layer
- **model.embed_tokens.weight (torch.Size([128256, 4096]))**
  - Converts input tokens into dense vectors of size 4096.

### 2. Transformer Blocks
Each transformer block consists of several components:

#### Transformer Block 0 to 31
- **Self-Attention (self_attn)**
  - **Query Linear Transformation (q_proj)**
    - **Weight:** model.layers.{i}.self_attn.q_proj.weight (torch.Size([4096, 4096]))
  - **Key Linear Transformation (k_proj)**
    - **Weight:** model.layers.{i}.self_attn.k_proj.weight (torch.Size([1024, 4096]))
  - **Value Linear Transformation (v_proj)**
    - **Weight:** model.layers.{i}.self_attn.v_proj.weight (torch.Size([1024, 4096]))
  - **Output Linear Transformation (o_proj)**
    - **Weight:** model.layers.{i}.self_attn.o_proj.weight (torch.Size([4096, 4096]))
- **Feed-Forward Neural Network (MLP)**
  - **Gate Projection (gate_proj)**
    - **Weight:** model.layers.{i}.mlp.gate_proj.weight (torch.Size([14336, 4096]))
  - **Up Projection (up_proj)**
    - **Weight:** model.layers.{i}.mlp.up_proj.weight (torch.Size([14336, 4096]))
  - **Down Projection (down_proj)**
    - **Weight:** model.layers.{i}.mlp.down_proj.weight (torch.Size([4096, 14336]))
- **LayerNorm 1 (input_layernorm)**
  - **Weight:** model.layers.{i}.input_layernorm.weight (torch.Size([4096]))
- **LayerNorm 2 (post_attention_layernorm)**
  - **Weight:** model.layers.{i}.post_attention_layernorm.weight (torch.Size([4096]))

### 3. Layer Normalization (Final)
- **model.norm.weight (torch.Size([4096]))**

### 4. Output Linear Layer (lm_head)
- **lm_head.weight (torch.Size([128256, 4096]))**
