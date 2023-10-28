# Signal Sampling studio application

## Table of Contents
- [Project Description](#project-description)
- [Demo](#Demo)
- [Features](#features)
- [Getting Started](#getting-started)
---

## Project Description
This desktop application is designed to illustrate the concepts of signal sampling and recovery, highlighting the importance and validation of the Nyquist rate. The application allows users to load a mid-length signal (approximately 1000 points) and perform various operations related to signal processing. It showcases the visualization, sampling, and recovery of signals, along with the ability to compose and manipulate signals with different components.

![image](https://github.com/SaraElsaggan/sampling_studio_DSP/assets/105241119/c3de3e5f-a892-4db1-bc91-2319560bd273)
![image](https://github.com/SaraElsaggan/sampling_studio_DSP/assets/105241119/c3877402-576f-48b3-80b4-6c50ab3508a7)
![image](https://github.com/SaraElsaggan/sampling_studio_DSP/assets/105241119/9632174c-9b9c-44f8-b6bb-a1f3f35e0427)
![image](https://github.com/SaraElsaggan/sampling_studio_DSP/assets/105241119/3309ce9c-9651-4cff-9cb7-1513a2f21c1d)



### Application Features
The application boasts the following key features:

### Sample & Recover
- Users can load a signal and visualize it.
- They can sample the signal at different frequencies.
- The sampled points can be used to recover the original signal using the Whittaker–Shannon interpolation formula.
- The sampling frequency is displayed either in actual frequency or normalized with respect to the maximum frequency.
- Three graphs are used: one to display the original signal with sampled point markers, another for the reconstructed signal, and a third to display the difference between the original and reconstructed signals.

### Load & Compose
- The loaded signal can come from a file or be composed in the application.
- Users can mix multiple sinusoidal signals of different frequencies and magnitudes.
- Components can be added or removed during signal composition.

### Additive Noise
- Users can introduce custom noise to the loaded signal with controllable Signal-to-Noise Ratio (SNR) levels.
- The application visually demonstrates the effect of noise on the signal and its dependency on the signal frequency.

### Real-time
- Sampling and recovery are performed in real time upon user changes, without the need for manual updates.

---

## Getting Started
Follow these instructions to get the application up and running on your system.

1. **Prerequisites**: 
   - Ensure you have a compatible operating system (Windows, macOS, or Linux).
   - Install Python 3.x on your system.

2. **Clone the Repository**:
   - Clone this repository to your local machine using your preferred Git client or by downloading the source code as a ZIP archive.

3. **Install Dependencies**:
   - Navigate to the project directory in your terminal and install the needed packages

4. **Run the Application**:
   - run the main.py using your IDE (ex. visual studio)




