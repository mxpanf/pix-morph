# -*- coding: utf-8 -*-
#!/usr/bin/env python
# PEP-8
# Copyright (C) 2023 Maksim Panfilov <mxpanf@proton.me>
# Licensed under MIT License <see LICENSE file>

import click
from pixmorph import ImageProcessor

# Define custom exception for invalid combinations
class InvalidUsageError(click.ClickException):
    pass

# Main command group
@click.group()
def cli():
    """PixMorph - Transform your images with unique effects."""
    pass

# Process command
@cli.command()
@click.argument('input_image', type=click.Path(exists=True, readable=True))
@click.argument('output_image', type=click.Path())
@click.option('--effect', type=click.Choice(['shift', 'dots', 'stripes']), required=True, help="Effect to be applied.")
@click.option('--direction', type=click.Choice(['horizontal', 'vertical']), default='horizontal', help="Direction for the shift effect. (Only applicable to 'shift' effect)")
@click.option('--shift_power', type=int, default=20, help="Maximum shift in pixels. (Only applicable to 'shift' effect)")
@click.option('--band_height', type=int, default=1, help="Height of each band. (Only applicable to 'shift' effect)")
@click.option('--cell_size', type=int, default=6, help="Size of the cell for dots or stripes effect. (Applicable to 'dots' and 'stripes' effects)")
@click.option('--angle', type=float, default=0, help="Angle for stripes orientation. (Only applicable to 'stripes' effect)")
def process(input_image, output_image, effect, direction, shift_power, band_height, cell_size, angle):
    """Process an INPUT_IMAGE to apply a specific effect and save it as OUTPUT_IMAGE."""

    processor = ImageProcessor(input_image)

    # Ensure options are compatible with chosen effect
    if effect == 'shift' and any([cell_size != 6, angle != 0]):
        raise InvalidUsageError("For 'shift' effect, only '--direction', '--shift_power', and '--band_height' parameters are applicable.")
    
    if effect in ['dots', 'stripes'] and any([direction != 'horizontal', shift_power != 20, band_height != 1]):
        raise InvalidUsageError(f"For '{effect}' effect, only '--cell_size' {( 'and --angle' if effect == 'stripes' else '')} parameters are applicable.")
    
    # Apply effect
    if effect == 'shift':
        result = ImageProcessor.Shift.basic(processor, shift_power=shift_power, direction=direction, band_height=band_height)
    elif effect == 'dots':
        result = ImageProcessor.Newsprint.dots_effect(processor, cell_size=cell_size)
    elif effect == 'stripes':
        result = ImageProcessor.Newsprint.stripes_effect(processor, cell_size=cell_size, angle=angle)
    
    result.save(output_image)
    click.echo(f"Image processed with '{effect}' effect and saved to {output_image}.")

if __name__ == "__main__":
    cli()
