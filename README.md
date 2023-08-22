# PixMorph

🖼 **PixMorph** is a versatile image manipulation tool that applies various artistic effects to your images, such as the newsprint halftone dots effect, shift blur effects, and many more.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
    - [Command Line Interface](#command-line-interface)
- [Flags and Parameters](#flags-and-parameters)
- [Examples](#examples)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/mxpanf/pix-morph
    ```

2. **Navigate to the project directory**:
    ```bash
    cd pix-morph
    ```

3. **Set up a virtual environment (recommended)**:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

4. **Install the required packages**:
    ```bash
    pip3 install -r requirements.txt
    ```

5. You're all set! Now you can run the command-line tool to start processing images.


## Usage

### Command Line Interface

After setting up the project, you can use the `pixmorph_cli.py` script to process images from the command line.

```bash
python3 pixmorph_cli.py process INPUT_IMAGE OUTPUT_IMAGE --effect EFFECT_NAME [OPTIONS]
```

For detailed help on using the command line interface:

```bash
python3 pixmorph_cli.py --help
```

### Python Module

```python
from pixmorph import ImageProcessor

# Initialize the processor with an image path
picture = ImageProcessor("path_to_your_image.jpg")

# Applying the dots effect with custom parameters
dots_image = ImageProcessor.Newsprint.dots_effect(picture, cell_size=10)
dots_image.show()

# Applying the shift effect with custom parameters
shifted_image = ImageProcessor.Shift.basic(picture, shift_power=10, direction="vertical")
shifted_image.show()
```

## Flags and Parameters

### Parameters fot CLI

| Flag            | Description                        | Allowed Values             | Default Value | Applicable Effects |
| --------------- | ---------------------------------- | -------------------------- | ------------- | ------------------ |
| `--effect`      | Name of the effect to apply        | `dots`, `stripes`, `shift` | None          | All                |
| `--cell_size`   | Size of the cell for the effect    | Any integer                | 6             | dots, stripes      |
| `--angle`       | Angle for the effect's orientation | Any float                  | 0             | stripes            |
| `--direction`   | Direction of the shift effect      | `horizontal`, `vertical`   | horizontal    | shift              |
| `--shift_power` | Maximum shift in pixels            | Any integer                | 20            | shift              |
| `--band_height` | Height of each band for shift      | Any integer                | 1             | shift              |

### Parameters for Python Module Usage

| Method                   | Parameter        | Description                                               | Default       | Example Values                           |
|--------------------------|------------------|-----------------------------------------------------------|---------------|------------------------------------------|
| `Newsprint.dots_effect`  | `cell_size`      | Size of the cell for the halftone effect                  | `6`           | `4`, `10`, `15`                          |
| `Newsprint.stripes_effect` | `cell_size`    | Size of the cell for the stripes effect                   | `6`           | `5`, `12`, `18`                          |
|                          | `angle`          | Angle in degrees for the stripes orientation              | `0` (vertical)| `45`, `90`                               |
| `Shift.basic`            | `shift_power`    | Maximum shift in pixels                                   | `20`          | `5`, `15`, `30`                          |
|                          | `direction`      | Direction of the shift                                    | "horizontal"  | "horizontal", "vertical"                 |
|                          | `band_height`    | Height of each band                                       | `1`           | `2`, `5`, `10`                           |


## Examples

1. Apply the shift effect on an image in the horizontal direction and shift power of 50:

    <details>
    <summary>Click this to collapse/fold.</summary>

    ![Tom Shifted](./.assets/tom_shifted.jpg)

    </details>

   ```bash
   python3 pixmorph_cli.py process tom.jpg tom_shifted.jpg --effect shift --direction horizontal --shift_power 50
   ```

2. Apply the dots (halftone) effect with a cell size of 8 pixels:

    <details>
    <summary>Click this to collapse/fold.</summary>

    ![Tom Shifted](./.assets/tom_dots.jpg)

    </details>

   ```bash
   python3 pixmorph_cli.py process tom.jpg tom_dots.jpg --effect dots --cell_size 8
   ```

3. Apply a stripes effect on an image at a 45-degree angle:

    <details>
    <summary>Click this to collapse/fold.</summary>

    ![Tom Shifted](./.assets/tom_stripes.jpg)

    </details>

   ```bash
   python3 pixmorph_cli.py process tom.jpg tom_stripes.jpg --effect stripes --angle 45
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Acknowledgements

[PIL (Python Imaging Library)](https://pillow.readthedocs.io/en/stable/)