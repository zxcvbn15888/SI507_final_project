

def isAnswer(ans):
    '''indicate if the answer is true or false
    
    Parameters  
    -------------------
    ans: answer to the question
    
    Returns
    -------
    True if the ans is positive,
    or False if the answer is negative

    '''
    answer = input(ans)
    if answer.lower() in ['yes', 'y', 'yep', 'sure', 'yup']:
        return True
    return False

def isLeaf(tree):
    '''indicate if the node is leaf or not
    
    Parameters  
    -------------------
    tree: a set of tuples contain three things: questions, what to do on 'yes', what to do on 'no'
    
    Returns
    -------
    True if the node is leaf,
    or False if the node is not leaf

    '''
    
    root, left, right = tree
    if left == None and right == None:
        return True
    return False

def saveTree(tree, treeFile):
    '''save current tree into a file
    
    Parameters  
    -------------------
    tree: a set of tuples contain three things: questions, what to do on 'yes', what to do on 'no'
    treeFile: file handle

    Returns
    -------
    None

    '''
    root, left, right = tree

    if isLeaf(tree):
        print('Leaf', file = treeFile)
        print(root, file = treeFile)
    else:
        print('Internal Node', file = treeFile)
        print(root, file = treeFile)
        
        saveTree(left, treeFile)        
        saveTree(right, treeFile)


def loadTree(treeFile):
    '''load tree from a file
    
    Parameters  
    -------------------
    treeFile: file handle

    Returns
    -------
    tuple that contains a tree

    '''
    line = treeFile.readline()
    if line == '':
        return None
    
    elif line == 'Leaf\n':
        root = treeFile.readline()
        root = root.rstrip('\n')
        return (root, None, None)
    
    root = treeFile.readline()
    root = root.rstrip('\n')
    left = loadTree(treeFile)
    right = loadTree(treeFile)
    
    return (root, left, right)


def main():
    pass

if __name__ == '__main__':
    main()