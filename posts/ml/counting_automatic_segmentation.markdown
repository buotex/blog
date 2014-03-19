{
  "title": "Automatic Segmentation",
  "date": "2014-03-04",
  "categories": [
    "counting"
  ],
  "tags": [
    
  ]
}

##Which steps did we use for automatic segmentation of microscope images

- Used ilastik pixel classification for foreground/background segmentation
- Use the foreground/background segmentation to create masks
- img: mask overlaid over cells
- Gaussian smoothing with small kernel over gray value image
- Select Local maxima in foreground as seeds
- img: seededImage.png
- labelImage: connected components ... (useful?)

Watershed:
- Distance transform over foreground/background image
- filtered.png
- Apply watershed on distance transform along with previous seeds
- Filter out false positives (watersheds which are not likely to represent cells) via thresholding too
  big / too small components
- Centers of the watersheds can now be considered our ground truth


##Alignment

- To use the gained ground truth for learning the locations of cells on the camera images, we
  attempt to align both microscope and camera images
- Do so by using image processing toolbox from Matlab


