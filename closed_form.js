// Function to calculate the mean (average) of an array
function calculateMean(sample) {
    // Step 1: Sum up all elements in the sample
    let sum = 0;
    for (let i = 0; i < sample.length; i++) {
        sum += sample[i];
    }

    // Step 2: Divide the sum by the number of elements
    let mean = sum / sample.length;

    // Return the calculated mean
    return mean;
}

// Example usage
let sampleData = [1, 2, 3, 4, 5];
let average = calculateMean(sampleData);
console.log(`The average of the sample is: ${average}`);

// Another example with different numbers
let anotherSample = [10, 20, 30, 40, 50];
let anotherAverage = calculateMean(anotherSample);
console.log(`The average of another sample is: ${anotherAverage}`);
