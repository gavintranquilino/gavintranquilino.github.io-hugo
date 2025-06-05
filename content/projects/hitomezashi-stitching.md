---
title: "Sashiko <br> Hitomezashi Stitching"
date: "2020-05-23"
imageUrl: "/img/hitomezashi-stitching/square.jpg"
subtitle: "High School Innovation Week"
---

## SMHS Innovation Week
During SMHS Innovation Week, students were challenged to explore creative problem solving through a variety of STEAM based activities. One of the optional challenges was to recreate traditional Hitomezashi stitching—a Japanese embroidery technique—using random patterns of 1s and 0s.

Instead of flipping coins or using a random number website as suggested, I decided to write my own program to generate the patterns digitally. This post documents how I built it, what I learned, and how traditional art can intersect with code.

## What is Hitomezashi Stitching?
Hitomezashi stitching is a form of Japanese embroidery characterized by its simple yet intricate patterns. It uses a grid system where stitches are made in alternating directions, creating a unique visual effect. The patterns can be generated randomly, which adds an element of surprise and creativity to the design.

## My Design

{{< slideshow >}}
    {{< slide src="/img/hitomezashi-stitching/finished-product.jpg" caption="My Hitomezashi Design" >}}
    {{< slide src="/img/hitomezashi-stitching/part1.jpg" caption="First Part" >}}
    {{< slide src="/img/hitomezashi-stitching/part2.jpg" caption="Second Part" >}}
    {{< slide src="/img/hitomezashi-stitching/part3.jpg" caption="Third Part" >}}
{{< /slideshow >}}

## Building the Pattern Generator
The first step in my process was to choose a programming language. I opted for Python due to its simplicity and my fluency at the time.

### Generating Random Patterns
To create the random patterns, I wrote a function that generates random values of 1s and 0s. Each value 
represents the presence or absence of a stitch in the Hitomezashi pattern.

```python
import random

# Hitomezashi stitching uses random values on the lines of the grid cells,
# so we take n-1 random digits on the horizontal and vertical axis.

n = int(input("Square grid width\n"))

print("Horizontal:")
for _ in range(n - 1):
    print(random.randint(0, 1), end=' ')
print()

print("Vertical:")
for _ in range(n - 1):
    print(random.randint(0, 1), end=' ')
print()
```

### Visualizing the Pattern
To visualize the generated pattern, I colored every cell on some paper. 