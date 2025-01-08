// Sample data - this would represent features extracted from brain scans
// In real scenarios, these would be complex image data, not just simple numbers.
const brainScans = [
  { pixels: [0, 1, 1, 0], hasAneurysm: true },
  { pixels: [1, 0, 0, 1], hasAneurysm: false },
  { pixels: [0, 0, 1, 1], hasAneurysm: true },
  { pixels: [1, 1, 0, 0], hasAneurysm: false }
];

// A very simplified model for demonstration. Real models would be much more complex.
class AneurysmDetector {
  constructor() {
    // This threshold would be learned from data in real scenarios
    this.threshold = 1.5;
  }

  // Predict if a scan suggests an aneurysm
  predict(scan) {
    // Sum of pixels - a very naive feature for detection
    let pixelSum = scan.pixels.reduce((sum, pixel) => sum + pixel, 0);
    return pixelSum > this.threshold;
  }
}

// Training or adjusting the model - here we'd normally use more data and adjust the threshold dynamically
function trainModel(scans, detector) {
  let correct = 0;
  for (let scan of scans) {
    let prediction = detector.predict(scan);
    if (prediction === scan.hasAneurysm) correct++;
  }
  console.log(`Model accuracy: ${(correct / scans.length * 100).toFixed(2)}%`);
  
  // Here, we'd adjust the threshold based on performance, but for simplicity:
  if (correct / scans.length < 0.75) {
    detector.threshold += 0.1; // Increase threshold if accuracy is low
  }
}

// Use the model
const detector = new AneurysmDetector();
trainModel(brainScans, detector);

// Test with a new scan
const newScan = { pixels: [1, 1, 1, 0] };
let result = detector.predict(newScan);
console.log(`Does the new scan suggest an aneurysm? ${result}`);
