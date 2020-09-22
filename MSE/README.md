# MoData Vision Presentation: MSE
The accompanying code to my MoData presentation on Vision on 2/13

# Disclaimer:
This demonstrates vision techniques using "Magic: The Gathering" Cards. These scans belong to Wizards of the Coast.

# What is Vision?
Vision is the process of extracting information from images and video. There are a lot of tools and techniques,
like __Feature Detection, Similarity Indices, De-Noising, Clustering, OCR__ and more. Eventually, I'd like to get into
some of these, but let's start at a simple point. I'm using Sci-Kit Image for Python, but there are other libaries out there
like OpenCV. I like how straightforward Sci-Kit is, and I like working in Python.

# Similarity Between Images
If you want to identify a specific image, or if you want to identify a specific slice of an image,
then computing the similarity of your test image with a group of known images may be the way to go.
There are a few ways to do this: __Descriptor Matching, Mean Square Error and Structural Similarity Index.__
Today, we'll focus on __Mean Square Error.__

# Mean Square Error (MSE)
This technique directly compares the two images. It takes two matricies, A and B, and uses this equation:
norm(A-B). This basically gives you the sum of all different pixels between the two images.
The images must be the same size, and while it could potentially bypass some noise and compression, there is no way to track
any transformation or uncertainty. However, this is an extremely simple and fast technique. It's perfect for picking
out things in video that never move.

# The Example
This example will take a unique slice of the given cards, and it matches __whoami.jpg__ to the set of __imagea.jpg, imageb.jpg and imagec.jpg.__ It finds the lowest MSE and decides that the corresponding card must its match. The second example
automatically opens a directory and names the cards according to their file names. This allows us to search
for a match with a much larger set.
