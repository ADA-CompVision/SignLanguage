import os
import random
import cv2
from imgaug import augmenters as iaa

def videoAugmentation():
    cropRatio = round(random.uniform(0, 0.2), 1)
    flipBoolean = 0.0 if random.uniform(0, 1) % 2 == 0 else 1.0
    makeGrayScale = 1.0 if random.uniform(0, 1) % 5 == 0 else 0.0
    gaussBlurRatio = round(random.uniform(0, 0.5), 1)
    linearRatio = round(random.uniform(0.75, 1.5), 1)
    gaussNoise = round(random.uniform(0, 0.05 * 255), 2)
    multiplyRatio = round(random.uniform(0.8, 1.2), 1)
    scaleRatio = round(random.uniform(0.9, 1.1), 1)
    translateRatio = round(random.uniform(-0.1, 0.1), 1)
    rotateRatio = round(random.uniform(-3, 3), 1)
    shearRatio = round(random.uniform(-5, 5), 1)
    addRatio = random.randint(-10, 10)


    return iaa.Sequential([
        iaa.Fliplr(flipBoolean),
        iaa.Crop(percent=(cropRatio, cropRatio)),
        # # Small gaussian blur with random sigma between 0 and 0.5.
        # # But we only blur about 50% of all images.
        iaa.GaussianBlur(sigma=(gaussBlurRatio, gaussBlurRatio)),
        # # Strengthen or weaken the contrast in each image.
        iaa.LinearContrast((linearRatio, linearRatio)),
        iaa.AverageBlur(k=(2, 7)),
        iaa.EdgeDetect(alpha=(0, 0.7)),
        iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5)),
        # iaa.Dropout((0.01, 0.1), per_channel=0.5),
        iaa.ElasticTransformation(alpha=(0.5, 3.5), sigma=0.25),
        # # Add gaussian noise.
        # # For 50% of all images, we sample the noise once per pixel.
        # # For the other 50% of all images, we sample the noise per pixel AND
        # # channel. This can change the color (not only brightness) of the
        # # pixels.
        iaa.AdditiveGaussianNoise(loc=0, scale=(gaussNoise, gaussNoise), per_channel=1),
        # # Make some images brighter and some darker.
        # # In 20% of all cases, we sample the multiplier once per channel,
        # # which can end up changing the color of the images.
        iaa.Multiply((multiplyRatio, multiplyRatio), per_channel=1),
        iaa.Add(addRatio, per_channel=1),
        # # Apply affine transformations to each image.
        # # Scale/zoom them, translate/move them, rotate them and shear them.
        iaa.Affine(
            scale={"x": (scaleRatio, scaleRatio), "y": (scaleRatio, scaleRatio)},
            translate_percent={"x": (translateRatio, translateRatio), "y": (translateRatio, translateRatio)},
            rotate=(rotateRatio, rotateRatio),
            shear=(shearRatio, shearRatio)
        ),
        iaa.Grayscale(alpha=makeGrayScale)
    ], random_order=False)

def augmentVideo(file, newFile):
    cap = cv2.VideoCapture(file)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    videoWriter = cv2.VideoWriter(newFile, cv2.VideoWriter_fourcc('M','J','P','G'), fps, (width, height))

    videoAug = videoAugmentation()
    for _ in range(frameCount):
        _, frame = cap.read()
        frame_aug = videoAug(image=frame)
        # colorful = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        videoWriter.write(frame_aug)

    cap.release()
    videoWriter.release()

def augmentVideos(main_folder, duplicates):
    destination_folder = os.path.join(main_folder, 'Augmented')

    if not os.path.isdir(destination_folder):
        os.mkdir(destination_folder)

    video_folders = ('D','G','K', 'Y', 'Z', 'Ç', 'Ö', 'Ü')
    
    for folder in os.listdir(main_folder):
        subfolder = os.path.join(main_folder, folder)

        if os.path.isdir(subfolder) and len(folder) in (1,2) and folder in video_folders:
            new_folder = os.path.join(destination_folder, folder)
            os.mkdir(new_folder)
            print('> Created folder', folder)

            for file in os.listdir(subfolder):
                file_path = os.path.join(subfolder, file)
                if file.split('.')[-1] in ('mp4', 'avi'):
                    for i in range(1, duplicates + 1):
                        try:
                            filename = file.split('\\')[-1]
                            filenameNoExt = filename.split('.')[0]
                            newFilename = filenameNoExt + f'_aug{i}.avi'
                            newFile = os.path.join(new_folder, newFilename)
                            
                            augmentVideo(file_path, newFile)
                        except Exception as e:
                            print(str(e))

main_video_folder = "D:/{Samir}/Personal/Education/ADA/{{Study}}/Thesis/Scripts/videos"
augmentVideos(main_video_folder, 5)
