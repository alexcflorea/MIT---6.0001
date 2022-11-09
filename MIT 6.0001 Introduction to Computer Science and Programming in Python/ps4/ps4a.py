# Problem Set 4A
# Name: Alex Florea
# Collaborators: None
# Time Spent: 2:00

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    sequence = sequence.strip()
    
    if len(sequence) <= 1:
        return [sequence]

    else:
       permList = []
       
       for char in sequence:
           seqCopy = sequence.replace(char,'',1)
           permList += [char + i for i in get_permutations(seqCopy)]
           
           
       
       return list(set(permList))


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)
    
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print()
    
    example_input = 'aba'
    print('Input:', example_input)
    print('Expected Output:', ['aba', 'aab', 'baa'])
    print('Actual Output:', get_permutations(example_input))
    print()
    
    example_input = 'ab'
    print('Input:', example_input)
    print('Expected Output:', ['ab', 'ba'])
    print('Actual Output:', get_permutations(example_input))
    print()
    
    example_input = '       abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print()
    
    example_input = 'abA'
    print('Input:', example_input)
    print('Expected Output:', ['abA', 'aAb', 'baA', 'bAa', 'Aab', 'Aba'])
    print('Actual Output:', get_permutations(example_input))