import numpy as np

def calculate(digits_list):
    """
    Converts a list containing 9 digits into a 3 x 3 Numpy array 
    and returns a dictionary containing the mean, variance, standard deviation, 
    max, min, and sum along both axes and for the flattened matrix.
    """
    # raise ValueError for list containing more or less than 9 digits
    try:
        digits_matrix = np.array(digits_list).reshape(3, 3)
    except ValueError:
        raise ValueError("List must contain nine numbers.")

    # build dictionary
    calculations = {
                     'mean':                [np.mean(digits_matrix, 0).tolist(), np.mean(digits_matrix, 1).tolist(), np.mean(digits_matrix)],
                     'variance':            [np.var(digits_matrix, 0).tolist(),  np.var(digits_matrix, 1).tolist(),  np.var(digits_matrix)],
                     'standard deviation':  [np.std(digits_matrix, 0).tolist(),  np.std(digits_matrix, 1).tolist(),  np.std(digits_matrix)],
                     'max':                 [np.max(digits_matrix, 0).tolist(),  np.max(digits_matrix, 1).tolist(),  np.max(digits_matrix)],
                     'min':                 [np.min(digits_matrix, 0).tolist(),  np.min(digits_matrix, 1).tolist(),  np.min(digits_matrix)],
                     'sum':                 [np.sum(digits_matrix, 0).tolist(),  np.sum(digits_matrix, 1).tolist(),  np.sum(digits_matrix)]
                   }

    return calculations