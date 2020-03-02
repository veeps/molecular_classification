import matplotlib.pyplot as plt

epochs = 20

# function to plot accuracy and loss plots
def plot_accuracy_loss(model_history):
    acc = model_history.history['accuracy']
    val_acc = model_history.history['val_accuracy']

    loss=model_history.history['loss']
    val_loss=model_history.history['val_loss']

    epochs_range = range(epochs)

    plt.figure(figsize=(15, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()