import numpy as np


def test_average():
    # Make new output file
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1
    np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

    # Run sagital brain file to generate output
    exec(open("sagital_brain.py").read())

    # Load output
    loaded = np.loadtxt('brain_average.csv', delimiter=',')

    # Expected output
    expected = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0])

    # Check the values are identical
    np.testing.assert_array_equal(loaded, expected)
