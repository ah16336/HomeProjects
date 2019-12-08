## CALCULATING GINI SCORE ##

# Defining function to complete method described in word doc.

def gini_index(groups, classes):
	# count all samples at split point
	n_instances = float(sum([len(group) for group in groups]))
	# sum weighted Gini index for each group
	gini = 0.0
	for group in groups:
		size = float(len(group))
		# avoid divide by zero
		if size == 0:
			continue
		score = 0.0
		# score the group based on the score for each class
		for class_val in classes:
            # p is proportion
			p = [row[-1] for row in group].count(class_val) / size
			score += p * p
		# weight the group score by its relative size
		gini += (1.0 - score) * (size / n_instances)
	return gini

# example testing Gini values

# We have two attempts to make two groups of data with 2 rows in each group.
#Our first attempt at grouping values are in group_1
group_1 = [[[1, 1], [1, 0]], [[1, 1], [1, 0]]]
#Our second attempt at grouping values are in group_2 (perfect split)
group_2 = [[[1, 0], [1, 0]], [[1, 1], [1, 1]]]
#the different classes possible
classes = [0, 1]
# gini_index(group_1, classes) = 0.5 => worst gini score
# gini_index(group_2, classes) = 0.0 => best gini score


## SPLITTING DATA ##

# Test whether value is smaller or larger than split value and group 
# accordingly. We would then test each group made by evaluating the
# gini score.


# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
	left, right = list(), list()
	for row in dataset:
		if row[index] < value:
			left.append(row)
		else:
			right.append(row)
	return left, right

# once the groups are made, we use the gini function above to evaluate.


## TESTING POSSIBLE SPLITS ##

# Iterates through ever element in column testing it as a split value
# Finds the value in test_split s.t. gini score is as low as possible

def get_split(dataset):
	class_values = list(set(row[-1] for row in dataset))
	b_index, b_value, b_score, b_groups = 999, 999, 999, None
	for index in range(len(dataset[0])-1):
		for row in dataset:
			groups = test_split(index, row[index], dataset)
			gini = gini_index(groups, class_values)
			if gini < b_score:
				b_index, b_value, b_score, b_groups = index, row[index], gini, groups
	return {'index':b_index, 'value':b_value, 'groups':b_groups}

## MID WAY TEST ##

dataset = [[2.771244718,1.784783929,0],
	[1.728571309,1.169761413,0],
	[3.678319846,2.81281357,0],
	[3.961043357,2.61995032,0],
	[2.999208922,2.209014212,0],
	[7.497545867,3.162953546,1],
	[9.00220326,3.339047188,1],
	[7.444542326,0.476683375,1],
	[10.12493903,3.234550982,1],
	[6.642287351,3.319983761,1]]
#split = get_split(dataset)
#print('Split: [X%d < %.3f]' % ((split['index']+1), split['value'])) 

# Now we know where to divide a data on the x axis.

### BUILDING A TREE ###

## RECURSIVE SPLITING ##

# Create a terminal node value
def to_terminal(group):
	outcomes = [row[-1] for row in group]
	return max(set(outcomes), key=outcomes.count)

# Deciding when to stop growing a tree, define two values:
# Maximum Tree Depth: maximum number of levels in the tree; distance
# from root node to terminal. 
# Minimum Node Records: the minimum number of training patterns that 
# a given node is responsible for. The number of records in its group to 
# be split.

# Create child splits for a node or make terminal
def split(node, max_depth, min_size, depth):
	left, right = node['groups']
	del(node['groups'])
	# check for a no split
	if not left or not right:
		node['left'] = node['right'] = to_terminal(left + right) # groups what values we have left as terminal
		return
	# check for max depth
	if depth >= max_depth:
		node['left'], node['right'] = to_terminal(left), to_terminal(right) #both are terminal
		return
	# process left child
	if len(left) <= min_size:
		node['left'] = to_terminal(left) #makes left terminal
	else:
		node['left'] = get_split(left) # finds split value for left group
		split(node['left'], max_depth, min_size, depth+1)
	# process right child
	if len(right) <= min_size:
		node['right'] = to_terminal(right) #makes right terminal
	else:
		node['right'] = get_split(right) #finds split value for right group
		split(node['right'], max_depth, min_size, depth+1)

# Call upon the above function recursively to build the tree:
# Build a decision tree
def build_tree(train, max_depth, min_size):
	root = get_split(train)
	split(root, max_depth, min_size, 1)
	return root

# returning the tree:
# Print a decision tree
def print_tree(node, depth=0):
	if isinstance(node, dict):
		print('%s[X%d < %.3f]' % ((depth*' ', (node['index']+1), node['value'])))
		print_tree(node['left'], depth+1)
		print_tree(node['right'], depth+1)
	else:
		print('%s[%s]' % ((depth*' ', node)))
 
## TREE TEST ##

# using the same dataset above

print("Depth = 1" + "\n")
tree = build_tree(dataset, 1, 1)
print_tree(tree)
print("\n")

print("Depth = 2" + "\n")
tree = build_tree(dataset, 2, 1)
print_tree(tree)
print("\n")

print("Depth = 3" + "\n")
tree = build_tree(dataset, 3, 1)
print_tree(tree)


 
