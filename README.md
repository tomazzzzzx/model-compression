# Model Compression

Model compression toolkit: pruning, distillation, quantization.

## Methods
- **Pruning**: Structured (L1, movement) and unstructured
- **Distillation**: Feature-based and logit-based
- **Quantization**: INT8, INT4, GPTQ, AWQ, GGUF

## Results (Llama-3-8B)
| Method | Size | PPL | Speedup |
|--------|------|-----|--------|
| FP16 | 16GB | 6.1 | 1x |
| INT8 | 8GB | 6.2 | 1.8x |
| INT4 (GPTQ) | 4GB | 6.5 | 3.2x |

## License
MIT
