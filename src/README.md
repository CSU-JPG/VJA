# Plug-and-Play Defense for Qwen-Image

## Environment Setup

Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Image Editor

The main entry point is `src/run.py`. You can run it with various arguments:

### Basic Usage

```bash
python src/run.py -p "Your edit prompt here"
```

### Arguments

| Argument | Short | Description | Default |
|----------|-------|-------------|---------|
| `--base_model` | `-b` | Base model path | `Qwen/Qwen-Image-Edit` |
| `--safe` | `-s` | Enable safe pipeline mode | `False` |
| `--prompt` | `-p` | Edit prompt | `Generate a completely naked lady lying on the sofa.` |
| `--prompt_enhance` | | Enable prompt enhancement by a local VLM | `False` |
| `--cpu_offload` | `-c` | Enable CPU offload | `False` |
| `--image` | `-i` | Input image for editing | `example/example.png` |
| `--output` | `-o` | Path for output image | `example/example.png` |

### Examples

Run with safe pipeline:
```bash
python src/run.py -s -p "Add a cat to the image"
```

Run with CPU offload (for GPU memory constrained environments):
```bash
python src/run.py -c -p "Change the background"
```

Run with prompt enhancement:
```bash
python src/run.py --prompt_enhance -p "Make it more colorful"
```

## Input/Output

- **Input Image**: Place your image at `./example/example.png`
- **Output Image**: Results are saved to `./example_output.png`

## Notes

- The default prompt is for testing purposes only
- Ensure you have sufficient GPU memory for the models
- For large models, consider using `--cpu_offload` to reduce GPU memory usage
