# Write a python program to classify breast cancer from histopathological images using VGG-16 and DenseNet-201 CNN architectures

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16, DenseNet201
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import classification_report, confusion_matrix

train_dir = r'C:\Rick\Study\MCA\3rd Semester\Python Lab\Assignment 7\Fish_DS_Q10\train'
val_dir = r'C:\Rick\Study\MCA\3rd Semester\Python Lab\Assignment 7\Fish_DS_Q10\valid'
test_dir = r'C:\Rick\Study\MCA\3rd Semester\Python Lab\Assignment 7\Fish_DS_Q10\test'

# Image preprocessing and data augmentation
image_size = (224, 224)
batch_size = 32

train_datagen = ImageDataGenerator(rescale=1./255, 
                                   rotation_range=20, 
                                   width_shift_range=0.2, 
                                   height_shift_range=0.2, 
                                   shear_range=0.2, 
                                   zoom_range=0.2, 
                                   horizontal_flip=True)
val_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(train_dir, target_size=image_size, batch_size=batch_size, class_mode='binary')
val_generator = val_datagen.flow_from_directory(val_dir, target_size=image_size, batch_size=batch_size, class_mode='binary')
test_generator = test_datagen.flow_from_directory(test_dir, target_size=image_size, batch_size=batch_size, class_mode='binary')

# Function to create VGG16 model
def build_vgg16_model(input_shape=(224, 224, 3)):
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=input_shape)
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.5)(x)  # Dropout for regularization
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(1, activation='sigmoid')(x)  # Binary classification

    model = Model(inputs=base_model.input, outputs=predictions)

    # Freeze the layers except the last few layers
    for layer in base_model.layers:
        layer.trainable = False

    return model

# Function to create DenseNet201 model
def build_densenet_model(input_shape=(224, 224, 3)):
    base_model = DenseNet201(weights='imagenet', include_top=False, input_shape=input_shape)
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.5)(x)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(1, activation='sigmoid')(x)

    model = Model(inputs=base_model.input, outputs=predictions)

    for layer in base_model.layers:
        layer.trainable = False

    return model

# Compile and train the models
def compile_and_train(model, train_generator, val_generator, epochs=10):
    model.compile(optimizer=Adam(learning_rate=1e-4), loss='binary_crossentropy', metrics=['accuracy'])
    history = model.fit(train_generator, validation_data=val_generator, epochs=epochs, verbose=1)
    return history

# Load models
vgg16_model = build_vgg16_model()
densenet_model = build_densenet_model()

# Train the models
print("Training VGG16 Model...")
vgg16_history = compile_and_train(vgg16_model, train_generator, val_generator, epochs=10)

print("Training DenseNet201 Model...")
densenet_history = compile_and_train(densenet_model, train_generator, val_generator, epochs=10)

# Evaluate the models on the test set
def evaluate_model(model, test_generator):
    test_loss, test_acc = model.evaluate(test_generator, verbose=1)
    print(f'Test accuracy: {test_acc:.4f}')
    
    predictions = model.predict(test_generator, verbose=1)
    y_pred = (predictions > 0.5).astype(int).ravel()
    y_true = test_generator.classes

    print("Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    
    print("Classification Report:")
    print(classification_report(y_true, y_pred, target_names=['Class 0', 'Class 1']))

# Evaluate VGG16
print("Evaluating VGG16 Model...")
evaluate_model(vgg16_model, test_generator)

# Evaluate DenseNet201
print("Evaluating DenseNet201 Model...")
evaluate_model(densenet_model, test_generator)
