# Image Classification
This will be an attempt to merge the concepts of classifiers and vision techniques.

## Features/Descriptors
MSE is subject to a lot of disruption. Scale, rotation, distortion, compression and more. As such, while it's a very fast method to identify images, it's also very sensitive. Paying attention to image features is a way to address this problem. Features are defined by descriptors. In a lot of computer vision resources, you'll see SIFT (Scale Invariant Feature Transform) mentioned a lot. However, it's actually a patented algorithm, and using it involves using black-box software to label images. Personally, I prefer using the ORB descriptor through Sci-Kit Image. 

Descriptors are very handy for a lot of things: You can fit them to work with machine learning classifiers, use them to track movement, but the takeaway is that they're fairly slow, but they're more robust than something like MSE.

## Machine Learning Classification
Something that was touched on with KNN is the hyperplane. Basically, a hyperplane is a plane of n dimensions. Something like KNN can only work on a hyperplane. Support Vector Machines, or SVMs are another concept that works on a hyperplane. Basically, SVMs will find a function to cleanly split predictors into groups corresponding to their target value. But for each predictor, the hyperplane operates on another dimension. This usually means that SVMs are relatively accurate, but they use a lot of RAM from my experience.

What does this have to do with images? Images, when handled by something like Sci-Kit Image, are treated as numpy arrays, with one dimension representing the image height, width and color values.

If we flatten the array, forming a long, one-dimensional list, then we can use the image as a predictor value in something like SVMs or KNN classification. If trained well, this method can also overcome some of the issues posed by MSE. While training could take come time, that's computation done ahead of run time (assuming an eager learner). Prediction is potentially faster than using feature descriptors.