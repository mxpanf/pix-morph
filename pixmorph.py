# -*- coding: utf-8 -*-
#!/usr/bin/env python
# PEP-8
# Copyright (C) 2023 Maksim Panfilov <mxpanf@proton.me>
# Licensed under MIT License <see LICENSE file>

import random
from typing import Union, Literal
from PIL import Image, ImageFilter, ImageDraw


class ImageProcessor:
    """
    A class to apply various image processing effects.
    """

    class Newsprint:
        """
        Subclass to apply newsprint-like effects.
        """
        
        @staticmethod
        def dots_effect(processor: 'ImageProcessor', cell_size: int = 6) -> Image:
            """
            Apply a newspaper (halftone dots) effect to the image.
            
            Args:
                processor (ImageProcessor): Processor instance with the loaded image.
                cell_size (int): Cell size for the halftone effect.
                
            Returns:
                PIL.Image: Image with the halftone dots effect.
            """
            original = processor.image
            grayscale = original.convert("L")
            blurred = grayscale.filter(ImageFilter.GaussianBlur(radius=cell_size / 3))

            halftoned = Image.new("L", original.size, 255)
            w, h = original.size
            
            for y in range(0, h, cell_size):
                for x in range(0, w, cell_size):
                    average_luminance = int(sum(blurred.crop((x, y, x+cell_size, y+cell_size)).point(lambda p: p).getdata()) / (cell_size * cell_size))
                    radius = (cell_size / 2) * (1 - average_luminance / 255)
                    ImageDraw.Draw(halftoned).ellipse((x, y, x + 2*radius, y + 2*radius), fill=0)

            return halftoned
        
        @staticmethod
        def stripes_effect(processor: 'ImageProcessor', cell_size: int = 6, angle: float = 0) -> Image:
            """
            Apply a stripes effect to the image.
            
            Args:
                processor (ImageProcessor): Processor instance with the loaded image.
                cell_size (int): Cell size for the stripes effect.
                angle (float): Angle in degrees for stripe orientation.
                
            Returns:
                PIL.Image: Image with the stripes effect.
            """
            original = processor.image
            grayscale = original.convert("L")
            blurred = grayscale.filter(ImageFilter.GaussianBlur(radius=cell_size / 3))
            
            # Rotate the image
            rotated = blurred.rotate(-angle, expand=True)
            
            striped = Image.new("L", rotated.size, 255)
            w, h = rotated.size
            
            for y in range(0, h, cell_size):
                for x in range(0, w, cell_size):
                    average_luminance = int(sum(rotated.crop((x, y, x+cell_size, y+cell_size)).point(lambda p: p).getdata()) / (cell_size * cell_size))
                    line_width = cell_size * (1 - average_luminance / 255)
                    if line_width > 0:
                        start_x = x + (cell_size - line_width) // 2
                        ImageDraw.Draw(striped).rectangle([start_x, y, start_x + line_width, y + cell_size], fill=0)

            # Rotate back and crop to the original size
            striped = striped.rotate(angle)
            left_upper = (striped.width - original.width) // 2
            right_lower = left_upper + original.width
            top_upper = (striped.height - original.height) // 2
            bottom_lower = top_upper + original.height

            return striped.crop((left_upper, top_upper, right_lower, bottom_lower))
        
    class Shift:
        """
        Subclass to apply shift-like effects.
        """
        
        @staticmethod
        def basic(processor: 'ImageProcessor', 
                  shift_power: int = 20, 
                  direction: Literal["horizontal", "vertical"] = "horizontal", 
                  band_height: int = 1) -> Image:
            """
            Apply a shift blur effect to the image by shifting bands.
            
            Args:
                processor (ImageProcessor): Processor instance with the loaded image.
                shift_power (int): Maximum shift in pixels.
                direction (Literal["horizontal", "vertical"]): Shift direction.
                band_height (int): Height of each band.
                
            Returns:
                PIL.Image: Image with the shift blur effect.
            """
            original = processor.image
            shifted = Image.new(original.mode, original.size)

            w, h = original.size

            if direction == "horizontal":
                for band_start in range(0, h, band_height):
                    band_shift = random.randint(0, shift_power)
                    for x in range(w):
                        for y in range(band_start, min(band_start + band_height, h)):
                            new_x = (x + band_shift) % w
                            shifted.putpixel((x, y), original.getpixel((new_x, y)))

            elif direction == "vertical":
                for band_start in range(0, w, band_height):
                    band_shift = random.randint(0, shift_power)
                    for y in range(h):
                        for x in range(band_start, min(band_start + band_height, w)):
                            new_y = (y + band_shift) % h
                            shifted.putpixel((x, y), original.getpixel((x, new_y)))

            return shifted

    def __init__(self, image_path: str):
        """
        Initialize with an image path.
        
        Args:
            image_path (str): Path to the image to be processed.
        """
        self.image = Image.open(image_path)

    def save(self, image: Image, output_path: str) -> None:
        """
        Save the processed image.
        
        Args:
            image (PIL.Image): The image to save.
            output_path (str): Path for the saved image.
        """
        image.save(output_path)
