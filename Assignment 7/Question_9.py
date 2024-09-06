# Write a python program to identify a person from the walking style (gait recognition) using convolutional recurrent neural network.



import os
import numpy as np
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import TimeDistributed, Conv2D, MaxPooling2D, Flatten, LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import Adam

np.random.seed(42)

# Parameters
DATA_DIR = r'C:\Rick\Study\MCA\3rd Semester\Python Lab\Assignment 7\GaitDataset_Classi'  # Replace with your main data directory
CLASSES = ['001', '002']
IMG_HEIGHT = 64
IMG_WIDTH = 64
CHANNELS = 3  # Use 1 for grayscale
SEQUENCE_LENGTH = 30  # Number of frames per sequence
BATCH_SIZE = 32
EPOCHS = 20
LEARNING_RATE = 1e-4

def load_data(data_dir, classes, sequence_length, img_size, channels):
    X = []
    y = []
    label_map = {cls: idx for idx, cls in enumerate(classes)}

    for cls in classes:
        cls_dir = os.path.join(data_dir, cls)
        if not os.path.isdir(cls_dir):
            print(f"Directory {cls_dir} does not exist. Skipping.")
            continue

        img_files = sorted([
            os.path.join(cls_dir, img) for img in os.listdir(cls_dir)
            if img.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))
        ])

        print(f"Loading {len(img_files)} images for class '{cls}'")

        # Create sequences
        for i in range(0, len(img_files) - sequence_length + 1, sequence_length):
            seq = []
            for j in range(i, i + sequence_length):
                img_path = img_files[j]
                img = cv2.imread(img_path)

                if img is None:
                    print(f"Warning: Unable to read image {img_path}. Skipping.")
                    break

                if channels == 1:
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                else:
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                img = cv2.resize(img, img_size)
                
                if channels == 1:
                    img = img.reshape(img_size[0], img_size[1], 1)
                seq.append(img)

            if len(seq) == sequence_length:
                X.append(seq)
                y.append(label_map[cls])

    X = np.array(X)
    y = np.array(y)

    print(f"Total sequences: {X.shape[0]}")
    print(f"Shape of X: {X.shape}")
    print(f"Shape of y: {y.shape}")

    return X, y

def preprocess_data(X, y, num_classes):
    # Normalize the images
    X = X.astype('float32') / 255.0

    # Convert labels to categorical
    y = to_categorical(y, num_classes)

    return X, y

def build_crnn_model(sequence_length, img_height, img_width, channels, num_classes):
    model = Sequential()

    # TimeDistributed Conv Layers
    model.add(TimeDistributed(Conv2D(32, (3, 3), activation='relu'), 
                              input_shape=(sequence_length, img_height, img_width, channels)))
    model.add(TimeDistributed(MaxPooling2D((2, 2))))
    
    model.add(TimeDistributed(Conv2D(64, (3, 3), activation='relu')))
    model.add(TimeDistributed(MaxPooling2D((2, 2))))
    
    model.add(TimeDistributed(Conv2D(128, (3, 3), activation='relu')))
    model.add(TimeDistributed(MaxPooling2D((2, 2))))
    
    model.add(TimeDistributed(Flatten()))
    
    # LSTM layer
    model.add(LSTM(128, return_sequences=False))
    
    # Fully connected layers
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    
    model.add(Dense(num_classes, activation='softmax'))

    model.summary()
    
    return model

def main():
    # Load data
    X, y = load_data(DATA_DIR, CLASSES, SEQUENCE_LENGTH, (IMG_WIDTH, IMG_HEIGHT), CHANNELS)
    
    num_classes = len(CLASSES)
    
    # Preprocess data
    X, y = preprocess_data(X, y, num_classes)
    
    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Training sequences: {X_train.shape[0]}")
    print(f"Testing sequences: {X_test.shape[0]}")
    
    # Build model
    model = build_crnn_model(SEQUENCE_LENGTH, IMG_HEIGHT, IMG_WIDTH, CHANNELS, num_classes)
    
    # Compile model
    optimizer = Adam(lr=LEARNING_RATE)
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    
    # Train model
    history = model.fit(
        X_train, y_train,
        validation_data=(X_test, y_test),
        epochs=EPOCHS,
        batch_size=BATCH_SIZE
    )
    
    # Evaluate model
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Test Loss: {loss}")
    print(f"Test Accuracy: {accuracy}")

    # Optionally, save the model
    model.save('gait_recognition_crnn_model.h5')
    print("Model saved as 'gait_recognition_crnn_model.h5'")

if __name__ == '__main__':
    main()



