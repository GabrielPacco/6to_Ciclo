// A C++ program to demonstrate delete in K D tree
#include <iostream>
using namespace std;

const int k = 2;

// A structure to represent node of kd tree
struct Node
{
	int point[k]; // To store k dimensional point
	Node *left, *right;
};

// A method to create a node of K D tree
struct Node* newNode(int arr[])
{
	struct Node* temp = new Node;

	for (int i=0; i<k; i++)
		temp->point[i] = arr[i];

	temp->left = temp->right = NULL;
	return temp;
}

// Inserts a new node and returns root of modified tree
// The parameter depth is used to decide axis of comparison
Node *insertRec(Node *root, int point[], unsigned depth)
{
	// Tree is empty?
	if (root == NULL)
		return newNode(point);

	// Calculate current dimension (cd) of comparison
	unsigned cd = depth % k;

	// Compare the new point with root on current dimension 'cd'
	// and decide the left or right subtree
	if (point[cd] < (root->point[cd]))
		root->left = insertRec(root->left, point, depth + 1);
	else
		root->right = insertRec(root->right, point, depth + 1);

	return root;
}

// Function to insert a new point with given point in
// KD Tree and return new root. It mainly uses above recursive
// function "insertRec()"
Node* insert(Node *root, int point[])
{
	return insertRec(root, point, 0);
}

// A utility function to find minimum of three integers
Node *minNode(Node *x, Node *y, Node *z, int d)
{
	Node *res = x;
	if (y != NULL && y->point[d] < res->point[d])
	res = y;
	if (z != NULL && z->point[d] < res->point[d])
	res = z;
	return res;
}

// Recursively finds minimum of d'th dimension in KD tree
// The parameter depth is used to determine current axis.
Node *findMinRec(Node* root, int d, unsigned depth)
{
	// Base cases
	if (root == NULL)
		return NULL;

	// Current dimension is computed using current depth and total
	// dimensions (k)
	unsigned cd = depth % k;

	// Compare point with root with respect to cd (Current dimension)
	if (cd == d)
	{
		if (root->left == NULL)
			return root;
		return findMinRec(root->left, d, depth+1);
	}

	// If current dimension is different then minimum can be anywhere
	// in this subtree
	return minNode(root,
			findMinRec(root->left, d, depth+1),
			findMinRec(root->right, d, depth+1), d);
}

// A wrapper over findMinRec(). Returns minimum of d'th dimension
Node *findMin(Node* root, int d)
{
	// Pass current level or depth as 0
	return findMinRec(root, d, 0);
}

// Un método útil para determinar si dos puntos son iguales
// in K Dimensional space
bool arePointsSame(int point1[], int point2[])
{
	// Compare individual pointinate values
	for (int i = 0; i < k; ++i)
		if (point1[i] != point2[i])
			return false;

	return true;
}

// Copies point p2 to p1
void copyPoint(int p1[], int p2[])
{
for (int i=0; i<k; i++)
	p1[i] = p2[i];
}

// Función para eliminar un punto dado 'punto[]' del árbol con la raíz
// como 'raíz'. depth es la profundidad actual y se pasa como 0 inicialmente.
// Devuelve la raíz del árbol modificado.
Node *deleteNodeRec(Node *root, int point[], int depth)
{
	// Si el punto indicado no está presente
	if (root == NULL)
		return NULL;

	// Encontrar la dimensión del nodo actual
	int cd = depth % k;

	// Si el punto a eliminar está presente en la raíz
	if (arePointsSame(root->point, point))
	{
		// 2.b) Si el hijo derecho no es NULL
		if (root->right != NULL)
		{
			// Encontrar el mínimo de la dimensión de la raíz en el subárbol derecho
			Node *min = findMin(root->right, cd);

			// Copiar el mínimo a la raíz
			copyPoint(root->point, min->point);

			// Eliminar recursivamente el mínimo
			root->right = deleteNodeRec(root->right, min->point, depth+1);
		}
		else if (root->left != NULL) // lo mismo que lo anterior
		{
			Node *min = findMin(root->left, cd);
			copyPoint(root->point, min->point);
			root->right = deleteNodeRec(root->left, min->point, depth+1);
		}
		else // Si el nodo a eliminar es un nodo hoja
		{
			delete root;
			return NULL;
		}
		return root;
	}

	// 2) Si el nodo actual no contiene un punto, busca hacia abajo
	if (point[cd] < root->point[cd])
		root->left = deleteNodeRec(root->left, point, depth+1);
	else
		root->right = deleteNodeRec(root->right, point, depth+1);
	return root;
}

// Función para eliminar un punto dado del árbol K D con 'raíz'
Node* deleteNode(Node *root, int point[])
{
// Pasar la profundidad como 0
return deleteNodeRec(root, point, 0);
}

// Driver program to test above functions
int main()
{
	struct Node *root = NULL;
	int points[][k] = {{30, 40}, {5, 25}, {70, 70},
					{10, 12}, {50, 30}, {35, 45}};

	int n = sizeof(points)/sizeof(points[0]);

	for (int i=0; i<n; i++)
		root = insert(root, points[i]);

	// Delete (30, 40);
	root = deleteNode(root, points[0]);

	cout << "Root after deletion of (30, 40)\n";
	cout << root->point[0] << ", " << root->point[1] << endl;

	return 0;
}
